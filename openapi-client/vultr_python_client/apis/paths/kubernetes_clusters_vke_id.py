from vultr_python_client.paths.kubernetes_clusters_vke_id.get import ApiForget
from vultr_python_client.paths.kubernetes_clusters_vke_id.put import ApiForput
from vultr_python_client.paths.kubernetes_clusters_vke_id.delete import ApiFordelete


class KubernetesClustersVkeId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
