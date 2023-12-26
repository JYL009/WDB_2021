from django.shortcuts import render, redirect
from .models import Question
from member.models import Member
from django.utils import timezone
from .models import Answer

# Create your views here.

def question_list(request):
    question_list = Question.objects.order_by('-create_dttm')
    print(question_list)
    print(type(question_list))
    
    context = {'question_list': question_list}
    print(context)
    print(type(context))
    
    try:
        user_id = request.session["user"]
    except:
        user_id = False
        
    if user_id:
        context["user_id"] = user_id
        return render(request, 'qna/question_list.html', context)
    else:
        return render(request, 'qna/question_list.html', context)

def question_write(request):
    if request.method == "GET":
        try:
            user_id = request.session["user"]
        except:
            user_id = False

        if user_id:
            data_dic = {}
            data_dic["user_id"] = request.session["user"]
            return render(request, 'qna/question_write.html', data_dic)
        else:
            return render(request, 'qna/question_write.html')
    
    elif request.method == "POST":
        try:
            user_id = request.session["user"]
        except:
            user_id = False

        if user_id:
            memberID = request.POST['memberID']
            writer = Member.objects.get(memberID=memberID)
            subject = request.POST['subject']
            content = request.POST['content']
            create_dttm = timezone.now()

            register = Question(
                subject = subject,
                content = content,
                create_dttm = create_dttm,
                memberID_id = writer.id
            )
            register.save()
            return redirect('/qna/list/')
        else:
            memberID = request.POST['memberID']
            writer = None
            subject = request.POST['subject']
            content = request.POST['content']
            create_dttm = timezone.now()

            register = Question(
                subject = subject,
                content = content,
                create_dttm = create_dttm,
                memberID_id = writer
            )
            register.save()
            return redirect('/qna/list/')
    
def question_detail(request, question_id):
    try:
        user_id = request.session["user"]
        content = Question.objects.get(id=question_id)
        member = Member.objects.get(id=content.memberID_id)
        answer_list = Answer.objects.filter(questionID_id=question_id).order_by('-create_dttm')
        data_dic = {"contents":contents, "memberID":member.memberID, "user_id":user_id, "answer_list":answer_list}
    except:
        contents = Question.objects.get(id=question_id)
        member = Member.objects.get(id=contents.memberID_id)
        answer_list = Answer.objects.filter(questionID_id=question_id).order_by('-create_dttm')
        data_dic = {"contents":contents, "memberID":member.memberID, "answer_list":answer_list}

    return render(request, 'qna/question_detail.html/', data_dic)
    
    if request.method == "GET":
        return redirect('/qna/list/')

def answer_write(request, question_id):
    try:
        user_id = request.session["user"]
    except:
        user_id = False

    if user_id:
        user_id = request.session["user"]
        content = request.POST["content"]
        create_dttm = timezone.now()
        questionID = question_id
        writerID = user_id

        register = Answer(
            content_a = content_a,
            create_dttm = create_dttm,
            questionID_id = questionID,
            writerID = writerID
        )

        register.save()

        q = str(question_id)
        return redirect('/qna/detail/' + q)
    else:
        user_id = request.session["user"]
        content = request.POST["content"]
        create_dttm = timezone.now()
        questionID = question_id
        writerID = None

        register = Answer(
            content_a = content_a,
            create_dttm = create_dttm,
            questionID_id = questionID,
            writerID = writerID
        )

        register.save()

        q = str(question_id)
        return redirect('/qna/detail/' + q)