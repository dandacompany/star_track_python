def my_decorator(func):
    """
    간단한 데코레이터 예제입니다. 이 데코레이터는 함수 호출 전후에 메시지를 출력합니다.
    """
    def wrapper(*args, **kwargs):
        print("함수가 호출되기 전입니다.")
        result = func(*args, **kwargs)
        print("함수가 호출된 후입니다.")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    """
    이름을 받아서 인사하는 함수입니다.
    """
    print(f"안녕하세요, {name}님!")

# 데코레이터가 적용된 함수 호출
say_hello("홍길동")




