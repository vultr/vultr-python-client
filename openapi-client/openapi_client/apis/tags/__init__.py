# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_client.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    ACCOUNT = "account"
    APPLICATION = "application"
    BACKUP = "backup"
    BAREMETAL = "baremetal"
    BILLING = "billing"
    BLOCK = "block"
    DNS = "dns"
    FIREWALL = "firewall"
    INSTANCES = "instances"
    ISO = "iso"
    KUBERNETES = "kubernetes"
    LOADBALANCER = "load-balancer"
    S3 = "s3"
    OS = "os"
    PLANS = "plans"
    PRIVATE_NETWORKS = "private Networks"
    VPCS = "VPCs"
    RESERVEDIP = "reserved-ip"
    REGION = "region"
    SNAPSHOT = "snapshot"
    SSH = "ssh"
    STARTUP = "startup"
    USERS = "users"
