from constructs import Construct
from aws_cdk import aws_apigateway
from pathlib import Path
from vacationtracker_service.constructs.functions import FunctionConstructs

class ApiGatewayConstruct(Construct):
    
    def __init__(self,scope:Construct,id:str,functions:FunctionConstructs)->None:
        super().__init__(scope,id) # parent class constructor calling
        
        #Rest Api
        
        self.rest_api=aws_apigateway.RestApi(
            scope=self,
            id="RestApi",
            rest_api_name="dev-vacationtracker-service-rest-api",   
        )
        
       #Data Endpoint 
        self.data_resource= self.rest_api.root.add_resource("data")
        self.data_resource.add_method("GET",aws_apigateway.LambdaIntegration(functions.RandomLambda))
        
        
        
        