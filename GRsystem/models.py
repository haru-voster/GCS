from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.validators import RegexValidator
from datetime import datetime

class Meta:
    app_label = 'GRsystem'

class Profile(models.Model):
    TYPE_USER = (('student', 'student'), ('grievance', 'grievance'))
    COLLEGES = (('College1', 'College1'), ('College2', 'College2'))
    BRANCHES = (
        ('ComputerScience', "ComputerScience"),
        ('InformationScience', "InformationScience"),
        ('Electronics and Communication', "Electronics and Communication"),
        ('Mechanical', "Mechanical")
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    collegename = models.CharField(max_length=29, choices=COLLEGES)
    phone_regex = RegexValidator(
        regex=r'^\d{10}$',
        message="Phone number must be exactly 10 digits."
    )
    contactnumber = models.CharField(validators=[phone_regex], max_length=10, blank=True)
    type_user = models.CharField(max_length=20, choices=TYPE_USER, default='student')
    Branch = models.CharField(max_length=29, choices=BRANCHES, default='ComputerScience')

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

class Complaint(models.Model):
    STATUS = ((1, 'Solved'), (2, 'InProgress'), (3, 'Pending'))
    TYPE = (
        ('ClassRoom', "ClassRoom"),
        ('Security', "Security"),
        ('Management', "Management"),
        ('College', "College"),
        ('Other', "Other")
    )

    Subject = models.CharField(max_length=200, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    Type_of_addressee = models.CharField(choices=TYPE, max_length=200, null=True)
    Description = models.TextField(max_length=4000, null=True)
    Time = models.DateField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=3)

    def __str__(self):
        subject = self.Subject or "No Subject"
        username = self.user.username if self.user else "Unknown User"
        return f"{subject} by {username}"

class Grievance(models.Model):
    guser = models.OneToOneField(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.guser.username if self.guser else "Unknown Grievance User"
