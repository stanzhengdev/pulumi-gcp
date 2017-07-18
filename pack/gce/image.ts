// *** WARNING: this file was generated by the Lumi Terraform Bridge (TFGEN) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as lumi from "@lumi/lumi";
import * as lumirt from "@lumi/lumirt";

export class Image extends lumi.NamedResource implements ImageArgs {
    public readonly createTimeout?: number;
    public /*out*/ readonly description: string;
    public readonly family?: string;
    public readonly imageName?: string;
    public readonly project?: string;
    public readonly rawDisk?: { containerType?: string, sha1?: string, source: string }[];
    public /*out*/ readonly selfLink: string;
    public readonly sourceDisk?: string;

    constructor(name: string, args: ImageArgs) {
        super(name);
        this.createTimeout = args.createTimeout;
        this.family = args.family;
        this.imageName = args.imageName;
        this.project = args.project;
        this.rawDisk = args.rawDisk;
        this.sourceDisk = args.sourceDisk;
    }
}

export interface ImageArgs {
    readonly createTimeout?: number;
    readonly family?: string;
    readonly imageName?: string;
    readonly project?: string;
    readonly rawDisk?: { containerType?: string, sha1?: string, source: string }[];
    readonly sourceDisk?: string;
}
