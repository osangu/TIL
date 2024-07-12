Python의 라이브러리들을 사용하기 위해서는 `pip`를 통해서 그 의존성을 관리하곤 한다.  

이 pip는 여러 곳에 위치할 수 있는데 기본적으로는, 해당 디렉토리의 가상 환경에 있는 것을 사용하곤 한다.  

<img src="../../../../.images/python.venv.png" height="350">

해당 venv(가상 환경)을 자세히 보면, `pip`, `pip`, `pip3.11`로 구별되어 있다.  
- pip3.11인 이유는 가상환경을 생성할 때 버전을 python3.11로 해서 그렇다. 

```python
# print는 임의로 넣은 거다.

# pip.py
import re
import sys
from pip._internal.cli.main import main
if __name__ == '__main__':
    print('pip')
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(main())

# pip3.py
import re
import sys
from pip._internal.cli.main import main
if __name__ == '__main__':
    print('pip3')
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(main())


# pip3.11.py
import re
import sys
from pip._internal.cli.main import main
if __name__ == '__main__':
    print('pip3.11')
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(main())

```

그러나 내부의 코드들은 동일하다.  
pip, pip3, pip3.11 중 어떤 것을 사용해서 의존성을 관리하더라도 일관성 있는 것이 이 때문이다.


<img src="../../../../.images/python.venv-pip.png" width="350">
<img src="../../../../.images/python.venv-pip3.png" width="350">
<img src="../../../../.images/python.venv-pip3.11.png" width="350">

위 처럼 각 명령어에 맞게 print에 새긴 버전들이 나오게 된다.