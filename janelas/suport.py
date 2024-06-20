from flet import *
import asyncio


def main(page: Page):
    page.appbar = AppBar(title=Text('Suporte'), center_title=True)


    suport_telegram = 't.me/raaaffaaa'
    suport_mail = 'raafaellacerdaa@gmail.com'

    interce = Container(
        bgcolor='white',
        height=300,
        width=150,
        content=Container(
            Row(
                controls=[TextButton(text=suport_mail),TextButton(text=suport_telegram)]
            )
        )
    )

    page.add(interce)
app(target=main)