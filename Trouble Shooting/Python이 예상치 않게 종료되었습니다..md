## 사건 경위

Uvicorn & FastAPI로 개발한 API를 실행시켜 보는 과정에서, 특정  API에서만 아래 traceback이 뜨더니 Python 자체가 죽어버렸다.  

아래 로그 제외하고도, `memory free twice`와 같은 다른 경우를 출력할 때도 있었다.  

```
Python(2581,0x1708f3000) malloc: *** error for object 0xf: pointer being freed was not allocated 
Python(2581,0x1708f3000) malloc: *** set a breakpoint in malloc_error_break to debug
```


## 접근법
1. Parameter값에 따라 300개 정도를 쿼리할 수 있는 API라서, 메모리에 문제가 생긴 건가 생각했다.  
    > 사용하고 있던 다른 프로그램들을 종료하고, 매개변수 값을 조정하여 1개만 SELECT 하였는데도 발생하였다.


2. Memory Free Twice 로그를 보고, Session 부분을 의심하게 되었다.  
	>새로운 프로젝트를 파고, `fastapi - Depends`말고 `contextmanager`로 with문을 통해 실행해보았다.  


3. 프로세스 종료 로그 확인
	> "Python이 예기치 않게 종료되었습니다" 알림창과 Python 로그에 집중하다 보니, 프로세스 종료 로그 확인이 늦었다.
	> 
	> `exit code 133 (interrupted by signal 5: SIGTRAP)`를 구글링 해보니, [R을 사용하면서 같은 로그를 마주한 사람](https://stackoverflow.com/questions/74325059/process-finished-with-exit-code-133-interrupted-by-signal-5-sigtrap)이 있었다.


# 해결법
Brew에서 기존에 사용하던 python@3.9와 python@3.12를 삭제하였다.    
공식 홈페이지를 통해서 다시 설치하고, venv를 삭제하였다가 생성하니 잘 작동하였다.

