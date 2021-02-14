# Ex05.py
# 210214

# 인자 목록 언패킹

# 인자가 리스트나 튜플에 있지만, 분리된 위치 인자를 요구하는 함수 존재함
# 예를 들어 범위인 range() 내장함수는 시작과 끝 존재함
# 따로 없는 경우, * 연산자로 함수 호출하면 됨

# 뭔말인지 모르겠으니 그냥 계속 따라갑니다

print(list(range(3,6)))
# 분리된 인자를 평범하게 호출함
# 3, 4, 5

args = [3, 6]
print(list(range(*args)))
# 리스트에서 언팩된 인자와 함께 호출함
# 3, 4, 5


# 딕셔너리도 ** 연산자를 써서 키워드 인자 전달가능


def parrot(voltage, state='깡', action='붐'):
    print("-- 이 앵무새는", action, end=' ')
    print('네가 만약', voltage, '볼트를 통과시키면.', end=' ')
    print("얘는", state, '!')


d = {'voltage': '사백만', 'state': '피나요', 'action': '붐--'}
parrot(**d)