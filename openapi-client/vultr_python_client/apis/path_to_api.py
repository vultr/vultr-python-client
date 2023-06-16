import typing_extensions

from vultr_python_client.paths import PathValues
from vultr_python_client.apis.paths.private_networks_network_id import PrivateNetworksNetworkId
from vultr_python_client.apis.paths.private_networks import PrivateNetworks
from vultr_python_client.apis.paths.vpcs_vpc_id import VpcsVpcId
from vultr_python_client.apis.paths.vpcs import Vpcs
from vultr_python_client.apis.paths.users_user_id import UsersUserId
from vultr_python_client.apis.paths.users import Users
from vultr_python_client.apis.paths.startup_scripts_startup_id import StartupScriptsStartupId
from vultr_python_client.apis.paths.startup_scripts import StartupScripts
from vultr_python_client.apis.paths.ssh_keys_ssh_key_id import SshKeysSshKeyId
from vultr_python_client.apis.paths.ssh_keys import SshKeys
from vultr_python_client.apis.paths.snapshots_snapshot_id import SnapshotsSnapshotId
from vultr_python_client.apis.paths.snapshots import Snapshots
from vultr_python_client.apis.paths.snapshots_create_from_url import SnapshotsCreateFromUrl
from vultr_python_client.apis.paths.reserved_ips_reserved_ip import ReservedIpsReservedIp
from vultr_python_client.apis.paths.reserved_ips import ReservedIps
from vultr_python_client.apis.paths.reserved_ips_reserved_ip_attach import ReservedIpsReservedIpAttach
from vultr_python_client.apis.paths.reserved_ips_reserved_ip_detach import ReservedIpsReservedIpDetach
from vultr_python_client.apis.paths.reserved_ips_convert import ReservedIpsConvert
from vultr_python_client.apis.paths.os import Os
from vultr_python_client.apis.paths.applications import Applications
from vultr_python_client.apis.paths.account import Account
from vultr_python_client.apis.paths.backups import Backups
from vultr_python_client.apis.paths.blocks import Blocks
from vultr_python_client.apis.paths.blocks_block_id import BlocksBlockId
from vultr_python_client.apis.paths.blocks_block_id_attach import BlocksBlockIdAttach
from vultr_python_client.apis.paths.blocks_block_id_detach import BlocksBlockIdDetach
from vultr_python_client.apis.paths.firewalls import Firewalls
from vultr_python_client.apis.paths.firewalls_firewall_group_id import FirewallsFirewallGroupId
from vultr_python_client.apis.paths.firewalls_firewall_group_id_rules import FirewallsFirewallGroupIdRules
from vultr_python_client.apis.paths.firewalls_firewall_group_id_rules_firewall_rule_id import FirewallsFirewallGroupIdRulesFirewallRuleId
from vultr_python_client.apis.paths.iso import Iso
from vultr_python_client.apis.paths.iso_iso_id import IsoIsoId
from vultr_python_client.apis.paths.iso_public import IsoPublic
from vultr_python_client.apis.paths.object_storage import ObjectStorage
from vultr_python_client.apis.paths.object_storage_object_storage_id import ObjectStorageObjectStorageId
from vultr_python_client.apis.paths.object_storage_object_storage_id_regenerate_keys import ObjectStorageObjectStorageIdRegenerateKeys
from vultr_python_client.apis.paths.object_storage_clusters import ObjectStorageClusters
from vultr_python_client.apis.paths.domains import Domains
from vultr_python_client.apis.paths.domains_dns_domain import DomainsDnsDomain
from vultr_python_client.apis.paths.domains_dns_domain_soa import DomainsDnsDomainSoa
from vultr_python_client.apis.paths.domains_dns_domain_dnssec import DomainsDnsDomainDnssec
from vultr_python_client.apis.paths.domains_dns_domain_records import DomainsDnsDomainRecords
from vultr_python_client.apis.paths.domains_dns_domain_records_record_id import DomainsDnsDomainRecordsRecordId
from vultr_python_client.apis.paths.regions import Regions
from vultr_python_client.apis.paths.regions_region_id_availability import RegionsRegionIdAvailability
from vultr_python_client.apis.paths.load_balancers import LoadBalancers
from vultr_python_client.apis.paths.load_balancers_load_balancer_id import LoadBalancersLoadBalancerId
from vultr_python_client.apis.paths.load_balancers_load_balancer_id_forwarding_rules import LoadBalancersLoadBalancerIdForwardingRules
from vultr_python_client.apis.paths.load_balancers_load_balancer_id_forwarding_rules_forwarding_rule_id import LoadBalancersLoadBalancerIdForwardingRulesForwardingRuleId
from vultr_python_client.apis.paths.plans import Plans
from vultr_python_client.apis.paths.plans_metal import PlansMetal
from vultr_python_client.apis.paths.bare_metals import BareMetals
from vultr_python_client.apis.paths.bare_metals_baremetal_id import BareMetalsBaremetalId
from vultr_python_client.apis.paths.bare_metals_baremetal_id_ipv4 import BareMetalsBaremetalIdIpv4
from vultr_python_client.apis.paths.bare_metals_baremetal_id_ipv6 import BareMetalsBaremetalIdIpv6
from vultr_python_client.apis.paths.bare_metals_baremetal_id_start import BareMetalsBaremetalIdStart
from vultr_python_client.apis.paths.bare_metals_baremetal_id_reboot import BareMetalsBaremetalIdReboot
from vultr_python_client.apis.paths.bare_metals_baremetal_id_reinstall import BareMetalsBaremetalIdReinstall
from vultr_python_client.apis.paths.bare_metals_baremetal_id_halt import BareMetalsBaremetalIdHalt
from vultr_python_client.apis.paths.bare_metals_baremetal_id_bandwidth import BareMetalsBaremetalIdBandwidth
from vultr_python_client.apis.paths.bare_metals_halt import BareMetalsHalt
from vultr_python_client.apis.paths.bare_metals_reboot import BareMetalsReboot
from vultr_python_client.apis.paths.bare_metals_start import BareMetalsStart
from vultr_python_client.apis.paths.bare_metals_baremetal_id_user_data import BareMetalsBaremetalIdUserData
from vultr_python_client.apis.paths.instances import Instances
from vultr_python_client.apis.paths.instances_instance_id import InstancesInstanceId
from vultr_python_client.apis.paths.instances_halt import InstancesHalt
from vultr_python_client.apis.paths.instances_reboot import InstancesReboot
from vultr_python_client.apis.paths.instances_start import InstancesStart
from vultr_python_client.apis.paths.instances_instance_id_start import InstancesInstanceIdStart
from vultr_python_client.apis.paths.instances_instance_id_reboot import InstancesInstanceIdReboot
from vultr_python_client.apis.paths.instances_instance_id_reinstall import InstancesInstanceIdReinstall
from vultr_python_client.apis.paths.instances_instance_id_bandwidth import InstancesInstanceIdBandwidth
from vultr_python_client.apis.paths.instances_instance_id_neighbors import InstancesInstanceIdNeighbors
from vultr_python_client.apis.paths.instances_instance_id_private_networks import InstancesInstanceIdPrivateNetworks
from vultr_python_client.apis.paths.instances_instance_id_vpcs import InstancesInstanceIdVpcs
from vultr_python_client.apis.paths.instances_instance_id_iso import InstancesInstanceIdIso
from vultr_python_client.apis.paths.instances_instance_id_iso_attach import InstancesInstanceIdIsoAttach
from vultr_python_client.apis.paths.instances_instance_id_iso_detach import InstancesInstanceIdIsoDetach
from vultr_python_client.apis.paths.instances_instance_id_private_networks_attach import InstancesInstanceIdPrivateNetworksAttach
from vultr_python_client.apis.paths.instances_instance_id_private_networks_detach import InstancesInstanceIdPrivateNetworksDetach
from vultr_python_client.apis.paths.instances_instance_id_vpcs_attach import InstancesInstanceIdVpcsAttach
from vultr_python_client.apis.paths.instances_instance_id_vpcs_detach import InstancesInstanceIdVpcsDetach
from vultr_python_client.apis.paths.instances_instance_id_backup_schedule import InstancesInstanceIdBackupSchedule
from vultr_python_client.apis.paths.instances_instance_id_restore import InstancesInstanceIdRestore
from vultr_python_client.apis.paths.instances_instance_id_ipv4 import InstancesInstanceIdIpv4
from vultr_python_client.apis.paths.instances_instance_id_ipv6 import InstancesInstanceIdIpv6
from vultr_python_client.apis.paths.instances_instance_id_ipv6_reverse import InstancesInstanceIdIpv6Reverse
from vultr_python_client.apis.paths.instances_instance_id_ipv4_reverse import InstancesInstanceIdIpv4Reverse
from vultr_python_client.apis.paths.backups_backup_id import BackupsBackupId
from vultr_python_client.apis.paths.instances_instance_id_user_data import InstancesInstanceIdUserData
from vultr_python_client.apis.paths.instances_instance_id_halt import InstancesInstanceIdHalt
from vultr_python_client.apis.paths.instances_instance_id_ipv4_reverse_default import InstancesInstanceIdIpv4ReverseDefault
from vultr_python_client.apis.paths.instances_instance_id_ipv4_ipv4 import InstancesInstanceIdIpv4Ipv4
from vultr_python_client.apis.paths.instances_instance_id_ipv6_reverse_ipv6 import InstancesInstanceIdIpv6ReverseIpv6
from vultr_python_client.apis.paths.instances_instance_id_upgrades import InstancesInstanceIdUpgrades
from vultr_python_client.apis.paths.bare_metals_baremetal_id_upgrades import BareMetalsBaremetalIdUpgrades
from vultr_python_client.apis.paths.bare_metals_baremetal_id_vnc import BareMetalsBaremetalIdVnc
from vultr_python_client.apis.paths.load_balancers_loadbalancer_id_firewall_rules import LoadBalancersLoadbalancerIdFirewallRules
from vultr_python_client.apis.paths.load_balancers_loadbalancer_id_firewall_rules_firewall_rule_id import LoadBalancersLoadbalancerIdFirewallRulesFirewallRuleId
from vultr_python_client.apis.paths.kubernetes_clusters import KubernetesClusters
from vultr_python_client.apis.paths.kubernetes_clusters_vke_id import KubernetesClustersVkeId
from vultr_python_client.apis.paths.kubernetes_clusters_vke_id_delete_with_linked_resources import KubernetesClustersVkeIdDeleteWithLinkedResources
from vultr_python_client.apis.paths.kubernetes_clusters_vke_id_resources import KubernetesClustersVkeIdResources
from vultr_python_client.apis.paths.kubernetes_clusters_vke_id_available_upgrades import KubernetesClustersVkeIdAvailableUpgrades
from vultr_python_client.apis.paths.kubernetes_clusters_vke_id_upgrades import KubernetesClustersVkeIdUpgrades
from vultr_python_client.apis.paths.kubernetes_clusters_vke_id_node_pools import KubernetesClustersVkeIdNodePools
from vultr_python_client.apis.paths.kubernetes_clusters_vke_id_node_pools_nodepool_id import KubernetesClustersVkeIdNodePoolsNodepoolId
from vultr_python_client.apis.paths.kubernetes_clusters_vke_id_node_pools_nodepool_id_nodes_node_id import KubernetesClustersVkeIdNodePoolsNodepoolIdNodesNodeId
from vultr_python_client.apis.paths.kubernetes_clusters_vke_id_node_pools_nodepool_id_nodes_node_id_recycle import KubernetesClustersVkeIdNodePoolsNodepoolIdNodesNodeIdRecycle
from vultr_python_client.apis.paths.kubernetes_clusters_vke_id_config import KubernetesClustersVkeIdConfig
from vultr_python_client.apis.paths.kubernetes_versions import KubernetesVersions
from vultr_python_client.apis.paths.billing_history import BillingHistory
from vultr_python_client.apis.paths.billing_invoices import BillingInvoices
from vultr_python_client.apis.paths.billing_invoices_invoice_id import BillingInvoicesInvoiceId
from vultr_python_client.apis.paths.billing_invoices_invoice_id_items import BillingInvoicesInvoiceIdItems

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.PRIVATENETWORKS_NETWORKID: PrivateNetworksNetworkId,
        PathValues.PRIVATENETWORKS: PrivateNetworks,
        PathValues.VPCS_VPCID: VpcsVpcId,
        PathValues.VPCS: Vpcs,
        PathValues.USERS_USERID: UsersUserId,
        PathValues.USERS: Users,
        PathValues.STARTUPSCRIPTS_STARTUPID: StartupScriptsStartupId,
        PathValues.STARTUPSCRIPTS: StartupScripts,
        PathValues.SSHKEYS_SSHKEYID: SshKeysSshKeyId,
        PathValues.SSHKEYS: SshKeys,
        PathValues.SNAPSHOTS_SNAPSHOTID: SnapshotsSnapshotId,
        PathValues.SNAPSHOTS: Snapshots,
        PathValues.SNAPSHOTS_CREATEFROMURL: SnapshotsCreateFromUrl,
        PathValues.RESERVEDIPS_RESERVEDIP: ReservedIpsReservedIp,
        PathValues.RESERVEDIPS: ReservedIps,
        PathValues.RESERVEDIPS_RESERVEDIP_ATTACH: ReservedIpsReservedIpAttach,
        PathValues.RESERVEDIPS_RESERVEDIP_DETACH: ReservedIpsReservedIpDetach,
        PathValues.RESERVEDIPS_CONVERT: ReservedIpsConvert,
        PathValues.OS: Os,
        PathValues.APPLICATIONS: Applications,
        PathValues.ACCOUNT: Account,
        PathValues.BACKUPS: Backups,
        PathValues.BLOCKS: Blocks,
        PathValues.BLOCKS_BLOCKID: BlocksBlockId,
        PathValues.BLOCKS_BLOCKID_ATTACH: BlocksBlockIdAttach,
        PathValues.BLOCKS_BLOCKID_DETACH: BlocksBlockIdDetach,
        PathValues.FIREWALLS: Firewalls,
        PathValues.FIREWALLS_FIREWALLGROUPID: FirewallsFirewallGroupId,
        PathValues.FIREWALLS_FIREWALLGROUPID_RULES: FirewallsFirewallGroupIdRules,
        PathValues.FIREWALLS_FIREWALLGROUPID_RULES_FIREWALLRULEID: FirewallsFirewallGroupIdRulesFirewallRuleId,
        PathValues.ISO: Iso,
        PathValues.ISO_ISOID: IsoIsoId,
        PathValues.ISOPUBLIC: IsoPublic,
        PathValues.OBJECTSTORAGE: ObjectStorage,
        PathValues.OBJECTSTORAGE_OBJECTSTORAGEID: ObjectStorageObjectStorageId,
        PathValues.OBJECTSTORAGE_OBJECTSTORAGEID_REGENERATEKEYS: ObjectStorageObjectStorageIdRegenerateKeys,
        PathValues.OBJECTSTORAGE_CLUSTERS: ObjectStorageClusters,
        PathValues.DOMAINS: Domains,
        PathValues.DOMAINS_DNSDOMAIN: DomainsDnsDomain,
        PathValues.DOMAINS_DNSDOMAIN_SOA: DomainsDnsDomainSoa,
        PathValues.DOMAINS_DNSDOMAIN_DNSSEC: DomainsDnsDomainDnssec,
        PathValues.DOMAINS_DNSDOMAIN_RECORDS: DomainsDnsDomainRecords,
        PathValues.DOMAINS_DNSDOMAIN_RECORDS_RECORDID: DomainsDnsDomainRecordsRecordId,
        PathValues.REGIONS: Regions,
        PathValues.REGIONS_REGIONID_AVAILABILITY: RegionsRegionIdAvailability,
        PathValues.LOADBALANCERS: LoadBalancers,
        PathValues.LOADBALANCERS_LOADBALANCERID: LoadBalancersLoadBalancerId,
        PathValues.LOADBALANCERS_LOADBALANCERID_FORWARDINGRULES: LoadBalancersLoadBalancerIdForwardingRules,
        PathValues.LOADBALANCERS_LOADBALANCERID_FORWARDINGRULES_FORWARDINGRULEID: LoadBalancersLoadBalancerIdForwardingRulesForwardingRuleId,
        PathValues.PLANS: Plans,
        PathValues.PLANSMETAL: PlansMetal,
        PathValues.BAREMETALS: BareMetals,
        PathValues.BAREMETALS_BAREMETALID: BareMetalsBaremetalId,
        PathValues.BAREMETALS_BAREMETALID_IPV4: BareMetalsBaremetalIdIpv4,
        PathValues.BAREMETALS_BAREMETALID_IPV6: BareMetalsBaremetalIdIpv6,
        PathValues.BAREMETALS_BAREMETALID_START: BareMetalsBaremetalIdStart,
        PathValues.BAREMETALS_BAREMETALID_REBOOT: BareMetalsBaremetalIdReboot,
        PathValues.BAREMETALS_BAREMETALID_REINSTALL: BareMetalsBaremetalIdReinstall,
        PathValues.BAREMETALS_BAREMETALID_HALT: BareMetalsBaremetalIdHalt,
        PathValues.BAREMETALS_BAREMETALID_BANDWIDTH: BareMetalsBaremetalIdBandwidth,
        PathValues.BAREMETALS_HALT: BareMetalsHalt,
        PathValues.BAREMETALS_REBOOT: BareMetalsReboot,
        PathValues.BAREMETALS_START: BareMetalsStart,
        PathValues.BAREMETALS_BAREMETALID_USERDATA: BareMetalsBaremetalIdUserData,
        PathValues.INSTANCES: Instances,
        PathValues.INSTANCES_INSTANCEID: InstancesInstanceId,
        PathValues.INSTANCES_HALT: InstancesHalt,
        PathValues.INSTANCES_REBOOT: InstancesReboot,
        PathValues.INSTANCES_START: InstancesStart,
        PathValues.INSTANCES_INSTANCEID_START: InstancesInstanceIdStart,
        PathValues.INSTANCES_INSTANCEID_REBOOT: InstancesInstanceIdReboot,
        PathValues.INSTANCES_INSTANCEID_REINSTALL: InstancesInstanceIdReinstall,
        PathValues.INSTANCES_INSTANCEID_BANDWIDTH: InstancesInstanceIdBandwidth,
        PathValues.INSTANCES_INSTANCEID_NEIGHBORS: InstancesInstanceIdNeighbors,
        PathValues.INSTANCES_INSTANCEID_PRIVATENETWORKS: InstancesInstanceIdPrivateNetworks,
        PathValues.INSTANCES_INSTANCEID_VPCS: InstancesInstanceIdVpcs,
        PathValues.INSTANCES_INSTANCEID_ISO: InstancesInstanceIdIso,
        PathValues.INSTANCES_INSTANCEID_ISO_ATTACH: InstancesInstanceIdIsoAttach,
        PathValues.INSTANCES_INSTANCEID_ISO_DETACH: InstancesInstanceIdIsoDetach,
        PathValues.INSTANCES_INSTANCEID_PRIVATENETWORKS_ATTACH: InstancesInstanceIdPrivateNetworksAttach,
        PathValues.INSTANCES_INSTANCEID_PRIVATENETWORKS_DETACH: InstancesInstanceIdPrivateNetworksDetach,
        PathValues.INSTANCES_INSTANCEID_VPCS_ATTACH: InstancesInstanceIdVpcsAttach,
        PathValues.INSTANCES_INSTANCEID_VPCS_DETACH: InstancesInstanceIdVpcsDetach,
        PathValues.INSTANCES_INSTANCEID_BACKUPSCHEDULE: InstancesInstanceIdBackupSchedule,
        PathValues.INSTANCES_INSTANCEID_RESTORE: InstancesInstanceIdRestore,
        PathValues.INSTANCES_INSTANCEID_IPV4: InstancesInstanceIdIpv4,
        PathValues.INSTANCES_INSTANCEID_IPV6: InstancesInstanceIdIpv6,
        PathValues.INSTANCES_INSTANCEID_IPV6_REVERSE: InstancesInstanceIdIpv6Reverse,
        PathValues.INSTANCES_INSTANCEID_IPV4_REVERSE: InstancesInstanceIdIpv4Reverse,
        PathValues.BACKUPS_BACKUPID: BackupsBackupId,
        PathValues.INSTANCES_INSTANCEID_USERDATA: InstancesInstanceIdUserData,
        PathValues.INSTANCES_INSTANCEID_HALT: InstancesInstanceIdHalt,
        PathValues.INSTANCES_INSTANCEID_IPV4_REVERSE_DEFAULT: InstancesInstanceIdIpv4ReverseDefault,
        PathValues.INSTANCES_INSTANCEID_IPV4_IPV4: InstancesInstanceIdIpv4Ipv4,
        PathValues.INSTANCES_INSTANCEID_IPV6_REVERSE_IPV6: InstancesInstanceIdIpv6ReverseIpv6,
        PathValues.INSTANCES_INSTANCEID_UPGRADES: InstancesInstanceIdUpgrades,
        PathValues.BAREMETALS_BAREMETALID_UPGRADES: BareMetalsBaremetalIdUpgrades,
        PathValues.BAREMETALS_BAREMETALID_VNC: BareMetalsBaremetalIdVnc,
        PathValues.LOADBALANCERS_LOADBALANCERID_FIREWALLRULES: LoadBalancersLoadbalancerIdFirewallRules,
        PathValues.LOADBALANCERS_LOADBALANCERID_FIREWALLRULES_FIREWALLRULEID: LoadBalancersLoadbalancerIdFirewallRulesFirewallRuleId,
        PathValues.KUBERNETES_CLUSTERS: KubernetesClusters,
        PathValues.KUBERNETES_CLUSTERS_VKEID: KubernetesClustersVkeId,
        PathValues.KUBERNETES_CLUSTERS_VKEID_DELETEWITHLINKEDRESOURCES: KubernetesClustersVkeIdDeleteWithLinkedResources,
        PathValues.KUBERNETES_CLUSTERS_VKEID_RESOURCES: KubernetesClustersVkeIdResources,
        PathValues.KUBERNETES_CLUSTERS_VKEID_AVAILABLEUPGRADES: KubernetesClustersVkeIdAvailableUpgrades,
        PathValues.KUBERNETES_CLUSTERS_VKEID_UPGRADES: KubernetesClustersVkeIdUpgrades,
        PathValues.KUBERNETES_CLUSTERS_VKEID_NODEPOOLS: KubernetesClustersVkeIdNodePools,
        PathValues.KUBERNETES_CLUSTERS_VKEID_NODEPOOLS_NODEPOOLID: KubernetesClustersVkeIdNodePoolsNodepoolId,
        PathValues.KUBERNETES_CLUSTERS_VKEID_NODEPOOLS_NODEPOOLID_NODES_NODEID: KubernetesClustersVkeIdNodePoolsNodepoolIdNodesNodeId,
        PathValues.KUBERNETES_CLUSTERS_VKEID_NODEPOOLS_NODEPOOLID_NODES_NODEID_RECYCLE: KubernetesClustersVkeIdNodePoolsNodepoolIdNodesNodeIdRecycle,
        PathValues.KUBERNETES_CLUSTERS_VKEID_CONFIG: KubernetesClustersVkeIdConfig,
        PathValues.KUBERNETES_VERSIONS: KubernetesVersions,
        PathValues.BILLING_HISTORY: BillingHistory,
        PathValues.BILLING_INVOICES: BillingInvoices,
        PathValues.BILLING_INVOICES_INVOICEID: BillingInvoicesInvoiceId,
        PathValues.BILLING_INVOICES_INVOICEID_ITEMS: BillingInvoicesInvoiceIdItems,
    }
)

