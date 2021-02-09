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

