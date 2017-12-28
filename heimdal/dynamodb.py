from collectors import BaseCollector

class TablesCollector(BaseCollector):
    @property
    def region_name(self):
        return self.region

    def __init__(self, region=None):
        super().__init__()
        self.region=region
        self.service_name='dynamodb'

    def list_all_tables(self):
        svc = self.getResource(serviceName=self.service_name, region=self.region)
        return svc.tables.all()

    def collect(self):
         return self.list_all_tables()

class StreamsCollector(BaseCollector):
    @property
    def region_name(self):
        return self.region

    def __init__(self, region=None):
        super().__init__()
        self.region=region
        self.service_name='dynamodbstreams'
        self.table = None

    def list_all_streams(self):
        svc = self.getClient(serviceName=self.service_name, region=self.region)
        marker = None
        fetchPending = True
        streams = []

        while fetchPending:
            if marker:
                if self.table:
                    result = svc.list_streams(TableName=self.table, ExclusiveStartStreamArn=marker)
                else:
                    result = svc.list_streams(ExclusiveStartStreamArn=marker)
            else:
                if self.table:
                    result = svc.list_streams(TableName=self.table)
                else:
                    result = svc.list_streams()

                streams.extend(result['Streams'])

            if 'Marker' in result:
                marker = result['LastEvaluatedStreamArn']
                fetchPending = True
            else:
                fetchPending = False

        return streams

    def collect(self):
         return self.list_all_streams()

class TableStreamsCollector(StreamsCollector):
    @property
    def region_name(self):
        return self.region

    @property
    def table_name(self):
        return self.table

    def __init__(self, table_name, region=None):
        self.table = table_name
        super().__init__()
        self.region=region
        self.service_name='dynamodbstreams'

