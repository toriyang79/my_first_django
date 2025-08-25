# My First Django Project

이 프로젝트는 Django 프레임워크 학습을 위해 만들어진 첫 번째 프로젝트입니다.

## 프로젝트 소개

Django의 기본 개념을 익히기 위한 간단한 게시글(Article) 및 메모(Memo) 관리 애플리케이션입니다. 프로젝트의 앱 이름은 `polls`로 되어 있지만, 실제 기능은 설문이 아닌 게시글과 메모 관리에 중점을 두고 있습니다. 학습 과정에서 만들어진 다양한 테스트용 뷰와 코드 주석이 포함되어 있습니다.

## 주요 기능

*   **게시글 및 메모 관리:** 간단한 텍스트 기반의 게시글과 메모를 생성하고 조회할 수 있습니다.
*   **Django Admin:** Django의 기본 관리자 페이지(`http://127.0.0.1:8000/admin/`)를 통해 데이터를 손쉽게 관리할 수 있습니다.
*   **학습용 뷰:** Django의 뷰, URL, ORM 등의 개념을 학습하기 위한 다양한 실험적인 뷰가 포함되어 있습니다.

## 프로젝트 구조

*   `config/`: 프로젝트의 전반적인 설정을 관리하는 메인 설정 디렉토리입니다. (e.g., `settings.py`, `urls.py`)
*   `polls/`: 게시글 및 메모 관리 기능이 구현된 메인 애플리케이션입니다. (e.g., `models.py`, `views.py`, `urls.py`)

## 실행 방법

1.  **Django 설치:**
    ```bash
    pip install Django
    ```

2.  **데이터베이스 설정 (Migration):**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

3.  **개발 서버 실행:**
    ```bash
    python manage.py runserver
    ```

4.  **애플리케이션 접속:**
    *   메인 페이지: `http://127.0.0.1:8000/`
    *   관리자 페이지: `http://127.0.0.1:8000/admin/` (관리자 계정은 `python manage.py createsuperuser` 명령어로 생성해야 합니다.)
