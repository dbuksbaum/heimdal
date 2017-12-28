from lambda_functions import FunctionCollector, AliasCollector, EventSourceCollector
from dynamodb import TablesCollector, StreamsCollector, TableStreamsCollector
from rds import InstanceCollector, EngineVersionCollector, ReservedInstanceCollector, SecurityGroupsCollector
from cloudtrail import TrailsCollector
from cloudwatch import AlarmsCollector, MetricsCollector
from iam import UsersCollector, GroupsCollector, RolesCollector, PolicyCollector
from route53 import DomainsCollector, HostedZoneCollector
from s3 import BucketsCollector
import logging

def main():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    logger.info("Starting main!")

    # S3
    # for bucket in BucketsCollector().collect():
    #     print(bucket.name, bucket.arn)

    # Route 53
    # domains = DomainsCollector().collect()
    # if domains:
    #     for domain in domains:
    #         print(domain)
    #
    # hosted_zones = HostedZoneCollector().collect()
    # if hosted_zones:
    #     for hz in hosted_zones:
    #         print(hz)

    # IAM
    # for user in UsersCollector().collect():
    #     print(user.name, user.arn)
    #
    # for group in GroupsCollector().collect():
    #     print(group.name, group.arn)
    #
    # for role in RolesCollector().collect():
    #     print(role.name, role.arn)
    #
    # for policy in PolicyCollector().collect():
    #     print(policy.policy_name, policy.arn)

    # Cloud Watch
    # for alarm in AlarmsCollector().collect():
    #     print(alarm.name)
    #
    # for metric in MetricsCollector().collect():
    #     print(metric.name)

    # Cloud Trail
    # for trail in TrailsCollector().collect():
    #     print(trail)

    # RDS
    # for instance in InstanceCollector().collect():
    #     print(instance)
    #
    # for instance in ReservedInstanceCollector().collect():
    #     print(instance)
    #
    # for engine_version in EngineVersionCollector().collect():
    #     print(engine_version)
    #
    # for group in SecurityGroupsCollector().collect():
    #     print(group)

    # DynamoDB
    # for table in TablesCollector().collect():
    #     print(table.table_name, table.table_arn)
    #     for stream in TableStreamsCollector(table_name=table.table_name).collect():
    #         print(stream)
    #
    # for stream in StreamsCollector().collect():
    #     print(stream)

    # Lambda
    for function in FunctionCollector().collect():
        print(function)
        for alias in AliasCollector(function['FunctionName']).collect():
            print(alias)

    for event_source in EventSourceCollector().collect():
        print(event_source)


    logger.info("Ending main!")


if __name__ == '__main__':
    # execute only if run as a script
    main()
