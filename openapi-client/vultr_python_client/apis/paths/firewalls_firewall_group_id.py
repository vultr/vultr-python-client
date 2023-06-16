from vultr_python_client.paths.firewalls_firewall_group_id.get import ApiForget
from vultr_python_client.paths.firewalls_firewall_group_id.put import ApiForput
from vultr_python_client.paths.firewalls_firewall_group_id.delete import ApiFordelete


class FirewallsFirewallGroupId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
