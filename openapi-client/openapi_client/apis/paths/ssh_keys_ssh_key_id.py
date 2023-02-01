from openapi_client.paths.ssh_keys_ssh_key_id.get import ApiForget
from openapi_client.paths.ssh_keys_ssh_key_id.delete import ApiFordelete
from openapi_client.paths.ssh_keys_ssh_key_id.patch import ApiForpatch


class SshKeysSshKeyId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
