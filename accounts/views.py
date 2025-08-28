
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError

def login_view(request):
    """로그인 처리 함수형 뷰"""
    # 이미 로그인한 사용자는 메인으로
    if request.user.is_authenticated:
        return redirect('polls:index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 사용자 인증
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # 로그인 성공
            login(request, user)
            messages.success(request, f'{user.username}님 환영합니다!')

            # next 파라미터가 있으면 해당 페이지로, 없으면 메인으로
            next_page = request.GET.get('next', 'polls:index')
            return redirect(next_page)
        else:
            # 로그인 실패
            messages.error(request, '아이디 또는 비밀번호가 올바르지 않습니다.')

    return render(request, 'accounts/login.html')


@login_required  # 로그인한 사용자만 로그아웃 가능
def logout_view(request):
    """로그아웃 처리 함수형 뷰"""
    username = request.user.username
    logout(request)
    messages.info(request, f'{username}님 로그아웃되었습니다.')
    return redirect('polls:index')

# 회원가입 기능 구현
def signup_view(request):
    """회원가입 처리 함수형 뷰"""
    if request.user.is_authenticated:
        return redirect('polls:index')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # 유효성 검사
        errors = []

        if not username or not password1:
            errors.append('아이디와 비밀번호는 필수입니다.')

        if password1 != password2:
            errors.append('비밀번호가 일치하지 않습니다.')

        if len(password1) < 8:
            errors.append('비밀번호는 8자 이상이어야 합니다.')

        if User.objects.filter(username=username).exists():
            errors.append('이미 사용중인 아이디입니다.')

        if errors:
            for error in errors:
                messages.error(request, error)
        else:
            try:
                # 사용자 생성
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password1
                )

                # 자동 로그인
                login(request, user)
                messages.success(request, f'{user.username}님 가입을 환영합니다!')
                return redirect('polls:index')

            except IntegrityError:
                messages.error(request, '회원가입 중 오류가 발생했습니다.')

    return render(request, 'accounts/signup.html')