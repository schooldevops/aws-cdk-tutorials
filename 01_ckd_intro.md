# CDK 소개

- AWS Cloud Development Kit 은 Infrastructure as Code 를 위한 도구이다. 
- CDK를 이용하면 AWS Cloud Resource 를 코드를 이용하여 프로비저닝할 수 있도록 도와준다. 
- 일반적 수동 생성
  - 쉽게 리소스 생성을 수행할 수 있다. 
  - 다시 생성하기 위해서는 노력이 필요하다. 
  - 사람에 의한 오류를 유발한다. (오퍼레이션 오류, 리소스 자원/정책 등에 대한 누락등)
  - 시간이 소요된다. 
- IaC를 이용한 생성
  - API 호출이 실패한경우 원인 파악이 쉽다. 
  - 업데이트를 어떻게 수행할지 쉽게 정할 수 있다.
  - 리소스가 운영준비 상태인지 쉽게 파악할 수 있다.
  - 롤백을 수행할 수 있다.
- Cloud Formation을 이용한 IaC
  - 쉽게 자동화 할 수 있다. 
  - 리소스 재 생성이 쉽다. 
  - 설정을 위한 문법등을 다시 알아야한다. 
  - 추상화 되지 않고, 상당히 구체적이다.
- Document Object Model(DOMs)
  - 실제 코드 (순차, 조건, 반복등)
  - 원하는 State를 지정한다. 
  - 추상화 기능이 내제되어 있지 않다.
- AWS CDK
  - 리소스 생성에 대한 높은 레벨의 추상화 
  - AWS best practices 를 기본적으로 제공
  - 클라우드 컴포넌트 생성
  - 인프라 스트럭쳐의 컴포넌트화
  - 복잡한 아키텍처 지원
  - 다양한 언어를 지원한다. 
    - typescript
    - python
    - javascript
    - Java 
    - C#
    - Go

### CDK 참고 자료

- CDK 메뉴얼
  - [CDK 메뉴얼](https://docs.aws.amazon.com/cdk)
  - [API 문서](https://docs.aws.amazon.com/cdk/api/v2/index.html)

### CDK 처리과정

- 소스코드 작성 (CDK이용)
- CDK CLI를 이용하여 Compile 수행
- AWS CloudFormation template 로 변환
- AWS CloudFormation 에서 IaC 수행

* 참고

- 과거: Infrastructure as a Code
- 현재: Infrastructure is a Code

## Install CDK

### AWS CLI 설치

- AWS CDK 를 수행하기 위해서는 AWS CLI 를 우선 설치해야한다. 
- 이는 터미널 세션에서 AWS 서비스와 상호 통신할 수 있는 역할을 한다. 
- [aws-cli](https://docs.aws.amazon.com/ko_kr/cli/latest/userguide/getting-started-install.html) 에서 설치 진행

#### AWS Configure 수행

```go
$ aws configure
AWS Access Key ID [**************]:
```

### Node.JS 설치

- AWS CDK는 Node.js (>= 10.3.0) 을 사용하여 수행된다. 해당 버젼을 확인하자. 

```go
$ node --version
```

- Node.JS를 사음 위치에서 설치한다. 
  - [node-js](https://nodejs.org/en/download/)

### 주력 언어 IDE 선택하기

- AWS CDK 의 장점중에 하나는 다양한 언어를 지원하여 CDK 스크립트를 작성할 수 있다는 것이다. 
- 또한 다양한 IDE를 이용하여 CDK를 작성할 수도 있다. 
  - VSCode (추천)
  - AWS Cloud9
  - Atom 에 atom-typescrip 플러그인 추가
  - vim 에 tsuquyomi 추가
  - WebStorm
  - Emacs 에 tide 모드로 사용
  - PyCharm

### Python 도구 최신화 하기

```go
python -m ensurepip --upgrade
python -m pip install --upgrade pip
python -m pip install --upgrade virtualenv
```


### AWS CDK 설치하기

```go
npm install -g aws-cdk
```

- 다음으로 버젼 체크

```go
cdk --version
```

- 다음으로 cdk 언어 의존성을 업그레이드 한다. 

```go
pip install --upgrade aws-cdk.core
```