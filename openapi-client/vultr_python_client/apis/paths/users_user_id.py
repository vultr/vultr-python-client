from vultr_python_client.paths.users_user_id.get import ApiForget
from vultr_python_client.paths.users_user_id.delete import ApiFordelete
from vultr_python_client.paths.users_user_id.patch import ApiForpatch


class UsersUserId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
