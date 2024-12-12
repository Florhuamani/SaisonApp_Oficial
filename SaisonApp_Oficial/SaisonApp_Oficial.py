import reflex as rx

from .login import login
from .home import home_page
from .cart import cart_page
from .ideas import ideas_page
from .categorias import categoria_page
from .search import search_page
from .reserva import reserva
from .products import products_page

# Crear la aplicación
app = rx.App()


# Agregar las páginas
app.add_page(login, route="/")
app.add_page(home_page, route="/home")
app.add_page(cart_page, route="/cart")
app.add_page(ideas_page, route="/ideas")
app.add_page(categoria_page, route="/categorias")
app.add_page(search_page, route="/search")
app.add_page(reserva, route="/reserva")
app.add_page(products_page, route="/products")
