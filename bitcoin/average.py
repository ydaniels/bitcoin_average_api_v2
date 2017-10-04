import hashlib
import hmac
import requests
import time
class BitcoinAverageException(Exception):
    pass
class ApiV2:

    base_url = 'https://apiv2.bitcoinaverage.com'

    def __init__(self,secret_ket=None,public_key=None):
        self.secret_key = secret_ket
        self.public_key = public_key
    def ticker(self,crypto,fiat):
        return self.worker('/indices/global/ticker/short?crypto=%s&fiat=%s'%(crypto,fiat))
    def convert(self,from_,to,amount=1):
        return self.worker('/convert/global?from=%s&to=%s&amount=%s'%(from_,to,amount))
    def worker(self,url,sign=False):

        headers = {}
        if sign:
            if not self.secret_key or not self.public_key:
                raise BitcoinAverageException('Please use a valid secret key and public key')
            timestamp = int(time.time())
            payload = '{}.{}'.format(timestamp, self.public_key)
            hex_hash = hmac.new(self.secret_key.encode(), msg=payload.encode(), digestmod=hashlib.sha256).hexdigest()
            signature = '{}.{}'.format(payload, hex_hash)
            headers = {'X-Signature': signature}
        url = self.base_url+url
        result = requests.get(url=url, headers=headers)

        return  result.json()


