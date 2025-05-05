from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = None  # Remove inherited username field

    user_id = models.AutoField(primary_key=True)

    # Personal Information
    first_name = models.CharField(max_length=30, null=False)
    middle_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=False)
    suffix = models.CharField(max_length=10, null=True, blank=True)
    nickname = models.CharField(max_length=30, null=True, blank=True, default="User")  # Default value added
    birthdate = models.DateField(null=False)
    sex_at_birth_choices = [('M', 'Male'), ('F', 'Female')]
    sex_at_birth = models.CharField(max_length=1, choices=sex_at_birth_choices, null=False)

    # Email as unique identifier
    email = models.EmailField(unique=True, null=False)

    # Profile Information (New fields)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    region = models.CharField(max_length=50, null=True, blank=True)
    province = models.CharField(max_length=50, null=True, blank=True)
    municipality = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    address_block = models.CharField(max_length=100, null=True, blank=True)

    # Health Profile Information (Integrated directly here)
    asthma = models.BooleanField(default=False)  # Does the user have asthma?
    hypertension = models.BooleanField(default=False)  # Does the user have hypertension?
    thyroid_problem = models.BooleanField(default=False)  # Does the user have thyroid problems?
    acid_peptic_disorder = models.BooleanField(default=False)  # Does the user have acid peptic disorder?
    convulsions_or_seizure = models.BooleanField(default=False)  # Does the user have convulsions or seizures?
    anxiety_mood_problems = models.BooleanField(default=False)  # Does the user have anxiety/mood problems?
    depression = models.BooleanField(default=False)  # Does the user have depression?
    diabetes = models.BooleanField(default=False)  # Does the user have diabetes?
    g6pd_deficiency = models.BooleanField(default=False)  # Does the user have glucose-6-phosphate dehydrogenase deficiency?
    tuberculosis = models.BooleanField(default=False)  # Does the user have tuberculosis?
    stroke_heart_disease = models.BooleanField(default=False)  # Has the user experienced stroke or heart disease before age 40?
    kidney_urinary_problems = models.BooleanField(default=False)  # Does the user have kidney or urinary problems?
    recurrent_headaches = models.BooleanField(default=False)  # Does the user have recurring headaches or migraines?
    eating_problems = models.BooleanField(default=False)  # Does the user have eating or nutritional problems?
    suicidal_thoughts = models.BooleanField(default=False)  # Has the user had suicidal thoughts?
    surgeries = models.BooleanField(default=False)  # Has the user undergone surgeries?
    covid_history = models.BooleanField(default=False)  # Has the user had COVID-19?
    menstrual_problems = models.BooleanField(default=False)  # Does the user have menstrual problems?
    other_medical_conditions = models.TextField(null=True, blank=True)  # Other conditions
    diagnosis_date = models.DateField(null=True, blank=True)  # Date of diagnosis for other conditions
    illness_status = models.CharField(max_length=100, null=True, blank=True)  # Illness status (e.g., active, resolved)
    other_medications = models.TextField(null=True, blank=True)  # Other medications for additional conditions
    smoker = models.BooleanField(default=False)  # Does the user smoke?
    alcohol_rate = models.CharField(max_length=100, null=True, blank=True)  # Alcohol consumption rate
    alcohol_units_per_day = models.CharField(max_length=100, null=True, blank=True)  # Units of alcohol consumed per day
    psychoactive_substance = models.BooleanField(default=False)  # Has the user consumed psychoactive substances in the last three months?
    special_needs = models.BooleanField(default=False)  # Does the user have special needs?
    medications_taken = models.TextField(null=True, blank=True)  # Medications currently being taken (with search functionality)
    allergies = models.BooleanField(default=False)  # Does the user have allergies?
    allergy_name = models.CharField(max_length=255, null=True, blank=True)  # Name of allergy
    allergy_severity = models.CharField(max_length=50, null=True, blank=True, choices=[('Mild', 'Mild'), ('Moderate', 'Moderate'), ('Severe', 'Severe')])  # Allergy severity

    # Consent and Declarations (unchanged)
    expression_of_consent = models.BooleanField(default=False, null=False)
    declaration_undertaking = models.BooleanField(default=False, null=False)

    last_updated = models.DateTimeField(auto_now=True, null=False)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

    def get_nickname(self):
        return self.nickname if self.nickname else "User"
