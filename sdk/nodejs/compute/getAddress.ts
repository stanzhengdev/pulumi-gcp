// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Get the IP address from a static address. For more information see
 * the official [API](https://cloud.google.com/compute/docs/reference/latest/addresses/get) documentation.
 */
export function getAddress(args: GetAddressArgs, opts?: pulumi.InvokeOptions): Promise<GetAddressResult> {
    return pulumi.runtime.invoke("gcp:compute/getAddress:getAddress", {
        "name": args.name,
        "project": args.project,
        "region": args.region,
    }, opts);
}

/**
 * A collection of arguments for invoking getAddress.
 */
export interface GetAddressArgs {
    /**
     * A unique name for the resource, required by GCE.
     */
    readonly name: string;
    /**
     * The project in which the resource belongs. If it
     * is not provided, the provider project is used.
     */
    readonly project?: string;
    /**
     * The Region in which the created address reside.
     * If it is not provided, the provider region is used.
     */
    readonly region?: string;
}

/**
 * A collection of values returned by getAddress.
 */
export interface GetAddressResult {
    /**
     * The IP of the created resource.
     */
    readonly address: string;
    readonly project: string;
    readonly region: string;
    /**
     * The URI of the created resource.
     */
    readonly selfLink: string;
    /**
     * Indicates if the address is used. Possible values are: RESERVED or IN_USE.
     */
    readonly status: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
