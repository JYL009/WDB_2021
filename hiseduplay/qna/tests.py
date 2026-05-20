from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from member.models import Member
from .models import Answer, Question


class QnaViewTests(TestCase):
    def setUp(self):
        self.member = Member.objects.create(
            memberID="tester",
            nickname="Tester",
            password="unused",
            name_mem="Test User",
            email="tester@example.com",
            point=0,
        )

    def login_session(self):
        session = self.client.session
        session["user"] = self.member.memberID
        session.save()

    def test_anonymous_question_write_redirects_to_login(self):
        response = self.client.post(
            reverse("qna:write"),
            {"subject": "Question", "content": "Body"},
        )

        self.assertRedirects(response, reverse("member:login"))
        self.assertFalse(Question.objects.exists())

    def test_logged_in_user_can_create_question(self):
        self.login_session()

        response = self.client.post(
            reverse("qna:write"),
            {"subject": "Question", "content": "Body"},
        )

        self.assertRedirects(response, reverse("qna:list"))
        question = Question.objects.get()
        self.assertEqual(question.subject, "Question")
        self.assertEqual(question.content_q, "Body")
        self.assertEqual(question.memberID, self.member)

    def test_question_detail_renders_question_and_answer(self):
        question = Question.objects.create(
            subject="Question",
            content_q="Body",
            create_dttm=timezone.now(),
            memberID=self.member,
        )
        Answer.objects.create(
            content_a="Answer body",
            create_dttm=timezone.now(),
            questionID=question,
            writerID=self.member.memberID,
        )

        response = self.client.get(reverse("qna:detail", args=[question.id]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Question")
        self.assertContains(response, "Body")
        self.assertContains(response, "Answer body")

    def test_logged_in_user_can_create_answer(self):
        self.login_session()
        question = Question.objects.create(
            subject="Question",
            content_q="Body",
            create_dttm=timezone.now(),
            memberID=self.member,
        )

        response = self.client.post(
            reverse("qna:answer_write", args=[question.id]),
            {"content": "Answer body"},
        )

        self.assertRedirects(response, reverse("qna:detail", args=[question.id]))
        answer = Answer.objects.get()
        self.assertEqual(answer.content_a, "Answer body")
        self.assertEqual(answer.writerID, self.member.memberID)

    def test_anonymous_answer_write_redirects_to_login(self):
        question = Question.objects.create(
            subject="Question",
            content_q="Body",
            create_dttm=timezone.now(),
            memberID=self.member,
        )

        response = self.client.post(
            reverse("qna:answer_write", args=[question.id]),
            {"content": "Answer body"},
        )

        self.assertRedirects(response, reverse("member:login"))
        self.assertFalse(Answer.objects.exists())
