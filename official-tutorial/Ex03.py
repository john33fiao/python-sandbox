# Ex03.py
# 210209

# 루프의 break 와 continue 문, else 절

# 함수 정의하기
# 피보나치 수열
# 함수 전에 두 줄 안띄우면 린트가 싫어합니다
# 가독성 검사 되게 Strict 하네요...


def fib(n):
    """피보나치 수열을 n까지 표출하는 함수"""
    # 뭐야 이거 주석 위에처럼 써도 되는 거였음?
    # 와 씨 함수에 대한 설명을 vscode에서 보여주네 개쩐다
    # docstring 이라고 해서, 함수 설명서를 자동 생성하는 기능이라고 함
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


fib(2000)
# 함수 실행
# 변수 쓸 경우 함수 내부 > 전역 변수 순으로 탐색해서 사용
# 단, global 이나 nonlocal 변수로 명시하지 않는 경우에만 (일반적이지 않음)

# 구름 ide로 옮겨서 계속 진행

# 함수 이름은 현재 심볼 테이블의 함수 객체와 연결 > 인터프리터는 해당 객체를 사용자 정의 함수로 인식

fib   # 이거 안됨
# <function fib at 10042ed0> 이런 거 나온다

f = fib
f(100)

fib(0)
print(fib(0))

# return 문 없어도 None 값 돌려주기는 함
# 근데 인터프리터는 어지간하면 None 출력 안함
# 정 보고싶으면 print() 써볼것

# 피보나치 수열 리스트를 돌려주는 함수 작성 한 번 해봅시다


def fib2(n):
    """피보나치 수열을 리스트로 돌려주는 함수"""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


f100 = fib2(100)
# 두 줄 안띄우면 E305 납니다...

print(f100)

# 표현식 인자 없으면 return은 None 돌려줌
# 함수 끝으로 떨어져도 None 돌려줌

# result.append(a)
# result 메서드 호출
# result = result + [a] 라도 써도 되기는 하는데 비효율적이니 하지 말래요

# 정해지지 않은 개수의 인자로 함수 정의하는 것도 가능함

# 기본 인자 값


def ask_ok(prompt, retries=4, reminder='부디 다시 시도하세요!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('잘못 대답했다 이놈아')
        print(reminder)


ask_ok('정말 종료하기를 원하세요? (y/n)', 2, 'y/n 으로 답해주세요?')
ask_ok('정말 종료하기를 원하세요? (y/n)', 2)
ask_ok('정말 종료하기를 원하세요? (y/n)')
