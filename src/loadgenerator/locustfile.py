#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import random
import time

import jwt
from locust import HttpLocust, TaskSet, task

products = [
    '0PUK6V6EV0',
    '1YMWWN1N4O',
    '2ZYFJ3GM2N',
    '66VCHSJNUP',
    '6E92ZMYYFZ',
    '9SIQT8TOJO',
    'L9ECAV7KIM',
    'LS4PSXUNUM',
    'OLJCESPC7Z',
]


def create_token():
    """
    Creates a JWT token to pass to all requests.
    See gen_token.py in the root directory.
    """

    iat = int(time.time())
    exp = 60 * 60 * 24 * 365  # 1 year
    payload = {
        # Public claims
        'iat': iat,  # Issued At
        'nbf': iat,  # Not Before
        'exp': iat + exp,  # Expiration

        # Private claims
        'scopes': ['frontend'],
    }

    # Remember to update secret key if it is changed
    token = jwt.encode(payload, "MySuperSecretKey", algorithm='HS256')

    return token.decode('utf-8')


class UserBehavior(TaskSet):
    headers = {}

    def on_start(self):
        # Create headers
        token = create_token()
        self.headers['Authorization'] = 'Bearer ' + token

        self.index()

    @task(1)
    def index(self):
        self.client.get("/", headers=self.headers)

    @task(2)
    def setCurrency(self):
        currencies = ['EUR', 'USD', 'JPY', 'CAD']
        self.client.post("/setCurrency", {'currency_code': random.choice(currencies)}, headers=self.headers)

    @task(10)
    def browseProduct(self):
        self.client.get("/product/" + random.choice(products), headers=self.headers)

    @task(3)
    def viewCart(self):
        self.client.get("/cart", headers=self.headers)

    @task(2)
    def addToCart(self):
        product = random.choice(products)
        self.client.get("/product/" + product, headers=self.headers)
        self.client.post("/cart", {'product_id': product, 'quantity': random.choice([1, 2, 3, 4, 5, 10])}, headers=self.headers)

    @task(1)
    def checkout(self):
        addToCart(l)
        self.client.post(
            "/cart/checkout", {
                'email': 'someone@example.com',
                'street_address': '1600 Amphitheatre Parkway',
                'zip_code': '94043',
                'city': 'Mountain View',
                'state': 'CA',
                'country': 'United States',
                'credit_card_number': '4432-8015-6152-0454',
                'credit_card_expiration_month': '1',
                'credit_card_expiration_year': '2039',
                'credit_card_cvv': '672',
            }, headers=self.headers
        )


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 10000
