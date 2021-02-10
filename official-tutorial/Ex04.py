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

# 함수는 kwarg=value 형식의 키워드 인자를 사용해서 호출 가능
# kwarg : keyword argument
# key 오타인줄 알았네;;


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print('-- This parrot wouldn\'t', action, end=' ')
    print('if you put', voltage, 'volts throught it.')
    print('-- Lovely plumge, the', type)
    print('-- It\'s', state, '!')

# 하나의 필수 인자(voltage), 세 개의 선택적 인자(state, action, type)


parrot(1000)
print('----------------')
parrot(voltage=1000)
print('----------------')
parrot(voltage=1000000, action='VOOOOOM')
print('----------------')
parrot(action='VOOOOOOOM', voltage=12345)
print('----------------')
parrot('a million', 'bereft of life', 'jump')
print('----------------')
parrot('a thound', state='pushing up the dasies')
