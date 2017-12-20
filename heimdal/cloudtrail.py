from collectors import BaseCollector

class TrailsCollector(BaseCollector):
    @property
    def region_name(self):
        return self.region

    def __init__(self, region=None):
        super().__init__()
        self.region=region

    def list_all_trails(self):
        ct = self.getClient(serviceName='cloudtrail', region=self.region)
        trails = ct.describe_trails()
        if len(trails['trailList']) == 0:
            return []
        else:
            return trails['trailList']

    def collect(self):
         return self.list_all_trails()
