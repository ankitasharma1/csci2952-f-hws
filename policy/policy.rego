package envoy.authz

import input.attributes.request.http as http_request

default allow = false

token = {"valid": valid, "payload": payload} {
    [_, encoded] := split(http_request.headers.authorization, " ")
    [valid, _, payload] := io.jwt.decode_verify(encoded, {"secret": "MySuperSecretKey", "alg": "hs256"})
}

allow {
    is_token_valid
    action_allowed
}

# Check to make sure provided token is a valid JWT
is_token_valid {
  token.valid
  # "Not Before" claim is not before current time
  token.payload.nbf <= time.now_ns()
  # "Expiration" claim is after current time
  time.now_ns() < token.payload.exp
}

# Allow all CartService requests to pass
action_allowed {
  glob.match("/hipstershop.CartService/*", [], http_request.path)
}
