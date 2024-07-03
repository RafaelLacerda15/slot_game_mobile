from flet import *
from req import Slot
import asyncio
import webbrowser

def main(page: Page):
    page.adaptive = True
    page.window.height = 740
    page.window.width = 430
    page.window.always_on_top = True

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
        if icone.name == icons.PLAY_CIRCLE:

            continue_loop = True
            snack_bar.open = True
            page.update()

            while continue_loop:

                gridImagens.controls.clear()
                await asyncio.sleep(5)

                slot = Slot()
                resultados = await slot.iniciar()

                for url, nome, porcentagem in resultados:
                    gridImagens.controls.append(
                        Container(
                            Column(
                                controls=[
                                    Image(src=url),
                                    Text(value=f'{nome} -- Vitória: {porcentagem}')
                                ]
                            )
                        )
                    )
                

                page.update()

                icone.name = icons.STOP
                icone.update()

                Botao_iniciar_stop.controls[0].bgcolor = colors.RED
                Botao_iniciar_stop.update()

                snack_bar2.open = True
                page.update()
                await asyncio.sleep(90)
                
        elif icone.name == icons.STOP:
            continue_loop = False
            snack_bar.open = False

            icone.name = icons.PLAY_CIRCLE
            icone.update()

            Botao_iniciar_stop.controls[0].bgcolor = colors.GREEN
            Botao_iniciar_stop.update()

        page.update()
     
    def platStake(e): # Abrir site Stake
        # page.launch_url('stake.com/?c=6a4afcb1fc', web_window_name='Stake')
        # page.update()
        webbrowser.open('stake.com/?c=6a4afcb1fc')
    
    def platSssgame(e):  # Abrir site SSSGame
        # page.launch_url('sssgame.com?code=1622706', web_window_name='SSSGAME')
        # page.update()
        webbrowser.open('sssgame.com?code=1622706')

    def platSpicyBet(e):  # Abrir site spicybet
        webview = WebView(src="spicy01.com/c-sTBhfZ4J?lang=pt")
        page.controls.clear()
        page.add(webview)
        page.update()
    
    def change(e): # Mudar para página Informação
        interface.visible = False
        Botao_iniciar_stop.visible = False
        
        
        page.appbar.leading = IconButton(icon=icons.HOME, on_click=voltar)
        page.appbar.title = Text('info')
        
        interce.visible = True
        
        page.update()
    
    def voltar(e):  # Mudar para página Inicial
        interface.visible = True
        Botao_iniciar_stop.visible = True

        page.appbar.leading = Icon(name=icons.DIAMOND)
        page.appbar.title = Text('Slots para Ganhar')
        page.appbar.actions = [
            
            PopupMenuButton(
                items=[PopupMenuItem(icon=icons.INFO, text='Sobre', on_click=change),
                       PopupMenuItem(),
                       PopupMenuItem(icon=icons.WB_SUNNY_OUTLINED, text='Tema', on_click=theme),]
            ),
        ]

        interce.visible = False

        page.update()
    
    def theme(e): # Mudar o tema da pagina
        page.theme_mode = 'Dark' if page.theme_mode == 'light' else 'light'
        page.update()
    
    # Layout da página Informação    
    interce = ResponsiveRow(
        controls=[
            Container(
                height=750,
                width=600,
                content=Container(
                    height=750,
                    width=600,
                    content=Column(
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                        controls=[
                            Image(src='assets/slot.png',
                                  fit=ImageFit.COVER, width=200),
                            Text(value=info, text_align=TextAlign.CENTER, size=15),
                            Container(height=80),
                            Container(
                                Column(
                                    horizontal_alignment=CrossAxisAlignment.CENTER,
                                    controls=[Text(value='Acessem as plataformas para ganhar bônus no primeiro depósito!'),
                                              Container(
                                        Row(alignment=MainAxisAlignment.CENTER, controls=[
                                              IconButton(on_click=platSpicyBet, content=Image(
                                                  src='assets/spyce.jpg', fit=ImageFit.COVER, height=100, border_radius=border_radius.all(50), tooltip='SpicyBet')),
                                              IconButton(on_click=platStake, content=Image(
                                                  src='assets/stake.webp', fit=ImageFit.CONTAIN, height=100, border_radius=border_radius.all(50), tooltip='stake')),
                                              IconButton(on_click=platSssgame, content=Image(
                                                  src='assets/sssgamer.webp', fit=ImageFit.COVER, height=100, border_radius=border_radius.all(50), tooltip='sssgamer')),

                                              ])
                                    )]
                                )
                            )
                        ]
                    )
                )
            )
        ]
    )
    interce.visible = False
    
    # AppBar
    page.appbar = AppBar(
        leading=Icon(name=icons.DIAMOND),
        title=Text('Slots para Ganhar'),
        center_title=True,
        bgcolor=colors.BLUE_500,
        actions=[
            PopupMenuButton(
                items=[
                    PopupMenuItem(icon=icons.INFO, text='Sobre', on_click=change),
                    PopupMenuItem(),
                    PopupMenuItem(icon=icons.WB_SUNNY_OUTLINED, text='Tema', on_click=theme),
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
        spacing=50,
        run_spacing=5,
    )
    
    # Layout da página Inicial
    interface = ResponsiveRow(
        controls=[
            Container(
                bgcolor=colors.BLUE_500,
                width=800,  # Largura
                height=530,  # Altura
                border_radius=border_radius.all(10),
                content=Container(
                    Column(
                        controls=[gridImagens]
                    )
                )
            )
        ]
    )
    interface.visible = True
    
    # Botão
    icone = Icon(name=icons.PLAY_CIRCLE, size=50)
    Botao_iniciar_stop = ResponsiveRow(
        controls=[
            Container(
                col=1.8,
                width=50,  # Largura
                height=50,  # Altura
                bgcolor=colors.GREEN,
                border_radius=border_radius.all(25),
                on_click=inicia,  # Correção para lidar com async
                content=Container(
                    Row(alignment=MainAxisAlignment.CENTER,
                        controls=[icone]
                        )
                )
            )
        ]
    )

    # Adicionar a página Flet
    page.add(interface, interce, Botao_iniciar_stop)


app(target=main)
