import abc
import boto3
from region_provider import RegionProvider

class BaseCollector:
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.region_provider = RegionProvider()

    @abc.abstractmethod
    def collect(self):
         """Method that should do something."""

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

    def getRegions(self, serviceName):
        return self.region_provider.get_service_region(serviceName)
