# Generated by Django 3.2.7 on 2021-10-02 17:58

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=12)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LineItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='ToppingType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('topping_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='products', to='dubsapi.toppingtype')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('description', models.CharField(max_length=255)),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('image_path', django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, quality=75, size=[250, 250], upload_to='products')),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='products', to='dubsapi.producttype')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merchant_name', models.CharField(max_length=25)),
                ('account_number', models.CharField(max_length=16)),
                ('expiration_date', models.CharField(max_length=7)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='payment_types', to='dubsapi.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(blank=True, default=datetime.datetime.now)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dubsapi.customer')),
                ('payment_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dubsapi.payment')),
            ],
        ),
        migrations.CreateModel(
            name='LineItemTopping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dubsapi.lineitem')),
                ('topping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dubsapi.topping')),
            ],
        ),
        migrations.AddField(
            model_name='lineitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='lineitems', to='dubsapi.order'),
        ),
        migrations.AddField(
            model_name='lineitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='lineitems', to='dubsapi.product'),
        ),
        migrations.AddField(
            model_name='lineitem',
            name='toppings',
            field=models.ManyToManyField(related_name='lineitemtoppings', through='dubsapi.LineItemTopping', to='dubsapi.Topping'),
        ),
    ]
