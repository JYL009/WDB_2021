from django.contrib.auth.hashers import check_password, identify_hasher, make_password
from django.shortcuts import redirect, render
from django.urls import reverse

from .models import Member


def _session_user_id(request):
    return request.session.get("user")


def _render_with_user(request, template_name, context=None):
    context = context or {}
    context["user_id"] = _session_user_id(request)
    return render(request, template_name, context)


def _is_hashed_password(value):
    try:
        identify_hasher(value)
    except ValueError:
        return False
    return True


def _password_matches(member, raw_password):
    if _is_hashed_password(member.password):
        return check_password(raw_password, member.password)
    return raw_password == member.password


def _upgrade_password_hash(member, raw_password):
    if not _is_hashed_password(member.password):
        member.password = make_password(raw_password)
        member.save(update_fields=["password"])


def about(request):
    return _render_with_user(request, "home/about.html")


def home(request):
    return _render_with_user(request, "home/index.html")


def logout(request):
    request.session.flush()
    return redirect("home")


def login(request):
    if request.method == "GET":
        return render(request, "login/login.html")

    memberID = request.POST.get("userid", "").strip()
    password = request.POST.get("password", "")

    data_dic = {}
    if not (memberID and password):
        data_dic["err"] = "Please enter both user ID and password."
        return render(request, "login/login.html", data_dic)

    try:
        member = Member.objects.get(memberID=memberID)
    except Member.DoesNotExist:
        data_dic["err"] = "The user ID is not registered."
        return render(request, "login/login.html", data_dic)

    if not _password_matches(member, password):
        data_dic["err"] = "The password is incorrect."
        return render(request, "login/login.html", data_dic)

    _upgrade_password_hash(member, password)
    request.session["user"] = member.memberID
    return redirect("home")


def register(request):
    if request.method == "GET":
        return render(request, "register/register.html")

    memberID = request.POST.get("userid", "").strip()
    nickname = request.POST.get("nickname", "").strip()
    password1 = request.POST.get("password1", "")
    password2 = request.POST.get("password2", "")
    name_mem = request.POST.get("username", "").strip()
    email = request.POST.get("exampleInputEmail1", "").strip()
    data_dic = {}

    if not (memberID and nickname and password1 and password2 and name_mem and email):
        data_dic["err"] = "Please enter all required values."
    elif Member.objects.filter(memberID=memberID).exists():
        data_dic["err"] = "This user ID is already registered."
    elif Member.objects.filter(nickname=nickname).exists():
        data_dic["err"] = "This nickname is already registered."
    elif password1 != password2:
        data_dic["err"] = "Passwords do not match."
    else:
        Member.objects.create(
            memberID=memberID,
            nickname=nickname,
            password=make_password(password1),
            name_mem=name_mem,
            email=email,
            point=0,
        )
        return redirect(reverse("member:login"))

    return render(request, "register/register.html", data_dic)
