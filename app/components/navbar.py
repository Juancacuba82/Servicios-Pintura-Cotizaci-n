import reflex as rx
from app.state import State


def nav_item(item: dict) -> rx.Component:
    return rx.el.a(
        rx.el.p(
            item["name"],
            class_name=rx.cond(
                State.current_page == item["path"],
                "font-semibold text-indigo-600",
                "font-medium text-gray-500 hover:text-indigo-600 transition-colors",
            ),
        ),
        href=item["path"],
        class_name="px-3 py-2 rounded-md text-sm",
    )


def navbar() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.div(
                rx.el.a(
                    rx.el.div(
                        rx.icon("paintbrush", class_name="h-6 w-6 text-indigo-600"),
                        rx.el.p(
                            "PintaPro", class_name="text-xl font-bold text-gray-800"
                        ),
                        class_name="flex items-center space-x-2",
                    ),
                    href="/",
                ),
                rx.el.div(
                    rx.foreach(State.nav_menu, nav_item),
                    class_name="hidden md:flex items-center space-x-2",
                ),
            ),
            rx.el.a(
                rx.el.button(
                    "Cotizar ahora",
                    rx.icon("arrow-right", class_name="ml-2 h-4 w-4"),
                    class_name="hidden md:flex items-center bg-indigo-600 text-white font-semibold px-4 py-2 rounded-lg hover:bg-indigo-700 transition-transform transform hover:scale-105",
                ),
                href="/cotizacion",
            ),
            class_name="flex items-center justify-between h-16 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8",
        ),
        class_name="sticky top-0 z-50 w-full bg-white/80 backdrop-blur-md border-b border-gray-200",
    )