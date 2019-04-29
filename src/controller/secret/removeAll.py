from src.dao.aws_connect import get_secret
from flask_restful import Resource, Api
from flask import Flask, request, Response
import logging as log
import json
from src.dao.dbConn import connectionRedis
from decouple import config

log_level = config('LOG_LEVEL', 'DEBUG')
redis_password = config('REDIS_PASSWORD', '')
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
                return Response({'message': 'REDIS: Cache cleaned'}, status=200, mimetype='application/json') 
            else:
                log.info('[INFO] RemoveAll: ERROR: Authentication failed')
                return Response({'message': 'ERROR: Authentication failed'}, status=500, mimetype='application/json')
        except:
            log.error('[ERROR] Problem when remove Secret')
            return Response({'message': 'Problem when remove secret'}, status=500, mimetype='application/json')