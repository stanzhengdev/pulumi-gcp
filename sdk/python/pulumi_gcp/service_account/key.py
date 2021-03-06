# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class Key(pulumi.CustomResource):
    """
    Creates and manages service account key-pairs, which allow the user to establish identity of a service account outside of GCP. For more information, see [the official documentation](https://cloud.google.com/iam/docs/creating-managing-service-account-keys) and [API](https://cloud.google.com/iam/reference/rest/v1/projects.serviceAccounts.keys).
    
    """
    def __init__(__self__, __name__, __opts__=None, key_algorithm=None, pgp_key=None, private_key_type=None, public_key_type=None, service_account_id=None):
        """Create a Key resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if key_algorithm and not isinstance(key_algorithm, basestring):
            raise TypeError('Expected property key_algorithm to be a basestring')
        __self__.key_algorithm = key_algorithm
        """
        The algorithm used to generate the key. KEY_ALG_RSA_2048 is the default algorithm.
        Valid values are listed at
        [ServiceAccountPrivateKeyType](https://cloud.google.com/iam/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountKeyAlgorithm)
        (only used on create)
        """
        __props__['keyAlgorithm'] = key_algorithm

        if pgp_key and not isinstance(pgp_key, basestring):
            raise TypeError('Expected property pgp_key to be a basestring')
        __self__.pgp_key = pgp_key
        """
        An optional PGP key to encrypt the resulting private
        key material. Only used when creating or importing a new key pair. May either be
        a base64-encoded public key or a `keybase:keybaseusername` string for looking up
        in Vault.
        """
        __props__['pgpKey'] = pgp_key

        if private_key_type and not isinstance(private_key_type, basestring):
            raise TypeError('Expected property private_key_type to be a basestring')
        __self__.private_key_type = private_key_type
        """
        The output format of the private key. TYPE_GOOGLE_CREDENTIALS_FILE is the default output format.
        """
        __props__['privateKeyType'] = private_key_type

        if public_key_type and not isinstance(public_key_type, basestring):
            raise TypeError('Expected property public_key_type to be a basestring')
        __self__.public_key_type = public_key_type
        """
        The output format of the public key requested. X509_PEM is the default output format.
        """
        __props__['publicKeyType'] = public_key_type

        if not service_account_id:
            raise TypeError('Missing required property service_account_id')
        elif not isinstance(service_account_id, basestring):
            raise TypeError('Expected property service_account_id to be a basestring')
        __self__.service_account_id = service_account_id
        """
        The Service account id of the Key Pair. This can be a string in the format
        `{ACCOUNT}` or `projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT}`, where `{ACCOUNT}` is the email address or
        unique id of the service account. If the `{ACCOUNT}` syntax is used, the project will be inferred from the account.
        """
        __props__['serviceAccountId'] = service_account_id

        __self__.name = pulumi.runtime.UNKNOWN
        """
        The name used for this key pair
        """
        __self__.private_key = pulumi.runtime.UNKNOWN
        """
        The private key in JSON format, base64 encoded. This is what you normally get as a file when creating
        service account keys through the CLI or web console. This is only populated when creating a new key, and when no
        `pgp_key` is provided.
        """
        __self__.private_key_encrypted = pulumi.runtime.UNKNOWN
        """
        The private key material, base 64 encoded and
        encrypted with the given `pgp_key`. This is only populated when creating a new
        key and `pgp_key` is supplied
        """
        __self__.private_key_fingerprint = pulumi.runtime.UNKNOWN
        """
        The MD5 public key fingerprint for the encrypted
        private key. This is only populated when creating a new key and `pgp_key` is supplied
        """
        __self__.public_key = pulumi.runtime.UNKNOWN
        """
        The public key, base64 encoded
        """
        __self__.valid_after = pulumi.runtime.UNKNOWN
        """
        The key can be used after this timestamp. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z".
        """
        __self__.valid_before = pulumi.runtime.UNKNOWN
        """
        The key can be used before this timestamp.
        A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z".
        """

        super(Key, __self__).__init__(
            'gcp:serviceAccount/key:Key',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'keyAlgorithm' in outs:
            self.key_algorithm = outs['keyAlgorithm']
        if 'name' in outs:
            self.name = outs['name']
        if 'pgpKey' in outs:
            self.pgp_key = outs['pgpKey']
        if 'privateKey' in outs:
            self.private_key = outs['privateKey']
        if 'privateKeyEncrypted' in outs:
            self.private_key_encrypted = outs['privateKeyEncrypted']
        if 'privateKeyFingerprint' in outs:
            self.private_key_fingerprint = outs['privateKeyFingerprint']
        if 'privateKeyType' in outs:
            self.private_key_type = outs['privateKeyType']
        if 'publicKey' in outs:
            self.public_key = outs['publicKey']
        if 'publicKeyType' in outs:
            self.public_key_type = outs['publicKeyType']
        if 'serviceAccountId' in outs:
            self.service_account_id = outs['serviceAccountId']
        if 'validAfter' in outs:
            self.valid_after = outs['validAfter']
        if 'validBefore' in outs:
            self.valid_before = outs['validBefore']
