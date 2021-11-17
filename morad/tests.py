from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Car
from django.urls import reverse

class BlogTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='morad',
            email="issa@admin.com",
            password='0000'
        )

        self.post = Car.objects.create(
            name = "mbw",
            color = 'red',
            type_car = 'car',
            model_car = 2020,
            description = 'carspeed',
            honer = self.user
         
          
        )

    
    def test_string_representation(self):
        post = Car(name='mbw')
        self.assertEqual(str(post), post.name)


# #####################
    def test_all_fields(self):
        
        self.assertEqual(str(self.post), 'mbw')
        self.assertEqual(f'{self.post.honer}', 'issa@admin.com')
        self.assertEqual(self.post.description, 'carspeed')

#    ###########################

    def test_blog_list_view(self):
        response = self.client.get(reverse('list-cars'))
        self.assertEqual(response.status_code, 200)

    def test_blog_details_view(self):
        response = self.client.get(reverse('detail-car', args='1'))
        self.assertEqual(response.status_code, 200)


#         ####### 

        
    def test_blog_update_view(self):
        response = self.client.post(reverse('update-car', args='1'), {
            'name': 'bmw',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'bmw')

#     ############

    def test_home_status(self):
        expected = 200
        url = reverse('list-cars')
        response = self.client.get(url)
        actual = response.status_code 
        self.assertEquals(expected,actual)
        
    def test_home_template(self):
        url = reverse('list-cars')
        response = self.client.get(url)
        actual = 'cars/cars.html'
        self.assertTemplateUsed(response, actual)
    
# #    ################

    def test_create_view(self):
        response = self.client.post(reverse('create-car'), {
            'name': 'bmw',
            'honer': self.user,
            'description' :'veryfast',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'bmw')
        self.assertContains(response, 'veryfast')
        self.assertContains(response, 'issa@admin.com')

    def test_delete_view(self):
        response = self.client.get(reverse('delete-car', args='1'))
        self.assertEqual(response.status_code, 200)
  
