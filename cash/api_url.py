__token = 'YOUR TOKEN HERE'

__base_url = 'https://finnhub.io/api/v1/'
def __get_token():
    return __token

def get_endpoint(endpoint_name, category = 'general'):
    return base_url() + endpoint_name + '?/category=' + category

def base_url():
    return __base_url

def auth_param():
    return {'token' : __get_token()}

def get_profile_endpoint(ticker):
    return base_url() + 'stock/profile2?symbol=' + ticker.upper()
