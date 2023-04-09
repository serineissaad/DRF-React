from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1) #default catgory with id=1
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(
        max_length=10, choices=options, default='published')
    objects = models.Manager()  # default manager
    postobjects = PostObjects()  # custom manager

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title


class Owner(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    
    def __str__(self):
        return self.name
    
    #class Meta:
    #    verbose_name_plural = "Owners"

class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Property(models.Model):
    STATUS_CHOICES = [
        (0, 'Available'),
        (1, 'Booked for now'),
        (-1, 'Unavailable'),
    ]
    options = (
        ('house','House'),
        ('apartment','Apartment'),
    )
    type = models.CharField(max_length=10, choices=options, default='House')
    title = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    amenities = models.ManyToManyField('Amenity')
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    nb_ppl = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)]) 
    nb_bed = models.IntegerField()
    area = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.title
    
class Amenity(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Images(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_images/')
    
class Tenant(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name
    
class Booking(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    payment_method = models.CharField(max_length=20)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.tenant.name} - {self.property.name} - {self.start_date} - {self.end_date}"
    
class Review(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    stars = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.tenant.name} - {self.property.name}"
    
class Payment(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.tenant.name} - {self.booking.property.name} - {self.payment_date}"

