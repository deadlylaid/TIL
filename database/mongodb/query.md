## skip 에 대해서

pagination 기능을 사용할 때, document 수가 적을 때는 skip 을 사용한다.

```javascript
> var page1 = db.request.find().limit(100)
> var page2 = db.request.find().skip(100).limit(100) # 101 ~ 200 요소 반환
```

skip은 생략하게 될 document 를 모두 찾아서 생략하기 때문에 수가 많을수록 성능에 매우 불리하다.

```python
> requests = db.request.find().sort({"startDate": -1}).limit(100)
> last_request = list(requests)[-1]

> requests = db.request.find(
        {"startDate": {"$lt": last_request.startDate}}
    ).limit(100)
```

아래처럼 사용할 경우 쿼리를 2번에 걸쳐 사용하지만, skip을 쓰지 않는 로직으로 더 빠르게 데이터를 응답할 수 있다.