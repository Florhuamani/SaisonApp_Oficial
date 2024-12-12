import reflex as rx

def home_page()->rx.Component:
    return rx.box(
        rx.container(
            rx.vstack(
                 rx.heading("Página Principal", size="6"),
            rx.text("Explora todos los productos disponibles."),
            rx.button("Ver Carrito", on_click=rx.redirect("/cart")),
            rx.button("Inspiración", on_click=rx.redirect("/ideas")),
            rx.button("Categorías", on_click=rx.redirect("/cart")),
            rx.button("Buscar por Categorías", on_click=rx.redirect("/cart")),
            spacing="4",
            align="center",
        ),
        padding="4",
        center_content=False,
    )
    )