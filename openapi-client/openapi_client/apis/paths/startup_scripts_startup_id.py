from openapi_client.paths.startup_scripts_startup_id.get import ApiForget
from openapi_client.paths.startup_scripts_startup_id.delete import ApiFordelete
from openapi_client.paths.startup_scripts_startup_id.patch import ApiForpatch


class StartupScriptsStartupId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
