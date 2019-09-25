from flask import json, route, request, Response, Flask

from generic import Workload, MountPoint, Credentials, Migration, MountPoint

workloads = {}
migrations = {}


@route('/workload', method=['POST'])
def workload_post(ip_addr):
    load = json.loads(request.json)
    credentials = Credentials.from_dict(**load['credentials'])
    storages = [MountPoint(**kwargs) for kwargs in load['storages']]
    workload = Workload(ip_addr, credentials, storages)
    workloads[ip_addr] = workload
    return Response(200)


@route('/workload', method=['PUT'])
def workload_put(ip_addr):
    workload = workloads.get(ip_addr, Workload(ip_addr, None, None))
    load = json.loads(request.json)
    data = {**workload.as_dict(), **load}
    workloads[ip_addr] = Workload.from_dict(**data)
    return Response(200)
    

@route('/workload', method=['DELETE'])
def workload_delete(ip_addr):
    del workloads[ip_addr]
    return Response(200)


@route('/migration', method=['POST'])
def migration_post(migration_id):
    load = json.loads(request.json)
    mount_points = [MountPoint(**kwargs) for kwargs in load['mount_points']]
    source = Workload.from_dict(**load['source'])
    credentials = Credentials.from_dict(**load['credentials'])
    target_vm = Workload.from_dict(**load['target'])
    target = MigrationTarget(
        load['cloud_type'], credentials, target_vm)
    migration = Migration(mount_points, source, target)


@route('/migration', method=['PUT'])
def migration_put(migration_id):
    ''' Its code is similar with previous '''


@route('/migration', method=['DELETE'])
def migration_delete(migration_id):
    ''' Its code is similar with previous '''


@route('/run_migration', method=['POST'])
def run_migration(migration_id):
    migration = migrations[migration_id]
    migration.run()
    return Response(200)


@route('/is_finished', method=['GET'])
def is_finished(migration_id):
    migration = migrations[migration_id]
    return Response(status=200, json=migration.state)


if __name__ == '__main__':
    app = Flask(__name__)
    app.run()
