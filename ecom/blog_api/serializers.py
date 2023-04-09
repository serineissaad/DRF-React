from rest_framework import serializers
from product.models import Post, Tenant, Owner, Amenity, Property, Images, Booking, Review, Payment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'author', 'excerpt', 'content', 'status')
        model = Post

class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'email', 'phone')
        model = Tenant

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'email', 'phone')
        model = Owner

class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'icon')
        model = Amenity

class PropertySerializer(serializers.ModelSerializer):
    amenities = AmenitySerializer(many=True, read_only=True)
    city = serializers.CharField(source='city.name')
    owner = OwnerSerializer(read_only=True)

    class Meta:
        fields = ('id', 'type', 'title', 'description', 'address', 'city', 'owner', 'amenities', 'status', 'nb_ppl', 'price_per_night')
        model = Property

class ImageSerializer(serializers.ModelSerializer):
    property = PropertySerializer(read_only=True)

    class Meta:
        fields = ('id', 'image', 'property')
        model = Images

class BookingSerializer(serializers.ModelSerializer):
    tenant = TenantSerializer(read_only=True)
    property = PropertySerializer(read_only=True)

    class Meta:
        fields = ('id', 'check_in_date', 'check_out_date', 'nb_nights', 'nb_adults', 'nb_children', 'tenant', 'property')
        model = Booking

class ReviewSerializer(serializers.ModelSerializer):
    tenant = TenantSerializer(read_only=True)
    property = PropertySerializer(read_only=True)

    class Meta:
        fields = ('id', 'stars', 'comment', 'tenant', 'property')
        model = Review

class PaymentSerializer(serializers.ModelSerializer):
    booking = BookingSerializer(read_only=True)

    class Meta:
        fields = ('id', 'payment_date', 'amount', 'booking')
        model = Payment
