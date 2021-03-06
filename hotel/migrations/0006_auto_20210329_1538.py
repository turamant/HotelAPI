# Generated by Django 3.1.7 on 2021-03-29 15:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotel', '0005_auto_20210329_0848'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomcategory',
            name='price_for_night',
            field=models.DecimalField(decimal_places=2, help_text='Цена за одну ночь', max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='customer',
            field=models.ForeignKey(help_text='', on_delete=django.db.models.deletion.CASCADE, related_name='payments', to=settings.AUTH_USER_MODEL, verbose_name='customer'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='customer',
            field=models.ForeignKey(help_text='', on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to=settings.AUTH_USER_MODEL, verbose_name='customer'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='payment',
            field=models.OneToOneField(blank=True, help_text='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sale', to='hotel.payment', verbose_name='payment'),
        ),
    ]
