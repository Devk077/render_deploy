from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Patient(models.Model):
    name = models.CharField(unique=True, max_length=100)
    phone_number = PhoneNumberField(null=True, blank=False, default='+91')
    email = models.EmailField(max_length=100, default='', null=True, blank=True)
    occupation = models.CharField(max_length=500, default='', null=True, blank=True)
    address = models.TextField(default='', null=True, blank=True)
    age = models.PositiveIntegerField(default=18)
    sex = models.CharField(max_length=10, default='other')
    marital_status = models.CharField(max_length=20, default='single')
    weight = models.DecimalField(max_digits=7, decimal_places=2, default='', null=True, blank=True, verbose_name="Weight (kg)")
    height = models.DecimalField(max_digits=7, decimal_places=2, default='', null=True, blank=True, verbose_name="Height (cm)")
    blood_group = models.CharField(max_length=5, default='', null=True, blank=True, verbose_name="Blood Group")

    purpose = models.TextField(default='', null=True, blank=True)
    medical_issue = models.TextField(default='', null=True, blank=True)
    medicine = models.TextField(default='', null=True, blank=True)
    supplement = models.TextField(default='', null=True, blank=True)


    wake_up_time = models.CharField(max_length=100, null=True, blank=True)
    sleep_time = models.CharField(max_length=100, null=True, blank=True)
    noon_nap = models.CharField(max_length=100, null=True, blank=True)

    family_history = models.TextField(default='', null=True, blank=True)

    #food preferences
    veg = models.BooleanField(default=False)
    non_veg = models.BooleanField(default=False)
    jain = models.BooleanField(default=False)
    egg = models.BooleanField(default=False)
    chicken = models.BooleanField(default=False)
    sea_food = models.BooleanField(default=False)

    #favorite food 
    sweet = models.BooleanField(default=False)
    spicy = models.BooleanField(default=False)
    sour = models.BooleanField(default=False)
    salty = models.BooleanField(default=False)
    blend = models.BooleanField(default=False)
    pungeant = models.BooleanField(default=False)

    #allergies
    food_allergy = models.TextField(default='', null=True, blank=True, verbose_name="Food Allergy")
    outside_food = models.CharField(max_length=100, default='', null=True, blank=True, verbose_name="Outside food")

    dessert = models.TextField(default='', null=True, blank=True)
    fruits = models.TextField(default='', null=True, blank=True)

    water_intake = models.CharField(max_length=100, default='', null=True, blank=True)
    beverage = models.TextField(default='', null=True, blank=True)
    
    alcohol = models.CharField(max_length=100, default='', null=True, blank=True)
    smoke = models.CharField(max_length=100, default='', null=True, blank=True)

    excercise = models.TextField(default='', null=True, blank=True)
    time_excercise = models.TextField(default='', null=True, blank=True, verbose_name="Time of Exercise")
    what_excercise = models.TextField(default='', null=True, blank=True, verbose_name="Type of Exercise")
    day_excercise = models.TextField(default='', null=True, blank=True, verbose_name="Days of Exercise")

    hair_problem = models.TextField(default='', null=True, blank=True)
    hair_qaulity = models.TextField(default='', null=True, blank=True)

    skin_quality = models.TextField(default='', null=True, blank=True)

    diabetes = models.BooleanField(default=False)
    thyroid = models.BooleanField(default=False)
    pcos = models.BooleanField(default=False)
    hypertension = models.BooleanField(default=False)
    heart_disease = models.BooleanField(default=False)
    cholesterol = models.BooleanField(default=False)
    
    constipation = models.BooleanField(default=False)
    diarrhea = models.BooleanField(default=False)
    acidity = models.BooleanField(default=False)    
    head_ache = models.BooleanField(default=False)
    body_pain = models.BooleanField(default=False)

    irregular_period = models.BooleanField(default=False)
    how_irrugular = models.TextField(default='', null=True, blank=True)

    kids = models.BooleanField(default=False)
    how_dilevery = models.TextField(default='', null=True, blank=True)

    consume_oil = models.TextField(default='', null=True, blank=True)
    consume_ghee = models.TextField(default='', null=True, blank=True)
    consume_salt = models.TextField(default='', null=True, blank=True)
    consume_sugar = models.TextField(default='', null=True, blank=True)
    consume_milk = models.TextField(default='', null=True, blank=True)
    consume_rice = models.TextField(default='', null=True, blank=True)
    consume_flour = models.TextField(default='', null=True, blank=True)

    def __str__(self):
        return str(self.name)
    

class BodyComposition(models.Model):
    height = models.FloatField(verbose_name="Height (Cm)")
    weight = models.FloatField(verbose_name="Weight (kg)")
    body_fat = models.FloatField(verbose_name="Body Fat (%)")
    age = models.PositiveIntegerField(verbose_name="Age")
    BMI = models.FloatField(verbose_name="Body Mass Index")
    RMR = models.FloatField(verbose_name="Resting Metabolic Rate (kcal/day)")
    visceral_fat = models.PositiveIntegerField(verbose_name="Visceral Fat")

    def __str__(self):
        return f"Composition"

class Session(models.Model):
    session_notes = models.TextField(default='', null=True, blank=True)
    session_date = models.DateField(blank=True, null=True)
    start_meal_line = models.PositiveIntegerField( null=True, blank=True)
    end_meal_line = models.PositiveIntegerField( null=True, blank=True)
    body_composition = models.ForeignKey(BodyComposition, on_delete=models.CASCADE, null=True, blank=True)
    client_session = models.ForeignKey('ClientSession', on_delete=models.CASCADE,related_name='client_session', null=True, blank=True)

    def __str__(self):
        return str(self.client_session.patient.name) + " " + str(self.session_date)

    # function in this to print pdf
class ClientSession(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    patient_url = models.URLField(blank=True)

    def __str__(self):
        return str(self.patient.name)
