"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import reflex as rx

# Login en el archivo principal
def login_page()-> rx.Component:
    return rx.container(
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

# Crear la aplicación
app = rx.App()
