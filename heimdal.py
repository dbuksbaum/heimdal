from buckets import BucketsCollector


def main():
    bc = BucketsCollector()
    buckets = bc.collect()
    for bucket in buckets:
        print(bucket.name, bucket.arn)

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

    #aws = boto3.client('route53domains')
    #domains = aws.list_domains()['Domains']
    #print(domains)

if __name__ == '__main__':
    # execute only if run as a script
    main()
