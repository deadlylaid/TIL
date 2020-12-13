# pytest 의 fixture scope 종류에 대해서 알아보자


## fixture 란?

일반적으로 테스트 관련 용어에서 fixture 가 나온다면 테스트 해야하는 대상을 매 순간 동일한 환경에서 테스트가 작동될 수 있도록 '초기화'해주는 것을 의미한다.
이는 내가 공부하는 소프트웨어 뿐 아니라 전자기기, 물리장치 등등 테스트가 필요한 어느 영역에서든 fixture 가 존재한다. 물론 pytest의 fixture 도 이와 매우 유사한 성격을 띄고 있다.



## fixture scope

pytest의 fixture에서는 scope라는 키워드 인자를 매개변수로 받을 수 있는데, 이는 해당 fixture가 어느 영역까지 적용되게 할 것인가를 설정하는 변수이며 pytest에서는 총 5가지의 scope 가 정의되어 있다.



### function

```python
# 선언 방법 2가지 모두 사용 가능
@pytest.fixture()
def initial_data_set():
    pass

@pytest.fixture(scope='function')
def initial_data_set():
    pass
```

default 단위 scope로 굳이 매개변수를 입력할 필요가 없다. function 단위로 선언된 fixture는 테스트 함수 단위로 실행 된다. 이 fixture 는 함수 별로 다른 값을 제공하거나, 단 한번만 사용하는 경우 등에 사용된다.



### class

```python
# 선언 방법
@pytest.fixture(scope='class')
def initial_data_set():
    pass


@pytest.mark.usefixtures('initial_data_set')
class TestA:

    def test_a(self):
        pass

    def test_b(self):
        pass
```

class 단위로 실행되는 fixture 로, class 단위로 선언된 fixture는 위와 같이 usefixtures 를 이용하여 원하는 class 에 적용할 수 있다.
이는 class 안에 테스트 함수가 몇 개가 있던 단 한번만 실행되는 fixture 로 비슷한 종류의 test 함수를 하나의 클래스로 묶어서 관리하고자 할 때 매우 유용하다. 이렇게 선언된 fixture는 클래스 내부에 있는 테스트 함수들이 실행되기 **전에** 작동한다.
하지만 간혹 class 단위 테스트가 실행하기 전에, 그리고 class 안에 존재하는 모든 테스트가 끝나고 나서 작동하는 `setUp/tearDown` 기능을 사용해야되는 경우가 있는데, 그럴 땐 아래처럼 작성하면 된다.



```python
@pytest.fixture(scope='class')
def initial_data_set():
    # 테스트 함수가 작동하기 전에 실행할 코드
    yield
    # 테스트 함수가 모두 작동이 끝나고 나서 실행할 코드
    

@pytest.mark.usefixtures('initial_data_set')
def TestA:
    def test_a(self):
        pass
    
    def test_b(self):
        pass

```

이럴 경우 `yield` 앞에 존재 하는 코드는 테스트 함수가 실행되기 전에 `setup` 처럼 작동하고 `yield` 뒤에 있는 코드는 모든 함수가 작동하고 난 후인 `teardown` 처럼 작동하게 된다.



### module

```python
# 선언 방법

# conftest.py
@pytest_fixture(scope='module')
def initial_data_set():
    pass

# test_first.py
def test_first_a(initial_data_set):
    pass

def test_first_b(initial_data_set):
    pass

# test_second.py
def test_second_a(initial_data_set):
    pass

def test_second_b(initial_data_set):
    pass
```

module 단위로 실행되는 scope 는,  하나의 파일 단위로 한 번 실행되는 fixture를 말한다. 위의 코드를 예로 들면 `test_first.py` 와 `test_second.py` 라는 파일이 존재하므로, fixture는 각 모듈(파일)당 한번씩 총 2번 실행된다.



### session

```python
# 선언 방법
@pytest_fixture(scope='session')
def initial_data_set():
    pass
```

session 당 한 번씩만, 즉 `pytest` 명령어를 입력하여 테스트를 실행할 때마다 딱 한 번 실행되는 fixture를 이야기한다.

그렇기 때문에 비교적 자원이 많이 소모되는 초기화(테스트를 위해서 database를 초기화 하는 작업등이 그렇다.) 작업에 이용된다. 테스트가 처음 실행되고 종료될 때 작동하는 `setup` 과 `teardown` 역시 session scope 단위로 작동한다. 