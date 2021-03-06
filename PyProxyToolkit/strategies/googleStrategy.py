"""
Copyright (C) 2016 Garry Lachman garry@lachman.co under GNU LGPL
https://github.com/garrylachman/PyProxyToolkit
https://rev.proxies.online

This library is free software; you can redistribute it and/or modify it under the terms of the
GNU Lesser General Public License version 2.1, as published by the Free Software Foundation.

This library is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU Lesser General Public License for more details.
"""

from .strategyAbstract import StrategyAbstract
from ..proxy import Proxy
import sys

class GoogleStrategy(StrategyAbstract):
    def __init__(self):
        super(GoogleStrategy, self).__init__()
        self._url = 'https://www.google.com/search?q=rev.proxies.online'

    def match(self, response, proxy: Proxy):
        try:
            return str(response).find("Sorry...") == -1 and str(response).find("'captcha'") == -1
        except:
            self.logger.error(sys.exc_info()[0])

        return False
