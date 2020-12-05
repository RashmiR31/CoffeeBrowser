from django.db import models

# Create your models here.
class Types(models.Model):
    Coffee_name = models.CharField(max_length=25)
    def __str__(self):
        return self.Coffee_name

class Country(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name

class Import(models.Model):
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)
    type_id = models.ForeignKey(Types, on_delete=models.CASCADE)
    #type_name = models.ForeignKey(Types.Coffee_name, on_delete=models.CASCADE)
    I_coffeerate = models.DecimalField(max_digits=15,decimal_places=4)
    I_rate_in_INR = models.DecimalField(max_digits=15,decimal_places=4)
    I_customduty_charges = models.DecimalField(max_digits=15,decimal_places=4)
    I_total_charges = models.DecimalField(max_digits=15,decimal_places=4)

class Export(models.Model):
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)
    type_id = models.ForeignKey(Types, on_delete=models.CASCADE)
    #type_name = models.ForeignKey(Types.Coffee_name, on_delete=models.CASCADE)
    E_coffeerate = models.DecimalField(max_digits=15,decimal_places=4)
    E_rate_in_INR = models.DecimalField(max_digits=15,decimal_places=4)
    E_IGST = models.DecimalField(max_digits=15,decimal_places=4)
    E_shipping_charges = models.DecimalField(max_digits=15,decimal_places=4)
    E_total_charges = models.DecimalField(max_digits=15,decimal_places=4)


