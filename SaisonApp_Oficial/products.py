import reflex as rx

def products_page()->rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading("Productos de la Categoría"),
            rx.text("Aquí se mostrarán los productos específicos de la categoría seleccionada."),
            rx.button("Volver a Categorías", on_click="/categories"),
            spacing="4",
            align="center",
        ),
        padding="4",
        center_content=True,
    )
