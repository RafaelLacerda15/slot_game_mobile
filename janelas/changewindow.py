from flet import *

from janelas.inicio import home
from janelas.info import info


class router:
    def __init__(self, page: Page):
        self.page = page
        self.routers = {
            '/': home(page),
            '/info': info(page)
        }
        self.body = Container(content=self.routers['/'])
        
    def route_change(self, route):
        self.body.content = self.routers[route.route]
        self.body.update()
