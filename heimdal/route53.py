from collectors import BaseCollector

class DomainsCollector(BaseCollector):
    @property
    def region_name(self):
        return self.region

    def __init__(self, region=None):
        super().__init__()
        self.region=region

    def list_all_domains(self):
        svc = super().getClient(serviceName='route53domains', region=self.region)
        marker = None
        fetchPending = True
        domains = []

        while fetchPending:
            if marker:
                result = svc.list_domains(Marker=marker)
            else:
                result = svc.list_domains()
            domains.extend(result['Domains'])
            if 'NextPageMarker' in result:
                marker = result['NextPageMarker']
                fetchPending = True
            else:
                fetchPending = False

        return domains

    def collect(self):
         return self.list_all_domains()


class HostedZoneCollector(BaseCollector):
    @property
    def region_name(self):
        return self.region

    def __init__(self, region=None):
        super().__init__()
        self.region=region

    def list_all_hosted_zones(self):
        svc = super().getClient(serviceName='route53', region=self.region)
        marker = None
        fetchPending = True
        domains = []

        while fetchPending:
            if marker:
                result = svc.list_hosted_zones(Marker=marker)
            else:
                result = svc.list_hosted_zones()
            domains.extend(result['HostedZones'])
            if 'Marker' in result:
                marker = result['Marker']
                fetchPending = True
            else:
                fetchPending = False

        return domains

    def collect(self):
         return self.list_all_hosted_zones()

