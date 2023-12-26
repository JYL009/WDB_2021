from django.shortcuts import render, redirect
from .models import Member

# Create your views here.

def about(request):
    return render(request, 'home/about.html')

def home(request):
    user_data = {}
    user_data["user_id"] = request.session.get("user")
    print(user_data)
    print(type(user_data))
    return render(request, 'home/index.html', user_data)
    
def logout(request):
    request.session.flush()
    return redirect('/')
    
def login(request):
    if request.method == "GET":
        return render(request, 'login/login.html')
    elif request.method == "POST":
        memberID = request.POST['memberID']
        password = request.POST['password']
        
        try:
            check_id = Member.objects.get(memberID=memberID)
            print(check_id)
            print(type(check_id))
        except:
            check_id = False
        
        data_dic = {}
        if not(memberID and password):
            data_dic["err"] = "모든 값을 입력해 주세요."
        elif check_id == False:
            data_dic["err"] = "등록된 아이디가 없습니다."
        else:
            if password == check_id.password:
                request.session["user"] = check_id.memberID
                return redirect('/')
            else:
                data_dic["err"] = "비밀번호가 잘못되었습니다."
        
        return render(request, 'login/login.html', data_dic)

def register(request):
    if request.method == "GET":
        return render(request, 'register/register.html')
    elif request.method == "POST":
        print(request.POST)
        print(type(request.POST))
        memberID = request.POST['userid']
        nickname = request.POST['nickname']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        name_mem = request.POST['username']
        email = request.POST['exampleInputEmail1']
        try:
            check_id1 = Member.objects.get(memberID=memberID)
            check_id2 = Member.objects.get(nickname=nickname)
        except:
            check_id1 = False
            check_id2 = False
        data_dic = {}

        if not(memberID and password1 and password2 and name_mem and email):
            data_dic["err"] = "모든 값을 입력해 주세요."

        elif check_id1:
            data_dic["err"] = "이미 등록된 아이디 입니다."

        elif check_id2:
            data_dic["err"] = "중복되는 별명 입니다."

        elif password1 != password2:
            data_dic["err"] = "비밀번호가 일치하지 않습니다."

        else:
            memberregister = Member(
                memberID=memberID,
                nickname=nickname,
                password=password1,
                name_mem=name_mem,
                email=email,
                point=0,
            )
            memberregister.save()
            return redirect('/')
        return render(request, 'register/register.html', data_dic)