from django.db import models

class Reviews(models.Model):
    count = models.IntegerField()
    stars = models.IntegerField()

class Users(models.Model):
    first_name = models.CharField(max_length=100, blank=True, default='')
    last_name = models.CharField(max_length=100, blank=True, default='')
    email = models.EmailField(max_length=254,default='')
    location = models.CharField(max_length=100, blank=True, default='',unique = True)
    postal = models.CharField(max_length=100, blank=True, default='',unique = True)

  
class Services(models.Model):
    wifi = models.BooleanField(default=True)
    shower = models.BooleanField(default=True)
    kitchen = models.BooleanField(default=True)
    surveillanceCamera = models.BooleanField(default=True)
    HeatingSystem = models.BooleanField(default=True)
    Television = models.BooleanField(default=True)

class Accomodations(models.Model):   
    title = models.CharField(max_length=100, blank=True, default='')
    address = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(default='') 
    price = models.IntegerField()
    image = models.URLField()
    image2 = models.URLField()
    image3 = models.URLField()
    image4 = models.URLField()
    owner = models.ForeignKey(Users,on_delete=models.CASCADE)
    visibility = models.BooleanField(default=True)
    guests = models.IntegerField(default=1)
    bedrooms = models.IntegerField(default=1)
    beds = models.IntegerField(default=1)
    bathroom = models.IntegerField(default=1)
    services = models.ForeignKey(Services,null=False,on_delete=models.CASCADE)
    rules = models.TextField(default='')
    extraInfo = models.TextField(default='')
    city = models.CharField(max_length=100, blank=False, default='')
    kindOfHouse = models.CharField(max_length=100, blank=True, default='')
    reviews = models.ForeignKey(Reviews,on_delete=models.CASCADE)
    locationMap = models.TextField(default='')
    published_date = models.DateTimeField(blank=True, null=True)

class Restaurant(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(default='')
    priceRange = models.CharField(max_length=100, blank=True, default='')
    address = models.CharField(max_length=100, blank=True, default='')
    image = models.URLField()
    image2 = models.URLField()
    image3 = models.URLField()
    city = models.CharField(max_length=100, blank=False, default='')
    link = models.URLField()
    locationMap = models.TextField()
    kindOfRestaurant=models.CharField(max_length=100, blank=False, default='')

class Attractions(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    built = models.CharField(max_length=100, blank=True, default='')
    kindOfAttractions = models.CharField(max_length=100, blank=True, default='')
    title1 = models.CharField(max_length=100, blank=True, default='')
    title2 = models.CharField(max_length=100, blank=True, default='')
    title3 = models.CharField(max_length=100, blank=True, default='')
    description1 = models.TextField(default='')
    description2 = models.TextField(default='')
    description3 = models.TextField(default='')
    address = models.CharField(max_length=100, blank=True, default='')
    image = models.URLField()
    image2 = models.URLField()
    image3 = models.URLField()
    city = models.CharField(max_length=100, blank=False, default='')
    link = models.URLField()
    locationMap = models.TextField()

class Deal(models.Model):
    price = models.IntegerField()
    description = models.TextField()
    accomodations = models.ForeignKey(Accomodations,on_delete=models.CASCADE)
    attractions = models.ForeignKey(Attractions,on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    