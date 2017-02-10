from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class Register(models.Model):
    GROUP_ID = (
        ('A', 'Age < 12'),
        ('B', '13 > Age > 22'),
        ('C', '23 > Age > 35'),
        ('D', 'Age > 36'),
    )
    LANGUAGE_ID = (
        ('ENGLISH', 'English'),
        ('TAMIL', 'Tamil'),
        ('KANNADA', 'Kannada'),
        ('TELEGU', 'Telegu'),
        ('MALAYALAM', 'Malayalam'),
        ('HINDI', 'Hindi'),
        )
    full_name  = models.CharField(max_length=30)
    age   = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    group = models.CharField(max_length=1, choices=GROUP_ID, default='A')
    language = models.CharField(max_length=15, choices=LANGUAGE_ID, default='EN')
    mobile_number = models.CharField(max_length=12)
    email_id = models.EmailField(max_length=70,blank=True)
    paid = models.BooleanField(default=False)
    registered_date = models.DateTimeField(default=timezone.now)
    payment_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.full_name

    def create_payment_time(self):
        if self.paid:
            self.payment_date = timezone.now()

    def select_group(self):
        if self.age <=12:
            self.group = 'A'
        elif 12 < self.age <= 22:
            self.group = 'B'
        elif 22 < self.age <= 35:
            self.group = 'C'
        elif self.age > 35:
            self.group = 'D'
