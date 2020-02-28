import sys

import click
import grpc

# import the generated classes
import pb.demo_pb2
import pb.demo_pb2_grpc

DEFAULT_ADDR = 'localhost:8888'
config = {'addr': DEFAULT_ADDR}


@click.group()
@click.option('--addr', default=DEFAULT_ADDR, help='set the address of the API gateway')
def cli(addr):
    if addr:
        config['addr'] = addr


@cli.command()
@click.argument('user_id')
@click.option('--token', help='authorization token to pass to gRPC server')
def cart(user_id, token):
    with grpc.insecure_channel(config['addr']) as channel:
        stub = pb.demo_pb2_grpc.CartServiceStub(channel)
        request = pb.demo_pb2.GetCartRequest(user_id=user_id)
        call_method(stub.GetCart, request, metadata=get_metadata(token))


@cli.command()
@click.option('--token', help='authorization token to pass to gRPC server')
def ad(token):
    with grpc.insecure_channel(config['addr']) as channel:
        stub = pb.demo_pb2_grpc.AdServiceStub(channel)
        request = pb.demo_pb2.AdRequest()
        call_method(stub.GetAds, request, metadata=get_metadata(token))


@cli.command()
@click.argument('user_id')
@click.option('--token', help='authorization token to pass to gRPC server')
def rec(user_id, token):
    with grpc.insecure_channel(config['addr']) as channel:
        stub = pb.demo_pb2_grpc.RecommendationServiceStub(channel)
        request = pb.demo_pb2.ListRecommendationsRequest(user_id=user_id, product_ids=[])
        call_method(stub.ListRecommendations, request, metadata=get_metadata(token))


def get_metadata(token):
    if token:
        return (('authorization', 'Bearer ' + token), )

    return tuple()


def call_method(method, request, metadata=tuple()):
    try:
        # Pass metadata and call method
        response, call = method.with_call(request, metadata=metadata)
        click.secho('Response received:', fg='green')
        print(response)
    except grpc.RpcError as rpc_error:
        # Handle error
        click.secho('RPC failed:', fg='red')
        print(rpc_error)
        sys.exit(1)


if __name__ == "__main__":
    cli()
