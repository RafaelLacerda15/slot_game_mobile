from flet import *
import asyncio


def informacao(page: Page):
    page.window.height = 750
    page.window.width = 600
    
    def platStake(e):
        plataforma_stake = WebView('stake.com/?c=6a4afcb1fc')
        print(f'Abrindo: {plataforma_stake}')
        
    def platSssgame(e):
        plataforma_sssgame = WebView('https://www.sssgame.com?code=1622706')
        print(f'Abrindo: {plataforma_sssgame}')
        
    def platSpicyBet(e):
        plataforma_spicybet = WebView('https://www.spicy01.com/c-sTBhfZ4J?lang=pt')
        print(f'Abrindo: {plataforma_spicybet}')
    
    page.appbar = AppBar(leading=IconButton(icon=icons.HOME), title=Text('info'), center_title=True,
                         bgcolor=colors.BLUE_500,)

    info = '''Aplicativo com intenção de ajudar você a ganhar nos slots das plataformas.
    Não me responsabilizando por quebras/perdas da banca. Quaisquer ações imprudentes serão do seu total concentimento.'''
    
    plataforma_stake = WebView('stake.com/?c=6a4afcb1fc')
    plataforma_sssgame = WebView('https://www.sssgame.com?code=1622706')
    plataforma_spicybet = WebView('https://www.spicy01.com/c-sTBhfZ4J?lang=pt')

    interce = Container(
        height=750,
        width=600,
        content=Container(
            height=750,
            width=600,
            content=Column(
                alignment=MainAxisAlignment.CENTER,
                controls=[
                    Text(value=info, text_align=TextAlign.CENTER, size=15),
                    Container(height=80),
                    Container(
                        Row(
                            alignment=MainAxisAlignment.CENTER,
                            controls=[IconButton(on_click=platSpicyBet, content=Image(
                                src='assets/Spicybet.webp', fit=ImageFit.COVER, height=100, border_radius=border_radius.all(50))),
                                IconButton(on_click=platStake, content=Image(
                                    src='assets/icon.webp', fit=ImageFit.CONTAIN, height=100, border_radius=border_radius.all(50))),
                                IconButton(on_click=platSssgame, content=Image(
                                    src='assets/sssgame.png', fit=ImageFit.COVER, height=100, border_radius=border_radius.all(50))),
                                ]
                        )
                    )
                ]
            )
        )
    )
    page.add(interce, plataforma_stake, plataforma_sssgame, plataforma_spicybet)


app(target=informacao)
