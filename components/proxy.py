import requests
from proxyscrape import create_collector, get_collector

def make_collector(page_i=''):
        http_collector = create_collector(f'http-collector-{page_i}', 'https')
        return http_collector

# Returns requests session with proxies (http, https)
def setup_new_proxies(http_collector, http):    
    proxy_http = http_collector.get_proxy()
    proxy_https = http_collector.get_proxy({'type':'https'})
    http.proxies={
        'http': f'http://{proxy_http.host}:{proxy_http.port}',
        'https' : f'https://{proxy_https.host}:{proxy_https.port}'
    }
    return http

def create_new_session(http_collector):
    http = requests.Session()
    http = setup_new_proxies(http_collector, http)
    return http