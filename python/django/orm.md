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



## get_or_create()

해당 함수는 동시성 이슈가 있다. 구현된 코드를 살펴본다.

```python
  def get_or_create(self, defaults=None, **kwargs):
        self._for_write = True
        try:
            return self.get(**kwargs), False
        except self.model.DoesNotExist:
            params = self._extract_model_params(defaults, **kwargs)
            try:
                with transaction.atomic(using=self.db):
                    params = dict(resolve_callables(params))
                    return self.create(**params), True
            except IntegrityError:
                try:
                    return self.get(**kwargs), False
                except self.model.DoesNotExist:
                    pass
                raise
```

`try… except` 구문에서 `select` 를 한 시점에 모델 객체가 없으면 생성 절차를 밟지만, 생성 단계에 들어가는 그 순간 `get_or_create` 이 같은 오브젝트를 기준으로 실행될 때 아직 생성이 되지 않았기 때문에 똑같이 생성 단계를 밟고 그 때문에 2개의 모델 객체를 생성하게 된다.

이를 막는 가장 쉬운 방법은 Database 단에서 `unique constraint` 를 거는 것이다.