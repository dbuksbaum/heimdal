from collectors import BaseCollector

class AlarmsCollector(BaseCollector):
    @property
    def region_name(self):
        return self.region

    def __init__(self, region=None):
        super().__init__()
        self.region=region

    def list_all_alarms(self):
        return self.getResource(serviceName='cloudwatch', region=self.region).alarms.all()

    def collect(self):
         return self.list_all_alarms()


class MetricsCollector(BaseCollector):
    @property
    def region_name(self):
        return self.region

    def __init__(self, region=None):
        super().__init__()
        self.region=region

    def list_all_metrics(self):
        return self.getResource(serviceName='cloudwatch', region=self.region).metrics.all()

    def collect(self):
         return self.list_all_metrics()
