from django.db import models

# Create your models here.
from backend.utils import VGENRE
from vehiclesmanagement.models import Vehicle


class VehicleRegDocument(models.Model):

    vehicle = models.OneToOneField(Vehicle, on_delete=models.SET_NULL, null=True)

    is_present = models.BooleanField(default=False)

    reg_doc_code = models.CharField(max_length=10, default="", unique=True, blank=True)
    reg_doc_date = models.DateField(blank=True, verbose_name="I")
    new_reg_doc_type = models.BooleanField(default=True)

    vin = models.CharField(max_length=20, default="", unique=True, verbose_name="E")
    cnit_number = models.CharField(max_length=20, default="", unique=True, verbose_name="D.2.1")

    previous_reg_number = models.CharField(max_length=20, default="", verbose_name="A.1")
    first_reg = models.DateField(blank=True, verbose_name="B")

    titular_name = models.CharField(max_length=40, verbose_name="C.1")
    titular_address = models.CharField(max_length=100, verbose_name="C.3")
    titular_address_zipcode = models.SmallIntegerField(blank=True, verbose_name="C.3")
    titular_address_city = models.CharField(max_length=10, verbose_name="C.3")
    is_owner = models.BooleanField(default=True, verbose_name="C.4.a")
    sec_titular = models.CharField(max_length=40, verbose_name="C.4.1")

    vmake = models.CharField(max_length=20, default="", blank=True, verbose_name="D.1")
    vvariant = models.CharField(max_length=20, default="", blank=True, verbose_name="D.2")
    vdenomination = models.CharField(max_length=20, default="", blank=True, verbose_name="D.3")
    vweight_1 = models.IntegerField(default=0, blank=True, verbose_name="F.1")
    vweight_2 = models.IntegerField(default=0, blank=True, verbose_name="F.2")
    vweight_3 = models.IntegerField(default=0, blank=True, verbose_name="F.3")
    vweight_4 = models.IntegerField(default=0, blank=True, verbose_name="G")
    vweight_empty = models.IntegerField(default=0, blank=True, verbose_name="G.1")

    vgenre = models.CharField(max_length=3, choices=VGENRE, verbose_name="J.1")

    vfuel_type = models.CharField(max_length=20, default="", blank=True, verbose_name="P.3")
    vcylinders = models.CharField(max_length=20, default="", blank=True, verbose_name="P.1")
    vpower_kw = models.PositiveSmallIntegerField(default=0, blank=True, verbose_name="P.2")
    vfiscal_power = models.PositiveSmallIntegerField(default=0, blank=True, verbose_name="P.6")

    vfield1 = models.IntegerField(default=0, blank=True, verbose_name="x")
    vfield2 = models.IntegerField(default=0, blank=True, verbose_name="x")
    vfield3 = models.IntegerField(default=0, blank=True, verbose_name="x")
    vfield4 = models.IntegerField(default=0, blank=True, verbose_name="x")
    vfield5 = models.IntegerField(default=0, blank=True, verbose_name="x")
    vfield6 = models.IntegerField(default=0, blank=True, verbose_name="x")
    vfield7 = models.IntegerField(default=0, blank=True, verbose_name="x")
    vfield8 = models.IntegerField(default=0, blank=True, verbose_name="x")
    vfield9 = models.IntegerField(default=0, blank=True, verbose_name="x")
    vfield10 = models.DateField(blank=True, verbose_name="x")
    vfield11 = models.IntegerField(default=0, blank=True, verbose_name="x")
    vfield12 = models.IntegerField(default=0, blank=True, verbose_name="x")
    vfield13 = models.IntegerField(default=0, blank=True, verbose_name="x")
    vfield14 = models.IntegerField(default=0, blank=True, verbose_name="x")
    vfield15 = models.IntegerField(default=0, blank=True, verbose_name="x")
    vfield16 = models.IntegerField(default=0, blank=True, verbose_name="x")
    vfield17 = models.IntegerField(default=0, blank=True, verbose_name="x")
    vfield18 = models.IntegerField(default=0, blank=True, verbose_name="x")
    vfield19 = models.IntegerField(default=0, blank=True, verbose_name="x")
    vfield20 = models.IntegerField(default=0, blank=True, verbose_name="x")
    vfield21 = models.IntegerField(default=0, blank=True, verbose_name="x")

    def __str__(self):
        return "{0}-{1}-{2}-{3}-{4}-".format(self.vehicle.reg_number, self.reg_doc_code, self.reg_doc_date, self.vin, self.titular_name)

