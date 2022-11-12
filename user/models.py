from django.db import models
from enum import Enum

# Create your models here.

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    class GENDER(Enum):
        none = (0, 'None')
        male = (1, 'Male')
        female = (2, 'Female')
        other = (3, 'Other')

        @classmethod
        def get_value(cls, member):
            return member.value[0]
        
    class ROLE(Enum):
        guest = (0, "Guest")
        host = (1, 'Host')

        @classmethod
        def get_value(cls, member):
            return member.value[0]
    
    class DEPARTMENT(Enum):
        arts_humanities = (1, 'Arts/Humanities')
        business = (2, 'Business')
        dentistry = (3, 'Dentistry')
        engineering = (4, 'Engineering')
        law = (5, 'Law')
        medic_lifesciences = (6, 'Medic/Life Sciences')
        natural_sciences = (7, 'Natural Sciences')
        nursing = (8, 'Nursing')
        psych_neuroscience = (9, 'Pysch/Neuroscience')
        social_science = (10, 'Social Science')

        @classmethod
        def get_value(cls, member):
            return member.value[0]

    name = models.CharField(null=True, blank=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    gender = models.IntegerField(choices=[x.value for x in GENDER], null=True, default=GENDER.get_value(GENDER.none))
    birthdate = models.DateField(null=True, )
    department = models.IntegerField(null=True, choices=[x.value for x in DEPARTMENT])
    profile_picture = models.ImageField(null=True, upload_to='profile_pictures/')
    role = models.IntegerField(choices=[x.value for x in ROLE], default=ROLE.get_value(ROLE.guest))

    def __str__(self):
        return f"{self.id}: {self.name}"