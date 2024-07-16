from flet import *
from req import Slot
import asyncio
import webbrowser


def main(page: Page):
    page.adaptive = True
    page.window.height = 740
    page.window.width = 430
    page.window.always_on_top = True

    # SnackBar PG
    snack_bar_PG = SnackBar(content=Text(value='Começando! >>PG<<'))
    page.overlay.append(snack_bar_PG)
    # SnackBar PRAGMATIC
    snack_bar_PRAGMATIC = SnackBar(content=Text(value='Começando! >>PRAGMATIC<<'))
    page.overlay.append(snack_bar_PRAGMATIC)
    # SnackBar Iniciando
    snack_bar = SnackBar(content=Text(value='Começando!'))
    page.overlay.append(snack_bar)
    # SnackBar Atualizando
    snack_bar_atualizando = SnackBar(content=Text(value='Atualizando...'))
    page.overlay.append(snack_bar_atualizando)

    info = '''Aplicativo com intenção de ajudar você a ganhar nos slots das plataformas.
        Não me responsabilizando por quebras/perdas da banca. Quaisquer ações imprudentes serão do seu total concentimento.'''
    
    global continue_loop
    continue_loop = False
    
    # Funções
    async def pgEpragCheckBox(e): # Iniciar a raspagem de dados
        global continue_loop
        gridImagens.controls.clear()
        if botao.icon == icons.PLAY_CIRCLE:

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
                                    Container(
                                        height=180,
                                        content=Column([
                                            Image(src=url, width=180, border_radius=border_radius.all(25)),
                                            Text(value=f'{nome} -- Vitória: {porcentagem}', weight=FontWeight.BOLD)
                                        ])
                                    ),
                                ]
                            )
                        )
                    )
                

                page.update()

                botao.icon = icons.STOP_CIRCLE
                botao.icon_color = colors.RED
                botao.update()

                await asyncio.sleep(50)
                
                snack_bar_atualizando.open = True
                page.update()
                
        elif botao.icon == icons.STOP_CIRCLE:
            continue_loop = False
            snack_bar.open = False

            botao.icon = icons.PLAY_CIRCLE
            botao.icon_color = colors.GREEN_300
            botao.update()
            gridImagens.controls.clear()
            
        page.update()
        
    async def pgsoftCheckBox(e):  # Iniciar a raspagem de dados
        global continue_loop
        gridImagens.controls.clear()
        if botao.icon == icons.PLAY_CIRCLE:

            continue_loop = True
            snack_bar_PG.open = True
            page.update()

            while continue_loop:

                gridImagens.controls.clear()
                await asyncio.sleep(5)

                slot = Slot()
                resultados = await slot.pg()

                for url, nome, porcentagem in resultados:
                    gridImagens.controls.append(
                        Container(
                            Column(
                                controls=[
                                    Container(
                                        height=180,
                                        content=Column([
                                            Image(src=url, width=180, border_radius=border_radius.all(25)),
                                            Text(value=f'{nome} -- Vitória: {porcentagem}', weight=FontWeight.BOLD)
                                        ])
                                    ),
                                ]
                            )
                        )
                    )
                

                page.update()

                botao.icon = icons.STOP_CIRCLE
                botao.icon_color = colors.RED
                botao.update()

                await asyncio.sleep(50)
                
                snack_bar_atualizando.open = True
                page.update()
                
        elif botao.icon == icons.STOP_CIRCLE:
            continue_loop = False
            snack_bar_PG.open = False

            botao.icon = icons.PLAY_CIRCLE
            botao.icon_color = colors.GREEN_300
            botao.update()
            gridImagens.controls.clear()

        page.update()
        
    async def pragmaticCheckBox(e): # Iniciar a raspagem de dados
        global continue_loop
        gridImagens.controls.clear()
        if botao.icon == icons.PLAY_CIRCLE:

            continue_loop = True
            snack_bar_PRAGMATIC.open = True
            page.update()

            while continue_loop:

                gridImagens.controls.clear()
                await asyncio.sleep(5)

                slot = Slot()
                resultados = await slot.pragmatic()

                for url, nome, porcentagem in resultados:
                    gridImagens.controls.append(
                        Container(
                            Column(
                                controls=[
                                    Container(
                                        height=180,
                                        content=Column([
                                            Image(src=url, width=180, border_radius=border_radius.all(25)),
                                            Text(value=f'{nome} -- Vitória: {porcentagem}', weight=FontWeight.BOLD)
                                        ])
                                    ),
                                ]
                            )
                        )
                    )
                

                page.update()

                botao.icon = icons.STOP_CIRCLE
                botao.icon_color = colors.RED
                botao.update()

                await asyncio.sleep(50)
                
                snack_bar_atualizando.open = True
                page.update()
                
        elif botao.icon == icons.STOP_CIRCLE:
            continue_loop = False
            snack_bar_PRAGMATIC.open = False
            

            botao.icon = icons.PLAY_CIRCLE
            botao.icon_color = colors.GREEN_300
            botao.update()
            gridImagens.controls.clear()
            
        page.update()

    async def verificarCheckBox(e): # Verificar o checkbox
        if pg.value:
            await pgsoftCheckBox(e)
        elif pragmatic.value:
            await pragmaticCheckBox(e)
        elif todos.value:
            await pgEpragCheckBox(e)
            
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
        provedoras.visible = False
        
        page.appbar.leading = IconButton(icon=icons.HOME, on_click=voltar)
        page.appbar.title = Text('info')
        page.appbar.actions=[
            PopupMenuButton(
                items=[
                    PopupMenuItem(icon=icons.WB_SUNNY_OUTLINED, text='Tema', on_click=theme),
                    ]
                ),
            ]
    
        
        interce.visible = True
        
        page.update()
    
    def voltar(e):  # Mudar para página Inicial
        interface.visible = True
        provedoras.visible = True
        
        page.appbar.leading = Icon(name=icons.DIAMOND)
        page.appbar.title = Text('Slots para Ganhar')
        page.appbar.actions = [
            botao,
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
                width=800,
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
    
    # botao iconButton
    botao = IconButton(icon=icons.PLAY_CIRCLE, icon_color=colors.GREEN_300, on_click=verificarCheckBox)
    
    # AppBar
    page.appbar = AppBar(
        leading=Icon(name=icons.DIAMOND),
        title=Text('Slots para Ganhar'),
        center_title=True,
        bgcolor=colors.BLUE_500,
        actions=[
            botao,
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
    
    # CheckBox
    pg = Checkbox(label='PgSoft', value=False)
    pragmatic = Checkbox(label='Pragmatic', value=False)
    todos = Checkbox(label='Todas', value=False)

    
    # Escolher a provedora
    provedoras = Row([pg, pragmatic, todos], alignment=MainAxisAlignment.CENTER)
    
    # Layout da página Inicial
    interface = ResponsiveRow(
        controls=[
            Container(
                col={"sm": 4, "md": 6, "xl": 20},
                # bgcolor=colors.BLUE_500,
                # width=800,  # Largura
                height=510,  # Altura
                border_radius=border_radius.all(10),
                content=Container(
                    Column(
                        controls=[gridImagens]
                    )
                )
            )
        ],
        run_spacing={"xl": 10}
    )
    interface.visible = True
    
    # Adicionar a página Flet
    page.add(provedoras,interface, interce)


app(target=main)
