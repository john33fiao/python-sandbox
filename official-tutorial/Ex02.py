# Ex02.py
# https://docs.python.org/ko/3/tutorial/controlflow.html
# 210205

print('hello world')

# if문

# x = int(input('Please enter an integer: '))
x = 30
if x< 0:
    x = 0
    print('Negative changed to zero')
elif x==0:  # 이게 else if 줄임말임? 엘리프 하니까 뭔 게임캐릭터인줄
    print('zero')
elif x ==1:
    print('single')
else:
    print('more')

# for 문
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
# 파이썬은 시퀀스 순서대로 이터레이션함

# 그래서이터레이션 중에 컬렉션 수정하면 잘 작동 안함
# (1)복사본으로 루프 만들거나 
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]

# (2)새 컬렉션 만들어라
# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user]=status

# 그래서 range 같은 거 써야함
for i in range(5):
    print(i, end=' ')
print('')

for i in range(5,10):
    print(i, end=' ')
print('')


for i in range(0, 10, 3):
    print(i, end=' ')
print('')

for i in range(10, 0, -3):
    print(i, end=' ')
print('')

for i in range(-100, -10, 3):
    print(i, end=' ')
print('')

a = ['mary', 'had', 'a', 'little', 'bomb']
for i in range(len(a)):
    print(i, a[i])

# 보통 enmerate() 쓰는 경우가 많음
print(list(enumerate(a)))

# 범위 그냥 프린트하면 이상한 거 나옴
print(range(5,10))
# 왜냐면 이건 리스트가 아니라 그냥 이터러블 객체이기 때문

# 루프 break, continue, else
# 소수 찾기 알고리즘
for n in range(2, 10):
    for x in range(2,n):
        if n % x == 0: # 예외인 경우 실행함
            print(n, '=', x, '*', n//x, '임')
            break    # 실행하고 빠져나감 (다음 이터러블 객체로)
        # break가 실행되지 않고 for 문이 종료하면 실행함
    else:  # 이 else는 if가 아니라 for에 붙어있음 > try와 비슷하게 생각하면 됨
        print('소수', n, '찾았음')
        # 예외가 발생하지 않을 때 실행함

# 홀짝 찾기 알고리즘
for num in range(2, 10):
    if num%2 == 0:
        print('짝수', num, '찾았음')
        continue # 이번 이터러블 끝냄
    print('홀수', num, '찾았음')

# pass문
# 아무 것도 하지 않음
# 문법적으로 필요하긴 한데 뭐 시킬 일은 없을 때 사용함

# while True:
#     pass

# 최소한의 클래스를 만들 때 사용되기도 함
# 뭐야 너네 interface 같은 거도 없니 어휴 저런