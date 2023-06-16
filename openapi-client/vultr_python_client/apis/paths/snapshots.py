from vultr_python_client.paths.snapshots.get import ApiForget
from vultr_python_client.paths.snapshots.post import ApiForpost


class Snapshots(
    ApiForget,
    ApiForpost,
):
    pass
