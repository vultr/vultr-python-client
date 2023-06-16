from vultr_python_client.paths.reserved_ips_reserved_ip.get import ApiForget
from vultr_python_client.paths.reserved_ips_reserved_ip.delete import ApiFordelete
from vultr_python_client.paths.reserved_ips_reserved_ip.patch import ApiForpatch


class ReservedIpsReservedIp(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
