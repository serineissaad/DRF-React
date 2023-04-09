from django.test import TestCase
from django.contrib.auth.models import User
from product.models import Post, Category, Tenant, City, Owner, Property, Images, Booking, Review, Payment


class Test_Create_Post(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='django')

        testuser1 = User.objects.create_user(
            username='test_user1', password='123456789')
        testuser1.save()

        test_post = Post.objects.create(
            category_id=1, title='Post Title', excerpt='Post Excerpt', content='Post Content', slug='post-title', author_id=1, status='published')
        test_post.save()

    def test_blog_content(self):
        post = Post.postobjects.get(id=1)
        cat = Category.objects.get(id=1)
        author = f'{post.author}'
        excerpt = f'{post.excerpt}'
        title = f'{post.title}'
        content = f'{post.content}'
        status = f'{post.status}'
        self.assertEqual(author, 'test_user1')
        self.assertEqual(title, 'Post Title')
        self.assertEqual(content, 'Post Content')
        self.assertEqual(status, 'published')
        self.assertEqual(str(post), "Post Title")
        self.assertEqual(str(cat), "django")

#_________________
class Test_Create_Tenant(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_tenant = Tenant.objects.create(name='Test Tenant', phone='1234567890', email='test@tenant.com')

    def test_tenant_content(self):
        tenant = Tenant.objects.get(id=1)
        name = f'{tenant.name}'
        phone = f'{tenant.phone}'
        email = f'{tenant.email}'
        self.assertEqual(name, 'Test Tenant')
        self.assertEqual(phone, '1234567890')
        self.assertEqual(email, 'test@tenant.com')
        self.assertEqual(str(tenant), "Test Tenant")

#_________________
class Test_Create_Owner(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_owner = Owner.objects.create(name='Test Owner', phone='1234567890', email='test@owner.com')

    def test_owner_content(self):
        owner = Owner.objects.get(id=1)
        name = f'{owner.name}'
        phone = f'{owner.phone}'
        email = f'{owner.email}'
        self.assertEqual(name, 'Test Owner')
        self.assertEqual(phone, '1234567890')
        self.assertEqual(email, 'test@owner.com')
        self.assertEqual(str(owner), "Test Owner")

#_________________
class Test_Create_Property(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_city = City.objects.create(name='Test City')
        test_owner = Owner.objects.create(name='Test Owner', phone='1234567890', email='test@owner.com')
        test_property = Property.objects.create(type='House', title='Test Property', description='Test Description', address='Test Address', city=test_city, owner=test_owner)

    def test_property_content(self):
        property = Property.objects.get(id=1)
        type = f'{property.type}'
        title = f'{property.title}'
        description = f'{property.description}'
        address = f'{property.address}'
        city = f'{property.city}'
        owner = f'{property.owner}'
        self.assertEqual(type, 'House')
        self.assertEqual(title, 'Test Property')
        self.assertEqual(description, 'Test Description')
        self.assertEqual(address, 'Test Address')
        self.assertEqual(city, 'Test City')
        self.assertEqual(owner, 'Test Owner')
        self.assertEqual(str(property), "Test Property")

#_________________
class Test_Create_Image(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_property = Property.objects.create(type='House', title='Test Property', description='Test Description', address='Test Address')
        test_image = Images.objects.create(property=test_property, image='test.jpg')

    def test_image_content(self):
        image = Images.objects.get(id=1)
        property = f'{image.property}'
        self.assertEqual(property, 'Test Property')
        self.assertEqual(str(image), "Image for Test Property")

#_________________
class Test_Create_Booking(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_tenant = Tenant.objects.create(name='Test Tenant', phone='1234567890', email='test@tenant.com')
        test_property = Property.objects.create(type='House', title='Test Property', description='Test Description', address='Test Address')
        test_booking = Booking.objects.create(tenant=test_tenant, property=test_property, start_date='2022-01-01', end_date='2022-01-05', nb_ppl=4, status='confirmed')

    def test_booking_model(self):
        booking = Booking.objects.get(id=1)
        property = f'{booking.property}'
        self.assertEqual(property, 'Test Property')
        self.assertEqual(str(booking), f'Booking for {property}')

#_________________
#_________________