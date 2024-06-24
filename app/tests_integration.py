from django.test import TestCase
from django.shortcuts import reverse
from app.models import Client, Provider, Pet

class HomePageTest(TestCase):
    def test_use_home_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")


class ClientsTest(TestCase):
    def test_repo_use_repo_template(self):
        response = self.client.get(reverse("clients_repo"))
        self.assertTemplateUsed(response, "clients/repository.html")

    def test_repo_display_all_clients(self):
        response = self.client.get(reverse("clients_repo"))
        self.assertTemplateUsed(response, "clients/repository.html")

    def test_form_use_form_template(self):
        response = self.client.get(reverse("clients_form"))
        self.assertTemplateUsed(response, "clients/form.html")

    def test_can_create_client(self):
        response = self.client.post(
            reverse("clients_form"),
            data={
                "name": "Juan Sebastian Veron",
                "phone": "221555232",
                "address": "13 y 44",
                "email": "brujita75@hotmail.com",
            },
        )
        clients = Client.objects.all()
        self.assertEqual(len(clients), 1)

        self.assertEqual(clients[0].name, "Juan Sebastian Veron")
        self.assertEqual(clients[0].phone, "221555232")
        self.assertEqual(clients[0].address, "13 y 44")
        self.assertEqual(clients[0].email, "brujita75@hotmail.com")

        self.assertRedirects(response, reverse("clients_repo"))

    def test_validation_errors_create_client(self):
        response = self.client.post(
            reverse("clients_form"),
            data={},
        )

        self.assertContains(response, "Por favor ingrese un nombre")
        self.assertContains(response, "Por favor ingrese un teléfono")
        self.assertContains(response, "Por favor ingrese un email")

    def test_should_response_with_404_status_if_client_doesnt_exists(self):
        response = self.client.get(reverse("clients_edit", kwargs={"id": 100}))
        self.assertEqual(response.status_code, 404)

    def test_validation_invalid_email(self):
        response = self.client.post(
            reverse("clients_form"),
            data={
                "name": "Juan Sebastian Veron",
                "phone": "221555232",
                "address": "13 y 44",
                "email": "brujita75",
            },
        )

        self.assertContains(response, "Por favor ingrese un email valido")

    def test_edit_user_with_valid_data(self):
        client = Client.objects.create(
            name="Juan Sebastián Veron",
            address="13 y 44",
            phone="221555232",
            email="brujita75@hotmail.com",
        )

        response = self.client.post(
            reverse("clients_form"),
            data={
                "id": client.id,
                "name": "Guido Carrillo",
            },
        )

        # redirect after post
        self.assertEqual(response.status_code, 302)

        editedClient = Client.objects.get(pk=client.id)
        self.assertEqual(editedClient.name, "Guido Carrillo")
        self.assertEqual(editedClient.phone, client.phone)
        self.assertEqual(editedClient.address, client.address)
        self.assertEqual(editedClient.email, client.email)



