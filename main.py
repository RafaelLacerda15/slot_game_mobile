from flet import *
import janelas.inicio as inicio
import janelas.info as info


def main(page: Page):
    page.window_height = 750
    page.window_width = 600
    
    
    page.add()


app(target=main)
