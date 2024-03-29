# IAM

IAM은 AWS 서비스를 인프라를 사용하는데 필요한 자격/접근을 관리하는 서비스이다. IAM은 크게 그룹(Group), 사용자(User), 역할(Role), 정책(Policy) 4가지로 나뉜다.

## 정책(Policy)

실질적으로 AWS 이용 권한들을 말한다. 이 정책들은 JSON 형식으로 정의되며 다양한 세부적인 권한들을 정의한다.<br>
정책은 사용자나 그룹에 연결되어 권한을 관리한다.


## 사용자(User)

말 그대로 AWS 사용자를 의미한다. 하지만 여기서 뜻하는 사용자는 AWS에 이메일로 가입했을 때 생성되는 `계정` 과는 전혀 다른 개념임을 명심해야한다. <br> `계정`은 모든 권한을 갖고있으며, 사용자는 그저 `계정`에 의해 만들어진 존재일 뿐이다.
AWS는 이 이메일 `계정` 을 사용하지 말고 `어드민 권한(AdministratorAccess)` 을 갖고 있는 사용자를 만들어서 서비스를 이용하기를 권장하고 있다.<br>
이 사용자는 하나 혹은 다수의 정책에 연결된 객체라고도 해석할 수 있다.


## 그룹(Group)

그룹은 IAM 사용자들의 묶음이다. 같은 역할들을 소요 하는 여러 개의 사용자를 이 그룹에 소속시킬 수 있다.


## 역할(Role)

> AWS 서비스를 요청하기 위한 “권한 세트”를 정의하는 IAM 기능이다. 권한이라 하면 정책(Policy)에 부여하는 권한과 같은 것을 의미한다.<br>
역할의 큰 특징은 IAM 사용자나 IAM 그룹에는 연결되지 않는다는 것이다.<br>
대신 **신뢰할 수 있는** IAM 사용자나 애플리케이션 또는 AWS 서비스(예: EC2_)가 역할을 맡을 수 있다.
 -- AWS Document
 
역할은 하나 혹은 다수의 정책을 연결하는 객체라는 점에서 사용자와 유사하지만, 이것이 EC2나 AWS API GATEWAY와 같은 AWS서비스로써의 사용자라는 점에서 차이가 있다.<br>(물론 이것에 한정한 것은 아니다. ACCESS KEY를 통해 인증받은 사용자 역시 역할을 부여받을 수 있다.)
예를들어 EC2인스턴스 내부에서 S3 로 파일을 업로드하는 권한이 필요하다면, S3 Put 정책을 소유하고있는 역할을 부여하면된다.
