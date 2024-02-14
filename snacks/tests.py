from django.test import TestCase, Client
from django.urls import reverse
from .models import Snack

class SnackDetailViewTest(TestCase):
    def setUp(self):
        # Create a sample snack for testing
        self.snack = Snack.objects.create(name='Test Snack', rating=5, critical_description='Test Description', purchaser_id=1)

    def test_snack_detail_view(self):
        # Get the URL for the snack detail page using the reverse function
        url = reverse('snack_detail', kwargs={'pk': self.snack.pk})

        # Create a test client
        client = Client()

        # Perform a GET request to the snack detail page
        response = client.get(url)

        # Check if the status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the correct template is used
        self.assertTemplateUsed(response, 'snack_detail.html')
