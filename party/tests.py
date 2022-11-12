from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Party
from invite.models import Invite

# Using Red-Green Refactor

class PartyTests(TestCase):
    @classmethod 
    def setUpTestData(cls):
        cls.user_host = get_user_model().objects.create_user(
            username = "TestHost",
            email = "testhost@kcl.ac.uk",
            password = "secret",
            name = "Test Host",
            gender = 1,
            birthdate = '2002-11-19',
            department = 1,
            profile_picture = '../user/profile_pictures/test_photo.png',
            role=1
        )  

        cls.user_guest = get_user_model().objects.create_user(
            username = "TestGuest",
            email="testguest@kcl.ac.uk",
            password = "secret",
            name = "Test Guest",
            gender = 1,
            birthdate = '2002-11-23',
            department = 3,
            profile_picture = '../user/profile_pictures/test_photo2.jpg',
            role = 0
        )

        cls.user_guest2 = get_user_model().objects.create_user(
            username="TestGuest2",
            email="testguest2@kcl.ac.uk",
            password="secret",
            name="Test Guest 2",
            gender=2,
            birthdate='2002-11-20',
            department=2,
            profile_picture='../user/profile_pictures/test_photo3.jpg',
            role=0
        )

        cls.party = Party.objects.create(
            host_id=cls.user_host,
            flat="123",
            first_entry = '2022-12-04T00:05:23',
            vibe = 1
        )

        cls.invite = Invite.objects.create(
            party_id=cls.party,
            guest_id=cls.user_guest,
            status=0,
            plus_ones=0
        )

# Testing for Parties Page
    def test_parties_page(self):
        self.assertEqual(self.invite.party_id.host_id.name, "Test Host")
        self.assertEqual(self.invite.party_id.host_id.department, 1)
        self.assertEqual(self.invite.party_id.host_id.birthdate, '2002-11-19')
        self.assertEqual(self.invite.party_id.host_id.profile_picture, '../user/profile_pictures/test_photo.png')
        self.assertEqual(self.invite.party_id.host_id.role, 1)
        self.assertEqual(self.invite.party_id.flat, "123")
        self.assertEqual(self.invite.guest_id.name, "Test Guest")
        self.assertEqual(self.invite.guest_id.department, 3)
        self.assertEqual(self.invite.guest_id.birthdate, '2002-11-23')
        self.assertEqual(self.invite.guest_id.profile_picture, '../user/profile_pictures/test_photo2.jpg')
        self.assertEqual(self.user_guest2.role, 0)
        self.assertEqual(self.invite.status, 0)
        self.assertEqual(self.invite.plus_ones, 0)

# Testing for Guests Page
    def test_guests_page(self):
        self.assertEqual(self.user_guest2.name, "Test Guest 2")
        self.assertEqual(self.user_guest2.email, "testguest2@kcl.ac.uk")
        self.assertEqual(self.user_guest2.gender, 2)
        self.assertEqual(self.user_guest2.department, 2)
        self.assertEqual(self.user_guest2.birthdate, '2002-11-20')
        self.assertEqual(self.user_guest2.profile_picture, '../user/profile_pictures/test_photo3.jpg')
        self.assertEqual(self.user_guest2.role, 0)
    
# Testing for Profile Page: Uses the 1st Guest User (Invited)
    def test_profile_page(self):
        self.assertEqual(self.user_guest.name, "Test Guest")
        self.assertEqual(self.user_guest.email, "testguest@kcl.ac.uk")
        self.assertEqual(self.user_guest.gender, 1)
        self.assertEqual(self.user_guest.department, 3)
        self.assertEqual(self.user_guest.birthdate, '2002-11-23')
        self.assertEqual(self.user_guest.profile_picture, '../user/profile_pictures/test_photo2.jpg')
        self.assertEqual(self.user_guest.role, 0)
    