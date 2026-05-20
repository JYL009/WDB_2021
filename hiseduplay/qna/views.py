from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.http import require_POST

from member.models import Member
from .models import Answer, Question


def _session_user_id(request):
    return request.session.get("user")


def _base_context(request, context=None):
    context = context or {}
    user_id = _session_user_id(request)
    if user_id:
        context["user_id"] = user_id
    return context


def question_list(request):
    question_list = Question.objects.order_by("-create_dttm")
    context = _base_context(request, {"question_list": question_list})
    return render(request, "qna/question_list.html", context)


def question_write(request):
    if request.method == "GET":
        return render(request, "qna/question_write.html", _base_context(request))

    user_id = _session_user_id(request)
    if not user_id:
        return redirect("member:login")

    writer = get_object_or_404(Member, memberID=user_id)
    subject = request.POST.get("subject", "").strip()
    content = request.POST.get("content", "").strip()

    if not (subject and content):
        context = _base_context(
            request,
            {"err": "Please enter both a subject and content."},
        )
        return render(request, "qna/question_write.html", context)

    Question.objects.create(
        subject=subject,
        content_q=content,
        create_dttm=timezone.now(),
        memberID=writer,
    )
    return redirect("qna:list")


def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    answer_list = Answer.objects.filter(questionID=question).order_by("-create_dttm")
    data_dic = _base_context(
        request,
        {
            "contents": question,
            "memberID": question.memberID.memberID,
            "answer_list": answer_list,
        },
    )
    return render(request, "qna/question_detail.html", data_dic)


@require_POST
def answer_write(request, question_id):
    user_id = _session_user_id(request)
    if not user_id:
        return redirect("member:login")

    question = get_object_or_404(Question, id=question_id)
    content = request.POST.get("content", "").strip()

    if content:
        Answer.objects.create(
            content_a=content,
            create_dttm=timezone.now(),
            questionID=question,
            writerID=user_id,
        )

    return redirect(reverse("qna:detail", kwargs={"question_id": question.id}))
