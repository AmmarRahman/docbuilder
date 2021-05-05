from aws_cdk import (
    core as cdk,
    aws_lambda as lambda_,
    aws_lambda_python as lambda_python,
    aws_secretsmanager as secretsmanager
)


class DocbuilderStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The secret
        mysecret = secretsmanager.Secret(self, "DocBuilderSecret",
                                         secret_name="docbuilder/bigsecret"
                                         )
        # The Lambda
        doc_builder = lambda_python.PythonFunction(self, "DocBuilderLambda",
                                                   runtime=lambda_.Runtime.PYTHON_3_8,
                                                   entry='./resources',
                                                   index='my_lambda.py',
                                                   environment=dict(
                                                       SECRET_ID=mysecret.secret_arn
                                                   )
                                                   )
        # The role
        mysecret.grant_read(doc_builder.role)

        # Still need to figure out what is the trigger that we are going to use.
