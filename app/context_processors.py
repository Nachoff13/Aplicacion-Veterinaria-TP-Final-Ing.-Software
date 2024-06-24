from django.urls import reverse

links = [
    {"label": "Home", "href": reverse("home"), "icon": "bi bi-house-door"},
    {"label": "Clientes", "href": reverse("clients_repo"), "icon": "bi bi-people"},
    {"label": "Medicamentos", "href": reverse("medicines_repo"), "icon": "bi bi-capsule"},
    {"label": "Mascotas", "href": reverse("pets_repo"), "icon": "bi bi-piggy-bank"},
    {"label": "Productos", "href": reverse("products_repo"), "icon": "bi bi-box"},
    {"label": "Proveedores", "href": reverse("providers_repo"), "icon": "bi bi-briefcase"},
    {"label": "Veterinarios", "href": reverse("vets_repo"), "icon": "bi bi-hospital"},

]


def navbar(request):
    def add_active(link):
        copy = link.copy()

        if copy["href"] == "/":
            copy["active"] = request.path == "/"
        else:
            copy["active"] = request.path.startswith(copy.get("href", ""))

        return copy

    return {"links": map(add_active, links)}
