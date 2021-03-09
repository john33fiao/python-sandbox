# 210118
# 5. 자료 구조

# 5.1. 리스트

buks = []
buks.append(35)
print(buks, '----------')
buks.extend({35, 23, 42})
print(buks, '----------')
buks.insert(3, '안녕하세요')
print(buks, '----------')
buks.remove(23)
print(buks, '----------')
print(buks.pop(1))
print(buks, '----------')
buks.clear()
print(buks, '----------')


# 210309


buks.extend({35, 23, 42, 41, 30})
print(buks, '-----ㅁㄴㅇ-----')
print(buks.index(42), 'index 함수 사용')
print(buks.index(42, 1), 'index start 사용')
# index(탐색대상, 탐색 시작위치, 탐색 끝 위치)
# 대상 없으면 에러난다
print(buks.count(42))
buks.sort()
print(buks)
buks.reverse()
print(buks)

bkks = buks.copy()
print(bkks)
# 자료형 다른 경우 정렬 안됨


# 5.1.1. 리스트를 스택으로 사용하기 - LIFO

stack = [3,4,5]
stack.append(6)
stack.append(7)
print(stack)

print(stack.pop())
# 스택 꼭대기에서 꺼내기

# 5.1.2 리스트를 큐로 사용하기 - FIFO
# 인생은 FIFO가 아니라며요
# 근데 이거 성능은 안좋음(다른 거 한 칸씩 이동해야해서)
# 큐 쓸 거면 아예 전용 리스트 써라
# 이거 뭐임 링크드리스트 같은 거임?

from collections import deque
queue = deque(['서요한', '포트폴리오', '써라'])
queue.append('귀찮지만')
queue.append('써야한단다')
print(queue.popleft())
print(queue.popleft())
print(queue)

# 5.1.3 리스트 컴프리헨션
# 특정 연산을 적용한 결과를 리스트로 만듦
# 거 그냥 쉽게 행렬이라고 해주면 안됩니까

squares = []
for x in range(10):
    squares.append(x**2)

print(squares)

# 그런데 이렇게 하면 x 변수 만들고, 루프 종료 후에도 남게됨
# 사이드이펙트 없이 계산하면 아래처럼 해라

# 1안
squares = list(map(lambda x: x**2, range(10)))
print(squares)

# 2안
squares = [x**2 for x in range(10)]
print(squares)


fibonacci = [1, 1]
for x in range(10):
    fibonacci.append(fibonacci[x]+fibonacci[x+1])

print(fibonacci)

# 근데 람다식 하면 피보나치수열처럼 x-1 번째 항목 참조는 어렵지 않음?
# 아 찾아보니까 아예 피보나치수 반환하는 함수 만들어서하는듯

# 리스트 이렇게 써도 되고
print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])

# 요렇게 써도 되기는 함
comb = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            comb.append((x, y))

print(comb)

# 표현식이 튜플이면 무조건 괄호로 둘러야함 (x, y) <- 요런 거

# 복잡한 표현식이나 중첩된 함수 사용하기 좋음

from math import pi

print([str(round(pi, i)) for i in range(1, 6)])


# 5.1.4 중첩된 리스트 컴프리헨션

# 아 왤케 재미없냐 파이썬... 뭔가 실용적으로 하고싶은데... 