class Test:
    """
    Test 클래스는 이름을 저장하고, 해당 이름을 출력하거나 작업 중임을 알리는 기능을 제공합니다.
    """

    def __init__(self, name: str):
        """
        Test 인스턴스를 초기화합니다.

        Args:
            name (str): 이름을 나타내는 문자열
        """
        self.name = name

    def __str__(self):
        return f"Test(name={self.name})"

    def work(self):
        """
        Test 인스턴스의 이름과 함께 작업 중임을 출력합니다.
        """
        print(f"{self.name} is working")

class AdvancedTest(Test):
    """
    AdvancedTest 클래스는 Test 클래스를 상속받아 추가적인 기능을 제공합니다.
    """

    def work(self):
        """
        AdvancedTest 인스턴스의 이름과 함께 고급 작업 중임을 출력합니다.
        """
        print(f"{self.name} is working on advanced tasks")

# Test 클래스 사용 예제
test = Test("test")
print(test)
test.work()

# AdvancedTest 클래스 사용 예제
advanced_test = AdvancedTest("advanced_test")
print(advanced_test)
advanced_test.work()
