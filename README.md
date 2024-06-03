# shorten_url

URL 단축 서비스는 긴 URL을 짧게 단축하여 사용하고, 단축된 URL을 통해 원본 URL로 리디렉션하는 기능을 제공합니다.

## 기본 환경
|이름|버전|
|-|-|
|Python|3.12.2|
|pip|24.0|

## 가상 환경 설정 및 패키지 설치
```zsh
# 가상 환경 생성
python -m venv env

# 가상 환경 실행
source env/bin/activate

# 모든 패키지 설치
pip install -r requirements.txt
```

## Database 설치
```zsh
# MacOS 기준(brew 설치 시)
brew install sqlite3

# Linux 기준
sudo apt install sqlite3
```

## 실행 방법 작성
```zsh
# app 디렉토리 이동 후 서버 실행
cd app && uvicorn main:app --reload
```

## Database 선정 기준
데이터베이스는 SQLite3를 사용하였습니다.<br>
SQLite는 임베디드 데이터베이스이기에 기본적으로 빠르며 메모리 모드를 사용하여 더욱 빠르게 사용하였습니다.<br>
또한 현재에는 key, value기반의 table을 사용하기에 나중에 확장하여 redis를 사용할 수도 있으며 추가적인 요구사항으로 인하여 schema가 늘어나고 sql을 사용해야한다면 다른 rdbm로 migration을 할 수 있기에 선택하였습니다.