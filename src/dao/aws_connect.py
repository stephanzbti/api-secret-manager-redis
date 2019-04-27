import boto3
from botocore.exceptions import ClientError
import json
import src.config.aws_regions as aws_regions


def get_secret(aws_login, aws_secret, aws_region, aws_secret_name):
    session = boto3.session.Session(
        aws_access_key_id=aws_login,
        aws_secret_access_key=aws_secret,
        region_name=aws_region
    )

    client = session.client(
        service_name='secretsmanager',
        region_name=aws_region,
        endpoint_url="https://secretsmanager."+aws_region+".amazonaws.com"
    )

    try:
        if(aws_region in aws_regions.regions):
            get_secret_value_response = client.get_secret_value(
                SecretId=aws_secret_name
            )
        else:
            return (None)
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            print("A secret " + aws_secret_name + " não foi encontrada")
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            print("A requisição foi rejeitada por:", e)
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            print("A requisição tem parâmetros inválidos:", e)
    else:
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
            return(json.loads(secret))
        else:
            return(None)
