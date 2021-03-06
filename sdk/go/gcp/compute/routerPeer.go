// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package compute

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manages a Cloud Router BGP peer. For more information see
// [the official documentation](https://cloud.google.com/compute/docs/cloudrouter)
// and
// [API](https://cloud.google.com/compute/docs/reference/latest/routers).
type RouterPeer struct {
	s *pulumi.ResourceState
}

// NewRouterPeer registers a new resource with the given unique name, arguments, and options.
func NewRouterPeer(ctx *pulumi.Context,
	name string, args *RouterPeerArgs, opts ...pulumi.ResourceOpt) (*RouterPeer, error) {
	if args == nil || args.Interface == nil {
		return nil, errors.New("missing required argument 'Interface'")
	}
	if args == nil || args.PeerAsn == nil {
		return nil, errors.New("missing required argument 'PeerAsn'")
	}
	if args == nil || args.Router == nil {
		return nil, errors.New("missing required argument 'Router'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["advertisedRoutePriority"] = nil
		inputs["interface"] = nil
		inputs["name"] = nil
		inputs["peerAsn"] = nil
		inputs["peerIpAddress"] = nil
		inputs["project"] = nil
		inputs["region"] = nil
		inputs["router"] = nil
	} else {
		inputs["advertisedRoutePriority"] = args.AdvertisedRoutePriority
		inputs["interface"] = args.Interface
		inputs["name"] = args.Name
		inputs["peerAsn"] = args.PeerAsn
		inputs["peerIpAddress"] = args.PeerIpAddress
		inputs["project"] = args.Project
		inputs["region"] = args.Region
		inputs["router"] = args.Router
	}
	inputs["ipAddress"] = nil
	s, err := ctx.RegisterResource("gcp:compute/routerPeer:RouterPeer", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &RouterPeer{s: s}, nil
}

// GetRouterPeer gets an existing RouterPeer resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRouterPeer(ctx *pulumi.Context,
	name string, id pulumi.ID, state *RouterPeerState, opts ...pulumi.ResourceOpt) (*RouterPeer, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["advertisedRoutePriority"] = state.AdvertisedRoutePriority
		inputs["interface"] = state.Interface
		inputs["ipAddress"] = state.IpAddress
		inputs["name"] = state.Name
		inputs["peerAsn"] = state.PeerAsn
		inputs["peerIpAddress"] = state.PeerIpAddress
		inputs["project"] = state.Project
		inputs["region"] = state.Region
		inputs["router"] = state.Router
	}
	s, err := ctx.ReadResource("gcp:compute/routerPeer:RouterPeer", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &RouterPeer{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *RouterPeer) URN() *pulumi.URNOutput {
	return r.s.URN
}

// ID is this resource's unique identifier assigned by its provider.
func (r *RouterPeer) ID() *pulumi.IDOutput {
	return r.s.ID
}

// The priority of routes advertised to this BGP peer.
// Changing this forces a new peer to be created.
func (r *RouterPeer) AdvertisedRoutePriority() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["advertisedRoutePriority"])
}

// The name of the interface the BGP peer is associated with.
// Changing this forces a new peer to be created.
func (r *RouterPeer) Interface() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["interface"])
}

// IP address of the interface inside Google Cloud Platform.
func (r *RouterPeer) IpAddress() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["ipAddress"])
}

// A unique name for BGP peer, required by GCE. Changing
// this forces a new peer to be created.
func (r *RouterPeer) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// Peer BGP Autonomous System Number (ASN).
// Changing this forces a new peer to be created.
func (r *RouterPeer) PeerAsn() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["peerAsn"])
}

// IP address of the BGP interface outside Google Cloud.
// Changing this forces a new peer to be created.
func (r *RouterPeer) PeerIpAddress() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["peerIpAddress"])
}

// The ID of the project in which this peer's router belongs. If it
// is not provided, the provider project is used. Changing this forces a new peer to be created.
func (r *RouterPeer) Project() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["project"])
}

// The region this peer's router sits in. If not specified,
// the project region will be used. Changing this forces a new peer to be
// created.
func (r *RouterPeer) Region() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["region"])
}

// The name of the router in which this BGP peer will be configured.
// Changing this forces a new peer to be created.
func (r *RouterPeer) Router() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["router"])
}

// Input properties used for looking up and filtering RouterPeer resources.
type RouterPeerState struct {
	// The priority of routes advertised to this BGP peer.
	// Changing this forces a new peer to be created.
	AdvertisedRoutePriority interface{}
	// The name of the interface the BGP peer is associated with.
	// Changing this forces a new peer to be created.
	Interface interface{}
	// IP address of the interface inside Google Cloud Platform.
	IpAddress interface{}
	// A unique name for BGP peer, required by GCE. Changing
	// this forces a new peer to be created.
	Name interface{}
	// Peer BGP Autonomous System Number (ASN).
	// Changing this forces a new peer to be created.
	PeerAsn interface{}
	// IP address of the BGP interface outside Google Cloud.
	// Changing this forces a new peer to be created.
	PeerIpAddress interface{}
	// The ID of the project in which this peer's router belongs. If it
	// is not provided, the provider project is used. Changing this forces a new peer to be created.
	Project interface{}
	// The region this peer's router sits in. If not specified,
	// the project region will be used. Changing this forces a new peer to be
	// created.
	Region interface{}
	// The name of the router in which this BGP peer will be configured.
	// Changing this forces a new peer to be created.
	Router interface{}
}

// The set of arguments for constructing a RouterPeer resource.
type RouterPeerArgs struct {
	// The priority of routes advertised to this BGP peer.
	// Changing this forces a new peer to be created.
	AdvertisedRoutePriority interface{}
	// The name of the interface the BGP peer is associated with.
	// Changing this forces a new peer to be created.
	Interface interface{}
	// A unique name for BGP peer, required by GCE. Changing
	// this forces a new peer to be created.
	Name interface{}
	// Peer BGP Autonomous System Number (ASN).
	// Changing this forces a new peer to be created.
	PeerAsn interface{}
	// IP address of the BGP interface outside Google Cloud.
	// Changing this forces a new peer to be created.
	PeerIpAddress interface{}
	// The ID of the project in which this peer's router belongs. If it
	// is not provided, the provider project is used. Changing this forces a new peer to be created.
	Project interface{}
	// The region this peer's router sits in. If not specified,
	// the project region will be used. Changing this forces a new peer to be
	// created.
	Region interface{}
	// The name of the router in which this BGP peer will be configured.
	// Changing this forces a new peer to be created.
	Router interface{}
}
