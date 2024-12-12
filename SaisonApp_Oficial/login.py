import reflex as rx
def login_page():
    return rx.box(
        rx.container(
        rx.vstack(
            rx.heading("Iniciar Sesión", size="lg"),
            rx.input(placeholder="Correo electrónico"),
            rx.input(placeholder="Contraseña", type="password"),
            rx.button("Ingresar", on_click="/home"),
            spacing="4",
            align="center",
        ),
        padding="4",
        center_content=True,
    )
    )