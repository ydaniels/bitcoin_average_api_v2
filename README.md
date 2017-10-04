# bitcoin_average_api_v2
Bitcoin Average Version 2 api

Simple unfinished library to access bitcoin average api v2 . I needed to get crypto prices very fast and this has been switched off  https://github.com/bitcoinaverage/bitcoinaverage and for some reason this was not working for me https://github.com/bitcoinaverage/api-integration-examples/blob/master/python_pip_examples/


from bitcoin.average import ApiV2

bt =  ApiV2()

btc = bt.ticker('BTC', 'USD,NGN')


