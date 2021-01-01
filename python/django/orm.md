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