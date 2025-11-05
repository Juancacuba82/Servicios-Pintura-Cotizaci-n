import reflex as rx
from typing import TypedDict


class NavItem(TypedDict):
    name: str
    path: str


class Service(TypedDict):
    icon: str
    name: str
    description: str


class Advantage(TypedDict):
    icon: str
    title: str
    description: str


class Testimonial(TypedDict):
    name: str
    location: str
    rating: int
    comment: str
    avatar: str


class GalleryImage(TypedDict):
    src: str
    category: str
    title: str


class State(rx.State):
    """The base state for the app."""

    nav_menu: list[NavItem] = [
        {"name": "Inicio", "path": "/"},
        {"name": "Servicios", "path": "/servicios"},
        {"name": "Galería", "path": "/galeria"},
        {"name": "Cotización", "path": "/cotizacion"},
        {"name": "Contacto", "path": "/contacto"},
    ]
    services: list[Service] = [
        {
            "icon": "home",
            "name": "Pintura Residencial",
            "description": "Transformamos tu hogar con colores que inspiran y acabados de la más alta calidad.",
        },
        {
            "icon": "building",
            "name": "Pintura Comercial",
            "description": "Renovamos la imagen de tu negocio para atraer más clientes y crear un ambiente profesional.",
        },
        {
            "icon": "briefcase",
            "name": "Pintura de Oficinas",
            "description": "Creamos espacios de trabajo productivos y agradables con una selección de colores experta.",
        },
        {
            "icon": "brush",
            "name": "Acabados Especiales",
            "description": "Desde estucos hasta efectos decorativos, ofrecemos acabados únicos para paredes con carácter.",
        },
    ]
    advantages: list[Advantage] = [
        {
            "icon": "award",
            "title": "Calidad Garantizada",
            "description": "Utilizamos solo materiales de primera y técnicas probadas para un resultado duradero y excepcional.",
        },
        {
            "icon": "clock",
            "title": "Puntualidad y Eficiencia",
            "description": "Respetamos tu tiempo. Cumplimos con los plazos acordados sin sacrificar la calidad del trabajo.",
        },
        {
            "icon": "calculator",
            "title": "Cotización Transparente",
            "description": "Obtén un presupuesto claro y detallado al instante, sin costos ocultos ni sorpresas.",
        },
        {
            "icon": "users",
            "title": "Equipo Profesional",
            "description": "Nuestro equipo de pintores está altamente calificado, es respetuoso y está comprometido con la excelencia.",
        },
    ]
    testimonials: list[Testimonial] = [
        {
            "name": "Ana García",
            "location": "Madrid",
            "rating": 5,
            "comment": "¡El equipo de PintaPro es increíble! Transformaron mi salón por completo. Rápidos, limpios y muy profesionales.",
            "avatar": "Ana",
        },
        {
            "name": "Carlos Pérez",
            "location": "Barcelona",
            "rating": 5,
            "comment": "Contraté el servicio para mi oficina y el resultado superó mis expectativas. El acabado es perfecto y cumplieron con los plazos.",
            "avatar": "Carlos",
        },
        {
            "name": "Lucía Fernández",
            "location": "Valencia",
            "rating": 4,
            "comment": "Muy buen servicio. El presupuesto fue transparente desde el principio y el resultado final es de gran calidad.",
            "avatar": "Lucia",
        },
    ]
    gallery_images: list[GalleryImage] = [
        {
            "src": "/placeholder.svg",
            "category": "residencial",
            "title": "Salón Moderno",
        },
        {
            "src": "/placeholder.svg",
            "category": "comercial",
            "title": "Recepción de Hotel",
        },
        {
            "src": "/placeholder.svg",
            "category": "oficinas",
            "title": "Espacio de Co-working",
        },
        {
            "src": "/placeholder.svg",
            "category": "residencial",
            "title": "Dormitorio Infantil",
        },
        {
            "src": "/placeholder.svg",
            "category": "acabados",
            "title": "Pared con Estuco",
        },
        {
            "src": "/placeholder.svg",
            "category": "comercial",
            "title": "Tienda Boutique",
        },
    ]
    gallery_filter: str = "all"

    @rx.var
    def filtered_gallery_images(self) -> list[GalleryImage]:
        if self.gallery_filter == "all":
            return self.gallery_images
        return [
            image
            for image in self.gallery_images
            if image["category"] == self.gallery_filter
        ]

    @rx.event
    def set_gallery_filter(self, new_filter: str):
        self.gallery_filter = new_filter

    @rx.var
    def current_page(self) -> str:
        return self.router.page.path