# shorten_url

URL 단축 서비스는 긴 URL을 짧게 단축하여 사용하고, 단축된 URL을 통해 원본 URL로 리디렉션하는 기능을 제공합니다.

## 기본 환경
|이름|버전|
|-|-|
|Python|3.12.2|
|pip|24.0|

## 가상 환경 설정 및 설치
```zsh
# 가상 환경 생성
python -m venv env

# 가상 환경 실행
source env/bin/activate

# 모든 패키지 설치
pip install -r requirements.txt
```

## 실행 방법 작성
```zsh
# app 디렉토리 이동 후 서버 실행
cd app && uvicorn main:app --reload
```