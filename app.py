#!/usr/bin/env python3
import os

import aws_cdk as cdk

from scheduler_rds.scheduler_rds_stack import SchedulerRdsStack


app = cdk.App()
SchedulerRdsStack(app, "SchedulerRdsStack")

app.synth()