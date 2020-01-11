# extractor类，解决登录和解析网址
import requests

from .. import config


class Extractor:
    _section = 'Extractor'

    cookie_domain = ''

    def __init__(self, url, **options):
        self.url = url
        self.session = requests.Session()

        self._cookie_file = None
        self._cookie_jar = self.session.cookies
        self._init_headers()
        self._init_cookies()
        self._init_proxies()

    def config(self, option, value=None):
        if value:
            config.write(self._section, option, value)
            return config.get(self._section, option)
        else:
            return config.get(self._section, option)

    def _init_headers(self):
        headers = self.session.headers
        headers.clear()
        headers['User-Agent'] = self.config('User-Agent')
        headers['Accept'] = self.config('Accept')
        headers['Accept-Language'] = self.config('Accept-Language')
        headers['Accept-Encoding'] = self.config('Accept-Encoding')
        headers['Connection'] = self.config('Connection')
        headers['Upgrade-Insecure-Requests'] = self.config('Upgrade-Insecure-Requests')

    def _init_cookies(self):
        cookies = self.config('Cookie')
        if isinstance(eval(cookies, dict)):
            set_cookie = self._cookie_jar.set
            for name, value in cookies:
                set_cookie(name, value, domain=self.cookie_domain)
        elif isinstance(eval(cookies), str):
            pass
        else:
            pass


    def _init_proxies(self):
        proxies = self.config('Proxy')
        if proxies:
            self.session.proxies = eval(proxies)
