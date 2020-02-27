import sys
import grpc

# import the generated classes
import pb.demo_pb2
import pb.demo_pb2_grpc

NUM_PARAMS = 2

if len(sys.argv) >= NUM_PARAMS:
    service = sys.argv[1]

    # open a gRPC channel
    channel = grpc.insecure_channel('localhost:8888')

    if service == "cart":
        param = sys.argv[2]
        stub_cart = pb.demo_pb2_grpc.CartServiceStub(channel)
        cart_request = pb.demo_pb2.GetCartRequest(user_id=param)
        response_cart = stub_cart.GetCart(cart_request)
        print(response_cart)
    elif service == "ad":
        stub_ad = pb.demo_pb2_grpc.AdServiceStub(channel)
        ad_request = pb.demo_pb2.AdRequest()
        response_ad = stub_ad.GetAds(ad_request)
        print(response_ad)
    elif service == "rec":
        param = sys.argv[2]        
        stub_rec = pb.demo_pb2_grpc.RecommendationServiceStub(channel)
        rec_request = pb.demo_pb2.ListRecommendationsRequest(user_id=param, product_ids=[])
        response_rec = stub_rec.ListRecommendations(rec_request)
        print(response_rec)
else:
    print("Require [service] [param]")
