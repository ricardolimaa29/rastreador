from pyrastreio import correios, jadlog, sequoia
import flet as ft


# print('Correios:')
# print(correios('CODIGO_RASTREIO_CORREIOS'))
# print('Jadlog:')
# print(jadlog('CODIGO_RASTREIO_JADLOG'))
# # sequoia precisa do cpf ou cnpj além do código de rastreio
# print('Sequoia:')
# print(sequoia('CODIGO_RASTREIO_SEQUOIA', '11111111111'))

def main(pagina: ft.Page):

    pagina.vertical_alignment = ft.MainAxisAlignment.CENTER
    pagina.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    pagina.title = 'Rastreio - by Ricardo Lima'
    pagina.window_width  = '1250'
    pagina.window_height = '850'
    pagina.fonts = { #Fontes do PROJETO
                    "Poppins": "fonts/Poppins-Bold.ttf",
                    "Poppins2": "fonts/Poppins-Light.ttf",
                    "Poppins3": "fonts/Poppins-Regular.ttf"}

    titulo = ft.Text('Rastreador de produtos',
                        font_family='Poppins2',
                        size=50)
    def rastrear_correio(e):
        ...
    def on_houver(e):
        e.control.bgcolor = ft.colors.GREEN if e.data == 'true' else ''
        e.control.update()
    # IMAGENS
    img_correio = ft.Image(src=f"imagens\correios.png",width=100,height=100,fit=ft.ImageFit.CONTAIN)
    img_jadlog = ft.Image(src=f"imagens\jadlog.png",width=100,height=100,fit=ft.ImageFit.CONTAIN)
    img_sequoia = ft.Image(src=f"imagens\sequoia.png",width=100,height=100,fit=ft.ImageFit.CONTAIN)

    botao_correio = ft.ElevatedButton(text='Rastrear',
                                width=200,
                                color='White',on_hover=on_houver,on_click=rastrear_correio)
    botao_jadlog = ft.ElevatedButton(text='Rastrear',
                                width=200,
                                color='White',on_hover=on_houver)
    botao_sequoia = ft.ElevatedButton(text='Rastrear',
                                width=200,
                                color='White',on_hover=on_houver)

    field_correio = ft.TextField(label='Código de rastreio:',
                                    color='white',
                                    focused_border_color=ft.colors.WHITE,
                                    height=50)

    field_jadlog = ft.TextField(label='Código de rastreio:',
                                    color='white',
                                    focused_border_color=ft.colors.WHITE,
                                    height=50)

    field_sequoia = ft.TextField(label='Código de rastreio:',
                                    color='white',
                                    focused_border_color=ft.colors.WHITE,
                                    height=50)
    field_sequoia_cpf = ft.TextField(label='CPF ou CNPJ:',
                                    color='white',
                                    focused_border_color=ft.colors.WHITE,
                                    height=50)


    correio = ft.Container(
        theme=ft.Theme(color_scheme_seed=ft.Colors.INDIGO),
        theme_mode=ft.ThemeMode.DARK,
        content=ft.ResponsiveRow([
                img_correio
                ,field_correio
                ,botao_correio
        ]),
    margin=10,
    padding=10,
    width=350,
    height=350,
    )

    jadlog = ft.Container(
        theme=ft.Theme(color_scheme_seed=ft.Colors.INDIGO),
        theme_mode=ft.ThemeMode.DARK,
        content=ft.ResponsiveRow([
            img_jadlog
            ,field_jadlog
            ,botao_jadlog
        ]),
    margin=10,
    padding=10,
    width=350,
    height=350,
    )

    sequoia = ft.Container(
        theme=ft.Theme(color_scheme_seed=ft.Colors.INDIGO),
        theme_mode=ft.ThemeMode.DARK,
        content=ft.ResponsiveRow([
            img_sequoia
            ,field_sequoia
            ,field_sequoia_cpf
            ,botao_sequoia
        ]),
    margin=10,
    padding=10,
    width=350,
    height=350,
    )


    pagina.add(titulo,
                ft.Row([correio,jadlog,sequoia],
                    alignment=ft.MainAxisAlignment.CENTER)

    )

ft.app(target=main)