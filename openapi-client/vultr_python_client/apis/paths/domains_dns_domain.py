from vultr_python_client.paths.domains_dns_domain.get import ApiForget
from vultr_python_client.paths.domains_dns_domain.put import ApiForput
from vultr_python_client.paths.domains_dns_domain.delete import ApiFordelete


class DomainsDnsDomain(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
