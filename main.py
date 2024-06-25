from flet import *
from req import Slot
import asyncio

def main(page: Page):
    page.adaptive = True
    page.window.height = 750
    page.window.width = 600


    snack_bar = SnackBar(content=Text(value='Começando...'))
    snack_bar2 = SnackBar(content=Text(value='Aguarde 2 minutos...'))
    page.overlay.append(snack_bar)
    page.overlay.append(snack_bar2)

    info = '''Aplicativo com intenção de ajudar você a ganhar nos slots das plataformas.
        Não me responsabilizando por quebras/perdas da banca. Quaisquer ações imprudentes serão do seu total concentimento.'''
    
    global continue_loop
    continue_loop = False

    # Funções
    async def inicia(e): # Iniciar a raspagem de dados
        global continue_loop
        if texto_iniciar.value == 'Iniciar':

            continue_loop = True
            snack_bar.open = True
            page.update()

            while continue_loop:

                gridImagens.controls.clear()
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
                                            Text(
                                                value=f'{nome} -- Chance de Ganho: {porcentagem}')
                                        ]
                                        )
                                    )
                                ]
                            )
                        )
                    )

                page.update()
                snack_bar2.open = True
                page.update()

                icone.name = icons.STOP
                icone.update()

                texto_iniciar.value = 'Parar'
                texto_iniciar.update()

                Botao_iniciar_stop.bgcolor = colors.RED
                Botao_iniciar_stop.update()

        elif texto_iniciar.value == 'Parar':
            continue_loop = False
            snack_bar.open = False

            icone.name = icons.PLAY_CIRCLE
            icone.update()

            texto_iniciar.value = 'Iniciar'
            texto_iniciar.update()

            Botao_iniciar_stop.bgcolor = colors.GREEN
            Botao_iniciar_stop.update()

        page.update()

    def platStake(e): # Abrir site Stake
        plataforma_stake = WebView('stake.com/?c=6a4afcb1fc', javascript_enabled=True)
        print(f'Abrindo: {plataforma_stake}')

    def platSssgame(e):  # Abrir site SSSGame
        plataforma_sssgame = WebView('https://www.sssgame.com?code=1622706', javascript_enabled=True)
        print(f'Abrindo: {plataforma_sssgame}')

    def platSpicyBet(e):  # Abrir site spicybet
        plataforma_spicybet = WebView('https://www.spicy01.com/c-sTBhfZ4J?lang=pt', javascript_enabled=True)
        print(f'Abrindo: {plataforma_spicybet}')
    
    def change(e): # Mudar para página Informação
        interface.visible = False
        Botao_iniciar_stop.visible = False
        
        page.appbar.leading = IconButton(icon=icons.HOME, on_click=voltar)
        page.appbar.title = Text('info')
        page.appbar.actions = []
        
        interce.visible = True
        
        page.update()
    
    def voltar(e):  # Mudar para página Inicial
        interface.visible = True
        Botao_iniciar_stop.visible = True

        page.appbar.leading = Icon(name=icons.DIAMOND)
        page.appbar.title = Text('Slots para Ganhar')
        page.appbar.actions = [
            IconButton(icon=icons.WB_SUNNY_OUTLINED),
            PopupMenuButton(
                items=[
                    PopupMenuItem(icon=icons.INFO,
                                  text='Sobre', on_click=change),
                ]
            ),
        ]

        interce.visible = False

        page.update()
    
    def theme(e): # Mudar o tema da pagina
        ...
            
    # Layout da página Informação    
    interce = Container(
        height=750,
        width=600,
        content=Container(
            height=750,
            width=600,
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Image(src='assets/slot.jpg', fit=ImageFit.COVER, width=250),
                    Text(value=info, text_align=TextAlign.CENTER, size=15),
                    Container(height=80),
                    Container(
                        Column(
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            controls=[Text(value='Acessem as plataformas para ganhar bônus no primeiro depósito!'),
                                      Container(
                                          Row(alignment=MainAxisAlignment.CENTER, controls=[
                                              IconButton(on_click=platSpicyBet, content=Image(
                                                  src='assets/spyce.jpg', fit=ImageFit.COVER, height=100, border_radius=border_radius.all(50))),
                                              IconButton(on_click=platStake, content=Image(
                                                  src='assets/stake.webp', fit=ImageFit.CONTAIN, height=100, border_radius=border_radius.all(50))),
                                              IconButton(on_click=platSssgame, content=Image(
                                                  src='assets/sssgamer.webp', fit=ImageFit.COVER, height=100, border_radius=border_radius.all(50))),

                                          ])
                                      )]
                        )
                    )
                ]
            )
        )
    )
    interce.visible = False
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
                    PopupMenuItem(icon=icons.INFO,
                                    text='Sobre', on_click=change),
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
    
    # Layout da página Inicial
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

    # Adicionar a página Flet
    page.add(interface, Botao_iniciar_stop, interce)


app(target=main)
