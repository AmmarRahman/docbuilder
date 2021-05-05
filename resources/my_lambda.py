import boto3, os
##Any code outside the handler is only run when a new lambda is spun off.
# It's not counted as execution time, so try to put as much as possible outside the handler.
secretmanager = boto3.client('secretsmanager')
mysecret = secretmanager.get_secret_value (SecretId= os.environ['SECRET_ID'])
def handler(event, context):
    ## Any code that is run on every request goes here

    return "Hello World"