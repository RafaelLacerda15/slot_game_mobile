from flet import *
from time import sleep


def Screen_inicio(page: Page):
    page.window.height = 750
    page.window.width = 600
    page.window.always_on_top = True
    
    imagem_ = Image(src='assets/777.png', color='white', width=350, fit=ImageFit.CONTAIN)
    carregar = ProgressRing(stroke_width=10)
    
    interface = Container(
        bgcolor='blue',
        height=695,
        width=620,
        border_radius=border_radius.all(25),
        content=Container(
            Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    imagem_,
                    Container(
                        height=150
                    ),
                    carregar
                ]
            )
            )
    )
    
    page.add(interface)

app(target=Screen_inicio)
