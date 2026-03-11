from django.core.exceptions import ValidationError
from django.test import TestCase

from network.models import ElectronicsRetailNetwork


class RetailNetworkHierarchyTest(TestCase):

    def test_cannot_reference_itself(self):
        """Объект не может быть поставщиком сам себе."""

        node = ElectronicsRetailNetwork.objects.create(
            name='Test Factory',
            level=0,
            email='factory@test.com',
            country='USA',
            city='New York',
            street='Main',
            house_number='1'
        )

        node.provider = node

        with self.assertRaises(ValidationError):
            node.full_clean()

    def test_cannot_create_cycle(self):
        """Нельзя создать циклическую иерархию."""

        factory = ElectronicsRetailNetwork.objects.create(
            name='Factory',
            level=0,
            email='factory@test.com',
            country='USA',
            city='NY',
            street='Main',
            house_number='1'
        )

        store = ElectronicsRetailNetwork.objects.create(
            name='Store',
            level=1,
            provider=factory,
            email='store@test.com',
            country='USA',
            city='NY',
            street='Second',
            house_number='2'
        )

        entrepreneur = ElectronicsRetailNetwork.objects.create(
            name='IP',
            level=2,
            provider=store,
            email='ip@test.com',
            country='USA',
            city='NY',
            street='Third',
            house_number='3'
        )

        # пытаемся создать цикл
        factory.provider = entrepreneur

        with self.assertRaises(ValidationError):
            factory.full_clean()
