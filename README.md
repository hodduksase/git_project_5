# 개인 홈페이지 프로젝트

## 프로젝트 설명

이 프로젝트는 Django 웹 프레임워크를 사용하여 제작된 개인 홈페이지 웹 애플리케이션입니다. 본인 소개, 개발 실적, 관심 분야 등을 포함하는 페이지로 구성되어 있습니다.

## 프로젝트 설정 및 실행 방법

프로젝트를 실행하기 위해 다음 단계를 따라주세요.

1.  **저장소 클론 (Clone the repository)**
    GitHub 저장소에서 프로젝트 코드를 로컬 컴퓨터로 다운로드합니다. (이미 파일을 가지고 있다면 이 단계는 건너뛰셔도 됩니다.)

    ```bash
    # GitHub 저장소 URL은 실제 주소로 변경해야 합니다.
    git clone [GitHub 저장소 URL]
    cd [프로젝트 폴더명, 예: personal_website]
    ```

2.  **가상 환경 설정 및 활성화 (Set up and activate a virtual environment)**
    프로젝트에 필요한 패키지를 격리된 공간에 설치하기 위해 가상 환경을 설정하고 활성화합니다. Python 3가 설치되어 있어야 합니다.

    ```bash
    # 가상 환경 생성 (프로젝트 폴더 안에서 실행)
    python -m venv venv

    # 가상 환경 활성화
    # Windows PowerShell:
    .\venv\Scripts\Activate.ps1

    # Windows Command Prompt:
    # .\venv\Scripts\activate.bat

    # macOS/Linux:
    # source venv/bin/activate
    ```

3.  **종속성 설치 (Install dependencies)**
    프로젝트 실행에 필요한 모든 라이브러리(Django 등)를 설치합니다. `requirements.txt` 파일에 목록이 있습니다.

    ```bash
    pip install -r requirements.txt
    ```

4.  **데이터베이스 마이그레이션 적용 (Apply database migrations)**
    Django의 초기 설정 및 필요한 데이터베이스 구조를 생성합니다. 이 프로젝트는 기본 SQLite 데이터베이스를 사용합니다.

    ```bash
    python manage.py migrate
    ```

5.  **개발 서버 실행 (Run the development server)**
    로컬 개발 서버를 시작합니다. 서버가 실행되는 동안 웹사이트에 접속할 수 있습니다.

    ```bash
    python manage.py runserver
    ```

6.  **웹사이트 접속**
    서버가 성공적으로 실행되면 웹 브라우저를 열고 아래 주소로 접속하여 웹사이트를 확인합니다.

    ```
    http://127.0.0.1:8000/
    ```

## 프로젝트 구조

```
[프로젝트 루트 폴더]
├── manage.py
├── personal_website/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py     # 프로젝트 설정
│   ├── urls.py         # 프로젝트 URL 설정
│   └── wsgi.py
├── core/               # 메인 앱
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py         # 앱 URL 설정
│   └── views.py        # 뷰 함수
├── templates/          # HTML 템플릿 파일
│   ├── base.html
│   ├── home.html
│   ├── about.html
│   ├── projects.html
│   └── contact.html
├── static/             # 정적 파일 (CSS, JS, 이미지)
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   └── images/
├── venv/               # 가상 환경 (설정 시 생성)
├── requirements.txt    # 프로젝트 종속성 목록
└── README.md           # 프로젝트 설명 및 실행 방법 (현재 파일)
``` 