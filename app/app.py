import reflex as rx
from app.state import State
from app.components.layout import layout


def hero_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h1(
                "El ",
                rx.el.span("arte", class_name="text-indigo-600"),
                " de transformar tus espacios con color.",
                class_name="text-4xl md:text-6xl font-extrabold tracking-tight text-gray-900 text-center",
            ),
            rx.el.p(
                "Servicios de pintura profesionales para residencias y comercios. Calidad, eficiencia y un acabado perfecto, garantizado.",
                class_name="mt-6 max-w-3xl mx-auto text-lg md:text-xl text-gray-600 text-center",
            ),
            rx.el.div(
                rx.el.a(
                    "Obtener Cotización Instantánea",
                    href="/cotizacion",
                    class_name="px-8 py-4 bg-indigo-600 text-white font-bold rounded-xl shadow-lg hover:bg-indigo-700 transition-all duration-300 transform hover:scale-105",
                ),
                rx.el.a(
                    "Ver Servicios",
                    href="/servicios",
                    class_name="px-8 py-4 bg-gray-100 text-gray-800 font-bold rounded-xl shadow-sm hover:bg-gray-200 transition-all duration-300 transform hover:scale-105",
                ),
                class_name="mt-10 flex justify-center items-center gap-4",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20 md:py-32",
        ),
        class_name="bg-gray-50",
    )


def service_card(service: dict) -> rx.Component:
    return rx.el.div(
        rx.icon(service["icon"], class_name="h-10 w-10 text-indigo-500 mb-4"),
        rx.el.h3(service["name"], class_name="text-xl font-bold text-gray-900"),
        rx.el.p(service["description"], class_name="mt-2 text-gray-600"),
        class_name="bg-white p-8 rounded-2xl border border-gray-100 shadow-sm hover:shadow-lg hover:-translate-y-1 transition-all duration-300",
    )


def services_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Nuestros Servicios",
                    class_name="text-3xl font-extrabold text-gray-900 sm:text-4xl",
                ),
                rx.el.p(
                    "Soluciones completas para cada necesidad.",
                    class_name="mt-4 text-lg text-gray-500",
                ),
                class_name="max-w-3xl mx-auto text-center",
            ),
            rx.el.div(
                rx.foreach(State.services, service_card),
                class_name="mt-12 grid gap-8 md:grid-cols-2 lg:grid-cols-4",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 sm:py-24",
        )
    )


def advantage_item(advantage: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(advantage["icon"], class_name="h-6 w-6 text-white"),
            class_name="flex items-center justify-center h-12 w-12 rounded-xl bg-indigo-500",
        ),
        rx.el.div(
            rx.el.h3(
                advantage["title"], class_name="text-lg font-semibold text-gray-900"
            ),
            rx.el.p(advantage["description"], class_name="mt-1 text-gray-600"),
            class_name="ml-4",
        ),
        class_name="flex items-start",
    )


def advantages_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Por qué elegirnos",
                    class_name="text-3xl font-extrabold text-gray-900",
                ),
                rx.el.p(
                    "La diferencia está en los detalles. Te ofrecemos más que una simple capa de pintura.",
                    class_name="mt-3 text-xl text-gray-500",
                ),
                class_name="lg:col-span-1",
            ),
            rx.el.div(
                rx.foreach(State.advantages, advantage_item),
                class_name="mt-10 lg:mt-0 grid gap-10 sm:grid-cols-2",
            ),
            class_name="max-w-7xl mx-auto py-16 px-4 sm:px-6 lg:py-24 lg:grid lg:grid-cols-2 lg:gap-x-16",
        ),
        class_name="bg-gray-50",
    )


def cta_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "¿Listo para darle vida a tus paredes?",
                class_name="text-3xl font-extrabold text-white sm:text-4xl text-center",
            ),
            rx.el.p(
                "Solicita tu cotización gratuita y sin compromiso. Descubre lo fácil que es renovar tu espacio con PintaPro.",
                class_name="mt-4 max-w-2xl mx-auto text-lg text-indigo-100 text-center",
            ),
            rx.el.a(
                "Cotizar mi proyecto",
                href="/cotizacion",
                class_name="mt-8 inline-block bg-white text-indigo-600 font-bold px-8 py-4 rounded-xl shadow-lg hover:bg-gray-100 transition-transform transform hover:scale-105",
            ),
            class_name="max-w-3xl mx-auto text-center py-16 px-4 sm:py-20 sm:px-6 lg:px-8",
        ),
        class_name="bg-indigo-700",
    )


