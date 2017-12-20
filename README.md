# Heimdal

A simple Python library with two objectives:

1. Help me keep track of my AWS resources
2. Help me learn python

This library is inspired by [Cloud Reports](https://github.com/tensult/cloud-reports) project by Tensult.

# Functional Goals

* Scan AWS account(s) to create a snapshot inventory of all resources consumed
* React to AWS provisioning events to update the resource inventory
* Monitor utilization of all provision resources to identify idle resources
* Shut down idle resources
* Evaluate resources for compliance to defined rules (tags, scale, security, etc)
* Allocate & track costs over time

# To-Do List
## Collections
* S3
    * Buckets - _done_
    * Web Sites
* Route 53
    * Domains - _done_
    * Hosted Zones - _done_
* IAM
    * Users - _done_
    * Groups - _done_
    * Roles - _done_
    * Policies - _done_
* Cloud Watch
    * Alarms - _done_
    * Metrics - _done_
* Cloud Trails
    * Trails - _done_
* RDS
    * Instances - _done_
* DynamoDB
* Lambda
* API Gateway
* Cloud Front
* EC2
* VPC
* EBS
* ELB
* SNS
* SQS
* SES
* ACM
* RedShift

## Functions
* Determine Idle Resources
* Shut down idle resources
* Verify tagging policy
* Security checks
* Allocate costs across accounts, tags
* Calculate utilization & cost trends

# Resources, References, and Tools Used
* [Boto3 Documentation](http://boto3.readthedocs.io/en/stable/index.html)
* [BotoCore Documentation](http://botocore.readthedocs.io/en/latest/index.html)
* [AWS Documentation](https://aws.amazon.com/documentation/)
* [Python Documentation](https://docs.python.org/3/)
* [JetBrains PyCharm](https://www.jetbrains.com/pycharm/)
* [Visual Studio Code](https://code.visualstudio.com/)
* [SublimeText 3](http://www.sublimetext.com/)
* Tensult [Cloud Reports](https://github.com/tensult/cloud-reports)
