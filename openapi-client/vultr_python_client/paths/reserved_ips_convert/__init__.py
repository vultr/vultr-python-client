# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_client.paths.reserved_ips_convert import Api

from vultr_python_client.paths import PathValues

path = PathValues.RESERVEDIPS_CONVERT