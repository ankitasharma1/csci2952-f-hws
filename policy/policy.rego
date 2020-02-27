package ambassador.authz

import input.attributes.request.http as http_request

default allow = false

token = {"valid": valid, "payload": payload} {
    [_, encoded] := split(http_request.headers.authorization, " ")
    # TODO: Move secret key out of policy?
    [valid, _, payload] := io.jwt.decode_verify(encoded, {"secret": "MySuperSecretKey", "alg": "HS256"})
}

allow {
    is_token_valid
    action_allowed
}

# Check to make sure provided token is a valid JWT
is_token_valid {
  token.valid
  # "Not Before" claim is not before current time
  token.payload.nbf * 1000000000 <= time.now_ns()
  # "Expiration" claim is after current time
  time.now_ns() < token.payload.exp * 1000000000
}

# Check if path in scopes
action_allowed {
  glob.match("/hipstershop.CartService/*", [], http_request.path)
  in_scope("cartservice")
}

action_allowed {
  glob.match("/hipstershop.AdService/*", [], http_request.path)
  in_scope("adservice")
}

action_allowed {
  glob.match("/hipstershop.RecommendationService/*", [], http_request.path)
  in_scope("recommendationservice")
}

in_scope(elem) {
  is_array(token.payload.scopes)
  token.payload.scopes[_] = elem
}
