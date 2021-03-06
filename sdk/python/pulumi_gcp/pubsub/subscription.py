# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class Subscription(pulumi.CustomResource):
    """
    Creates a subscription in Google's pubsub queueing system. For more information see
    [the official documentation](https://cloud.google.com/pubsub/docs) and
    [API](https://cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions).
    
    """
    def __init__(__self__, __name__, __opts__=None, ack_deadline_seconds=None, name=None, project=None, push_config=None, topic=None):
        """Create a Subscription resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if ack_deadline_seconds and not isinstance(ack_deadline_seconds, int):
            raise TypeError('Expected property ack_deadline_seconds to be a int')
        __self__.ack_deadline_seconds = ack_deadline_seconds
        """
        The maximum number of seconds a
        subscriber has to acknowledge a received message, otherwise the message is
        redelivered. Changing this forces a new resource to be created.
        """
        __props__['ackDeadlineSeconds'] = ack_deadline_seconds

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        A unique name for the resource, required by pubsub.
        Changing this forces a new resource to be created.
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

        if push_config and not isinstance(push_config, dict):
            raise TypeError('Expected property push_config to be a dict')
        __self__.push_config = push_config
        """
        Block configuration for push options. More
        configuration options are detailed below.
        """
        __props__['pushConfig'] = push_config

        if not topic:
            raise TypeError('Missing required property topic')
        elif not isinstance(topic, basestring):
            raise TypeError('Expected property topic to be a basestring')
        __self__.topic = topic
        """
        The topic name or id to bind this subscription to, required by pubsub.
        Changing this forces a new resource to be created.
        """
        __props__['topic'] = topic

        __self__.path = pulumi.runtime.UNKNOWN
        """
        Path of the subscription in the format `projects/{project}/subscriptions/{sub}`
        """

        super(Subscription, __self__).__init__(
            'gcp:pubsub/subscription:Subscription',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'ackDeadlineSeconds' in outs:
            self.ack_deadline_seconds = outs['ackDeadlineSeconds']
        if 'name' in outs:
            self.name = outs['name']
        if 'path' in outs:
            self.path = outs['path']
        if 'project' in outs:
            self.project = outs['project']
        if 'pushConfig' in outs:
            self.push_config = outs['pushConfig']
        if 'topic' in outs:
            self.topic = outs['topic']
