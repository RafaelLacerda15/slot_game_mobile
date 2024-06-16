from flet import *
from requisições.req import Slot

def main(page: Page):
    page.window_height = 1920
    page.window_width = 600
    # page.horizontal_alignment = CrossAxisAlignment.CENTER
    # page.vertical_alignment = MainAxisAlignment.CENTER
    
    async def inicia(e):
        try:
            if texto_iniciar.value == 'Iniciar':
                slot = Slot()
                resultados = await slot.iniciar()

                for url, nome, porcentagem in resultados:
                    gridImagens.controls.append(
                        Container(
                            Column(
                                controls=[
                                    Container(
                                        Column(
                                            controls=[Image(src=url)]
                                        )
                                    ),
                                    Container(
                                        content=Column(
                                            controls=[
                                                Text(value=nome),
                                                Text(value=porcentagem)
                                            ]
                                        )
                                    )
                                    
                                ]
                            )
                        )
                    )
                page.update()

                icone.name = icons.STOP
                icone.update()

                texto_iniciar.value = 'Parar'
                texto_iniciar.update()

                Botao_iniciar_stop.bgcolor = colors.RED
                Botao_iniciar_stop.update()
            else:
                if texto_iniciar.value == 'Parar':
                    icone.name = icons.PLAY_CIRCLE
                    icone.update()

                    texto_iniciar.value = 'Iniciar'
                    texto_iniciar.update()

                    Botao_iniciar_stop.bgcolor = colors.GREEN
                    Botao_iniciar_stop.update()

                    for url, nome, porcentagem in resultados:
                        break
                    page.update()
            page.update()
        except:
            if texto_iniciar.value == 'Parar':
                icone.name = icons.PLAY_CIRCLE
                icone.update()

                texto_iniciar.value = 'Iniciar'
                texto_iniciar.update()

                Botao_iniciar_stop.bgcolor = colors.GREEN
                Botao_iniciar_stop.update()

                for url, nome, porcentagem in resultados:
                    break
                page.update()
        

            

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
                    PopupMenuItem(icon=icons.SUPPORT_AGENT,text='Suporte'),
                    PopupMenuItem(), # Divisão
                    PopupMenuItem(icon=icons.INFO, text='Sobre'),
                ]
            ),
        ]
    )
    
    # Imagens que Vão aparecer
    gridImagens = GridView(
        expand=1,
        runs_count=5,
        max_extent=200,
        child_aspect_ratio=1.0,
        spacing=100,
        run_spacing=5,
    )
    
    # Interface
    interface = Container(
        width=800, # Largura
        height=800, # Altura
        # bgcolor='white',
        content=Container(
            Column(
                controls=[gridImagens]
            )
        )
    )
    # Botão
    icone = Icon(name=icons.PLAY_CIRCLE)
    texto_iniciar = Text(value='Iniciar')
    
    Botao_iniciar_stop = Container(
        width=800,  # Largura
        height=50,  # Altura
        bgcolor=colors.GREEN,
        on_click=inicia,
        content=Container(
            Row(alignment=MainAxisAlignment.CENTER,
                controls=[
                    icone,
                    texto_iniciar
                ]
            )
        )
    )
    
    
    page.add(interface, Botao_iniciar_stop)
app(target=main)