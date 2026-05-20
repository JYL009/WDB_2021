from django.contrib.auth.hashers import check_password, identify_hasher, make_password
from django.test import TestCase
from django.urls import reverse

from .models import Member


class MemberAuthTests(TestCase):
    def test_register_hashes_password_and_redirects_to_login(self):
        response = self.client.post(
            reverse("member:register"),
            {
                "userid": "tester",
                "nickname": "Tester",
                "password1": "pass1234",
                "password2": "pass1234",
                "username": "Test User",
                "exampleInputEmail1": "tester@example.com",
            },
        )

        self.assertRedirects(response, reverse("member:login"))
        member = Member.objects.get(memberID="tester")
        self.assertNotEqual(member.password, "pass1234")
        self.assertTrue(check_password("pass1234", member.password))

    def test_login_sets_session_for_hashed_password(self):
        Member.objects.create(
            memberID="tester",
            nickname="Tester",
            password=make_password("pass1234"),
            name_mem="Test User",
            email="tester@example.com",
            point=0,
        )

        response = self.client.post(
            reverse("member:login"),
            {"userid": "tester", "password": "pass1234"},
        )

        self.assertRedirects(response, reverse("home"))
        self.assertEqual(self.client.session["user"], "tester")

    def test_login_upgrades_legacy_plain_text_password(self):
        Member.objects.create(
            memberID="legacy",
            nickname="Legacy",
            password="oldpass",
            name_mem="Legacy User",
            email="legacy@example.com",
            point=0,
        )

        response = self.client.post(
            reverse("member:login"),
            {"userid": "legacy", "password": "oldpass"},
        )

        self.assertRedirects(response, reverse("home"))
        member = Member.objects.get(memberID="legacy")
        identify_hasher(member.password)
        self.assertTrue(check_password("oldpass", member.password))

    def test_login_rejects_wrong_password(self):
        Member.objects.create(
            memberID="tester",
            nickname="Tester",
            password=make_password("pass1234"),
            name_mem="Test User",
            email="tester@example.com",
            point=0,
        )

        response = self.client.post(
            reverse("member:login"),
            {"userid": "tester", "password": "wrong"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertNotIn("user", self.client.session)
