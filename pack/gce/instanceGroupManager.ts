// *** WARNING: this file was generated by the Lumi Terraform Bridge (TFGEN) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as lumi from "@lumi/lumi";
import * as lumirt from "@lumi/lumirt";

export class InstanceGroupManager extends lumi.NamedResource implements InstanceGroupManagerArgs {
    public readonly baseInstanceName: string;
    public readonly description?: string;
    public /*out*/ readonly fingerprint: string;
    public /*out*/ readonly instanceGroup: string;
    public readonly instanceTemplate: string;
    public readonly instanceGroupManagerName?: string;
    public readonly namedPort?: { name: string, port: number }[];
    public readonly project: string;
    public /*out*/ readonly selfLink: string;
    public readonly targetPools?: string[];
    public readonly targetSize: number;
    public readonly updateStrategy?: string;
    public readonly zone: string;

    constructor(name: string, args: InstanceGroupManagerArgs) {
        super(name);
        if (lumirt.defaultIfComputed(args.baseInstanceName, "") === undefined) {
            throw new Error("Property argument 'baseInstanceName' is required, but was missing");
        }
        this.baseInstanceName = args.baseInstanceName;
        this.description = args.description;
        if (lumirt.defaultIfComputed(args.instanceTemplate, "") === undefined) {
            throw new Error("Property argument 'instanceTemplate' is required, but was missing");
        }
        this.instanceTemplate = args.instanceTemplate;
        this.instanceGroupManagerName = args.instanceGroupManagerName;
        this.namedPort = args.namedPort;
        this.project = args.project;
        this.targetPools = args.targetPools;
        this.targetSize = args.targetSize;
        this.updateStrategy = args.updateStrategy;
        if (lumirt.defaultIfComputed(args.zone, "") === undefined) {
            throw new Error("Property argument 'zone' is required, but was missing");
        }
        this.zone = args.zone;
    }
}

export interface InstanceGroupManagerArgs {
    readonly baseInstanceName: string;
    readonly description?: string;
    readonly instanceTemplate: string;
    readonly instanceGroupManagerName?: string;
    readonly namedPort?: { name: string, port: number }[];
    readonly project?: string;
    readonly targetPools?: string[];
    readonly targetSize?: number;
    readonly updateStrategy?: string;
    readonly zone: string;
}
