import time

import click
import jwt

ALL_SCOPES = ['adservice', 'cartservice', 'recommendationservice']


@click.command()
@click.option('--key', required=True, help='HS256 secret key to use to generate user token')
@click.option('--exp', default=3600, help='Number of seconds that token should expire in. Default is 1 hour.')
@click.option('--scopes', default='', help='List of scopes for the user token. Defaults to all scopes.')
def main(key, exp, scopes):
    if scopes == '':
        scopes = ALL_SCOPES
    else:
        scopes = [scope.strip() for scope in scopes.split(',') if scope in ALL_SCOPES]

    iat = int(time.time())
    payload = {
        # Public claims
        'iat': iat,  # Issued At
        'nbf': iat,  # Not Before
        'exp': iat + exp,  # Expiration

        # Private claims
        'scopes': scopes,
    }
    token = jwt.encode(payload, key, algorithm='HS256')

    click.secho('Generated token:', fg='green')
    click.secho(token.decode('utf-8'), fg='blue')


if __name__ == "__main__":
    main()
