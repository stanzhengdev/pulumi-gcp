// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package serviceAccount

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Get service account public key. For more information, see [the official documentation](https://cloud.google.com/iam/docs/creating-managing-service-account-keys) and [API](https://cloud.google.com/iam/reference/rest/v1/projects.serviceAccounts.keys/get).
// 
func LookupAccountKey(ctx *pulumi.Context, args *GetAccountKeyArgs) (*GetAccountKeyResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["project"] = args.Project
		inputs["publicKeyType"] = args.PublicKeyType
		inputs["serviceAccountId"] = args.ServiceAccountId
	}
	outputs, err := ctx.Invoke("gcp:serviceAccount/getAccountKey:getAccountKey", inputs)
	if err != nil {
		return nil, err
	}
	return &GetAccountKeyResult{
		KeyAlgorithm: outputs["keyAlgorithm"],
		Name: outputs["name"],
		PublicKey: outputs["publicKey"],
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getAccountKey.
type GetAccountKeyArgs struct {
	// The ID of the project that the service account will be created in.
	// Defaults to the provider project configuration.
	Project interface{}
	// The output format of the public key requested. X509_PEM is the default output format.
	PublicKeyType interface{}
	// The Service account id of the Key Pair. This can be a string in the format
	// `{ACCOUNT}` or `projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT}`, where `{ACCOUNT}` is the email address or
	// unique id of the service account. If the `{ACCOUNT}` syntax is used, the project will be inferred from the account.
	ServiceAccountId interface{}
}

// A collection of values returned by getAccountKey.
type GetAccountKeyResult struct {
	KeyAlgorithm interface{}
	// The name used for this key pair
	Name interface{}
	// The public key, base64 encoded
	PublicKey interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}
