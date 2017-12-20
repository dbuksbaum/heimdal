import boto3

class AWSCollector():
    @property
    def region_name(self):
        return self.region

    def __init__(self, region=None):
        super().__init__()
        self.region=region

    def getClient(self, serviceName, region=None):
        if region:
            return boto3.client(serviceName, region_name=region)
        else: # use default region
            return boto3.client(serviceName)

    def getResource(self, serviceName, region=None):
        if region:
            return boto3.resource(serviceName, region_name=region)
        else: # use default region
            return boto3.resource(serviceName)

    def collect_s3_buckets(self):
        buckets = []

        s3_buckets = self.getResource(serviceName='s3', region=self.region).buckets.all()
        for bucket in s3_buckets:
            bucket.arn = "arn:aws:s3:::" + bucket.name
            buckets.append(bucket)

        return buckets
