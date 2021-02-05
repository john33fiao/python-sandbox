# Ex01.py
# 210203 파이썬 튜토리얼 문서 학습 시작

print('hello world')
print(0.1+0.2) # 파이썬도 부동소수점이었어!
print(3/3) # 나눗셈 하면 항상 부동소수점 반환
print(3//3) # 나눗셈 두 번 넣어야 정수 반환
print(3**3) # 거듭제곱 계산

width = 30
height = 3*5 # 변수 대입은 동일함
print(width*height)

# print(부피)
# 변수 대입 안하고 쓰면 당연히 에러나고

print(3+3.0) # 계산에 실수 들어가있으면 부동소수점 되고
print((1+2)/10) # 얘는 되거든?
print((0.1+0.2)*10) # 얘는 안되고

tax = 12.5 / 100
price = 100.50
print(price*tax)
# print(price + _ ) 이거 대화형 모드에서만 먹힘
# _ 는 price*tax 입니다 / 마지막으로 인쇄된 표현이 _ 변수에 대입됨

print((3+5J)**2) # J 혹은 j 는 허수 부분 표현임

# print(math.pi)

import math

print(math.pi) # 3.141592653589793
print(math.exp(1)) # 2.718281828459045
print(1j**2) # (-1+0j)

print( ( ( math.exp(1) ) ** ( (math.pi) * 1j )).real ) # 실수부 -1.0
print( ( ( math.exp(1) ) ** ( (math.pi) * 1j )).imag ) # 허수부 1.2246467991473532e-16
# 뭐야 왜 오일러등식은 또 안됨
# (1.2246467991473532e-16).real
# .real 얘는 또 뭐임?

# e^{(pi)*i} = -1
# (math.exp(1)))**{(math.pi)*1j} = -1

print(math.sin(math.pi)) # 1.2246467991473532e-16
# 뭐야 그냥 부동소수점 연산 문제였네 에라이
# 근사값 쓰니까 그렇게 나오는거임 아오

print('hello "John"') # 큰/작은 따옴표로 구분
print('Hello \'John\'') # 역슬래시 사용
print('hello \nJohn') # 역슬래시로 줄바꿈 적용
print('hello \tJohn') # 역슬래시로 tap 적용
print('hello \\') # 그냥 두 번 적으면 적힘
print(r'hello \n john') # 앞에 r 적으면 raw 니까 \ 명령어 무시

print('''hello
world
''') # ''' 이렇게 세 번 적으면 String에 줄바꿈 입력됨

print('hello ' 'world') # 그냥 이어붙여짐 / 긴 문자열 쪼개서 적을 때 써라
# 다른 언어처럼 + 연산으로도 가능은 함
# 변수나 표현식에는 적용 안된다 > 이 때는 꼭 + 를 써야함

text = 'hello'
print(text[3]) # 인덱스 됨, 0부터 시작
print(text[-1]) # 끝에서부터 세서 인덱스, -1부터 시작

print(text[0:2]) # 슬라이싱 되게 쉽네

print(text[:3])
print(text[3:]) # 한쪽 안적으면 끝까지 감
print(text[:3] + text[3:]) # 한쪽 안적을 때 인덱스 위치에 주의할 것

#     h   e   l   l   o
#   0   1   2   3   4   5
#   -5  -4  -3  -2  -1
#  경계선 기준으로 인덱스
# [1:3] 이거 길이는 2임
# 인덱스 너무 크게 쓰면 에러남
# 인덱스에 직접 대입 불가능 > 문자열은 불변이며, 정 필요하면 새로 만들어라

print(len(text))

# 문자열은 그냥 배열이라고 생각하면 편하단다
# 슬라이스는 얕은 복사본 반환임
# 대신 리스트는 가변입니다

text2 = '안녕하세요'
text, text2 = text2, text # 변수 두 개 자리교체
# 파이썬은 이게 쩐다니까요
print(text2)

# 피보나치 수열
a, b = 0, 1
for c in range (1,10):
    print(b)
    a, b = b, a+b

print('-----------------------------')

a, b = 0, 1

while a < 30:
    print(a)
    a, b = b, a+b
# 파이썬에서는 들여쓰기로 묶음
# 와우, 콜백 지옥 PTSD가 몰려와요!

a, b = 0, 1
while a < 1000:
    if a!=0: # 파이썬은 왜 이리 괄호를 싫어함???
        # 혹시나 해서 if도 비슷하게 써봤는데 이렇게 쓰는게 맞네
        print(end=', ')
    print(a, end='') # 개행문제 제거하고 출력 이어가는 end
    a, b = b, a+b