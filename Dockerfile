# 이 이미지를 불러옴 (BASE IMAGE SELECT)
FROM python:3.8.0-alpine
# 프로젝트의 작업 폴더를 /usr/src/app 으로 지정 (cd명령어)
WORKDIR /usr/src/app

# 파이썬은 종종 소스코드를 컴파일해서 확장자가 .pyc인 파일을 생성함
# 도커를 이용할 때는 .pyc파일이 필요하지 않으므로 .pyc 파일을 생성하지 않도록 함
ENV PYTHONDONTWRITEBYTECODE 1
# 파이썬 로그가 버퍼링 없이 즉각적으로 출력하게 함
ENV PYTHONUNBUFFERED 1

# requirements.txt에서 살펴본 라이브러리를 설치하기 위해 필요한 gcc, musl-dev등을 미리 설치
RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev zlib-dev jpeg-dev libffi-dev openssl-dev cargo

# 로컬 컴퓨터의 현재위치(Dockerfile이 있는 위치)에 있는 파일을 모두 작업디렉토리로 복사
COPY . /usr/src/app/

# requirements.txt에 나열된 라이브러리 설치
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
