# Read Replication 처리를 통한 query 분산처리

AWS Aurora 의 기준으로 공부해본 내용

### Aurora DB에는 다양한 종류의 Endpoint 가 존재한다.

- cluster endpoint(read-write 가능)
- reader endpoint(read 가능)
- Custom endpoint
- instance endpoint

### Cluster 는 인스턴스의 집합이다.

각 endpoint를 어떤 인스턴스에 붙이게 될지는 모르지만 그 인스턴스의 조합을 클러스터라고 부른다.

- 전통적인 클러스터 - `reader endpoint` 와 `writer endpoint` 가 하나의 DB 인스턴스에서 query를 실행한다. 
- Read replication 클러스터 조합 - read replication DB를 따로 만들고 이를 `reader endpoint` 에 연결한다. `writer endpoint`는 기존 DB에 연결해서 read와 write를 2개의 DB로 분산처리한다.
- 다중 Read replication 클러스터 조합 - query 양이 엄청나게 많아질 경우 read replication DB를 여러게 만들고 `reader endpoint` 를 독립적으로 분산처리한다. 
- 다중 read/write replication 클러스터 조합 - read replication, write replication을 여러개 만들어서 각각 분산처리함

### Django Settings 처리

```python
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backend.mysql',
    [...]
    'OPTIONS': {
      'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
    },
    'replica': {
      'ENGINE': 'django.db.backends.mysql',
      [...]
      'OPTIONS': {
      	'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
      }
    }
  }
}

# 작성한 라우터들을 추가할 수 있다.
DATABASE_ROUTERS = ['myapp.router.Router']
```

#### myapp.router.Router

```python
class SensitiveDataRouter:
    def db_for_read(self, model, **hints):
      # read query인 경우 'replica' 설정을 따라가도록 함
      return 'replica'

    def db_for_write(self, model, **hints):
      # write query인 경우 'default' 설정을 따라가도록 함
      return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return None

```

### 주의사항

간혹 3rd party library 중에서 multi-database 에 대응되어있지 않은 라이브러리들이 존재한다. 생각보다 심각한 문제를 야기할 수 있는 원인이 될 수 있기 때문에 각별한 주의가 필요함