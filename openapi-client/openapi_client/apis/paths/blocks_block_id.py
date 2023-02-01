from openapi_client.paths.blocks_block_id.get import ApiForget
from openapi_client.paths.blocks_block_id.delete import ApiFordelete
from openapi_client.paths.blocks_block_id.patch import ApiForpatch


class BlocksBlockId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
