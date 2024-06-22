from flet import *
from janelas.requisições.req import Slot
import asyncio

class home(UserControl):
    
    def __init__(self, page: Page):
        super().__init__()
    
        snack_bar = SnackBar(content=Text(value='Começando...'))
        snack_bar2 = SnackBar(content=Text(value='Aguarde 2 minutos...'))
        page.overlay.append(snack_bar)
        page.overlay.append(snack_bar2)
        
        global continue_loop
        continue_loop = False

        async def inicia(e):
            global continue_loop
            if self.texto_iniciar.value == 'Iniciar':

                continue_loop = True
                snack_bar.open = True
                page.update()

                while continue_loop:
                    
                    self.gridImagens.controls.clear()
                    await asyncio.sleep(6)

                    slot = Slot()
                    resultados = await slot.iniciar()

                    for url, nome, porcentagem in resultados:
                        self.gridImagens.controls.append(
                            Container(
                                Column(
                                    controls=[
                                        Container(
                                            Column(controls=[
                                                Image(src=url),
                                                Text(
                                                    value=f'{nome} -- Chance de Ganho: {porcentagem}')
                                            ]
                                            )
                                        )
                                    ]
                                )
                            )
                        )

                    self.update()
                    snack_bar2.open = True
                    page.update()

                    self.icone.name = icons.STOP
                    self.icone.update()

                    self.texto_iniciar.value = 'Parar'
                    self.texto_iniciar.update()

                    self.Botao_iniciar_stop.bgcolor = colors.RED
                    self.Botao_iniciar_stop.update()

            elif self.texto_iniciar.value == 'Parar':
                continue_loop = False
                snack_bar.open = False

                self.icone.name = icons.PLAY_CIRCLE
                self.icone.update()

                self.texto_iniciar.value = 'Iniciar'
                self.texto_iniciar.update()

                self.Botao_iniciar_stop.bgcolor = colors.GREEN
                self.Botao_iniciar_stop.update()

            self.update()

        # AppBar
        page.appbar = AppBar(
            leading=Icon(name=icons.DIAMOND),
            title=Text('Slots para Ganhar'),
            center_title=True,
            bgcolor=colors.BLUE_500,
            actions=[
                IconButton(icon=icons.WB_SUNNY_OUTLINED),
                PopupMenuButton(
                    items=[
                        PopupMenuItem(icon=icons.INFO, text='Sobre', on_click=self.Change),
                    ]
                ),
            ]
        )

        # Imagens que Vão aparecer
        self.gridImagens = GridView(
            expand=1,
            runs_count=5,
            max_extent=200,
            child_aspect_ratio=1.0,
            spacing=60,
            run_spacing=5,
        )

        # Interface
        self.interface = Container(
            width=800,  # Largura
            height=530,  # Altura
            border_radius=border_radius.all(10),
            content=Container(
                Column(
                    controls=[self.gridImagens]
                )
            )
        )
        # Botão
        self.icone = Icon(name=icons.PLAY_CIRCLE, size=30)
        self.texto_iniciar = Text(value='Iniciar', size=25)

        self.Botao_iniciar_stop = Container(
            width=800,  # Largura
            height=50,  # Altura
            bgcolor=colors.GREEN,
            border_radius=border_radius.all(25),
            on_click=inicia,  # Correção para lidar com async
            content=Container(
                Row(alignment=MainAxisAlignment.CENTER,
                    controls=[
                        self.icone,
                        self.texto_iniciar
                    ]
                )
            )
        )

        self.interfaces = Container(
            Column([
                self.interface,
                self.Botao_iniciar_stop
            ])
        )

    def build(self):
        return self.interfaces
    
    def Change(self):
        self.page.go('/info')
