from django.db import models
from django.conf import settings
from party.models import Party
from enum import Enum

class Invite(models.Model):
    class STATUS(Enum):
        invited = (0, 'Guest Invited')
        confirmed = (1, 'Guest Confirmed')
        canceled = (2, 'Guest Canceled')
        checked_in = (3, 'Guest Checked-in')
        no_show = (4, 'Guest No-showed')

        @classmethod
        def get_value(cls, member):
            return member.value[0]

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    party_id = models.ForeignKey(Party, on_delete=models.CASCADE)
    guest_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.IntegerField(choices=[x.value for x in STATUS], null=True, default=STATUS.get_value(STATUS.invited))

    plus_ones = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return f"{self.guest_id} invited to {self.party_id}"

    class Meta:
        db_table = "invite"
