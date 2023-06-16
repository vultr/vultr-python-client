from vultr_python_client.paths.snapshots_snapshot_id.get import ApiForget
from vultr_python_client.paths.snapshots_snapshot_id.put import ApiForput
from vultr_python_client.paths.snapshots_snapshot_id.delete import ApiFordelete


class SnapshotsSnapshotId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
