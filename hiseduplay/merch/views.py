from django.shortcuts import render


def merch(request):
    return render(
        request,
        "merch/merch.html",
        {"user_id": request.session.get("user")},
    )


def quiz(request):
    return render(
        request,
        "merch/quiz.html",
        {"user_id": request.session.get("user")},
    )
