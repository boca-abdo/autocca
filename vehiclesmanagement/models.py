from django.db import models

from backend.utils import VCOLOR, VGEARTYPE, VBOOTTYPE, TTRANSACTION
from cvhus.models import Cvhu
from vehiclesreferences.models import Vreference
from vehiclesregistrations.models import VehicleRegDocument

class VehiculeStatus(models.Model):

    status_name = models.CharField(max_length=10)


#INITIAL -> VALIDE -> ANNULLE
#           L--> ENLEVE --> REPRIS
#                    L--> CEDE --> VENDU (date de vente,
#                            L--> PARC --> DEPOLLUE --> COMPACTE --> CEDE BROYEUR
#                                   L--> COMPACTE --> CEDE BROYEUR

class Invoice(models.Model):

    transaction = models.ForeignKey(Transaction)

    def generateInvoice(self):
        check = self.transaction_set.filter(trans_tiers=)


class Transaction(models.Model):

    trans_type = models.CharField(max_length=10, choices=TTRANSACTION)
    trans_date = models.DateField(auto_now=True)
    trans_tiers = models.ForeignKey(Tiers, on_delete=models.SET_NULL, null=True)
    trans_price = models.DecimalField(max_digits=10, decimal_places=2)
    trans_payment_type = models.CharField(max_length=10, choices=TPAYMENT)
    trans_payment_date = models.DateField(auto_now=True)
    trans_invoice = models.ManyToManyField(Invoice)
    trans_gross_price = models.DecimalField (max_digits=10, decimal_places=2)
    trans_vat_rate = models.DecimalField(max_digits=10, decimal_places=2)



class VehicleTransaction(Transaction):



    #vehicule objet de classe véhicule
    #acheteur objet de la classe Client


class Vehicle(models.Model):

    cvhu = models.ForeignKey(Cvhu, on_delete=models.SET_NULL, null=True)

    vstatus = models.ForeignKey(VehiculeStatus, on_delete=models.SET_NULL)

    is_valid = models.BooleanField(default=False)
    lp_number = models.PositiveIntegerField(null=True, blank=True)

    reg_number = models.CharField(max_length=10, default="", unique=True)

    reference = models.ForeignKey(Vreference, on_delete=models.SET_NULL, null=True)

    color = models.CharField(max_length=10, choices=VCOLOR)

    #vcolorcode = models.CharField(max_length=10)
    #color_code = getVehicleColorCode(vcolorcode, vmake)
    horse_power = models.PositiveSmallIntegerField(default=0)
    engine_code = models.CharField(max_length=20, default='', null=True)
    gear_code = models.CharField(max_length=20, default='', null=True)
    gear_type = models.CharField(max_length=3, choices=VGEARTYPE)
    no_of_doors = models.CharField(max_length=20, default="", null=True)
    boot_type = models.CharField(max_length=20, choices=VBOOTTYPE)

    def clean(self):
        if self.vstatus < 6:
            raise Validationerror()

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
