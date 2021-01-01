# Django ORM

가상 모델 설정

```python
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50)
```

## Annotate()

주워진 field 의 이름을 변경한다.

```
from django.db.models import F

# title 이라는 필드 이름을 name으로 변경했다.
Book.objects.annotate(name=F('title')).values('name')
```

## django.db.models.function

**TruncMonth**

Trunc는 끝을 자른다는 뜻이다. 날짜를 월 단위에서 자름 흔히 년+월로 group by 할 때 사용

```
Book.objects.values(month=TruncMonth('created_at').values('month').annotate(count=Count('id'))
```
