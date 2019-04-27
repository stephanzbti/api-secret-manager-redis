from src.dao.aws_connect import get_secret
from flask_restful import Resource, Api
from flask import Flask, request
import logging as log
import json
from src.dao.dbConn import connectionRedis
from decouple import config

log_level = config('LOG_LEVEL', 'DEBUG')
log.basicConfig(format='%(levelname)s:%(message)s', level=log_level)

conn = connectionRedis()

class GetSecret(Resource):
    def post(self):
        try:
            data = request.data.decode()
            dataDict = json.loads(data)

            log.info('[INFO] SECRET: Getting secret!')

            aws_login = dataDict['aws_login']
            aws_secret = dataDict['aws_secret']
            aws_region = dataDict['aws_region']
            aws_secret_name = dataDict['aws_secret_name']

            log.debug('[DEBUG] GetSecret: AWS_Login: '+aws_login+' - AWS_Secret: ' +
                      aws_secret+' - AWS_Region: '+aws_secret_name+' - AWS_Secret_Name: '+aws_secret_name)

            aws_key_word = ':'.join(
                [aws_login, aws_secret_name]).encode('utf-8')

            if(conn.exists(aws_key_word) == True):
                log.info('[INFO] GetSecret:  SECRET: Getting from Redis!')
                log.debug('[DEBUG] GetSecret: AWS_Key_Word: '+aws_key_word.decode())
                resp = conn.hgetall(aws_key_word)
                log.debug('[DEBUG] GetSecret: Resp: '+json.dumps(resp))
            else:
                log.info('[INFO] GetSecret: SECRET: Getting from AWS!')
                log.debug('[DEBUG] GetSecret: AWS_Key_Word: '+aws_key_word.decode())
                resp = get_secret(aws_login, aws_secret,
                                  aws_region, aws_secret_name)
                log.debug(resp)
                if resp is not None:
                    resp['aws_secret'] = aws_secret
                    resp['aws_region'] = aws_region
                    conn.hmset(aws_key_word, resp)
                    log.debug('[DEBUG] GetSecret: Resp: '+json.dumps(resp))

            if(resp['aws_secret'] == aws_secret and resp['aws_region'] == aws_region):
                if 'aws_secret' in resp:
                    del resp['aws_secret']
                log.debug('[DEBUG] GetSecret: Resp: '+json.dumps(resp))
                return { 'message': jsom.dumps(resp), 'status': 200 }

            return {'message': 'ERROR: Authentication failed', 'status': 500}
        except:
            log.error('[ERROR] Problem when getting secret')
            return {'message': 'ERROR: Problem when getting secret', 'status': 500}