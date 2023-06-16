from vultr_python_client.paths.instances_instance_id.get import ApiForget
from vultr_python_client.paths.instances_instance_id.delete import ApiFordelete
from vultr_python_client.paths.instances_instance_id.patch import ApiForpatch


class InstancesInstanceId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
