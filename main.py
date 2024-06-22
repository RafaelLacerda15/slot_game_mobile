from flet import *
from janelas.changewindow import router


def main(page: Page):
    page.update()


    page.window.height = 750
    page.window.width = 600
    myRoute = router(page)


    page.on_route_change = myRoute.route_change
    page.theme_mode = "dark"
    page.add(myRoute.body)
    page.go('/')


app(target=main)