def index() -> rx.Component:
    return layout(
        rx.el.div(
            hero_section(),
            services_section(),
            testimonials_section(),
            advantages_section(),
            cta_section(),
        )
    )


def testimonials_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Lo que dicen nuestros clientes",
                    class_name="text-3xl font-extrabold text-gray-900 sm:text-4xl",
                ),
                rx.el.p(
                    "La satisfacción de nuestros clientes es nuestra mejor carta de presentación.",
                    class_name="mt-4 text-lg text-gray-500",
                ),
                class_name="max-w-3xl mx-auto text-center",
            ),
            rx.el.div(
                rx.foreach(State.testimonials, testimonial_card),
                class_name="mt-12 grid gap-8 md:grid-cols-1 lg:grid-cols-3",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 sm:py-24",
        )
    )


def testimonial_card(testimonial: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.foreach(range(5), lambda i: star_icon(i, testimonial["rating"])),
            class_name="flex items-center text-yellow-400",
        ),
        rx.el.p(f'''"{testimonial["comment"]}"''', class_name="mt-4 text-gray-600"),
        rx.el.div(
            rx.image(
                src=f"https://api.dicebear.com/9.x/initials/svg?seed={testimonial['avatar']}",
                class_name="h-12 w-12 rounded-full",
            ),
            rx.el.div(
                rx.el.p(testimonial["name"], class_name="font-semibold text-gray-900"),
                rx.el.p(testimonial["location"], class_name="text-gray-500"),
            ),
            class_name="flex items-center mt-6",
        ),
        class_name="bg-white p-8 rounded-2xl border border-gray-100 shadow-sm",
    )


def star_icon(index: rx.Var, rating: rx.Var) -> rx.Component:
    return rx.icon(
        "star",
        class_name=rx.cond(
            index < rating, "text-yellow-400 fill-yellow-400", "text-gray-300"
        ),
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700;900&display=swap",
            rel="stylesheet",
        ),
        rx.el.link(
            rel="stylesheet",
            href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css",
            integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=",
            cross_origin="",
        ),
    ],
)
app.add_page(index)


def detailed_service_card(service: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.image(
                src=f"/placeholder.svg",
                class_name="object-cover w-full h-48 rounded-t-xl",
            ),
            rx.el.div(
                rx.el.div(
                    rx.icon(service["icon"], class_name="h-8 w-8 text-indigo-500"),
                    class_name="p-3 bg-white rounded-full shadow-md absolute -top-6 left-6",
                ),
                rx.el.h3(
                    service["name"], class_name="mt-8 text-2xl font-bold text-gray-900"
                ),
                rx.el.p(service["description"], class_name="mt-2 text-gray-600"),
                rx.el.a(
                    "Más información",
                    rx.icon("arrow-right", class_name="ml-2 h-4 w-4"),
                    href="#",
                    class_name="mt-4 inline-flex items-center text-indigo-600 font-semibold hover:text-indigo-800",
                ),
                class_name="p-6",
            ),
            class_name="relative",
        ),
        class_name="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden hover:shadow-lg transition-shadow duration-300",
    )


def servicios() -> rx.Component:
    return layout(
        rx.el.div(
            rx.el.section(
                rx.el.div(
                    rx.el.h1(
                        "Nuestros Servicios de Pintura Profesional",
                        class_name="text-4xl md:text-5xl font-extrabold text-white tracking-tight",
                    ),
                    rx.el.p(
                        "Ofrecemos una gama completa de soluciones de pintura para transformar cualquier espacio, con un compromiso inquebrantable con la calidad y la satisfacción del cliente.",
                        class_name="mt-4 max-w-3xl text-lg md:text-xl text-indigo-100",
                    ),
                    class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20 text-center",
                ),
                class_name="bg-indigo-700",
            ),
            rx.el.section(
                rx.el.div(
                    rx.el.div(
                        rx.foreach(State.services, detailed_service_card),
                        class_name="grid gap-8 md:grid-cols-2 lg:grid-cols-2",
                    ),
                    class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 sm:py-24",
                )
            ),
        )
    )


