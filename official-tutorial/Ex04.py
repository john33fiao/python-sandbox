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


cheeseshop('램버거', '매진이야', "너무너무 매진임",
           shopkeeper="서정은", client='서요한', sketch='치즈샵 그림')
# kind / arg 1,2 / keywords 1,2,3
# 인쇄된 키워드 인자 순서 = 함수 호출로 전달된 순서

# 야 점점 번역이 거지같아지는 것 같은데


# 특수 매개 변수
# 인자는 위치나 명시적인 키워드로 함수에 전달
# 가독성/성능을 위해 인자 전달 방법을 제한하면 더 좋음(당연하지)

# 함수 정의 예시

def f(pos1, pos2, /,
      pos_or_kwd, *, kwd1, kwd2):
    pass
# 위치만 가능 / 위치 또는 키워드 / 키워드만 가능
# *와 /는 선택적 > 인자가 함수에 전달되는 방식에 따른, 매개 변수의 종류 표시
# 명명된(named) 매개 변수라고 부르기도 함

# 위치-키워드 인자
# *, / 가 없으면 인자를 위치나 키워드로 함수에 전달 가능

# 위치 전용
# 매개 변수 순서 중요함 > 보통 /(슬래시) 앞에 놓임
# / 없으면 위치 전용 매개변수 없는 것임

# 키워드 전용
# 인자 목록에 * 넣으면 됨


def standard_arg(arg):
    """가장 익숙한 형식, 호출 규칙에 제한 없음"""
    print(arg)


# 아니 이거 어쩌라는 건데 대체 왜 flake8 뜨냐고
def pos_only_arg(arg, /):
    """위치 매개 변수만 사용하도록 제한"""
    print(arg)


def kwd_only_arg(*, arg):
    """함수 정의에서 *로 표시된 키워드 인자만 허용"""
    print(arg)


def combined_example(pos_only, /, standard, *, kwd_only):
    """세가지 호출 규칙 모두 사용"""
    print(pos_only, standard, kwd_only)


print('*' * 40)
standard_arg(2)
standard_arg(arg=20)

print('*' * 40)
pos_only_arg(1)
# pos_only_arg(arg=1)  # 타입에러 난다

print('*' * 40)
# kwd_only_arg(3)  # 타입에러 난다
kwd_only_arg(arg=3)

print('*' * 40)
# combined_example(1, 2, 3)  # 타입에러 난다고
combined_example(1, 2, kwd_only=3)  # 정상 출력
combined_example(1, standard=2, kwd_only=3) # 정상 출력
# combined_example(pos_only=1, standard=2, kwd_only=3)  # 타입에러 난다니까


# 한 번 고의로 잠재적인 충돌 있는 정의 한 번 해봅시다


def foo(name, **kwds):
    return 'name' in kwds


# print(foo(1, **{'name': 2}))  # 타입에러 난다니까 왜 자꾸 그러니
# 'name' 키워드는 항상 첫 번째 매개변수에 결합하거든
# 그러니까 위치 전용 인자 / 를 사용해봅시다, 그러면 name는 위치인자, 'name'은 키워드 인자의 키


def foo(name, /, **kwds):
    return 'name' in kwds


print(foo(1, **{'name': 2}))


# 지침
# 매개변수 이름 못쓰게 하려면 위치전용 써라
# 매개변수 이름이 의미가 없거나 / 인자 순서 강제하거나 / 임의 변수와 키워드 필요할 때

# 이름이 의미있거나 명시적으로 필요한 경우 키워드 전용
# 비호환 API 변경 발생을 방지하려면 위치 전용


# 임의의 인자 목록

# 함수가 임의의 개수 인자로 호출될 수 있도록 지정 / 튜플로 묶임

# def wwite_multiple_items(file, separator, *args):
#     file.write(separator.join(args))

# 가변 길이 인자 args 앞에 여러 인자가 온다
# *args 뒤에 있는 형식 매개변수는 <키워드=전용> 인자임 / 위치 인자 대신 키워드 인자로만 사용가능


def concat(*args, sep='/'):
    return sep.join(args)


print(concat('땅', '불', '물', '공기'))
print(concat('땅', '불', '물', '공기', sep='.'))


#인자 목록 언패킹

