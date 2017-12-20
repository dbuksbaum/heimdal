from collectors import BaseCollector

class InstanceCollector(BaseCollector):
    @property
    def region_name(self):
        return self.region

    def __init__(self, region=None):
        super().__init__()
        self.region=region
        self.service_name='rds'

    def list_all_instances(self):
        svc = self.getClient(serviceName=self.service_name, region=self.region)
        marker = None
        fetchPending = True
        instances = []

        while fetchPending:
            if marker:
                result = svc.describe_db_instances(Marker=marker)
            else:
                result = svc.describe_db_instances()

            instances.extend(result['DBInstances'])

            if 'Marker' in result:
                marker = result['Marker']
                fetchPending = True
            else:
                fetchPending = False

        return instances

    def collect(self):
         return self.list_all_instances()
