# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class SSLPolicy(pulumi.CustomResource):
    def __init__(__self__, __name__, __opts__=None, custom_features=None, description=None, min_tls_version=None, name=None, profile=None, project=None):
        """Create a SSLPolicy resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if custom_features and not isinstance(custom_features, list):
            raise TypeError('Expected property custom_features to be a list')
        __self__.custom_features = custom_features
        __props__['customFeatures'] = custom_features

        if description and not isinstance(description, basestring):
            raise TypeError('Expected property description to be a basestring')
        __self__.description = description
        __props__['description'] = description

        if min_tls_version and not isinstance(min_tls_version, basestring):
            raise TypeError('Expected property min_tls_version to be a basestring')
        __self__.min_tls_version = min_tls_version
        __props__['minTlsVersion'] = min_tls_version

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        __props__['name'] = name

        if profile and not isinstance(profile, basestring):
            raise TypeError('Expected property profile to be a basestring')
        __self__.profile = profile
        __props__['profile'] = profile

        if project and not isinstance(project, basestring):
            raise TypeError('Expected property project to be a basestring')
        __self__.project = project
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        __props__['project'] = project

        __self__.creation_timestamp = pulumi.runtime.UNKNOWN
        __self__.enabled_features = pulumi.runtime.UNKNOWN
        __self__.fingerprint = pulumi.runtime.UNKNOWN
        __self__.self_link = pulumi.runtime.UNKNOWN
        """
        The URI of the created resource.
        """

        super(SSLPolicy, __self__).__init__(
            'gcp:compute/sSLPolicy:SSLPolicy',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'creationTimestamp' in outs:
            self.creation_timestamp = outs['creationTimestamp']
        if 'customFeatures' in outs:
            self.custom_features = outs['customFeatures']
        if 'description' in outs:
            self.description = outs['description']
        if 'enabledFeatures' in outs:
            self.enabled_features = outs['enabledFeatures']
        if 'fingerprint' in outs:
            self.fingerprint = outs['fingerprint']
        if 'minTlsVersion' in outs:
            self.min_tls_version = outs['minTlsVersion']
        if 'name' in outs:
            self.name = outs['name']
        if 'profile' in outs:
            self.profile = outs['profile']
        if 'project' in outs:
            self.project = outs['project']
        if 'selfLink' in outs:
            self.self_link = outs['selfLink']
