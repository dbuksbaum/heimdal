from collectors import BaseCollector

class UsersCollector(BaseCollector):
    @property
    def region_name(self):
        return self.region

    def __init__(self, region=None):
        super().__init__()
        self.region=region

    def list_all_users(self):
        return self.getResource(serviceName='iam', region=self.region).users.all()

    def collect(self):
         return self.list_all_users()


class GroupsCollector(BaseCollector):
    @property
    def region_name(self):
        return self.region

    def __init__(self, region=None):
        super().__init__()
        self.region=region

    def list_all_groups(self):
        return self.getResource(serviceName='iam', region=self.region).groups.all()

    def collect(self):
         return self.list_all_groups()


class RolesCollector(BaseCollector):
    @property
    def region_name(self):
        return self.region

    def __init__(self, region=None):
        super().__init__()
        self.region=region

    def list_all_roles(self):
        return self.getResource(serviceName='iam', region=self.region).roles.all()

    def collect(self):
         return self.list_all_roles()


class PolicyCollector(BaseCollector):
    @property
    def region_name(self):
        return self.region

    def __init__(self, region=None):
        super().__init__()
        self.region=region

    def list_all_policies(self):
        return self.getResource(serviceName='iam', region=self.region).policies.all()

    def collect(self):
         return self.list_all_policies()

