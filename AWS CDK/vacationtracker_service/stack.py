from constructs import Construct
from aws_cdk import ( 
    Stack,
)

from vacationtracker_service.constructs.functions import FunctionConstructs
from vacationtracker_service.constructs.api_gateway import ApiGatewayConstruct
class VacationTrackerServiceStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        ## Resource
        
        #L3 Functions
        functions=FunctionConstructs(self,"Functions")
        
        # L3 API GateWAY
        api_gateway=ApiGatewayConstruct(self,"ApiGateWay",functions)

