import aws_cdk as core
import aws_cdk.assertions as assertions

from 01_first_cdk.01_first_cdk_stack import 01FirstCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in 01_first_cdk/01_first_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = 01FirstCdkStack(app, "01-first-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