class ProvidersTest(TestCase):

    def test_repo_use_repo_template(self):
        response = self.client.get(reverse("providers_repo"))
        self.assertTemplateUsed(response, "providers/repository.html")

    def test_repo_display_all_providers(self):
        response = self.client.get(reverse("providers_repo"))
        self.assertTemplateUsed(response, "providers/repository.html")

    def test_form_use_form_template(self):
        response = self.client.get(reverse("providers_form"))
        self.assertTemplateUsed(response, "providers/form.html")

    def test_can_create_provider(self):
        response = self.client.post(
            reverse("providers_form"),
            data={
                "name": "Proveedor de Prueba",
                "email": "proveedor@ejemplo.com",
                "address": "Calle Falsa 123",
            },
        )
        providers = Provider.objects.all()
        self.assertEqual(len(providers), 1)

        self.assertEqual(providers[0].name, "Proveedor de Prueba")
        self.assertEqual(providers[0].email, "proveedor@ejemplo.com")
        self.assertEqual(providers[0].address, "Calle Falsa 123")

        self.assertRedirects(response, reverse("providers_repo"))

    def test_validation_errors_create_provider(self):
        response = self.client.post(
            reverse("providers_form"),
            data={},
        )

        self.assertContains(response, "Por favor ingrese un nombre")
        self.assertContains(response, "Por favor ingrese un email")

    def test_should_response_with_404_status_if_provider_doesnt_exists(self):
        response = self.client.get(reverse("providers_edit", kwargs={"id": 100}))
        self.assertEqual(response.status_code, 404)

    def test_validation_invalid_email(self):
        response = self.client.post(
            reverse("providers_form"),
            data={
                "name": "Juan Perez",
                "email": "invalid-email",  # email inválido
                "address": "Calle 123",
            },
        )

        self.assertContains(response, "Por favor ingrese un email valido")


    def test_edit_provider_with_valid_data(self):
        provider = Provider.objects.create(
            name="Proveedor Original",
            address="Dirección Original",
            email="original@ejemplo.com",
        )

        response = self.client.post(
            reverse("providers_form"),
            data={
                "id": provider.id,
                "name": "Proveedor Actualizado",
                "address": provider.address,
                "email": provider.email,
            },
        )

        # Redirección después del POST
        self.assertEqual(response.status_code, 302)

        edited_provider = Provider.objects.get(pk=provider.id)
        self.assertEqual(edited_provider.name, "Proveedor Actualizado")
        self.assertEqual(edited_provider.email, provider.email)
        self.assertEqual(edited_provider.address, provider.address)

# TEST DE PET
class PetsTest(TestCase):
    
    # creacion de mascota
    def test_can_create_pet(self):
            response = self.client.post(
                reverse("pets_form"),
                data={
                    "name": "Roma",
                    "breed": "Labrador",
                    "birthday": "2021-10-10",
                    "weight": 10
                },
            )
            pets = Pet.objects.all()

            self.assertEqual(len(pets), 1)
            # verificamos coincidencias
            self.assertEqual(pets[0].name, "Roma")
            self.assertEqual(pets[0].breed, "Labrador")
            self.assertEqual(pets[0].birthday.strftime('%Y-%m-%d'), "2021-10-10") # formateo la fecha de cumple para comparar
            self.assertEqual(pets[0].weight, 10)

            # verifico si existe en la base de datos
            self.assertTrue(Pet.objects.filter(name="Roma").exists())
            # verifico si redirige a la url correcta
            self.assertRedirects(response, reverse("pets_repo"))



    # validar de que el peso no puede ser negativo
    def test_validation_errors_weight_less_than_zero(self):
        response = self.client.post(
                reverse("pets_form"),
                data={
                    "name": "Roma",
                    "breed": "Labrador",
                    "birthday": "2021-10-10",
                    "weight": -10
                },
            )
        # Verifico si el peso es negativo y muestra un mensaje de error
        self.assertContains(response, "El peso debe ser un número mayor a cero")
    
    def test_validation_invalid_birthday(self):
        
        response = self.client.post(
            reverse("pets_form"),
            data = {
            "name": "Pepe",
            "breed": "Labrador",
            "birthday": "2026-01-01",
            "weight": 10
        }
        )

        self.assertContains(response, "La fecha de nacimiento no puede ser mayor o igual a la fecha actual")


class ProductsTest(TestCase):
    def test_validation_invalid_price(self):
        # client es un objeto que proporciona Django para simular solicitudes HTTP en tus tests.
        response = self.client.post(
            reverse("products_form"),
            data={
                "name": "Paracetamol",
                "description": "Medicamento para el dolor",
                "price": 0,
            },
        )

        self.assertContains(response, "El precio debe ser mayor que cero")
        
class MedicinesTest(TestCase):
    def test_validation_invalid_dose(self):
        # client es un objeto que proporciona Django para simular solicitudes HTTP en tus tests.
        response = self.client.post(
            reverse("medicines_form"),
            data={
                "name": "Diclofenac",
                "description": "Calma el dolor muscular",
                "dose": 0,
            },
        )

        self.assertContains(response, "La dosis debe estar en un rango de 1 a 10")

