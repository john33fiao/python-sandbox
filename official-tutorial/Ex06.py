# 210218
# 함수 어노테이션

# 사용자 정의 함수가 사용하는 형들에 대한 선택적인 메타데이터
# 함수의 __annotations__ 에 딕셔너리로 저장, 다른 부분에는 저향 없음
# 매개변수부분름 뒤에 오는 콜론으로 정의


def f(ham: str, eggs: str = '계란') -> str:
    print('Annotations ', f.__annotations__)
    print('Annotations ', ham, eggs)
    return ham + 'and ' + eggs


print(f('스팸'))
# print 안에 함수 넣으면
# 1. 일단 그 함수 안에 있는 명령 실행함
# 2. 반환값을 인쇄함
