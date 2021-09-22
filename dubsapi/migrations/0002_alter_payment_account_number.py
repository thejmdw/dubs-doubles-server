from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dubsapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='account_number',
            field=models.CharField(max_length=16),
        ),
    ]