from django.test import TestCase, Client
from django.urls import reverse
from .models import Product # Import the Product model

# Assuming your URL name for fetch_products is 'fetchall'
# (Based on the 'return redirect(reverse('fetchall'))' in your views logic)

class ProductFetchTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('fetchall') 

    def test_multiple_products_exist(self):
        Product.objects.create(name='Widget A', price=10.00, description='Desc A', category='Gadget')
        Product.objects.create(name='Gizmo B',price=25.50,description='Desc B', category='Tool')
       
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products.html')
        self.assertEqual(len(response.context['products']), 2) 
        self.assertContains(response, 'Widget A')
        self.assertContains(response, 'Gizmo B')
        self.assertContains(response, '10.00')
        self.assertContains(response, '25.50')
        self.assertContains(response, 'Update')
        self.assertContains(response, 'Delete')