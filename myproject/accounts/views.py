from django.shortcuts import render, redirect
from django.contrib import auth
from shop.models import Member
# Member: user / name / addreses / pnumber / email
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User #django에 내장된 유저 객체
import os

# 회원가입
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        name = request.POST['name']
        pnumber = request.POST['pnumber']
        email = request.POST['email']

        if User.objects.filter(username = username).exists():
            return render(request, 'register.html', {'error': "이미 존재하는 사용자입니다."})

        if password == request.POST['password_check']:
            user = User.objects.create_user(
                username=username, password=password
            )
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            Member(user=user, name=name, pnumber=pnumber, email=email).save()

            return redirect('/')
        else:
            return render(request, 'register.html', {'error':"비밀번호가 일치하지 않습니다."})
    else:
        return render(request, 'register.html')

        
# 필요하다고 해서 임시로 넣어둠
def unregister(request):
    pass

# 회원 탈퇴
@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
    # 회원 탈퇴 이후 로그인 화면으로 이동하도록 했습니다.
    return redirect('account:login')


# 회원 정보 변경

def modify(request):
    if request.method == 'GET':
        return render(request, 'modify.html')

    elif request.method == 'POST':
        # 장고에 회원가입된 아이디, 비밀번호 변경
        target = request.user

        # Member 객체의 회원정보 변경
        # Member(user=user, name=name, address=address, pnumber=pnumber, email=email) 에서 목표 user을 가지는 Member을 찾는다.
        target_member = Member.objects.filter(user=target)

        username = request.POST['username']
        password = request.POST['password']
        name = request.POST['name']
        address = request.POST['address']
        pnumber = request.POST['pnumber']
        email = request.POST['email']

        target.username = username
        target.password = password
        target.save()

        for object in target_member:
            object.name = name
            object.address = address
            object.pnumber = pnumber
            object.email = email
            object.save()

        return render(request, 'home.html')

# 로그인
def login(request):
    # POST 요청시 로그인 검사
    if request.method == 'POST':
        id_input = request.POST['username']
        pw_input = request.POST['password']
        user = auth.authenticate(request, username=id_input, password=pw_input)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html')
    # GET 요청시 로그인 페이지 실행
    else:
        return render(request, 'login.html')


# 로그아웃
def logout(request):
    auth.logout(request) #auth클래스의 내장메소드인 logout 이용
    return redirect('home')
