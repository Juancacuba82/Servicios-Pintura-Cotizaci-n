import reflex as rx
from typing import TypedDict


class AdditionalService(TypedDict):
    id: str
    name: str
    description: str
    price: int


class QuoteState(rx.State):
    service_type: str = "residencial"
    area: int = 50
    finish_quality: str = "estandar"
    additional_services: dict[str, bool] = {
        "preparacion": False,
        "techos": False,
        "muebles": False,
    }
    form_data: dict[str, str] = {}
    form_submitted: bool = False
    PRICES_PER_M2 = {"residencial": 8, "comercial": 7, "oficinas": 6}
    FINISH_MULTIPLIERS = {"estandar": 1, "premium": 1.5, "especial": 2.2}
    ADDITIONAL_COSTS: list[AdditionalService] = [
        {
            "id": "preparacion",
            "name": "Preparación de superficie",
            "description": "Lijado, limpieza y reparación de pequeñas grietas.",
            "price": 150,
        },
        {
            "id": "techos",
            "name": "Pintura de techos",
            "description": "Aplicación de dos capas de pintura blanca en techos.",
            "price": 200,
        },
        {
            "id": "muebles",
            "name": "Mover y cubrir muebles",
            "description": "Protección completa de su mobiliario y suelo.",
            "price": 100,
        },
    ]

    @rx.event
    def toggle_additional_service(self, service_id: str):
        self.additional_services[service_id] = not self.additional_services[service_id]

    @rx.var
    def base_price(self) -> float:
        return self.PRICES_PER_M2.get(self.service_type, 0) * self.area

    @rx.var
    def finish_cost(self) -> float:
        multiplier = self.FINISH_MULTIPLIERS.get(self.finish_quality, 1)
        return self.base_price * multiplier - self.base_price

    @rx.var
    def additional_services_cost(self) -> int:
        cost = 0
        for service in self.ADDITIONAL_COSTS:
            if self.additional_services.get(service["id"]):
                cost += service["price"]
        return cost

    @rx.var
    def total_price(self) -> float:
        return self.base_price + self.finish_cost + self.additional_services_cost

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data
        self.form_submitted = True