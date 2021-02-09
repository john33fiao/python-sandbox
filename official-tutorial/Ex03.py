# Ex03.py
# 210209

# 루프의 break 와 continue 문, else 절

# 함수 정의하기

# 피보나치 수열
def fib(n):
    """피보나치 수열을 n까지 표출하는 함수"""
    # 뭐야 이거 주석 위에처럼 써도 되는 거였음?
    # 와 씨 함수에 대한 설명을 vscode에서 보여주네 개쩐다
    # docstring 이라고 해서, 함수 설명서를 자동 생성하는 기능이라고 함
    a, b = 0, 1
    while a<n:
        print(a, end = ' ')
        a, b = b, a+b
    print()

fib(2000) # 함수 실행
# 변수 쓸 경우 함수 내부 > 전역 변수 순으로 탐색해서 사용
# 단, global 이나 nonlocal 변수로 명시하지 않는 경우에만 (일반적이지 않음)

# 구름 ide로 옮겨서 계속 진행

# 함수 이름은 현재 심볼 테이블의 함수 객체와 연결 > 인터프리터는 해당 객체를 사용자 정의 함수로 인식

fib # 이거 안됨
# <function fib at 10042ed0> 이런 거 나온다

f = fib
f(100)

fib(0)
print(fib(0))