from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as lambda_,
    aws_events_targets as targets,
    aws_events as events,
    aws_iam as iam
)
from constructs import Construct

DATABASE_NAME = "database-1"
START_CORN = events.Schedule.cron(
    minute="40", hour="00", week_day="MON-FRI", month="*", year="*")
STOP_CRON = events.Schedule.cron(
    minute="10", hour="10", week_day="MON-FRI", month="*", year="*")


class SchedulerRdsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambda_role = iam.Role(self, id="lambda_rds_role",
                               assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"))
        lambda_role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name("AmazonRDSFullAccess"))

        lambdaFn = lambda_.Function(self, "ActionRDS", code=lambda_.Code.from_asset("lambda"),
                                    handler="index.main", runtime=lambda_.Runtime.PYTHON_3_9, role=lambda_role
                                    )
        start_rule = events.Rule(self, "Run start the RDS at 40:00 every Monday through Friday",
                                 schedule=START_CORN)

        start_rule.add_target(targets.LambdaFunction(lambdaFn, event=events.RuleTargetInput.from_object(
            {"action": "start", "dbIdentifier": DATABASE_NAME})))

        stop_rule = events.Rule(self, "Run stop the RDS at 10:10 every Monday through Friday",
                                schedule=STOP_CRON)

        stop_rule.add_target(targets.LambdaFunction(lambdaFn, event=events.RuleTargetInput.from_object(
            {"action": "stop", "dbIdentifier": DATABASE_NAME})))
