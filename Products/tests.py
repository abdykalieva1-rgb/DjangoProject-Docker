from Products.models import Car
from django.test import TestCase
from django.urls import reverse


class CarPagesTest(TestCase):
    def setUp(self):
        # Создаем временную машину специально для теста
        self.car = Car.objects.create(
            name="Test Car",
            year=2024,
            color="Blue"
        )

    def test_next_page_status_code(self):
        response = self.client.get(reverse('next_page'))
        self.assertEqual(response.status_code, 200)

    def test_second_page_status_code(self):
        # Теперь мы проверяем переход на страницу конкретной машины
        response = self.client.get(reverse('second_page', args=[self.car.id]))
        self.assertEqual(response.status_code, 200)