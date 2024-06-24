from flet import *
from time import sleep



class screen(UserControl):
    def __init__(self, page: Page):
        super().__init__()
        
        self.imagem_ = Image(src='assets/777.png', color='white', width=350, fit=ImageFit.CONTAIN)
        self.carregar = ProgressRing(stroke_width=10)
        
        self.interface = Container(
            bgcolor='blue',
            height=695,
            width=620,
            border_radius=border_radius.all(25),
            content=Container(
                Column(
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    controls=[
                        self.imagem_,
                        Container(
                            height=150
                        ),
                        self.carregar
                    ]
                )
                )
        )
    
        self.interfaces = Container(
            Column([
                self.interface
            ])
        )
        sleep(3)
        
    
    def build(self):
        self.page.go('/home')
        return self.interfaces
