import reflex as rx

def cart_page()->rx.Component:
    return rx.box(
        rx.container(
        rx.vstack(
            rx.heading("Carrito de Compras"),
            rx.text("Tu carrito está vacío."),
            rx.button("Volver a la Página Principal", on_click=rx.redirect("/home")),
            spacing="4",
            align="center",
        ),
        padding="4",
        center_content=True,
    )
    )