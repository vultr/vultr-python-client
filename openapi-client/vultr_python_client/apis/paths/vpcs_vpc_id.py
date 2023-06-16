from vultr_python_client.paths.vpcs_vpc_id.get import ApiForget
from vultr_python_client.paths.vpcs_vpc_id.put import ApiForput
from vultr_python_client.paths.vpcs_vpc_id.delete import ApiFordelete


class VpcsVpcId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
