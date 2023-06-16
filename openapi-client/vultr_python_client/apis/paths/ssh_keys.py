from vultr_python_client.paths.ssh_keys.get import ApiForget
from vultr_python_client.paths.ssh_keys.post import ApiForpost


class SshKeys(
    ApiForget,
    ApiForpost,
):
    pass
