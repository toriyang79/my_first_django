
# my_first_django

## 프로젝트 개요

이 프로젝트는 Django를 사용하여 만든 첫 번째 웹 애플리케이션입니다. 간단한 메모와 아티클을 관리하는 기능을 포함하고 있습니다.

## 주요 기능

- **메모 관리**: 메모를 생성하고, 목록을 조회할 수 있습니다.
- **아티클 관리**: 아티클을 생성하고 조회할 수 있습니다.

## 사용된 기술

- **언어**: Python
- **프레임워크**: Django

## 설치 및 실행 방법

1.  **저장소 복제**

    ```bash
    git clone https://github.com/your-username/my_first_django.git
    cd my_first_django
    ```

2.  **가상환경 생성 및 활성화**

    ```bash
    python -m venv venv
    source venv/bin/activate  # macOS/Linux
    .\venv\Scripts\activate  # Windows
    ```

3.  **의존성 설치**

    ```bash
    pip install -r requirements.txt
    ```

4.  **데이터베이스 마이그레이션**

    ```bash
    python manage.py migrate
    ```

5.  **개발 서버 실행**

    ```bash
    python manage.py runserver
    ```

6.  브라우저에서 `http://127.0.0.1:8000/` 로 접속하여 애플리케이션을 확인합니다.

## 애플리케이션 구조

-   `config/`: 프로젝트의 주요 설정을 담고 있는 디렉토리입니다.
-   `polls/`: 메모와 아티클 관리를 위한 애플리케이션 디렉토리입니다.
    -   `models.py`: `Article`과 `Memo` 모델이 정의되어 있습니다.
    -   `views.py`: 애플리케이션의 뷰 로직이 포함되어 있습니다.
    -   `urls.py`: `polls` 앱의 URL 라우팅을 관리합니다.
    -   `templates/`: HTML 템플릿 파일이 위치합니다.
