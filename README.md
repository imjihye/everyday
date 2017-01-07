# everyday

## 개발 환경
- python version: 3.4.3

## 개발 환경 설정 
### python 가상 환경 만들기
#### 용어 정리
- pyenv : "Simple Python Version Management" 로컬에 다양한 파이썬 버전을 설치하고 사용할 수 있도록 한다. pyenv를 사용함으로써 파이썬 버전에 대한 의존성을 해결할 수 있다. (https://github.com/yyuu/pyenv)
- virtualenv : “Virtual Python Environment builder”, 로컬에 다양한 파이썬 환경을 구축하고 사용할 수 있도록 한다. 일반적으로 Python Packages라고 부르는 (pip install을 통해서 설치하는) 패키지들에 대한 의존성을 해결할 수 있다.
(https://github.com/pypa/virtualenv)

##### mac osx
- 패키지 관리자 brew로 python 버전을 간단하게 설치할 수 있는 pyenv를 설치할 수 있다.

```
$ brew install pyenv # pyenv 설치
$ pyenv install x.x.x # python x.x.x버전으로 설치
$ pyenv versions # 설치되어 있는 파이선 버전들 확인
$ python global x.x.x # python 버전 선택
$ pyvenv env # pyenv에 설정되어 있는 python 버전으로 env이름의 가상 환경 생성
$ . env/bin/activate # 가상환경 진입
$ deactivate # 가상 환경 빠져나오기
```

##### ubuntu

```
$ pip install virtualenv # 가상 환경 생성
$ virtualenv env # env이름의 가상 환경 생성
$ . env/bin/activate # 가상환경 진입
$ deactivate # 가상 환경 빠져나오기
```

### python 패키지 설치
- 가상환경안에서 패키지를 설치 한다. 

```
(env) $ pip install django # 가상 환경에 설치 되어있는 python 패키지 설치
(env) $ pip freeze 또는 pip list # 가상 환경에 설치 되어있는 python 패키지 목록 확인
(env) $ pip install -r requirements.txt # 필요한 패키지들을 버전별로 설치한다.
(env) $ pip freeze > requirements.txt # 패키지가 추가된다면 requirements.txt 파일을 업데이트 한다.
```

### DB설정
- django에 기본으로 설정되어 있는 데이터베이스 sqlite3를 사용한다.

```
$ python manage.py migrate
```

### 서버 띄우기

```
$ python manage.py runserver
```

## 배포

- fabfile.py

