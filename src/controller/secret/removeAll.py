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

class RemoveAll(Resource):
    def post(self):
        try:
            data = request.data.decode()
            dataDict = json.loads(data)

            log.info('[INFO] RemoveAll: REDIS: Cleaning cache!')

            redis_passwd = dataDict['redis_password']
            log.debug('[DEBUG] RemoveAll: redis_passwd: '+redis_passwd)

            if redis_password == redis_passwd:
                resp = conn.flushall()
                log.debug('[DEBUG] RemoveAll: Resp: '+json.dumps(resp))
                log.info('[INFO] RemoveAll: REDIS: Cache clean!')
                return {'message': 'REDIS: Cache cleaned', 'status': 200}
            else:
                log.info('[INFO] RemoveAll: ERROR: Authentication failed')
                return {'message': 'ERROR: Authentication failed', 'status': 500}
        except:
            log.error('[ERROR] Problem when remove Secret')
            return {'message': 'Problem when remove secret', 'status': 500}