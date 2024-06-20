from flet import *
from requisições.req import Slot
import asyncio


def main(page: Page):
    page.window_height = 750
    page.window_width = 600
    
    
    page.snack_bar = SnackBar(Text(value='Começando...'))
    page.snack_bar.open = False

    async def inicia(e):
        if texto_iniciar.value == 'Iniciar':
            page.snack_bar.open = True
            page.update()
            while True:
                await asyncio.sleep(6)
                
                slot = Slot()
                resultados = await slot.iniciar()

                for url, nome, porcentagem in resultados:
                    gridImagens.controls.append(
                        Container(
                            Column(
                                controls=[
                                    Container(
                                        Column(controls=[
                                            Image(src=url),
                                            Text(value=f'{nome} -- Chance de Ganho: {porcentagem}')
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

        elif texto_iniciar.value == 'Parar':
            page.snack_bar.open = False
            page.update()
            
            icone.name = icons.PLAY_CIRCLE
            icone.update()

            texto_iniciar.value = 'Iniciar'
            texto_iniciar.update()

            Botao_iniciar_stop.bgcolor = colors.GREEN
            Botao_iniciar_stop.update()
            
            

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
                    PopupMenuItem(icon=icons.SUPPORT_AGENT, text='Suporte'),
                    PopupMenuItem(),  # Divisão
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
        spacing=60,
        run_spacing=5,
    )

    # Interface
    interface = Container(
        width=800,  # Largura
        height=530,  # Altura
        border_radius=border_radius.all(10),
        content=Container(
            Column(
                controls=[gridImagens]
            )
        )
    )
    # Botão
    icone = Icon(name=icons.PLAY_CIRCLE, size=30)
    texto_iniciar = Text(value='Iniciar', size=25)

    Botao_iniciar_stop = Container(
        width=800,  # Largura
        height=50,  # Altura
        bgcolor=colors.GREEN,
        border_radius=border_radius.all(25),
        on_click=inicia,  # Correção para lidar com async
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
