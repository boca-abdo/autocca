from django.db import models

from backend.utils import VGENRE, VCOLOR
from cvhus.models import Cvhu
from vehiclereference.models import Vreference


class Vehicles(models.Model):

    cvhu = models.ForeignKey(Cvhu, on_delete=models.SET_NULL, null=True)

    is_valid = models.BooleanField(default=False)
    lp_number = models.PositiveIntegerField(null=True, blank=True)

    reg_number = models.CharField("immatriculation", max_length=10, default="", unique=True)
    vin = models.CharField(max_length=20, default="", unique=True)
    type_number = models.CharField(max_length=20, default="", unique=True)

    reference = models.ForeignKey(Vreference, on_delete=models.SET_NULL, null=True)

    genre = models.CharField(max_length=3, choices=VGENRE)

    color = models.CharField(max_length=10, choices=VCOLOR)

    #vcolorcode = models.CharField(max_length=10)

    fuel_type = models.CharField(max_length=20, default="", null=True)

    cylinders = models.CharField(max_length=20, default="", null=True)

    power = models.PositiveSmallIntegerField(default=0)

    fiscal_power = models.PositiveSmallIntegerField(default=0)

    engine_code = models.CharField(max_length=20, default='', null=True)

    gear_code = models.CharField(max_length=20, default='', null=True)

    gear_type = models.CharField(max_length=3, choices=VGEARTYPE)

    no_of_doors = models.CharField(max_length=20, default="", null=True)

    #
    # #administrative fields
    # first_reg_date = models.DateField(null=True)
    #
    # reg_date = models.DateField(null=True)
    #
    # reg_formula_number = models.CharField(max_length=10, default='', null=True)
    #
    # #titlar informations
    # reg_titular_lname = models.CharField(max_length=10, default='', null=True)

    def get_vmake(self):
        return self.reference.vfinition.vversion.vbrand.vmodel.vmake

    def get_vmodel(self):
        return self.reference.vfinition.vversion.vbrand.vmodel

    def get_vbrand(self):
        return self.reference.vfinition.vversion.vbrand

    def get_vversion(self):
        return self.reference.vfinition.vversion

    def get_vfinition(self):
        return self.reference.vfinition

    def get_v(self):
        return self.reference.vfinition



    # def checklp(self):
    #     Vehicles.objects.filter(lpnumber__isnull=True).last()
    #
    # def lp_number_function(self):
    #     return "{0}/{1}".format(timezone.now().year, self.lp_number.zfill(5))
    #
    # def assignlpnumber(self):
    #     last_lpnumber = Vehicles.objects.filter(lpnumber__isnull=False).last()
    #     if int(lp_number_function[:4]) == timezone.now().year:
    #         self.lpnumber = Vehicles.objects.filter(lpnumber__isnull=False).last().lpnumber + 1
    #     self.lpnumber = int(str(timezone.now().year) + "00001")
