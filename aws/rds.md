# RDS read replica 적용기

각 RDS DB 는 최대 5개의 read replica를 갖을 수 있다.

### MariaDB replica 제약사항

- SQL Server DB 인스턴스 식별자여야한다.
- 복제될 기준 DB(이하 소스DB) 는 `automatic backups` 이 가능한 상태여야만 한다. `backup retention period` 는 0 이상으로 한다.



### 필요한 설정들

- **AllocatedStorage** : 할당할 용량
- **DBInstanceClass** : read replica를 생성할 서버의 규격을 설정한다. ex) db.m5.xlarge
- **Storagetype** : read replica DB에 연결할 스토리지 타입을 명시한다.
  - 가능한 값들 :  `Standard | gp2 | io2`

- **SourceDBInstanceIdentifier** : 복제될 DB instance의 식별자 이 식별자는 반드시 `ARN` 포맷이어야만 한다. 만약 `us-west-2` 리전에 있는 DB를 복사해서 replica를 만들려고 한다면, `arn:aws:rds:us-west 2:123456789012:instance:mysql-instance1-20161115` 처럼 되어있어야한다.

  > 이 값은 해당 인스턴스가 Read Replica 인스턴스인지 아닌지를 결정하는 역할을 한다. 해당 인자를 cloudformation template에서 삭제하면, AWS는 해당 read replica를 삭제하고 삭제한 규격과 똑같은 DB instance를 생성한다(당연히 이때 생성된 DB는 replica가 아니다.) 

  > 만약 소스DB와 Read Replica DB가 서로 다른 리전에 있기를 바란다면 `SourceRegion` 인자를 명시하라
  >
  > 만약 RDS가 아니라 AWS Aurora를 사용한다면 SourceDBInstanceIdentifier 는 필요없다.