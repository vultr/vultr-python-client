from vultr_python_client.paths.private_networks_network_id.get import ApiForget
from vultr_python_client.paths.private_networks_network_id.put import ApiForput
from vultr_python_client.paths.private_networks_network_id.delete import ApiFordelete


class PrivateNetworksNetworkId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
