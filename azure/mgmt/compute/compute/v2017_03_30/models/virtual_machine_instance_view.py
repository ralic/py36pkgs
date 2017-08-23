# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class VirtualMachineInstanceView(Model):
    """The instance view of a virtual machine.

    :param platform_update_domain: Specifies the update domain of the virtual
     machine.
    :type platform_update_domain: int
    :param platform_fault_domain: Specifies the fault domain of the virtual
     machine.
    :type platform_fault_domain: int
    :param rdp_thumb_print: The Remote desktop certificate thumbprint.
    :type rdp_thumb_print: str
    :param vm_agent: The VM Agent running on the virtual machine.
    :type vm_agent: :class:`VirtualMachineAgentInstanceView
     <azure.mgmt.compute.compute.v2017_03_30.models.VirtualMachineAgentInstanceView>`
    :param maintenance_redeploy_status: The Maintenance Operation status on
     the virtual machine.
    :type maintenance_redeploy_status: :class:`MaintenanceRedeployStatus
     <azure.mgmt.compute.compute.v2017_03_30.models.MaintenanceRedeployStatus>`
    :param disks: The virtual machine disk information.
    :type disks: list of :class:`DiskInstanceView
     <azure.mgmt.compute.compute.v2017_03_30.models.DiskInstanceView>`
    :param extensions: The extensions information.
    :type extensions: list of :class:`VirtualMachineExtensionInstanceView
     <azure.mgmt.compute.compute.v2017_03_30.models.VirtualMachineExtensionInstanceView>`
    :param boot_diagnostics: The boot diagnostics.
    :type boot_diagnostics: :class:`BootDiagnosticsInstanceView
     <azure.mgmt.compute.compute.v2017_03_30.models.BootDiagnosticsInstanceView>`
    :param statuses: The resource status information.
    :type statuses: list of :class:`InstanceViewStatus
     <azure.mgmt.compute.compute.v2017_03_30.models.InstanceViewStatus>`
    """

    _attribute_map = {
        'platform_update_domain': {'key': 'platformUpdateDomain', 'type': 'int'},
        'platform_fault_domain': {'key': 'platformFaultDomain', 'type': 'int'},
        'rdp_thumb_print': {'key': 'rdpThumbPrint', 'type': 'str'},
        'vm_agent': {'key': 'vmAgent', 'type': 'VirtualMachineAgentInstanceView'},
        'maintenance_redeploy_status': {'key': 'maintenanceRedeployStatus', 'type': 'MaintenanceRedeployStatus'},
        'disks': {'key': 'disks', 'type': '[DiskInstanceView]'},
        'extensions': {'key': 'extensions', 'type': '[VirtualMachineExtensionInstanceView]'},
        'boot_diagnostics': {'key': 'bootDiagnostics', 'type': 'BootDiagnosticsInstanceView'},
        'statuses': {'key': 'statuses', 'type': '[InstanceViewStatus]'},
    }

    def __init__(self, platform_update_domain=None, platform_fault_domain=None, rdp_thumb_print=None, vm_agent=None, maintenance_redeploy_status=None, disks=None, extensions=None, boot_diagnostics=None, statuses=None):
        self.platform_update_domain = platform_update_domain
        self.platform_fault_domain = platform_fault_domain
        self.rdp_thumb_print = rdp_thumb_print
        self.vm_agent = vm_agent
        self.maintenance_redeploy_status = maintenance_redeploy_status
        self.disks = disks
        self.extensions = extensions
        self.boot_diagnostics = boot_diagnostics
        self.statuses = statuses
