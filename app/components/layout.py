import reflex as rx
from app.components.navbar import navbar
from app.components.footer import footer


def layout(child: rx.Component) -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(child, class_name="flex-grow"),
        footer(),
        class_name="flex flex-col min-h-screen bg-white font-['Roboto']",
    )