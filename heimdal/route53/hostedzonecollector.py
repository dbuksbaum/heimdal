from collectors import BaseCollector

class HostedZoneCollector(BaseCollector):
    @property
    def region_name(self):
        return self.region

    def __init__(self, region=None):
        super().__init__()
        self.region=region

    def list_all_hosted_zones(self):
        marker = None
        fetchPending = True
        domains = []

        while fetchPending:
            result = super().getClient(serviceName='route53', region=self.region).list_hosted_zones()
            domains.extend(result['HostedZones'])
            if 'NextPageMarker' in result:
                marker = result['NextMarker']
                fetchPending = True
            else:
                fetchPending = False

        return domains

    def collect(self):
         return self.list_all_hosted_zones()

