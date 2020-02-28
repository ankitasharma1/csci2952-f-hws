import time
import sys

import click
import jwt

ALL_SCOPES = ['adservice', 'cartservice', 'recommendationservice']


@click.command()
@click.option('--key', required=True, help='HS256 secret key to use to generate user token')
@click.option('--exp', default=3600, help='Number of seconds that token should expire in. Default is 1 hour.')
@click.option('--scopes', default='', help='List of scopes for the user token. Defaults to all scopes.')
def main(key, exp, scopes):
    if scopes == '':
        scope_list = ALL_SCOPES
    else:
        scope_list = []
        for scope in scopes.split(','):
            if scope not in ALL_SCOPES:
                click.secho(f'Invalid scope specified: {scope}', fg='red')
                click.secho(f'Allowed scopes: {ALL_SCOPES}', fg='yellow')
                sys.exit(1)
            scope_list.append(scope)

    iat = int(time.time())
    payload = {
        # Public claims
        'iat': iat,  # Issued At
        'nbf': iat,  # Not Before
        'exp': iat + exp,  # Expiration

        # Private claims
        'scopes': scope_list,
    }
    token = jwt.encode(payload, key, algorithm='HS256')

    click.secho('Generated token:', fg='green')
    click.secho(token.decode('utf-8'), fg='blue')


if __name__ == "__main__":
    main()
