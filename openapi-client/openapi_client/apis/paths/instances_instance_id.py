from openapi_client.paths.instances_instance_id.get import ApiForget
from openapi_client.paths.instances_instance_id.delete import ApiFordelete
from openapi_client.paths.instances_instance_id.patch import ApiForpatch


class InstancesInstanceId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
