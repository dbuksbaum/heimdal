
# from: http://docs.aws.amazon.com/general/latest/gr/rande.html
class RegionProvider:
    def __init__(self):
        self.service_regions = \
            {
                'S3':
                    [
                        "us-east-2",
                        "us-east-1",
                        "us-west-1",
                        "us-west-2",
                        "ca-central-1",
                        "ap-south-1",
                        "ap-northeast-2",
                        "ap-southeast-1",
                        "ap-southeast-2",
                        "ap-northeast-1",
                        "cn-northwest-1",
                        "eu-central-1",
                        "eu-west-1",
                        "eu-west-2",
                        "sa-east-1"
                    ]
            }

    def get_service_region(self, service_name):
        return self.service_regions[service_name]
