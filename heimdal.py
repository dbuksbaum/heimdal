
import boto3
from buckets import BucketsCollector
from domains import DomainsCollector
from hostedzonecollector import HostedZoneCollector
from AWSCollector import AWSCollector

def main():
#    bc = BucketsCollector()
#    buckets = bc.collect()
#    for bucket in buckets:
#        print(bucket.name)
#
    # dc = DomainsCollector()
    # domains = dc.collect()
    # if domains:
    #     for domain in domains:
    #         print(domain)
    #
    # hzc = HostedZoneCollector()
    # hosted_zones = hzc.collect()
    # if hosted_zones:
    #     for hz in hosted_zones:
    #         print(hz)

    collector = AWSCollector()
    buckets = collector.collect_s3_buckets()
    for bucket in buckets:
        print(bucket.name, bucket.arn)


    #aws = boto3.client('route53domains')
    #domains = aws.list_domains()['Domains']
    #print(domains)

if __name__ == '__main__':
    # execute only if run as a script
    main()
