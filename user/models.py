from django.db import models
# from .validators import validate_file_extension
from enum import Enum
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
import os
from django.core.files import File
import urllib

from django.core.files.storage import FileSystemStorage

from storages.backends.gcloud import GoogleCloudStorage
storage = GoogleCloudStorage()

fs = FileSystemStorage(location='/profile_pictures')

# from rest_framework.authtoken.models import Token

class Upload:
    @staticmethod
    def upload_image(file, filename):
        try:
            target_path = '/images/' + filename
            path = storage.save(target_path, file)
            return storage.url(path)
        except Exception as e:
            print("Failed to upload!")

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

    username = models.CharField(null=True, unique=True, max_length=50)

    name = models.CharField(null=True, blank=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    gender = models.IntegerField(choices=[x.value for x in GENDER], null=True, default=GENDER.get_value(GENDER.none))
    birthdate = models.DateTimeField(null=True)
    department = models.IntegerField(null=True, choices=[x.value for x in DEPARTMENT])
    
    # ImageField is a File Object
    # validators = [validate_file_extension]
    # profile_picture = models.ImageField(
    #     null=True, storage=fs)
    profile_picture = models.CharField(null=True, blank=True, max_length=500)
    profile_picture_data = models.BinaryField(null=True, max_length=500)
    # url = models.CharField(max_length=255, unique=True)
    role = models.IntegerField(choices=[x.value for x in ROLE], default=ROLE.get_value(ROLE.guest))

    file_image = models.FileField(null=True)
    def __str__(self):
        return f"{self.id}: {self.name}"
    
    class Meta:
        db_table = "user"

    # def cache(self):
    #     # Store image locally if we have a URL 

    #     if self.url and not self.profile_picture:
    #         result = urllib.urlretrieve(self.url)
    #         self.profile_picture.save(os.path.basename(self.url), File(open(result[0], 'rb')))
    #         self.save()


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