def galeria() -> rx.Component:
    return layout(
        rx.el.div(
            rx.el.section(
                rx.el.div(
                    rx.el.h1(
                        "Galería de Proyectos",
                        class_name="text-4xl md:text-5xl font-extrabold text-gray-900 tracking-tight",
                    ),
                    rx.el.p(
                        "Explora una selección de nuestros trabajos recientes y encuentra inspiración para tu próximo proyecto.",
                        class_name="mt-4 max-w-3xl text-lg md:text-xl text-gray-600",
                    ),
                    class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 text-center",
                )
            ),
            rx.el.section(
                rx.el.div(
                    rx.el.div(
                        gallery_filter_button("Todos", "all"),
                        gallery_filter_button("Residencial", "residencial"),
                        gallery_filter_button("Comercial", "comercial"),
                        gallery_filter_button("Oficinas", "oficinas"),
                        gallery_filter_button("Acabados", "acabados"),
                        class_name="flex flex-wrap justify-center gap-2 mb-12",
                    ),
                    rx.el.div(
                        rx.foreach(State.filtered_gallery_images, gallery_image_card),
                        class_name="grid gap-8 md:grid-cols-2 lg:grid-cols-3",
                    ),
                    class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pb-16 sm:pb-24",
                )
            ),
        )
    )


def gallery_filter_button(text: str, filter_value: str) -> rx.Component:
    is_active = State.gallery_filter == filter_value
    return rx.el.button(
        text,
        on_click=State.set_gallery_filter(filter_value),
        class_name=rx.cond(
            is_active,
            "px-4 py-2 rounded-full font-semibold bg-indigo-600 text-white shadow-md",
            "px-4 py-2 rounded-full font-semibold bg-gray-100 text-gray-700 hover:bg-gray-200",
        ),
    )


def gallery_image_card(image: dict) -> rx.Component:
    return rx.el.div(
        rx.image(
            src=image["src"],
            class_name="object-cover w-full h-60 rounded-t-xl group-hover:scale-105 transition-transform duration-300",
        ),
        rx.el.div(
            rx.el.p(image["title"], class_name="font-bold text-gray-800"),
            rx.el.p(
                image["category"].to_string().capitalize(),
                class_name="text-sm text-indigo-600 font-medium",
            ),
            class_name="p-4 bg-white rounded-b-xl",
        ),
        class_name="rounded-xl shadow-sm border border-gray-100 overflow-hidden group hover:shadow-xl transition-shadow duration-300",
    )


from app.states.quote_state import QuoteState


def quote_option_card(text: str, value: str, state_var: rx.Var) -> rx.Component:
    is_selected = state_var == value
    return rx.el.div(
        rx.el.p(text, class_name="font-semibold"),
        class_name=rx.cond(
            is_selected,
            "p-6 rounded-xl border-2 border-indigo-500 bg-indigo-50 cursor-pointer text-indigo-700",
            "p-6 rounded-xl border border-gray-200 bg-white hover:border-gray-400 cursor-pointer text-gray-700",
        ),
    )


def additional_service_checkbox(service: dict) -> rx.Component:
    service_id = service["id"]
    is_checked = QuoteState.additional_services[service_id]
    return rx.el.label(
        rx.el.div(
            rx.el.div(
                rx.icon("check", class_name="h-4 w-4 text-white"),
                class_name=rx.cond(
                    is_checked,
                    "flex items-center justify-center h-6 w-6 rounded-md bg-indigo-600",
                    "flex items-center justify-center h-6 w-6 rounded-md border border-gray-300 bg-gray-50",
                ),
            ),
            rx.el.div(
                rx.el.p(service["name"], class_name="font-semibold text-gray-800"),
                rx.el.p(service["description"], class_name="text-sm text-gray-600"),
            ),
            class_name="flex items-center gap-4",
        ),
        rx.el.p(f"+${service['price']}", class_name="font-bold text-gray-800"),
        on_click=lambda: QuoteState.toggle_additional_service(service_id),
        class_name="flex justify-between items-center p-4 rounded-xl border bg-white hover:bg-gray-50 cursor-pointer",
    )


def quote_summary() -> rx.Component:
    return rx.el.div(
        rx.el.h3("Resumen de Cotización", class_name="text-xl font-bold text-gray-900"),
        rx.el.div(
            rx.el.div(
                rx.el.p("Costo base", class_name="text-gray-600"),
                rx.el.p(
                    f"${QuoteState.base_price.to_string()} €",
                    class_name="font-medium text-gray-900",
                ),
                class_name="flex justify-between",
            ),
            rx.el.div(
                rx.el.p("Calidad de acabado", class_name="text-gray-600"),
                rx.el.p(
                    f"+${QuoteState.finish_cost.to_string()} €",
                    class_name="font-medium text-gray-900",
                ),
                class_name="flex justify-between",
            ),
            rx.el.div(
                rx.el.p("Servicios adicionales", class_name="text-gray-600"),
                rx.el.p(
                    f"+${QuoteState.additional_services_cost.to_string()} €",
                    class_name="font-medium text-gray-900",
                ),
                class_name="flex justify-between",
            ),
            class_name="mt-4 space-y-2 border-b pb-4",
        ),
        rx.el.div(
            rx.el.p("Total Estimado", class_name="font-semibold text-gray-900"),
            rx.el.p(
                f"${QuoteState.total_price.to_string()} €",
                class_name="text-2xl font-bold text-gray-900",
            ),
            class_name="flex justify-between items-center mt-4",
        ),
        class_name="p-6 bg-gray-50 rounded-2xl h-fit sticky top-24",
    )


