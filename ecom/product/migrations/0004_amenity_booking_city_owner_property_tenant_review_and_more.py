# Generated by Django 4.2 on 2023-04-07 17:37

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_category_post_delete_house'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('payment_method', models.CharField(max_length=20)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_paid', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('house', 'House'), ('apartment', 'Apartment')], default='House', max_length=10)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('status', models.IntegerField(choices=[(0, 'Available'), (1, 'Booked for now'), (-1, 'Unavailable')], default=0)),
                ('nb_ppl', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)])),
                ('nb_bed', models.IntegerField()),
                ('area', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amenities', models.ManyToManyField(to='product.amenity')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.city')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.owner')),
            ],
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField()),
                ('comment', models.TextField()),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.property')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.tenant')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.booking')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.tenant')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='property_images/')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.property')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.property'),
        ),
        migrations.AddField(
            model_name='booking',
            name='tenant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.tenant'),
        ),
    ]
