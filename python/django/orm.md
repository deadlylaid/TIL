# Django ORM

가상 모델 설정

```python
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50)
    created_at = modelsDateTimeField(auto_now_add=True))
```



## Annotate()

주워진 field 의 이름을 변경한다.

```python
from django.db.models import F

# title 이라는 필드 이름을 name으로 변경했다.
Book.objects.annotate(name=F('title')).values('name')
```

## values()

query 결과에 보여주게 될 값을 표시한다. `GROUP BY` 로써의 역할을 수행하기도 한다.

- annotate 앞에 `values` 가 선언될 경우 `values` 의 매개변수로 `GROUP BY` 함을 의미한다.
- annotate 뒤에 `values` 가 선언될 경우 `select` 로 표시할 필드 값을 의미한다.

```python
Book.objects.values('title')
>>> <QuerySet [{'title':'title1'}, {'title':'title2'}]>
```



## django.db.models.function

### TruncMonth

Trunc는 끝을 자른다는 뜻이다. 날짜를 월 단위에서 자름 흔히 년+월로 group by 할 때 사용

```python
Book.objects.values(month=TruncMonth('created_at').values('month').annotate(count=Count('id'))
```