def quote_form() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "Completa para finalizar",
            class_name="text-2xl font-bold text-gray-900 mb-6",
        ),
        rx.el.form(
            rx.el.div(
                rx.el.div(
                    rx.el.label(
                        "Nombre", class_name="text-sm font-medium text-gray-700"
                    ),
                    rx.el.input(
                        name="name",
                        type="text",
                        required=True,
                        class_name="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500",
                    ),
                ),
                rx.el.div(
                    rx.el.label(
                        "Email", class_name="text-sm font-medium text-gray-700"
                    ),
                    rx.el.input(
                        name="email",
                        type="email",
                        required=True,
                        class_name="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500",
                    ),
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 gap-6",
            ),
            rx.el.div(
                rx.el.label(
                    "Teléfono (Opcional)",
                    class_name="text-sm font-medium text-gray-700",
                ),
                rx.el.input(
                    name="phone",
                    type="tel",
                    class_name="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500",
                ),
            ),
            rx.el.div(
                rx.el.label(
                    "Mensaje (Opcional)", class_name="text-sm font-medium text-gray-700"
                ),
                rx.el.textarea(
                    name="message",
                    class_name="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500",
                ),
            ),
            rx.el.button(
                "Enviar Cotización",
                type="submit",
                class_name="w-full bg-indigo-600 text-white font-bold py-3 px-4 rounded-lg hover:bg-indigo-700 transition-colors shadow-md",
            ),
            on_submit=QuoteState.handle_submit,
            reset_on_submit=True,
            class_name="space-y-6",
        ),
    )


def cotizacion() -> rx.Component:
    return layout(
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Calculadora de Presupuesto",
                    class_name="text-4xl font-extrabold text-gray-900 tracking-tight",
                ),
                rx.el.p(
                    "Obtén una estimación para tu proyecto en minutos.",
                    class_name="mt-4 text-xl text-gray-600",
                ),
                class_name="text-center",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.h2(
                        "1. ¿Qué deseas pintar?",
                        class_name="text-2xl font-bold text-gray-900",
                    ),
                    rx.el.div(
                        rx.el.div(
                            quote_option_card(
                                "Pintura Residencial",
                                "residencial",
                                QuoteState.service_type,
                            ),
                            on_click=lambda: QuoteState.set_service_type("residencial"),
                        ),
                        rx.el.div(
                            quote_option_card(
                                "Pintura Comercial",
                                "comercial",
                                QuoteState.service_type,
                            ),
                            on_click=lambda: QuoteState.set_service_type("comercial"),
                        ),
                        rx.el.div(
                            quote_option_card(
                                "Pintura de Oficinas",
                                "oficinas",
                                QuoteState.service_type,
                            ),
                            on_click=lambda: QuoteState.set_service_type("oficinas"),
                        ),
                        class_name="grid grid-cols-1 md:grid-cols-3 gap-4 mt-6",
                    ),
                    rx.el.h2(
                        "2. ¿Cuántos metros cuadrados?",
                        class_name="text-2xl font-bold text-gray-900 mt-12",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.p(
                                f"{QuoteState.area} m²",
                                class_name="text-3xl font-bold text-indigo-600",
                            ),
                            class_name="text-center mb-4",
                        ),
                        rx.el.input(
                            type="range",
                            min=10,
                            max=500,
                            default_value=QuoteState.area,
                            key=QuoteState.area,
                            on_change=QuoteState.set_area.throttle(50),
                            class_name="w-full",
                        ),
                        class_name="p-6 bg-white rounded-xl border mt-6",
                    ),
                    rx.el.h2(
                        "3. Elige la calidad del acabado",
                        class_name="text-2xl font-bold text-gray-900 mt-12",
                    ),
                    rx.el.div(
                        rx.el.div(
                            quote_option_card(
                                "Estándar", "estandar", QuoteState.finish_quality
                            ),
                            on_click=lambda: QuoteState.set_finish_quality("estandar"),
                        ),
                        rx.el.div(
                            quote_option_card(
                                "Premium", "premium", QuoteState.finish_quality
                            ),
                            on_click=lambda: QuoteState.set_finish_quality("premium"),
                        ),
                        rx.el.div(
                            quote_option_card(
                                "Especial Decorativo",
                                "especial",
                                QuoteState.finish_quality,
                            ),
                            on_click=lambda: QuoteState.set_finish_quality("especial"),
                        ),
                        class_name="grid grid-cols-1 md:grid-cols-3 gap-4 mt-6",
                    ),
                    rx.el.h2(
                        "4. Servicios adicionales",
                        class_name="text-2xl font-bold text-gray-900 mt-12",
                    ),
                    rx.el.div(
                        rx.foreach(
                            QuoteState.ADDITIONAL_COSTS, additional_service_checkbox
                        ),
                        class_name="space-y-4 mt-6",
                    ),
                    rx.el.div(
                        rx.cond(
                            QuoteState.form_submitted,
                            rx.el.div(
                                rx.icon(
                                    "check_check",
                                    class_name="h-12 w-12 text-green-500 mx-auto",
                                ),
                                rx.el.h3(
                                    "¡Cotización enviada!",
                                    class_name="mt-4 text-2xl font-bold text-gray-900 text-center",
                                ),
                                rx.el.p(
                                    "Gracias por tu interés. Nos pondremos en contacto contigo pronto.",
                                    class_name="mt-2 text-gray-600 text-center",
                                ),
                                class_name="p-8 bg-green-50 border border-green-200 rounded-2xl",
                            ),
                            quote_form(),
                        ),
                        class_name="mt-12 pt-12 border-t",
                    ),
                    class_name="col-span-2",
                ),
                quote_summary(),
                class_name="grid grid-cols-1 lg:grid-cols-3 gap-12 mt-12",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16",
        )
    )


