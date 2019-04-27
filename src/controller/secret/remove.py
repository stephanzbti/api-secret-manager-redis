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

class Remove(Resource):
    def post(self):
        try:
            data = request.data.decode()
            dataDict = json.loads(data)

            log.info('[INFO] RemoveAll: REDIS: Deleting Key!')

            aws_login = dataDict['aws_login']
            aws_secret_name = dataDict['aws_secret_name']

            aws_key_word = ':'.join(
                [aws_login, aws_secret_name]).encode('utf-8')

            log.debug('[DEBUG] RemoveAll: AWS_Key_Word: '+aws_key_word.decode())

            if(conn.exists(aws_key_word) == True):
                resp = conn.delete(aws_key_word)
                log.debug('[DEBUG] Remove: Resp: '+json.dumps(resp))
                log.info('[INFO] RemoveAll: REDIS: Key Deleted!')
                return {'message': 'REDIS: Key cleaned', 'status': 200}
            else:
                log.info('[INFO] RemoveAll: REDIS: Key not exists!')
                return {'message': 'REDIS: Key not exists', 'status': 500}

        except:
            log.error('[ERROR] Error removing from redis')
            return {'message': 'Error removing from redis', 'status': 500}