from vultr_python_client.paths.reserved_ips.get import ApiForget
from vultr_python_client.paths.reserved_ips.post import ApiForpost


class ReservedIps(
    ApiForget,
    ApiForpost,
):
    pass
