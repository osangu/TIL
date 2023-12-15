``` mysql
create table company(
	name VARCHAR(255) not null,
	score INTEGER not null
)
```

```mysql
	insert into company
	values ("a", 10), ("a", 20), ("a", 20), ("b", 10), ("b", 20)
```


## Group by
```mysql
select name, sum(score) from company group by name;
```

**Result**  

<img width="420" alt="스크린샷 2023-12-15 오후 4 46 31" src="https://github.com/osangu/TIL/assets/80697064/48aafb4f-9159-4e5b-b6b5-d46daf200825">


## 서브쿼리

```mysql
select 
	distinct name,
	(
		select
			sum(score) 
		from 
			company 
		where 
			name = cmp.name
	) as score
 from 
	 company as cmp
```

**Result**   

<img width="190" alt="스크린샷 2023-12-15 오후 4 45 41" src="https://github.com/osangu/TIL/assets/80697064/61d69660-801d-472c-841e-e2dc82808e2b">

