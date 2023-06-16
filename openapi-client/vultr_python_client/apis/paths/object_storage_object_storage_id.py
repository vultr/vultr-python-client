from vultr_python_client.paths.object_storage_object_storage_id.get import ApiForget
from vultr_python_client.paths.object_storage_object_storage_id.put import ApiForput
from vultr_python_client.paths.object_storage_object_storage_id.delete import ApiFordelete


class ObjectStorageObjectStorageId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
