#!/usr/bin/env python3

import aws_cdk as cdk

# from aws cdk.aws cdk_stack import AwsCdkStack

from vacationtracker_service.stack import VacationTrackerServiceStack

app = cdk.App()
VacationTrackerServiceStack(app,"VacationTrackerService")
app.synth()
