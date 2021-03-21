# 파이썬 문법 What I Used(WIU)

## 표준 라이브러리

### collections - 컨테이너 데이터형

#### defaultdict

`dict` 클래스의 서브 클래스다. 첫번째 매개변수로 default_factory 초기값을 제공한다. 기본값은 `None`이다.

*Example*

```
# Dict
>> pure_dict = dict()
>> print(pure_dict[0])
KeyError: 0

# defaultdict
>> default_dict = defaultdict(int)
>> print(default_dict[0])
>> 0
```

defaultdict 는 첫번째 매개변수로 초기값을 지정해줄 타입을 지정할 수 있는데 `int` 뿐 아니라 `list`, `set` 등 다양한 값을 지정해줄 수 있다.
ß