path_to_api = PathToApi(
    {
        PathValues.PRIVATENETWORKS_NETWORKID: PrivateNetworksNetworkId,
        PathValues.PRIVATENETWORKS: PrivateNetworks,
        PathValues.VPCS_VPCID: VpcsVpcId,
        PathValues.VPCS: Vpcs,
        PathValues.USERS_USERID: UsersUserId,
        PathValues.USERS: Users,
        PathValues.STARTUPSCRIPTS_STARTUPID: StartupScriptsStartupId,
        PathValues.STARTUPSCRIPTS: StartupScripts,
        PathValues.SSHKEYS_SSHKEYID: SshKeysSshKeyId,
        PathValues.SSHKEYS: SshKeys,
        PathValues.SNAPSHOTS_SNAPSHOTID: SnapshotsSnapshotId,
        PathValues.SNAPSHOTS: Snapshots,
        PathValues.SNAPSHOTS_CREATEFROMURL: SnapshotsCreateFromUrl,
        PathValues.RESERVEDIPS_RESERVEDIP: ReservedIpsReservedIp,
        PathValues.RESERVEDIPS: ReservedIps,
        PathValues.RESERVEDIPS_RESERVEDIP_ATTACH: ReservedIpsReservedIpAttach,
        PathValues.RESERVEDIPS_RESERVEDIP_DETACH: ReservedIpsReservedIpDetach,
        PathValues.RESERVEDIPS_CONVERT: ReservedIpsConvert,
        PathValues.OS: Os,
        PathValues.APPLICATIONS: Applications,
        PathValues.ACCOUNT: Account,
        PathValues.BACKUPS: Backups,
        PathValues.BLOCKS: Blocks,
        PathValues.BLOCKS_BLOCKID: BlocksBlockId,
        PathValues.BLOCKS_BLOCKID_ATTACH: BlocksBlockIdAttach,
        PathValues.BLOCKS_BLOCKID_DETACH: BlocksBlockIdDetach,
        PathValues.FIREWALLS: Firewalls,
        PathValues.FIREWALLS_FIREWALLGROUPID: FirewallsFirewallGroupId,
        PathValues.FIREWALLS_FIREWALLGROUPID_RULES: FirewallsFirewallGroupIdRules,
        PathValues.FIREWALLS_FIREWALLGROUPID_RULES_FIREWALLRULEID: FirewallsFirewallGroupIdRulesFirewallRuleId,
        PathValues.ISO: Iso,
        PathValues.ISO_ISOID: IsoIsoId,
        PathValues.ISOPUBLIC: IsoPublic,
        PathValues.OBJECTSTORAGE: ObjectStorage,
        PathValues.OBJECTSTORAGE_OBJECTSTORAGEID: ObjectStorageObjectStorageId,
        PathValues.OBJECTSTORAGE_OBJECTSTORAGEID_REGENERATEKEYS: ObjectStorageObjectStorageIdRegenerateKeys,
        PathValues.OBJECTSTORAGE_CLUSTERS: ObjectStorageClusters,
        PathValues.DOMAINS: Domains,
        PathValues.DOMAINS_DNSDOMAIN: DomainsDnsDomain,
        PathValues.DOMAINS_DNSDOMAIN_SOA: DomainsDnsDomainSoa,
        PathValues.DOMAINS_DNSDOMAIN_DNSSEC: DomainsDnsDomainDnssec,
        PathValues.DOMAINS_DNSDOMAIN_RECORDS: DomainsDnsDomainRecords,
        PathValues.DOMAINS_DNSDOMAIN_RECORDS_RECORDID: DomainsDnsDomainRecordsRecordId,
        PathValues.REGIONS: Regions,
        PathValues.REGIONS_REGIONID_AVAILABILITY: RegionsRegionIdAvailability,
        PathValues.LOADBALANCERS: LoadBalancers,
        PathValues.LOADBALANCERS_LOADBALANCERID: LoadBalancersLoadBalancerId,
        PathValues.LOADBALANCERS_LOADBALANCERID_FORWARDINGRULES: LoadBalancersLoadBalancerIdForwardingRules,
        PathValues.LOADBALANCERS_LOADBALANCERID_FORWARDINGRULES_FORWARDINGRULEID: LoadBalancersLoadBalancerIdForwardingRulesForwardingRuleId,
        PathValues.PLANS: Plans,
        PathValues.PLANSMETAL: PlansMetal,
        PathValues.BAREMETALS: BareMetals,
        PathValues.BAREMETALS_BAREMETALID: BareMetalsBaremetalId,
        PathValues.BAREMETALS_BAREMETALID_IPV4: BareMetalsBaremetalIdIpv4,
        PathValues.BAREMETALS_BAREMETALID_IPV6: BareMetalsBaremetalIdIpv6,
        PathValues.BAREMETALS_BAREMETALID_START: BareMetalsBaremetalIdStart,
        PathValues.BAREMETALS_BAREMETALID_REBOOT: BareMetalsBaremetalIdReboot,
        PathValues.BAREMETALS_BAREMETALID_REINSTALL: BareMetalsBaremetalIdReinstall,
        PathValues.BAREMETALS_BAREMETALID_HALT: BareMetalsBaremetalIdHalt,
        PathValues.BAREMETALS_BAREMETALID_BANDWIDTH: BareMetalsBaremetalIdBandwidth,
        PathValues.BAREMETALS_HALT: BareMetalsHalt,
        PathValues.BAREMETALS_REBOOT: BareMetalsReboot,
        PathValues.BAREMETALS_START: BareMetalsStart,
        PathValues.BAREMETALS_BAREMETALID_USERDATA: BareMetalsBaremetalIdUserData,
        PathValues.INSTANCES: Instances,
        PathValues.INSTANCES_INSTANCEID: InstancesInstanceId,
        PathValues.INSTANCES_HALT: InstancesHalt,
        PathValues.INSTANCES_REBOOT: InstancesReboot,
        PathValues.INSTANCES_START: InstancesStart,
        PathValues.INSTANCES_INSTANCEID_START: InstancesInstanceIdStart,
        PathValues.INSTANCES_INSTANCEID_REBOOT: InstancesInstanceIdReboot,
        PathValues.INSTANCES_INSTANCEID_REINSTALL: InstancesInstanceIdReinstall,
        PathValues.INSTANCES_INSTANCEID_BANDWIDTH: InstancesInstanceIdBandwidth,
        PathValues.INSTANCES_INSTANCEID_NEIGHBORS: InstancesInstanceIdNeighbors,
        PathValues.INSTANCES_INSTANCEID_PRIVATENETWORKS: InstancesInstanceIdPrivateNetworks,
        PathValues.INSTANCES_INSTANCEID_VPCS: InstancesInstanceIdVpcs,
        PathValues.INSTANCES_INSTANCEID_ISO: InstancesInstanceIdIso,
        PathValues.INSTANCES_INSTANCEID_ISO_ATTACH: InstancesInstanceIdIsoAttach,
        PathValues.INSTANCES_INSTANCEID_ISO_DETACH: InstancesInstanceIdIsoDetach,
        PathValues.INSTANCES_INSTANCEID_PRIVATENETWORKS_ATTACH: InstancesInstanceIdPrivateNetworksAttach,
        PathValues.INSTANCES_INSTANCEID_PRIVATENETWORKS_DETACH: InstancesInstanceIdPrivateNetworksDetach,
        PathValues.INSTANCES_INSTANCEID_VPCS_ATTACH: InstancesInstanceIdVpcsAttach,
        PathValues.INSTANCES_INSTANCEID_VPCS_DETACH: InstancesInstanceIdVpcsDetach,
        PathValues.INSTANCES_INSTANCEID_BACKUPSCHEDULE: InstancesInstanceIdBackupSchedule,
        PathValues.INSTANCES_INSTANCEID_RESTORE: InstancesInstanceIdRestore,
        PathValues.INSTANCES_INSTANCEID_IPV4: InstancesInstanceIdIpv4,
        PathValues.INSTANCES_INSTANCEID_IPV6: InstancesInstanceIdIpv6,
        PathValues.INSTANCES_INSTANCEID_IPV6_REVERSE: InstancesInstanceIdIpv6Reverse,
        PathValues.INSTANCES_INSTANCEID_IPV4_REVERSE: InstancesInstanceIdIpv4Reverse,
        PathValues.BACKUPS_BACKUPID: BackupsBackupId,
        PathValues.INSTANCES_INSTANCEID_USERDATA: InstancesInstanceIdUserData,
        PathValues.INSTANCES_INSTANCEID_HALT: InstancesInstanceIdHalt,
        PathValues.INSTANCES_INSTANCEID_IPV4_REVERSE_DEFAULT: InstancesInstanceIdIpv4ReverseDefault,
        PathValues.INSTANCES_INSTANCEID_IPV4_IPV4: InstancesInstanceIdIpv4Ipv4,
        PathValues.INSTANCES_INSTANCEID_IPV6_REVERSE_IPV6: InstancesInstanceIdIpv6ReverseIpv6,
        PathValues.INSTANCES_INSTANCEID_UPGRADES: InstancesInstanceIdUpgrades,
        PathValues.BAREMETALS_BAREMETALID_UPGRADES: BareMetalsBaremetalIdUpgrades,
        PathValues.BAREMETALS_BAREMETALID_VNC: BareMetalsBaremetalIdVnc,
        PathValues.LOADBALANCERS_LOADBALANCERID_FIREWALLRULES: LoadBalancersLoadbalancerIdFirewallRules,
        PathValues.LOADBALANCERS_LOADBALANCERID_FIREWALLRULES_FIREWALLRULEID: LoadBalancersLoadbalancerIdFirewallRulesFirewallRuleId,
        PathValues.KUBERNETES_CLUSTERS: KubernetesClusters,
        PathValues.KUBERNETES_CLUSTERS_VKEID: KubernetesClustersVkeId,
        PathValues.KUBERNETES_CLUSTERS_VKEID_DELETEWITHLINKEDRESOURCES: KubernetesClustersVkeIdDeleteWithLinkedResources,
        PathValues.KUBERNETES_CLUSTERS_VKEID_RESOURCES: KubernetesClustersVkeIdResources,
        PathValues.KUBERNETES_CLUSTERS_VKEID_AVAILABLEUPGRADES: KubernetesClustersVkeIdAvailableUpgrades,
        PathValues.KUBERNETES_CLUSTERS_VKEID_UPGRADES: KubernetesClustersVkeIdUpgrades,
        PathValues.KUBERNETES_CLUSTERS_VKEID_NODEPOOLS: KubernetesClustersVkeIdNodePools,
        PathValues.KUBERNETES_CLUSTERS_VKEID_NODEPOOLS_NODEPOOLID: KubernetesClustersVkeIdNodePoolsNodepoolId,
        PathValues.KUBERNETES_CLUSTERS_VKEID_NODEPOOLS_NODEPOOLID_NODES_NODEID: KubernetesClustersVkeIdNodePoolsNodepoolIdNodesNodeId,
        PathValues.KUBERNETES_CLUSTERS_VKEID_NODEPOOLS_NODEPOOLID_NODES_NODEID_RECYCLE: KubernetesClustersVkeIdNodePoolsNodepoolIdNodesNodeIdRecycle,
        PathValues.KUBERNETES_CLUSTERS_VKEID_CONFIG: KubernetesClustersVkeIdConfig,
        PathValues.KUBERNETES_VERSIONS: KubernetesVersions,
        PathValues.BILLING_HISTORY: BillingHistory,
        PathValues.BILLING_INVOICES: BillingInvoices,
        PathValues.BILLING_INVOICES_INVOICEID: BillingInvoicesInvoiceId,
        PathValues.BILLING_INVOICES_INVOICEID_ITEMS: BillingInvoicesInvoiceIdItems,
    }
)
