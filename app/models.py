from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length = 24)
    phone_number = models.CharField(max_length = 10)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="app/uploads/", null=True, blank=True)

class Properties(models.Model):
    user_props = models.ForeignKey(Account, on_delete=models.CASCADE)
    prop_name = models.CharField(max_length=255)
    price = models.IntegerField()
    state = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    zip_code = models.IntegerField()
    size = models.IntegerField()
    available = models.BooleanField()
    picture = models.ImageField(upload_to="app/uploads/", null=True, blank=True, default='app/uploads/default.png')
    desc = models.TextField(null = True, blank=True)

def filter_search(item):
    list_of_props = []
    print(item)
    if item.isdigit() == True:
        prop_zip = Properties.objects.filter(zip_code = item)
        for i in prop_zip:
            list_of_props.append(i)

        prop_price = Properties.objects.filter(price = item)
        for i in prop_price:
            list_of_props.append(i)

        prop_size = Properties.objects.filter(size = item)
        for i in prop_size:
            list_of_props.append(i)
        
    else:
        prop_address = Properties.objects.filter(address = item)
        for i in prop_address:
            list_of_props.append(i)

        prop_city = Properties.objects.filter(city = item)
        for i in prop_city:
            list_of_props.append(i)

        prop_name = Properties.objects.filter(prop_name = item)
        for i in prop_name:
            list_of_props.append(i)

        prop_state = Properties.objects.filter(state = item)
        for i in prop_state:
            list_of_props.append(i)
            

    return list_of_props
