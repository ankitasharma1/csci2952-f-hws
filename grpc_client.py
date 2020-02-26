import grpc

# import the generated classes
import pb.demo_pb2
import pb.demo_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub_cart = pb.demo_pb2_grpc.CartServiceStub(channel)
stub_ad = pb.demo_pb2_grpc.AdServiceStub(channel)
stub_rec = pb.demo_pb2_grpc.RecommendationServiceStub(channel)

# create a valid request message
cart_request = pb.demo_pb2.GetCartRequest(1)
response_cart = stub_card.GetCart(cart_request)
# print(response.value)

ad_request = pb.demo_pb2.AdRequest()
response_ad = stub_ad.GetAds(ad_request)

rec_request = pb.demo_pb2.ListRecommendationsRequest()
response_rec = stub_rec.ListRecommendations(rec_request)