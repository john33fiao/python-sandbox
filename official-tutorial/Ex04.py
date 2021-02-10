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


def parrot(voltage, state='가만히', action='붐', type='파랑파랑'):
    print('-- 패럿은', action, end=' ')
    print('너는', voltage, '볼트 통과')
    print('-- 색상은', type)
    print('-- 얘 지금', state, '있어')

# 하나의 필수 인자(voltage), 세 개의 선택적 인자(state, action, type)

print('1000 ---------')
parrot(1000)  # arg 하나
print('v=10 ---------')
parrot(voltage=1000)  # arg 하나
print('v=1000, a=vooom ----------')
parrot(voltage=1000000, action='VOOOOOM')  # 필수하나 선택하나
print('a=voooom, v=12345 ---------')
parrot(action='VOOOOOOOM', voltage=12345)  # 필수하나 선택하나
print('string 세 개 -------')
parrot('a million', 'bereft of life', 'jump')
print('string 하나, s=p u t d --------')
parrot('a thousand', state='pushing up the dasies')
# 필수 인자만 입력하면 상관 없이 출력함

# 그래서 아래와 같은 호출은 올바르지 않음
# 전부 타입에러 나니까 주석 풀지 마라 그냥

# parrot()
# parrot(voltage=5.0, 'dead')
# parrot(110, voltage=220)
# parrot(actor='John Seo')


# 함수 호출에서 키워드 인자는 위치 인자 뒤에 나옴
# 인자는 하나의 값만 받을 수 있음

def function(a):
    pass

# function(0, a=0)
# TypeError: function() got multiple values for argument 'a'

# 튜플(순서쌍)
print('-' * 80)  # 이런 방식은 또 신기하네요


def cheeseshop(kind, *arguments, **keywords):
    print('-- 어떤', kind, '있어요?')
    print('-- 미안,', kind, '매진이란다')
    for arg in arguments:
        print(arg)
    print('-' * 40)
    for kw in keywords:
        print(kw, ':', keywords[kw])


cheeseshop('램버거', '매진이야', "너무너무 매진임", shopkeeper="서정은", client='서요한', sketch='치즈샵 그림')
# kind / arg 1,2 / keywords 1,2,3
# 인쇄된 키워드 인자 순서 = 함수 호출로 전달된 순서

# 야 점점 번역이 거지같아지는 것 같은데
# 일단 계속 하긴 하는데... 다음 링크부터 계속 진행할 것
# https://docs.python.org/ko/3/tutorial/controlflow.html#special-parameters