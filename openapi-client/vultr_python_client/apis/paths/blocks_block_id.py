from vultr_python_client.paths.blocks_block_id.get import ApiForget
from vultr_python_client.paths.blocks_block_id.delete import ApiFordelete
from vultr_python_client.paths.blocks_block_id.patch import ApiForpatch


class BlocksBlockId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
