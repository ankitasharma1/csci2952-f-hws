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
def get_cart(user_id, token):
    # open a gRPC channel
    with grpc.insecure_channel(config['addr']) as channel:
        # create a stub (client)
        stub = pb.demo_pb2_grpc.CartServiceStub(channel)

        # create a valid request message
        request = pb.demo_pb2.GetCartRequest(user_id=user_id)

        try:
            # Pass metadata and call method
            response, call = stub.GetCart.with_call(request, metadata=get_metadata(token))
            click.secho('Response received:', fg='green')
            print(response)
        except grpc.RpcError as rpc_error:
            # Handle error
            click.secho('RPC failed:', fg='red')
            print(rpc_error)
            sys.exit(1)


def get_metadata(token):
    if token:
        return (('authorization', 'Bearer ' + token), )

    return tuple()


if __name__ == "__main__":
    cli()

# TODO
# stub_ad = pb.demo_pb2_grpc.AdServiceStub(channel)
# stub_rec = pb.demo_pb2_grpc.RecommendationServiceStub(channel)

# ad_request = pb.demo_pb2.AdRequest()
# response_ad = stub_ad.GetAds(ad_request)

# rec_request = pb.demo_pb2.ListRecommendationsRequest()
# response_rec = stub_rec.ListRecommendations(rec_request)
