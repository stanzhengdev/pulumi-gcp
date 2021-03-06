# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class SubnetworkIAMPolicy(pulumi.CustomResource):
    """
    Three different resources help you manage your IAM policy for GCE subnetwork. Each of these resources serves a different use case:
    
    * `google_compute_subnetwork_iam_policy`: Authoritative. Sets the IAM policy for the subnetwork and replaces any existing policy already attached.
    * `google_compute_subnetwork_iam_binding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the subnetwork are preserved.
    * `google_compute_subnetwork_iam_member`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the subnetwork are preserved.
    
    ~> **Note:** `google_compute_subnetwork_iam_policy` **cannot** be used in conjunction with `google_compute_subnetwork_iam_binding` and `google_compute_subnetwork_iam_member` or they will fight over what your policy should be.
    
    ~> **Note:** `google_compute_subnetwork_iam_binding` resources **can be** used in conjunction with `google_compute_subnetwork_iam_member` resources **only if** they do not grant privilege to the same role.
    
    ~> **Note:** These entire resources are in [Beta](https://www.terraform.io/docs/providers/google/index.html#beta-features)
    """
    def __init__(__self__, __name__, __opts__=None, policy_data=None, project=None, region=None, subnetwork=None):
        """Create a SubnetworkIAMPolicy resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not policy_data:
            raise TypeError('Missing required property policy_data')
        elif not isinstance(policy_data, basestring):
            raise TypeError('Expected property policy_data to be a basestring')
        __self__.policy_data = policy_data
        """
        The policy data generated by
        a `google_iam_policy` data source.
        """
        __props__['policyData'] = policy_data

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
        The region of the subnetwork. If
        unspecified, this defaults to the region configured in the provider.
        """
        __props__['region'] = region

        if not subnetwork:
            raise TypeError('Missing required property subnetwork')
        elif not isinstance(subnetwork, basestring):
            raise TypeError('Expected property subnetwork to be a basestring')
        __self__.subnetwork = subnetwork
        """
        The name of the subnetwork.
        """
        __props__['subnetwork'] = subnetwork

        __self__.etag = pulumi.runtime.UNKNOWN
        """
        (Computed) The etag of the subnetwork's IAM policy.
        """

        super(SubnetworkIAMPolicy, __self__).__init__(
            'gcp:compute/subnetworkIAMPolicy:SubnetworkIAMPolicy',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'etag' in outs:
            self.etag = outs['etag']
        if 'policyData' in outs:
            self.policy_data = outs['policyData']
        if 'project' in outs:
            self.project = outs['project']
        if 'region' in outs:
            self.region = outs['region']
        if 'subnetwork' in outs:
            self.subnetwork = outs['subnetwork']
