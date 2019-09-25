import time


class Credentials:
    def __init__(self, username, password, domain):
        if username is None:
            raise ValueError('username should not be None')

        if password is None:
            raise ValueError('password should not be None')
        
        self.username = str(username)
        self.password = str(password)
        self.domain = str(domain)

    @classmethod
    def from_dict(cls, **kwargs):
        return cls(**kwargs)
        
    def as_dict(self):
        return dict(
            username=self.username,
            password=self.password,
            domain=self.domain)


class MountPoint:
    def __init__(self, name, vol_size):
        self.name = str(name)
        self.vol_size = int(vol_size)

    @classmethod
    def from_dict(cls, **kwargs):
        return cls(**kwargs)
        
    def as_dict(self):
        return dict(
            name=self.name,
            vol_size=self.vol_size)


class Workload:
    def __init__(self, ip_addr, credentials, storages):
        if ip_addr is None:
            raise ValueError('ip_addr should not be None')
        
        self.__ip_addr = str(ip_addr)
        self.credentials = credentials
        self.storages = storages

    @property
    def ip_addr(self):
        return self.__ip_addr

    @ip_addr.setter
    def ip_addr(self, value):
        pass

    @classmethod
    def from_dict(cls, **kwargs):
        return cls(**kwargs)
    
    def as_dict(self):
        return dict(
            ip_addr=self.ip_addr,
            credentials=self.credentials.as_dict(),
            storages=[storage.as_dict() for storage in self.storages])


class MigrationTarget:
    
    _allowed_types = ('aws', 'azure', 'vsphere', 'vcloud')
    
    def __init__(self, cloud_type, credentials, target_vm):
        if cloud_type not in MigrationTarget._allowed_types:
            message = '{} - cloud_type of other types not allowed'
            ''.format(MigrationTarget._allowed_types)
            raise ValueError(message)
        
        self.cloud_type = cloud_type
        self.credentials = credentials
        self.target_vm = target_vm

    @classmethod
    def from_dict(cls, **kwargs):
        return cls(**kwargs)
        
    def as_dict(self):
        return dict(
            cloud_type=self.cloud_type,
            credentials=self.credentials.as_dict(),
            target_vm=self.target_vm.as_dict())


class Migration:
    _states = {0: 'Not started', 1: 'Running', 2: 'Error', 3: 'Success'}
    
    def __init__(self, mount_points, source, target, state=0):
        self.mount_points = mount_points
        self.source = source
        self.target = target
        self._state = state

    @property
    def state(self):
        return Migration._states[self._state]

    @state.setter
    def state_setter(self, value):
        self._state = value
        
    def run(self):
        if 'C:\\' not in self.mount_points:
            raise Exception(
                'Migration not allowed due to absence of '
                'C: in selected mount points')

        try:
            time.sleep(20)
        except Exception as e:
            print('Error occured during migration: {}'.format(e))
        else:
            source = self.source
            target_vm = Workload(
                source.ip_addr, source.credentials, self.mount_points)
            self.target.target_vm = target_vm

    @classmethod
    def from_dict(cls, **kwargs):
        return cls(**kwargs)

    def as_dict(self):
        return dict(
            mount_points=[storage.as_dict() for storage in self.mount_points],
            source=self.source.as_dict(),
            target=self.target.as_dict())

