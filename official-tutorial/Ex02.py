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