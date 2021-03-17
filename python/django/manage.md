# Manage Command

## Default Command

* manage.py sqlmigrate

해당 마이그레이션 파일의 내용을 SQL QUERY 로 변환한 상태를 출력해준다.

```
python manage.py sqlmigrate [app] [migration_file]
```



## Extensions Command

* manage.py shell_plus —print-sql

작성한 ORM을 sql query 문으로 변환하여 보여준다.

```
python manage.py shell_plus --print-sql
```

