# SQLite Quey


```
CREATE TABLE database_name.POST(
   id         INT PRIMARY   KEY   NOT NULL,
   title      TEXT                NOT NULL,
   content    TEXT                NOT NULL,
   creted_at  DATETIME
);
```


## 날짜 형식 변경

테이블 필드 값 중에서 DateTime 필드가 존재하는데 이를 이용해서 `년-월` GROUP BY 를 실행하고 싶을 경우 `STRFTIME` 을 사용한다.
