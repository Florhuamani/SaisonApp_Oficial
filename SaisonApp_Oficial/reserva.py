import reflex as rx

def reserva()-> rx.Component:
    return rx.box(
        rx.container(
        rx.vstack(
            rx.heading("Reservar o comprar"),
            rx.text("Selecciona una opción para continuar."),
            rx.button("Reservar"),
            rx.button("Volver a la página principal", on_click=rx.redirect("/home")),
            spacing="4",
            align="center",
        ),
        padding="4",
        center_content=True,
    )
    )