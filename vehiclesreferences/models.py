from django.db import models

from backend.utils import get_upload_make_logo


class Vmake(models.Model):

    name = models.CharField(max_length=10)
    logoimage = models.ImageField(upload_to=get_upload_make_logo)

class Vmodel(models.Model):

    name = models.CharField(max_length=20)
    vmake = models.ForeignKey(Vmake, on_delete=models.CASCADE)


class Vbrand(models.Model):

    name = models.CharField(max_length=20)
    vmodel = models.ForeignKey(Vmodel, on_delete=models.CASCADE)


class Vversion(models.Model):

    name = models.CharField(max_length=20)
    vbrand = models.ForeignKey(Vbrand, on_delete=models.CASCADE)


class Vfinition(models.Model):

    name = models.CharField(max_length=20)
    vversion = models.ForeignKey(Vversion, on_delete=models.CASCADE)


class Vreference(models.Model):

    vfinition = models.ForeignKey(Vfinition, on_delete=models.CASCADE)

    model_platform_years = models.CharField(max_length=20, default="",null=True)
    model_body_platform_years = models.CharField(max_length=20, default="",null=True)

    model_version_description_years = models.CharField(max_length=20, default="",null=True)
    years_sold = models.CharField(max_length=20, default="",null=True)
    sold_in_europe = models.CharField(max_length=20, default="",null=True)
    car_classification = models.CharField(max_length=20, default="",null=True)
    body_type = models.CharField(max_length=20, default="",null=True)
    #no_of_doors = models.CharField(max_length=20, default="",null=True)
    no_of_seats = models.CharField(max_length=20, default="",null=True)
    engine_place = models.CharField(max_length=20, default="",null=True)
    drivetrain = models.CharField(max_length=20, default="",null=True)
    #cylinders = models.CharField(max_length=20, default="",null=True)
    displacement_cm3 = models.CharField(max_length=20, default="",null=True)
    #power_kw = models.CharField(max_length=20, default="",null=True)
    #power_ps = models.CharField(max_length=20, default="",null=True)
    power_rpm = models.CharField(max_length=20, default="",null=True)
    torque_nm = models.CharField(max_length=20, default="",null=True)
    torque_rpm = models.CharField(max_length=20, default="",null=True)
    bore_stroke_mm = models.CharField(max_length=20, default="",null=True)
    compression_ratio = models.CharField(max_length=20, default="",null=True)
    valves_per_cylinder = models.CharField(max_length=20, default="",null=True)
    crankshaft = models.CharField(max_length=20, default="",null=True)
    fuel_injection_ = models.CharField(max_length=20, default="",null=True)
    supercharger = models.CharField(max_length=20, default="",null=True)
    catalytic = models.CharField(max_length=20, default="",null=True)

    suspension_front = models.CharField(max_length=20, default="",null=True)
    suspension_rear = models.CharField(max_length=20, default="",null=True)
    assisted_steering = models.CharField(max_length=20, default="",null=True)
    turning_circle_m = models.CharField(max_length=20, default="",null=True)
    brakes_front = models.CharField(max_length=20, default="",null=True)
    brakes_rear = models.CharField(max_length=20, default="",null=True)
    abs = models.CharField(max_length=20, default="",null=True)
    esp = models.CharField(max_length=20, default="",null=True)
    tire_size = models.CharField(max_length=20, default="",null=True)
    tire_size_rear_if_different_than_front = models.CharField(max_length=20, default="",null=True)
    wheel_base_mm = models.CharField(max_length=20, default="",null=True)
    track_front_mm = models.CharField(max_length=20, default="",null=True)
    track_rear_mm = models.CharField(max_length=20, default="",null=True)
    length_mm = models.CharField(max_length=20, default="",null=True)
    width_mm = models.CharField(max_length=20, default="",null=True)
    height_mm = models.CharField(max_length=20, default="",null=True)
    curb_weight_kg = models.CharField(max_length=20, default="",null=True)
    gross_weight_kg = models.CharField(max_length=20, default="",null=True)
    load_kg = models.CharField(max_length=20, default="",null=True)
    stutzlast_kg = models.CharField(max_length=20, default="",null=True)
    roof_load_kg = models.CharField(max_length=20, default="",null=True)
    cargo_space_litres = models.CharField(max_length=20, default="",null=True)
    tow_weight_kg = models.CharField(max_length=20, default="",null=True)
    gas_tank_litres = models.CharField(max_length=20, default="",null=True)
    kmph_sec = models.CharField(max_length=20, default="",null=True)
    max_speed_km_h = models.CharField(max_length=20, default="",null=True)
    fuel_eff_l_100km = models.CharField(max_length=20, default="",null=True)
    fuel_eff_city_l_100km = models.CharField(max_length=20, default="",null=True)
    fuel_eff_highway_l_100km = models.CharField(max_length=20, default="",null=True)
    #engine_type = models.CharField(max_length=20, default="",null=True)
    #fuel_type = models.CharField(max_length=20, default="",null=True)
    co2_g_km = models.CharField(max_length=20, default="",null=True)
    co2_efficiency_class = models.CharField(max_length=20, default="",null=True)
    pollution_class = models.CharField(max_length=20, default="",null=True)


