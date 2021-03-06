# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class RouterInterface(pulumi.CustomResource):
    """
    Manages a Cloud Router interface. For more information see
    [the official documentation](https://cloud.google.com/compute/docs/cloudrouter)
    and
    [API](https://cloud.google.com/compute/docs/reference/latest/routers).
    """
    def __init__(__self__, __name__, __opts__=None, ip_range=None, name=None, project=None, region=None, router=None, vpn_tunnel=None):
        """Create a RouterInterface resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if ip_range and not isinstance(ip_range, basestring):
            raise TypeError('Expected property ip_range to be a basestring')
        __self__.ip_range = ip_range
        """
        IP address and range of the interface. The IP range must be
        in the RFC3927 link-local IP space. Changing this forces a new interface to be created.
        """
        __props__['ipRange'] = ip_range

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        A unique name for the interface, required by GCE. Changing
        this forces a new interface to be created.
        """
        __props__['name'] = name

        if project and not isinstance(project, basestring):
            raise TypeError('Expected property project to be a basestring')
        __self__.project = project
        """
        The ID of the project in which this interface's router belongs. If it
        is not provided, the provider project is used. Changing this forces a new interface to be created.
        """
        __props__['project'] = project

        if region and not isinstance(region, basestring):
            raise TypeError('Expected property region to be a basestring')
        __self__.region = region
        """
        The region this interface's router sits in. If not specified,
        the project region will be used. Changing this forces a new interface to be
        created.
        """
        __props__['region'] = region

        if not router:
            raise TypeError('Missing required property router')
        elif not isinstance(router, basestring):
            raise TypeError('Expected property router to be a basestring')
        __self__.router = router
        """
        The name of the router this interface will be attached to.
        Changing this forces a new interface to be created.
        """
        __props__['router'] = router

        if not vpn_tunnel:
            raise TypeError('Missing required property vpn_tunnel')
        elif not isinstance(vpn_tunnel, basestring):
            raise TypeError('Expected property vpn_tunnel to be a basestring')
        __self__.vpn_tunnel = vpn_tunnel
        """
        The name or resource link to the VPN tunnel this
        interface will be linked to. Changing this forces a new interface to be created.
        """
        __props__['vpnTunnel'] = vpn_tunnel

        super(RouterInterface, __self__).__init__(
            'gcp:compute/routerInterface:RouterInterface',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'ipRange' in outs:
            self.ip_range = outs['ipRange']
        if 'name' in outs:
            self.name = outs['name']
        if 'project' in outs:
            self.project = outs['project']
        if 'region' in outs:
            self.region = outs['region']
        if 'router' in outs:
            self.router = outs['router']
        if 'vpnTunnel' in outs:
            self.vpn_tunnel = outs['vpnTunnel']
