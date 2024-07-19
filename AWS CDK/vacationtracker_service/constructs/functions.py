from constructs import Construct
from aws_cdk import aws_lambda
from pathlib import Path
app_root_dir=(Path(__file__).parent.parent.parent).resolve()

default_function_path=str((app_root_dir/"src").resolve())
print(default_function_path)
class FunctionConstructs(Construct):
    def __init__(self,scope:Construct,id:str)->None:
        super().__init__(scope,id) # parent class constructor calling
    
        ## Random Data Lambda
        self.RandomLambda=aws_lambda.Function(
            scope=self,
            id="LambdaFunction",
            function_name="dev-vacationtracker-service-lambda-function",
            runtime=aws_lambda.Runtime.PYTHON_3_12,
            code=aws_lambda.Code.from_asset(default_function_path),
            handler="handlers.handler"
        )
        
        
        
    