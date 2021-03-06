# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class TargetPool(pulumi.CustomResource):
    """
    Manages a Target Pool within GCE. This is a collection of instances used as
    target of a network load balancer (Forwarding Rule). For more information see
    [the official
    documentation](https://cloud.google.com/compute/docs/load-balancing/network/target-pools)
    and [API](https://cloud.google.com/compute/docs/reference/latest/targetPools).
    
    """
    def __init__(__self__, __name__, __opts__=None, backup_pool=None, description=None, failover_ratio=None, health_checks=None, instances=None, name=None, project=None, region=None, session_affinity=None):
        """Create a TargetPool resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if backup_pool and not isinstance(backup_pool, basestring):
            raise TypeError('Expected property backup_pool to be a basestring')
        __self__.backup_pool = backup_pool
        """
        URL to the backup target pool. Must also set
        failover\_ratio.
        """
        __props__['backupPool'] = backup_pool

        if description and not isinstance(description, basestring):
            raise TypeError('Expected property description to be a basestring')
        __self__.description = description
        """
        Textual description field.
        """
        __props__['description'] = description

        if failover_ratio and not isinstance(failover_ratio, float):
            raise TypeError('Expected property failover_ratio to be a float')
        __self__.failover_ratio = failover_ratio
        """
        Ratio (0 to 1) of failed nodes before using the
        backup pool (which must also be set).
        """
        __props__['failoverRatio'] = failover_ratio

        if health_checks and not isinstance(health_checks, basestring):
            raise TypeError('Expected property health_checks to be a basestring')
        __self__.health_checks = health_checks
        """
        List of zero or one health check name or self_link. Only
        legacy `google_compute_http_health_check` is supported.
        """
        __props__['healthChecks'] = health_checks

        if instances and not isinstance(instances, list):
            raise TypeError('Expected property instances to be a list')
        __self__.instances = instances
        """
        List of instances in the pool. They can be given as
        URLs, or in the form of "zone/name". Note that the instances need not exist
        at the time of target pool creation, so there is no need to use the
        Terraform interpolators to create a dependency on the instances from the
        target pool.
        """
        __props__['instances'] = instances

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        A unique name for the resource, required by GCE. Changing
        this forces a new resource to be created.
        """
        __props__['name'] = name

        if project and not isinstance(project, basestring):
            raise TypeError('Expected property project to be a basestring')
        __self__.project = project
        """
        The ID of the project in which the resource belongs. If it
        is not provided, the provider project is used.
        """
        __props__['project'] = project

        if region and not isinstance(region, basestring):
            raise TypeError('Expected property region to be a basestring')
        __self__.region = region
        """
        Where the target pool resides. Defaults to project
        region.
        """
        __props__['region'] = region

        if session_affinity and not isinstance(session_affinity, basestring):
            raise TypeError('Expected property session_affinity to be a basestring')
        __self__.session_affinity = session_affinity
        """
        How to distribute load. Options are "NONE" (no
        affinity). "CLIENT\_IP" (hash of the source/dest addresses / ports), and
        "CLIENT\_IP\_PROTO" also includes the protocol (default "NONE").
        """
        __props__['sessionAffinity'] = session_affinity

        __self__.self_link = pulumi.runtime.UNKNOWN
        """
        The URI of the created resource.
        """

        super(TargetPool, __self__).__init__(
            'gcp:compute/targetPool:TargetPool',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'backupPool' in outs:
            self.backup_pool = outs['backupPool']
        if 'description' in outs:
            self.description = outs['description']
        if 'failoverRatio' in outs:
            self.failover_ratio = outs['failoverRatio']
        if 'healthChecks' in outs:
            self.health_checks = outs['healthChecks']
        if 'instances' in outs:
            self.instances = outs['instances']
        if 'name' in outs:
            self.name = outs['name']
        if 'project' in outs:
            self.project = outs['project']
        if 'region' in outs:
            self.region = outs['region']
        if 'selfLink' in outs:
            self.self_link = outs['selfLink']
        if 'sessionAffinity' in outs:
            self.session_affinity = outs['sessionAffinity']
