# Ex04.py

# in 키워드
# 시퀀스가 어떤 값을 가졌는지 검사함

i = 5


def f(arg=i):
    print(arg)


i = 6
f()  # 5를 표시

# 스코프 내에서 구하니까 i=6 무시함

# 기본값은 오직 한 번만 값을 구함
# 함수는 계속된 호출로 인자 누적함


def f(a, L=[]):
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f(3))


# 연속된 호출 간에 기본값 공유 안하려면 아래처럼 써라


def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f(3))


# 키워드 인자


