from vultr_python_client.paths.bare_metals_baremetal_id.get import ApiForget
from vultr_python_client.paths.bare_metals_baremetal_id.delete import ApiFordelete
from vultr_python_client.paths.bare_metals_baremetal_id.patch import ApiForpatch


class BareMetalsBaremetalId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
