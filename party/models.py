from django.db import models
from enum import Enum
from django.conf import settings

# Create your models here.

class Party(models.Model):
    class VIBE(Enum):
        chill = (1, 'Chill: 5 - 10 People')
        party = (2, 'Party: 20 - 30 People')
        rager = (3, 'Rager: 50+ People')
       
        @classmethod
        def get_value(cls, member):
            return member.value[0]

    created_at = models.DateTimeField(auto_now_add = True)
   
    host_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    flat = models.CharField(max_length=50)

    # Default for first_entry should be right now, but user should also be allowed to add custom first_entry date/time
    # first_entry is entered in 2 parts: Date & Time through frontend
    # Then it is getting transformed into one DateTimeField to be saved into the database
    first_entry = models.DateTimeField()
    vibe = models.IntegerField(choices=[x.value for x in VIBE], null=True, default=VIBE.get_value(VIBE.chill))

    def __str__(self):
        return f"{self.flat}: {self.first_entry}"
