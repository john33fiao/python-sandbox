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


# 4.8 코딩 스타일

# 기본적인 가이드로 PEP 8 존재함
# 모든 파이썬 개발자는 언젠가는 이 문서를 읽어야 합니다

# 주요 항목
# 탭 대신 스페이스 사용
# 79자 넘기지 않기
# 주석은 ㅣ지의 줄에 넣기
# 함수, 클래스, 함수 내 코드를 빈 줄을 넣어 분리
# 독스트링 사용
# 연산자 주변과 콤마 뒤에 스페이스, 괄호 안쪽에는 스페이스 금지
# 일관성 있는 이름 사용
# 어지간하면 영어만 코드로 써라
# 식별자에도 아스키2 외 문자를 사용하지 마라