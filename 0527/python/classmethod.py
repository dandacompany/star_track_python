# 클래스 메서드, 정적 메서드, 일반 메서드에 대한 설명과 튜토리얼입니다.

# 1. 일반 메서드 (Instance Method)
#    - 일반 메서드는 클래스의 인스턴스와 관련된 메서드입니다.
#    - 첫 번째 인자로 항상 인스턴스 자신을 나타내는 'self'를 받습니다.
#    - 인스턴스 변수에 접근하거나 인스턴스의 상태를 변경할 수 있습니다.

# 예제:
class MyClass:
    def __init__(self, value):
        self.value = value

    def instance_method(self):
        print("This is an instance method.")
        print(f"Value: {self.value}")

# 2. 클래스 메서드 (Class Method)
#    - 클래스 메서드는 클래스 자체와 관련된 메서드입니다.
#    - 첫 번째 인자로 항상 클래스를 나타내는 'cls'를 받습니다.
#    - 클래스 변수에 접근하거나 클래스의 상태를 변경할 수 있습니다.
#    - @classmethod 데코레이터를 사용하여 정의합니다.

# 예제:
class MyClass:
    class_variable = "I am a class variable"

    @classmethod
    def class_method(cls):
        print("This is a class method.")
        print(cls.class_variable)

# 3. 정적 메서드 (Static Method)
#    - 정적 메서드는 클래스나 인스턴스와 관련이 없는 메서드입니다.
#    - 첫 번째 인자로 'self'나 'cls'를 받지 않습니다.
#    - 일반 함수처럼 동작하지만, 클래스의 네임스페이스에 포함됩니다.
#    - @staticmethod 데코레이터를 사용하여 정의합니다.

# 예제:
class MyClass:
    @staticmethod
    def static_method():
        print("This is a static method.")

# 튜토리얼:
# - 일반 메서드는 인스턴스의 상태를 조작하거나 인스턴스 변수에 접근할 때 사용합니다.
# - 클래스 메서드는 클래스 변수를 조작하거나 클래스 레벨의 로직을 구현할 때 사용합니다.
# - 정적 메서드는 클래스나 인스턴스와 무관한 기능을 구현할 때 사용합니다.

# 각 메서드의 사용 예제를 통해 차이점을 이해하고, 적절한 상황에 맞게 메서드를 선택하여 사용하세요.
