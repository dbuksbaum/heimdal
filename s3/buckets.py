from collectors import BaseCollector

class BucketsCollector(BaseCollector):
    @property
    def region_name(self):
        return self.region

    def __init__(self, region=None):
        super().__init__()
        self.region=region

    def list_all_buckets(self):
        buckets = []

        # get all the buckets
        s3_buckets = self.getResource(serviceName='s3', region=self.region).buckets.all()
        # now add the ARN for each one
        for bucket in s3_buckets:
            bucket.arn = "arn:aws:s3:::" + bucket.name
            buckets.append(bucket)

        return buckets

    def collect(self):
         return self.list_all_buckets()

