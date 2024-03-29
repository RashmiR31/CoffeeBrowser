# Generated by Django 3.1.3 on 2020-12-05 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeBrowser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='export',
            name='E_IGST',
            field=models.DecimalField(decimal_places=4, max_digits=15),
        ),
        migrations.AlterField(
            model_name='export',
            name='E_coffeerate',
            field=models.DecimalField(decimal_places=4, max_digits=15),
        ),
        migrations.AlterField(
            model_name='export',
            name='E_rate_in_INR',
            field=models.DecimalField(decimal_places=4, max_digits=15),
        ),
        migrations.AlterField(
            model_name='export',
            name='E_shipping_charges',
            field=models.DecimalField(decimal_places=4, max_digits=15),
        ),
        migrations.AlterField(
            model_name='export',
            name='E_total_charges',
            field=models.DecimalField(decimal_places=4, max_digits=15),
        ),
        migrations.AlterField(
            model_name='import',
            name='I_coffeerate',
            field=models.DecimalField(decimal_places=4, max_digits=15),
        ),
        migrations.AlterField(
            model_name='import',
            name='I_customduty_charges',
            field=models.DecimalField(decimal_places=4, max_digits=15),
        ),
        migrations.AlterField(
            model_name='import',
            name='I_rate_in_INR',
            field=models.DecimalField(decimal_places=4, max_digits=15),
        ),
        migrations.AlterField(
            model_name='import',
            name='I_total_charges',
            field=models.DecimalField(decimal_places=4, max_digits=15),
        ),
    ]
