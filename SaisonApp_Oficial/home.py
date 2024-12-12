import reflex as rx

def home_page():
    return rx.container(
        rx.vstack(
            rx.heading("Página Principal", size="lg"),
            rx.text("Explora todos los productos disponibles."),
            rx.button("Ver Carrito", on_click="/cart"),
            rx.button("Inspiración", on_click="/inspiration"),
            rx.button("Categorías", on_click="/categories"),
            rx.button("Buscar por Categorías", on_click="/search"),
            spacing="4",
            align="center",
        ),
        padding="4",
        center_content=True,
    )
