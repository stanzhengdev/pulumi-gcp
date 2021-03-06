# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class SecurityPolicy(pulumi.CustomResource):
    """
    A Security Policy defines an IP blacklist or whitelist that protects load balanced Google Cloud services by denying or permitting traffic from specified IP ranges. For more information
    see the [official documentation](https://cloud.google.com/armor/docs/configure-security-policies)
    and the [API](https://cloud.google.com/compute/docs/reference/rest/beta/securityPolicies).
    
    ~> **Note:** This entire resource is in [Beta](https://www.terraform.io/docs/providers/google/index.html#beta-features)
    """
    def __init__(__self__, __name__, __opts__=None, description=None, name=None, project=None, rules=None):
        """Create a SecurityPolicy resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if description and not isinstance(description, basestring):
            raise TypeError('Expected property description to be a basestring')
        __self__.description = description
        """
        An optional description of this security policy. Max size is 2048.
        """
        __props__['description'] = description

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        The name of the security policy.
        """
        __props__['name'] = name

        if project and not isinstance(project, basestring):
            raise TypeError('Expected property project to be a basestring')
        __self__.project = project
        """
        The project in which the resource belongs. If it
        is not provided, the provider project is used.
        """
        __props__['project'] = project

        if rules and not isinstance(rules, list):
            raise TypeError('Expected property rules to be a list')
        __self__.rules = rules
        """
        The set of rules that belong to this policy. There must always be a default
        rule (rule with priority 2147483647 and match "\*"). If no rules are provided when creating a
        security policy, a default rule with action "allow" will be added. Structure is documented below.
        """
        __props__['rules'] = rules

        __self__.fingerprint = pulumi.runtime.UNKNOWN
        """
        Fingerprint of this resource.
        """
        __self__.self_link = pulumi.runtime.UNKNOWN
        """
        The URI of the created resource.
        """

        super(SecurityPolicy, __self__).__init__(
            'gcp:compute/securityPolicy:SecurityPolicy',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'description' in outs:
            self.description = outs['description']
        if 'fingerprint' in outs:
            self.fingerprint = outs['fingerprint']
        if 'name' in outs:
            self.name = outs['name']
        if 'project' in outs:
            self.project = outs['project']
        if 'rules' in outs:
            self.rules = outs['rules']
        if 'selfLink' in outs:
            self.self_link = outs['selfLink']
