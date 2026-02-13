import flet as ft

def main(page: ft.Page):
    # Variável com a imagem certa
    imagem_correta = "Carro"
    page.bgcolor="#32e6f0"
    
    # Texto para feedback
    mensagem = ft.Text(
        f"Qual é o {imagem_correta}",
        text_align=ft.TextAlign.CENTER,
        size=20,
        height=50
    )

    # Função Jogar
    def jogar(e):
        imagem_selecionada = e.control.content.value
        if imagem_selecionada == imagem_correta:
            e.control.bgcolor = ft.Colors.GREEN
            e.control.image.opacity = 0.3
            e.control.content.value = "😄"
            e.control.content.size = 40
            mensagem.value = "Parabéns! Você acertou."
        else:
            e.control.bgcolor = ft.Colors.RED_200
            e.control.image.opacity = 0.3
            e.control.content.value = "😭"
            e.control.content.size = 40
            mensagem.value = f"Ops! Não é o {imagem_correta}. Tente de novo."
        
        container_moto.on_click = None
        container_carro.on_click = None
        container_bike.on_click = None

        btn_jogar_novamente.visible = True

        page.update()
    
    # Função Jogar Novamente
    def jogar_novamente(e):
        btn_jogar_novamente.visible = False
        mensagem.value = f"Clique no {imagem_correta}"

        container_moto.image.opacity = 1.0
        container_moto.on_click = jogar
        container_moto.content.size = 0
        container_moto.content.value = "Moto"

        container_carro.image.opacity = 1.0
        container_carro.on_click = jogar
        container_carro.content.size = 0
        container_carro.content.value = "Carro"

        container_bike.image.opacity = 1.0
        container_bike.on_click = jogar
        container_bike.content.size = 0
        container_bike.content.value = "Bike"
        
        page.update()

    # Container MOTO
    container_moto = ft.Container(
        content=ft.Text(
            "Moto",
            size=0
        ),
        image=ft.DecorationImage(
            src="images/moto.jpg",
            fit=ft.BoxFit.COVER
        ),
        width=120,
        height=120,
        margin=10,
        bgcolor=ft.Colors.GREY_200,
        border_radius=10,
        alignment=ft.Alignment(0, 0),
        ink=True,
        on_click=jogar
    )

    # Container CARRO
    container_carro = ft.Container(
        content=ft.Text(
            "Carro",
            size=0
        ),
        image=ft.DecorationImage(
            src="images/carro.jpg",
            fit=ft.BoxFit.COVER
        ),
        width=120,
        height=120,
        margin=10,
        bgcolor=ft.Colors.GREY_200,
        border_radius=10,
        alignment=ft.Alignment(0, 0),
        ink=True,
        on_click=jogar
    )

    # Container BIKE
    container_bike = ft.Container(
        content=ft.Text(
            "Bike",
            size=0
        ),
        image=ft.DecorationImage(
            src="images/bike.webp",
            fit=ft.BoxFit.COVER
        ),
        width=120,
        height=120,
        margin=10,
        bgcolor=ft.Colors.GREY_200,
        border_radius=10,
        alignment=ft.Alignment(0, 0),
        ink=True,
        on_click=jogar
    )

    # Botão "Jogar Novamente"
    btn_jogar_novamente = ft.Button(
        "Jogar Novamente",
        visible=False,
        on_click=jogar_novamente
    )

    page.add(
        ft.Column(
            [
                ft.Text(
                    "Selecione a imagem certa",
                    size=24,
                    weight="bold"
                ),
                mensagem,
                ft.Row(
                    [
                        container_moto,
                        container_carro,
                        container_bike
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                btn_jogar_novamente
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )

ft.run(main)