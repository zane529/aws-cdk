import aws_cdk as core
import aws_cdk.assertions as assertions

from scheduler_rds.scheduler_rds_stack import SchedulerRdsStack

# example tests. To run these tests, uncomment this file along with the example
# resource in scheduler_rds/scheduler_rds_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = SchedulerRdsStack(app, "scheduler-rds")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