def contacto() -> rx.Component:
    return layout(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.h1(
                        "Contáctanos",
                        class_name="text-4xl md:text-5xl font-extrabold text-gray-900 tracking-tight",
                    ),
                    rx.el.p(
                        "¿Tienes un proyecto en mente o alguna pregunta? Estamos aquí para ayudarte.",
                        class_name="mt-4 text-lg md:text-xl text-gray-600",
                    ),
                    class_name="mb-12",
                ),
                rx.el.div(
                    contact_form(),
                    contact_info(),
                    class_name="grid md:grid-cols-2 gap-12",
                ),
                class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 sm:py-24",
            )
        )
    )


def contact_form() -> rx.Component:
    return rx.el.form(
        rx.el.h2(
            "Envíanos un mensaje", class_name="text-2xl font-bold text-gray-900 mb-6"
        ),
        rx.el.div(
            rx.el.input(placeholder="Nombre", name="name", required=True),
            rx.el.input(placeholder="Email", name="email", type="email", required=True),
            class_name="grid grid-cols-1 sm:grid-cols-2 gap-6",
        ),
        rx.el.input(placeholder="Asunto", name="subject"),
        rx.el.textarea(placeholder="Tu mensaje...", name="message", rows=5),
        rx.el.button(
            "Enviar Mensaje",
            type="submit",
            class_name="w-full bg-indigo-600 text-white font-bold py-3 px-4 rounded-lg hover:bg-indigo-700 transition-colors shadow-md",
        ),
        on_submit=lambda form_data: rx.toast.success("Mensaje enviado con éxito"),
        reset_on_submit=True,
        class_name="space-y-6 bg-white p-8 rounded-2xl border border-gray-100 shadow-sm",
    )


def contact_info() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "Información de Contacto",
            class_name="text-2xl font-bold text-gray-900 mb-6",
        ),
        rx.el.div(
            contact_info_item(
                "map-pin", "Ubicación", "Calle Falsa 123, Madrid, España"
            ),
            contact_info_item("mail", "Email", "info@pintapro.com"),
            contact_info_item("phone", "Teléfono", "+1 (234) 567-890"),
            class_name="space-y-6",
        ),
    )


def contact_info_item(icon_name: str, title: str, text: str) -> rx.Component:
    return rx.el.div(
        rx.icon(icon_name, class_name="h-6 w-6 text-indigo-500"),
        rx.el.div(
            rx.el.h3(title, class_name="font-semibold text-gray-900"),
            rx.el.p(text, class_name="text-gray-600"),
        ),
        class_name="flex items-start gap-4",
    )


app.add_page(servicios)
app.add_page(galeria)
app.add_page(cotizacion)
app.add_page(contacto)