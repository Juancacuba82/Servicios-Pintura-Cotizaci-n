import reflex as rx


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon("paintbrush", class_name="h-8 w-8 text-indigo-500"),
                    rx.el.p("PintaPro", class_name="text-2xl font-bold text-gray-800"),
                    class_name="flex items-center space-x-2",
                ),
                rx.el.p(
                    "Transformando espacios con color y profesionalismo.",
                    class_name="mt-4 text-gray-500 max-w-xs",
                ),
                rx.el.div(
                    rx.el.a(
                        rx.icon(
                            "twitter", class_name="text-gray-400 hover:text-indigo-500"
                        ),
                        href="#",
                    ),
                    rx.el.a(
                        rx.icon(
                            "instagram",
                            class_name="text-gray-400 hover:text-indigo-500",
                        ),
                        href="#",
                    ),
                    rx.el.a(
                        rx.icon(
                            "facebook", class_name="text-gray-400 hover:text-indigo-500"
                        ),
                        href="#",
                    ),
                    class_name="flex mt-4 space-x-4",
                ),
                class_name="flex-shrink-0",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        "Navegación",
                        class_name="text-sm font-semibold text-gray-900 tracking-wider uppercase",
                    ),
                    rx.el.ul(
                        rx.el.li(
                            rx.el.a(
                                "Inicio",
                                href="/",
                                class_name="text-base text-gray-500 hover:text-gray-900",
                            )
                        ),
                        rx.el.li(
                            rx.el.a(
                                "Servicios",
                                href="/servicios",
                                class_name="text-base text-gray-500 hover:text-gray-900",
                            )
                        ),
                        rx.el.li(
                            rx.el.a(
                                "Galería",
                                href="/galeria",
                                class_name="text-base text-gray-500 hover:text-gray-900",
                            )
                        ),
                        rx.el.li(
                            rx.el.a(
                                "Cotización",
                                href="/cotizacion",
                                class_name="text-base text-gray-500 hover:text-gray-900",
                            )
                        ),
                        rx.el.li(
                            rx.el.a(
                                "Contacto",
                                href="/contacto",
                                class_name="text-base text-gray-500 hover:text-gray-900",
                            )
                        ),
                        class_name="mt-4 space-y-4",
                    ),
                ),
                rx.el.div(
                    rx.el.h3(
                        "Contacto",
                        class_name="text-sm font-semibold text-gray-900 tracking-wider uppercase",
                    ),
                    rx.el.ul(
                        rx.el.li(
                            rx.el.p(
                                "info@pintapro.com",
                                class_name="text-base text-gray-500",
                            )
                        ),
                        rx.el.li(
                            rx.el.p(
                                "+1 (234) 567-890", class_name="text-base text-gray-500"
                            )
                        ),
                        class_name="mt-4 space-y-4",
                    ),
                ),
                class_name="mt-16 grid grid-cols-2 gap-8 xl:mt-0 xl:col-span-2",
            ),
            class_name="max-w-7xl mx-auto py-12 px-4 sm:px-6 lg:px-8 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8",
        ),
        rx.el.div(
            rx.el.p(
                "© 2024 PintaPro. Todos los derechos reservados.",
                class_name="text-center text-sm text-gray-400",
            ),
            class_name="border-t border-gray-200 py-8",
        ),
        class_name="bg-gray-50",
    )