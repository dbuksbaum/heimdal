from collectors import BaseCollector

class FunctionCollector(BaseCollector):
    @property
    def region_name(self):
        return self.region

    def __init__(self, region=None):
        super().__init__()
        self.region=region
        self.service_name='lambda'

    def list_all_functions(self):
        svc = self.getClient(serviceName=self.service_name, region=self.region)
        marker = None
        fetchPending = True
        functions = []

        while fetchPending:
            if marker:
                result = svc.list_functions(Marker=marker)
            else:
                result = svc.list_functions()

            functions.extend(result['Functions'])

            if 'NextMarker' in result:
                marker = result['NextMarker']
                fetchPending = True
            else:
                fetchPending = False

        return functions

    def collect(self):
         return self.list_all_functions()

class AliasCollector(BaseCollector):
    @property
    def region_name(self):
        return self.region

    @property
    def function_name(self):
        return self.function

    def __init__(self, function_name, region=None):
        super().__init__()
        self.region=region
        self.service_name='lambda'
        self.function=function_name

    def list_all_aliases(self):
        svc = self.getClient(serviceName=self.service_name, region=self.region)
        marker = None
        fetchPending = True
        aliases = []

        while fetchPending:
            if marker:
                result = svc.list_aliases(FunctionName=self.function, Marker=marker)
            else:
                result = svc.list_aliases(FunctionName=self.function)

            aliases.extend(result['Aliases'])

            if 'NextMarker' in result:
                marker = result['NextMarker']
                fetchPending = True
            else:
                fetchPending = False

        return aliases

    def collect(self):
         return self.list_all_aliases()

class EventSourceCollector(BaseCollector):
    @property
    def region_name(self):
        return self.region

    # @property
    # def function_name(self):
    #     return self.function

#function_name,
    def __init__(self, region=None):
        super().__init__()
        self.region=region
        self.service_name='lambda'
        #self.function=function_name

    def list_all_event_sources(self):
        svc = self.getClient(serviceName=self.service_name, region=self.region)
        marker = None
        fetchPending = True
        event_sources = []

        while fetchPending:
            #FunctionName=self.function
            if marker:
                result = svc.list_event_source_mappings(Marker=marker)
            else:
                result = svc.list_event_source_mappings()

            event_sources.extend(result['EventSourceMappings'])

            if 'NextMarker' in result:
                marker = result['NextMarker']
                fetchPending = True
            else:
                fetchPending = False

        return event_sources

    def collect(self):
         return self.list_all_event_sources()

