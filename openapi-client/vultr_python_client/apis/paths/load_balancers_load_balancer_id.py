from vultr_python_client.paths.load_balancers_load_balancer_id.get import ApiForget
from vultr_python_client.paths.load_balancers_load_balancer_id.delete import ApiFordelete
from vultr_python_client.paths.load_balancers_load_balancer_id.patch import ApiForpatch


class LoadBalancersLoadBalancerId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
