"""
매직 메서드(Magic Methods) 또는 던더 메서드(Dunder Methods)는 Python에서 특별한 의미를 가지는 메서드들입니다.
이 메서드들은 클래스에 특정한 동작을 정의할 수 있게 해주며, 주로 두 개의 밑줄로 시작하고 끝납니다.
"""

class MagicMethodsExample:
    def __init__(self, name, age):
        """객체 초기화 메서드"""
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwargs):
        """객체 생성 메서드"""
        return super().__new__(cls)

    def __str__(self):
        """사용자 친화적 문자열 표현"""
        return f"{self.name}, {self.age}세"

    def __repr__(self):
        """개발자용 문자열 표현"""
        return f"MagicMethodsExample('{self.name}', {self.age})"

    def __add__(self, other):
        """+ 연산자 오버로딩"""
        return self.age + other.age

    def __eq__(self, other):
        """== 연산자 오버로딩"""
        return self.name == other.name and self.age == other.age

    def __lt__(self, other):
        """< 연산자 오버로딩"""
        return self.age < other.age

    def __len__(self):
        """len() 함수 지원"""
        return len(self.name)

    def __getitem__(self, key):
        """객체[key] 접근 지원"""
        if key == 'name':
            return self.name
        elif key == 'age':
            return self.age

    def __setitem__(self, key, value):
        """객체[key] = value 설정 지원"""
        if key == 'name':
            self.name = value
        elif key == 'age':
            self.age = value

    def __enter__(self):
        """with문 시작 시 동작"""
        print(f"{self.name}이 들어왔습니다")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """with문 종료 시 동작"""
        print(f"{self.name}이 나갔습니다")

# 실무에서 자주 사용하는 매직 메서드 예시
class DataProcessor:
    def __init__(self, data):
        self.data = data

    def __call__(self):
        """객체를 함수처럼 호출"""
        return self.process()

    def __bool__(self):
        """if문에서 True/False 판단"""
        return len(self.data) > 0

    def __iter__(self):
        """for문에서 반복 가능"""
        return iter(self.data)

# 사용 예시
processor = DataProcessor([1, 2, 3])
result = processor()  # __call__ 호출
if processor:  # __bool__ 호출
    for item in processor:  # __iter__ 호출
        print(item)
