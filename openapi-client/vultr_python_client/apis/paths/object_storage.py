from vultr_python_client.paths.object_storage.get import ApiForget
from vultr_python_client.paths.object_storage.post import ApiForpost


class ObjectStorage(
    ApiForget,
    ApiForpost,
):
    pass
