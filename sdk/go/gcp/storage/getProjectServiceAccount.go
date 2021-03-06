// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package storage

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Use this data source to get the email address of the project's Google Cloud Storage service account.
//  For more information see 
// [API](https://cloud.google.com/storage/docs/json_api/v1/projects/serviceAccount).
func LookupProjectServiceAccount(ctx *pulumi.Context, args *GetProjectServiceAccountArgs) (*GetProjectServiceAccountResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["project"] = args.Project
	}
	outputs, err := ctx.Invoke("gcp:storage/getProjectServiceAccount:getProjectServiceAccount", inputs)
	if err != nil {
		return nil, err
	}
	return &GetProjectServiceAccountResult{
		Project: outputs["project"],
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getProjectServiceAccount.
type GetProjectServiceAccountArgs struct {
	// The project in which the resource belongs. If it is not provided, the provider project is used.
	Project interface{}
}

// A collection of values returned by getProjectServiceAccount.
type GetProjectServiceAccountResult struct {
	Project interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}
