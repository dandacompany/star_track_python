# Python Dataclass 완전 가이드

## 데이터 클래스 튜토리얼

### 목차

1. [Dataclass란 무엇인가?](#1-dataclass란-무엇인가)
2. [기본 사용법](#2-기본-사용법)
3. [기본값과 타입 힌트](#3-기본값과-타입-힌트)
4. [Field 함수 활용](#4-field-함수-활용)
5. [메서드 추가하기](#5-메서드-추가하기)
6. [비교와 정렬](#6-비교와-정렬)
7. [불변 데이터 클래스](#7-불변-데이터-클래스)
8. [상속](#8-상속)
9. [고급 기능](#9-고급-기능)
10. [실전 예제](#10-실전-예제)

---

## 1. Dataclass란 무엇인가?

### 1.1 개념 소개

Python 3.7에서 도입된 `dataclass`는 주로 데이터를 저장하는 클래스를 쉽게 만들 수 있게 해주는 데코레이터입니다. 판다스의 DataFrame이 표 형태의 데이터를 다루는 것처럼, dataclass는 구조화된 데이터 객체를 만드는 데 사용됩니다.

### 1.2 기존 클래스 vs Dataclass

**기존 방식:**

```python
class Student:
    def __init__(self, name, age, grade, email):
        self.name = name
        self.age = age
        self.grade = grade
        self.email = email
    
    def __repr__(self):
        return f"Student(name='{self.name}', age={self.age}, grade={self.grade}, email='{self.email}')"
    
    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return (self.name, self.age, self.grade, self.email) == (other.name, other.age, other.grade, other.email)
```

**Dataclass 방식:**

```python
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    grade: float
    email: str
```

### 1.3 장점

1. **코드 간소화**: `__init__`, `__repr__`, `__eq__` 메서드 자동 생성
2. **타입 힌트 강제**: 필드 정의 시 타입 명시 필요
3. **가독성 향상**: 클래스 구조가 명확하게 보임
4. **유지보수성**: 필드 추가/제거가 간단

---

## 2. 기본 사용법

### 2.1 첫 번째 Dataclass

```python
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    category: str
    in_stock: bool

# 객체 생성
laptop = Product("MacBook Pro", 2500000, "Electronics", True)
print(laptop)
# 출력: Product(name='MacBook Pro', price=2500000, category='Electronics', in_stock=True)

# 속성 접근
print(f"제품명: {laptop.name}")
print(f"가격: {laptop.price:,}원")
```

### 2.2 자동 생성되는 메서드들

```python
# __init__ 메서드 자동 생성
product1 = Product("iPhone", 1200000, "Electronics", True)

# __repr__ 메서드 자동 생성
print(product1)

# __eq__ 메서드 자동 생성
product2 = Product("iPhone", 1200000, "Electronics", True)
print(product1 == product2)  # True

product3 = Product("Galaxy", 1000000, "Electronics", True)
print(product1 == product3)  # False
```

### 2.3 판다스와의 연동

```python
import pandas as pd
from dataclasses import dataclass, asdict
from typing import List

@dataclass
class SalesRecord:
    product_name: str
    quantity: int
    unit_price: float
    sale_date: str
    
    @property
    def total_amount(self) -> float:
        return self.quantity * self.unit_price

# 데이터 생성
sales_data = [
    SalesRecord("노트북", 2, 1500000, "2024-01-15"),
    SalesRecord("마우스", 10, 25000, "2024-01-16"),
    SalesRecord("키보드", 5, 80000, "2024-01-17")
]

# DataFrame으로 변환
df = pd.DataFrame([asdict(record) for record in sales_data])
df['total_amount'] = [record.total_amount for record in sales_data]
print(df)
```

---

## 3. 기본값과 타입 힌트

### 3.1 기본값 설정

```python
from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class Employee:
    name: str
    department: str
    salary: float = 0.0  # 기본값
    is_active: bool = True  # 기본값
    hire_date: Optional[datetime] = None  # 선택적 필드

# 다양한 방식으로 객체 생성
emp1 = Employee("김철수", "개발팀")
print(emp1)

emp2 = Employee("이영희", "마케팅팀", 5000000)
print(emp2)

emp3 = Employee("박민수", "인사팀", 4500000, True, datetime(2024, 1, 1))
print(emp3)
```

### 3.2 기본값 규칙

```python
# ❌ 잘못된 예: 기본값이 있는 필드 뒤에 기본값이 없는 필드
@dataclass
class WrongExample:
    name: str = "Unknown"
    age: int  # TypeError 발생!

# ✅ 올바른 예: 기본값이 없는 필드를 먼저
@dataclass
class CorrectExample:
    age: int
    name: str = "Unknown"
```

### 3.3 복잡한 타입 힌트

```python
from dataclasses import dataclass
from typing import List, Dict, Optional, Union
from datetime import date

@dataclass
class StudentRecord:
    student_id: str
    name: str
    grades: List[float]
    subjects: Dict[str, float]
    graduation_date: Optional[date] = None
    contact: Union[str, int] = ""  # 이메일 또는 전화번호
    
    def average_grade(self) -> float:
        return sum(self.grades) / len(self.grades) if self.grades else 0.0

# 사용 예제
student = StudentRecord(
    student_id="2024001",
    name="김학생",
    grades=[85.5, 92.0, 78.5, 88.0],
    subjects={"수학": 85.5, "영어": 92.0, "과학": 78.5, "국어": 88.0}
)

print(f"평균 점수: {student.average_grade():.1f}")
```

---

## 4. Field 함수 활용

### 4.1 Field 기본 사용법

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class ShoppingCart:
    customer_name: str
    items: List[str] = field(default_factory=list)  # 빈 리스트로 초기화
    total_amount: float = field(default=0.0, init=False)  # 초기화에서 제외
    created_at: str = field(repr=False)  # repr에서 제외
    
    def add_item(self, item: str, price: float):
        self.items.append(item)
        self.total_amount += price

# 사용 예제
cart = ShoppingCart("김고객", created_at="2024-01-20")
cart.add_item("노트북", 1500000)
cart.add_item("마우스", 25000)
print(cart)
```

### 4.2 Field 매개변수들

```python
from dataclasses import dataclass, field

@dataclass
class ConfigurableClass:
    # 기본값 설정
    name: str = field(default="Unknown")
    
    # 초기화에서 제외 (계산된 필드)
    computed_value: int = field(init=False, default=0)
    
    # repr에서 제외 (민감한 정보)
    password: str = field(repr=False, default="")
    
    # 비교에서 제외
    timestamp: str = field(compare=False, default="")
    
    # 메타데이터 추가
    score: float = field(metadata={"unit": "points", "max": 100})
    
    def __post_init__(self):
        self.computed_value = len(self.name) * 10

# 사용 예제
obj = ConfigurableClass("테스트", password="secret123", timestamp="2024-01-20")
print(obj)
```

### 4.3 Default Factory 활용

```python
from dataclasses import dataclass, field
from typing import List, Dict
from datetime import datetime
import uuid

def generate_id() -> str:
    return str(uuid.uuid4())[:8]

def current_timestamp() -> str:
    return datetime.now().isoformat()

@dataclass
class Order:
    order_id: str = field(default_factory=generate_id)
    customer_name: str = ""
    items: List[Dict[str, any]] = field(default_factory=list)
    created_at: str = field(default_factory=current_timestamp)
    
    def add_item(self, name: str, quantity: int, price: float):
        self.items.append({
            "name": name,
            "quantity": quantity,
            "price": price,
            "total": quantity * price
        })

# 사용 예제
order1 = Order(customer_name="김고객")
order1.add_item("커피", 2, 4500)
print(order1)

order2 = Order(customer_name="이고객")
order2.add_item("케이크", 1, 25000)
print(order2)
```

---

## 5. 메서드 추가하기

### 5.1 일반 메서드 추가

```python
from dataclasses import dataclass
from typing import List
import math

@dataclass
class Point:
    x: float
    y: float
    
    def distance_from_origin(self) -> float:
        """원점으로부터의 거리 계산"""
        return math.sqrt(self.x**2 + self.y**2)
    
    def distance_to(self, other: 'Point') -> float:
        """다른 점까지의 거리 계산"""
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
    def move(self, dx: float, dy: float) -> 'Point':
        """점을 이동시킨 새로운 점 반환"""
        return Point(self.x + dx, self.y + dy)

# 사용 예제
p1 = Point(3, 4)
p2 = Point(0, 0)

print(f"원점으로부터의 거리: {p1.distance_from_origin()}")
print(f"두 점 사이의 거리: {p1.distance_to(p2)}")

p3 = p1.move(1, 1)
print(f"이동 후 점: {p3}")
```

### 5.2 프로퍼티 활용

```python
from dataclasses import dataclass
from typing import List

@dataclass
class Rectangle:
    width: float
    height: float
    
    @property
    def area(self) -> float:
        """넓이 계산"""
        return self.width * self.height
    
    @property
    def perimeter(self) -> float:
        """둘레 계산"""
        return 2 * (self.width + self.height)
    
    @property
    def is_square(self) -> bool:
        """정사각형 여부 확인"""
        return self.width == self.height
    
    def scale(self, factor: float) -> 'Rectangle':
        """크기 조정"""
        return Rectangle(self.width * factor, self.height * factor)

# 사용 예제
rect = Rectangle(5, 3)
print(f"넓이: {rect.area}")
print(f"둘레: {rect.perimeter}")
print(f"정사각형 여부: {rect.is_square}")

scaled_rect = rect.scale(2)
print(f"2배 확대: {scaled_rect}")
```

### 5.3 클래스 메서드와 정적 메서드

```python
from dataclasses import dataclass
from typing import List, ClassVar
import json

@dataclass
class BankAccount:
    account_number: str
    owner_name: str
    balance: float = 0.0
    
    # 클래스 변수
    bank_name: ClassVar[str] = "Python Bank"
    interest_rate: ClassVar[float] = 0.02
    
    @classmethod
    def from_json(cls, json_str: str) -> 'BankAccount':
        """JSON 문자열로부터 객체 생성"""
        data = json.loads(json_str)
        return cls(**data)
    
    @classmethod
    def create_savings_account(cls, owner_name: str) -> 'BankAccount':
        """적금 계좌 생성"""
        import uuid
        account_number = f"SAV-{str(uuid.uuid4())[:8]}"
        return cls(account_number, owner_name, 0.0)
    
    @staticmethod
    def validate_account_number(account_number: str) -> bool:
        """계좌번호 유효성 검사"""
        return len(account_number) >= 10 and account_number.replace("-", "").isalnum()
    
    def deposit(self, amount: float):
        """입금"""
        if amount > 0:
            self.balance += amount
    
    def withdraw(self, amount: float) -> bool:
        """출금"""
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

# 사용 예제
account1 = BankAccount.create_savings_account("김고객")
print(account1)

json_data = '{"account_number": "CHK-12345678", "owner_name": "이고객", "balance": 100000}'
account2 = BankAccount.from_json(json_data)
print(account2)

print(BankAccount.validate_account_number("CHK-12345678"))
```

---

## 6. 비교와 정렬

### 6.1 기본 비교 기능

```python
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    grade: float
    age: int

# 기본 비교 (모든 필드 비교)
student1 = Student("김철수", 85.5, 20)
student2 = Student("김철수", 85.5, 20)
student3 = Student("이영희", 92.0, 19)

print(student1 == student2)  # True
print(student1 == student3)  # False
```

### 6.2 정렬 기능 활성화

```python
from dataclasses import dataclass

@dataclass(order=True)
class Student:
    name: str
    grade: float
    age: int

# 정렬 가능
students = [
    Student("김철수", 85.5, 20),
    Student("이영희", 92.0, 19),
    Student("박민수", 78.0, 21)
]

# 이름 순으로 정렬 (첫 번째 필드 기준)
sorted_students = sorted(students)
for student in sorted_students:
    print(student)
```

### 6.3 커스텀 정렬 기준

```python
from dataclasses import dataclass, field

@dataclass(order=True)
class Student:
    sort_index: float = field(init=False, repr=False)
    name: str
    grade: float
    age: int
    
    def __post_init__(self):
        # 성적을 기준으로 정렬 (높은 점수가 먼저)
        self.sort_index = -self.grade

# 사용 예제
students = [
    Student("김철수", 85.5, 20),
    Student("이영희", 92.0, 19),
    Student("박민수", 78.0, 21)
]

sorted_students = sorted(students)
print("성적 순 정렬:")
for student in sorted_students:
    print(f"{student.name}: {student.grade}")
```

### 6.4 다중 기준 정렬

```python
from dataclasses import dataclass, field
from typing import Tuple

@dataclass(order=True)
class Employee:
    sort_index: Tuple[str, float] = field(init=False, repr=False)
    name: str
    department: str
    salary: float
    
    def __post_init__(self):
        # 부서별로 먼저 정렬, 그 다음 급여 순 (높은 급여가 먼저)
        self.sort_index = (self.department, -self.salary)

# 사용 예제
employees = [
    Employee("김철수", "개발팀", 5500000),
    Employee("이영희", "마케팅팀", 4800000),
    Employee("박민수", "개발팀", 6000000),
    Employee("최지영", "마케팅팀", 5200000)
]

sorted_employees = sorted(employees)
print("부서별, 급여순 정렬:")
for emp in sorted_employees:
    print(f"{emp.department} - {emp.name}: {emp.salary:,}원")
```

---

## 7. 불변 데이터 클래스

### 7.1 Frozen 데이터 클래스

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class ImmutablePoint:
    x: float
    y: float
    
    def distance_from_origin(self) -> float:
        return (self.x**2 + self.y**2)**0.5

# 사용 예제
point = ImmutablePoint(3, 4)
print(point.distance_from_origin())

# 수정 시도 시 에러 발생
try:
    point.x = 5  # FrozenInstanceError
except Exception as e:
    print(f"에러: {e}")
```

### 7.2 불변성의 한계

```python
from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class ImmutableContainer:
    name: str
    items: List[str]

# 객체 자체는 불변이지만, 내부 리스트는 변경 가능
container = ImmutableContainer("컨테이너", ["item1", "item2"])
print(container)

# 리스트 내용 변경 가능 (주의!)
container.items.append("item3")
print(container)  # 내용이 변경됨
```

### 7.3 완전한 불변성 구현

```python
from dataclasses import dataclass
from typing import Tuple

@dataclass(frozen=True)
class TrulyImmutableContainer:
    name: str
    items: Tuple[str, ...]  # 튜플 사용으로 완전한 불변성 보장
    
    @classmethod
    def from_list(cls, name: str, items: List[str]) -> 'TrulyImmutableContainer':
        return cls(name, tuple(items))
    
    def add_item(self, item: str) -> 'TrulyImmutableContainer':
        """새로운 아이템을 추가한 새 객체 반환"""
        new_items = self.items + (item,)
        return TrulyImmutableContainer(self.name, new_items)

# 사용 예제
container = TrulyImmutableContainer.from_list("컨테이너", ["item1", "item2"])
new_container = container.add_item("item3")

print(f"원본: {container}")
print(f"새 객체: {new_container}")
```

---

## 8. 상속

### 8.1 기본 상속

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    email: str

@dataclass
class Employee(Person):
    employee_id: str
    department: str
    salary: float

# 사용 예제
emp = Employee("김철수", 30, "kim@company.com", "EMP001", "개발팀", 5500000)
print(emp)
```

### 8.2 기본값과 상속

```python
from dataclasses import dataclass
from datetime import date

@dataclass
class Person:
    name: str
    birth_date: date
    email: str = ""  # 기본값 있음

@dataclass
class Student(Person):
    student_id: str
    major: str = "미정"  # 부모에 기본값이 있으므로 자식도 기본값 필요
    gpa: float = 0.0

# 사용 예제
student = Student("김학생", date(2000, 5, 15), student_id="2024001")
print(student)
```

### 8.3 메서드 오버라이딩

```python
from dataclasses import dataclass
from typing import List

@dataclass
class Animal:
    name: str
    species: str
    
    def make_sound(self) -> str:
        return "동물 소리"
    
    def info(self) -> str:
        return f"{self.name}는 {self.species}입니다."

@dataclass
class Dog(Animal):
    breed: str = "믹스"
    
    def make_sound(self) -> str:
        return "멍멍!"
    
    def fetch(self, item: str) -> str:
        return f"{self.name}가 {item}을 가져왔습니다."

@dataclass
class Cat(Animal):
    indoor: bool = True
    
    def make_sound(self) -> str:
        return "야옹~"
    
    def climb(self) -> str:
        return f"{self.name}가 높은 곳으로 올라갔습니다."

# 사용 예제
dog = Dog("바둑이", "개", "진돗개")
cat = Cat("나비", "고양이")

print(dog.info())
print(dog.make_sound())
print(dog.fetch("공"))

print(cat.info())
print(cat.make_sound())
print(cat.climb())
```

---

## 9. 고급 기능

### 9.1 Post-init 처리

```python
from dataclasses import dataclass, field
from typing import List
import hashlib

@dataclass
class User:
    username: str
    email: str
    password: str
    full_name: str = ""
    user_id: str = field(init=False)
    password_hash: str = field(init=False, repr=False)
    
    def __post_init__(self):
        # 사용자 ID 생성
        self.user_id = f"USER_{hash(self.username) % 100000:05d}"
        
        # 비밀번호 해시화
        self.password_hash = hashlib.sha256(self.password.encode()).hexdigest()
        
        # full_name이 비어있으면 username 사용
        if not self.full_name:
            self.full_name = self.username.title()
        
        # 원본 비밀번호 제거 (보안)
        del self.password

# 사용 예제
user = User("john_doe", "john@example.com", "secret123")
print(user)
print(f"User ID: {user.user_id}")
```

### 9.2 슬롯 최적화

```python
from dataclasses import dataclass

@dataclass
class OptimizedPoint:
    __slots__ = ['x', 'y']
    x: float
    y: float
    
    def distance_from_origin(self) -> float:
        return (self.x**2 + self.y**2)**0.5

# 메모리 사용량 비교
import sys

@dataclass
class RegularPoint:
    x: float
    y: float

regular = RegularPoint(1.0, 2.0)
optimized = OptimizedPoint(1.0, 2.0)

print(f"일반 클래스 크기: {sys.getsizeof(regular)} bytes")
print(f"슬롯 클래스 크기: {sys.getsizeof(optimized)} bytes")
```

### 9.3 메타데이터 활용

```python
from dataclasses import dataclass, field, fields

@dataclass
class Product:
    name: str = field(metadata={"description": "제품명"})
    price: float = field(metadata={"description": "가격", "unit": "원", "min": 0})
    category: str = field(metadata={"description": "카테고리"})
    rating: float = field(metadata={"description": "평점", "min": 0, "max": 5})

def print_field_info(cls):
    """클래스의 필드 정보 출력"""
    print(f"\n{cls.__name__} 필드 정보:")
    for field_info in fields(cls):
        metadata = field_info.metadata
        print(f"- {field_info.name} ({field_info.type.__name__}): {metadata.get('description', '설명 없음')}")
        if 'unit' in metadata:
            print(f"  단위: {metadata['unit']}")
        if 'min' in metadata or 'max' in metadata:
            min_val = metadata.get('min', '없음')
            max_val = metadata.get('max', '없음')
            print(f"  범위: {min_val} ~ {max_val}")

# 사용 예제
print_field_info(Product)
```

### 9.4 동적 데이터 클래스 생성

```python
from dataclasses import make_dataclass, field

# 동적으로 데이터 클래스 생성
DynamicStudent = make_dataclass(
    'DynamicStudent',
    [
        'name',
        'age',
        ('grade', float, field(default=0.0)),
        ('subjects', list, field(default_factory=list))
    ]
)

# 사용 예제
student = DynamicStudent("김학생", 20)
student.subjects.append("수학")
student.subjects.append("영어")
print(student)
```

---

## 10. 실전 예제

### 10.1 데이터 분석용 클래스

```python
from dataclasses import dataclass, field
from typing import List, Dict, Optional
import pandas as pd
from datetime import datetime
import statistics

@dataclass
class DataAnalysisResult:
    dataset_name: str
    analysis_date: datetime = field(default_factory=datetime.now)
    row_count: int = 0
    column_count: int = 0
    missing_values: Dict[str, int] = field(default_factory=dict)
    numeric_summary: Dict[str, Dict[str, float]] = field(default_factory=dict)
    categorical_summary: Dict[str, Dict[str, int]] = field(default_factory=dict)
    
    @classmethod
    def from_dataframe(cls, df: pd.DataFrame, name: str) -> 'DataAnalysisResult':
        """DataFrame으로부터 분석 결과 생성"""
        result = cls(dataset_name=name)
        result.row_count = len(df)
        result.column_count = len(df.columns)
        
        # 결측값 분석
        result.missing_values = df.isnull().sum().to_dict()
        
        # 수치형 컬럼 분석
        numeric_cols = df.select_dtypes(include=['number']).columns
        for col in numeric_cols:
            values = df[col].dropna()
            if len(values) > 0:
                result.numeric_summary[col] = {
                    'mean': float(values.mean()),
                    'median': float(values.median()),
                    'std': float(values.std()),
                    'min': float(values.min()),
                    'max': float(values.max())
                }
        
        # 범주형 컬럼 분석
        categorical_cols = df.select_dtypes(include=['object']).columns
        for col in categorical_cols:
            result.categorical_summary[col] = df[col].value_counts().to_dict()
        
        return result
    
    def print_summary(self):
        """분석 결과 요약 출력"""
        print(f"\n=== {self.dataset_name} 분석 결과 ===")
        print(f"분석 일시: {self.analysis_date.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"데이터 크기: {self.row_count:,} 행 × {self.column_count} 열")
        
        print(f"\n결측값:")
        for col, missing in self.missing_values.items():
            if missing > 0:
                print(f"  {col}: {missing:,} ({missing/self.row_count*100:.1f}%)")
        
        print(f"\n수치형 변수 요약:")
        for col, stats in self.numeric_summary.items():
            print(f"  {col}: 평균={stats['mean']:.2f}, 중앙값={stats['median']:.2f}")

# 사용 예제
sample_data = pd.DataFrame({
    'age': [25, 30, 35, None, 28],
    'salary': [50000, 60000, 70000, 55000, None],
    'department': ['IT', 'HR', 'IT', 'Finance', 'HR']
})

analysis = DataAnalysisResult.from_dataframe(sample_data, "직원 데이터")
analysis.print_summary()
```

### 10.2 설정 관리 클래스

```python
from dataclasses import dataclass, field
from typing import Dict, Any, Optional
import json
from pathlib import Path

@dataclass
class DatabaseConfig:
    host: str = "localhost"
    port: int = 5432
    database: str = "mydb"
    username: str = "user"
    password: str = field(repr=False, default="")  # 비밀번호는 출력에서 제외
    
    def connection_string(self) -> str:
        return f"postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"

@dataclass
class APIConfig:
    base_url: str = "https://api.example.com"
    timeout: int = 30
    retry_count: int = 3
    api_key: str = field(repr=False, default="")

@dataclass
class AppConfig:
    app_name: str = "MyApp"
    version: str = "1.0.0"
    debug: bool = False
    database: DatabaseConfig = field(default_factory=DatabaseConfig)
    api: APIConfig = field(default_factory=APIConfig)
    custom_settings: Dict[str, Any] = field(default_factory=dict)
    
    @classmethod
    def from_file(cls, config_path: Path) -> 'AppConfig':
        """설정 파일로부터 설정 로드"""
        if config_path.exists():
            with open(config_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # 중첩된 설정 처리
            db_data = data.pop('database', {})
            api_data = data.pop('api', {})
            
            return cls(
                database=DatabaseConfig(**db_data),
                api=APIConfig(**api_data),
                **data
            )
        return cls()
    
    def save_to_file(self, config_path: Path):
        """설정을 파일로 저장"""
        config_dict = {
            'app_name': self.app_name,
            'version': self.version,
            'debug': self.debug,
            'database': {
                'host': self.database.host,
                'port': self.database.port,
                'database': self.database.database,
                'username': self.database.username
                # 비밀번호는 저장하지 않음
            },
            'api': {
                'base_url': self.api.base_url,
                'timeout': self.api.timeout,
                'retry_count': self.api.retry_count
                # API 키는 저장하지 않음
            },
            'custom_settings': self.custom_settings
        }
        
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(config_dict, f, indent=2, ensure_ascii=False)

# 사용 예제
config = AppConfig()
config.database.host = "production-db.example.com"
config.api.base_url = "https://api.production.com"
config.custom_settings['max_workers'] = 10

print(config)
```

### 10.3 로그 분석 클래스

```python
from dataclasses import dataclass, field
from typing import List, Dict, Counter
from datetime import datetime, timedelta
import re
from collections import defaultdict

@dataclass
class LogEntry:
    timestamp: datetime
    level: str
    message: str
    source: str = ""
    
    @classmethod
    def from_line(cls, line: str) -> Optional['LogEntry']:
        """로그 라인을 파싱하여 LogEntry 생성"""
        # 예: "2024-01-20 10:30:45 [INFO] main.py: Application started"
        pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[(\w+)\] (\w+\.py): (.+)'
        match = re.match(pattern, line.strip())
        
        if match:
            timestamp_str, level, source, message = match.groups()
            timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
            return cls(timestamp, level, message, source)
        return None

@dataclass
class LogAnalyzer:
    entries: List[LogEntry] = field(default_factory=list)
    analysis_period: timedelta = field(default_factory=lambda: timedelta(hours=24))
    
    def add_entry(self, entry: LogEntry):
        """로그 엔트리 추가"""
        self.entries.append(entry)
    
    def load_from_file(self, file_path: str):
        """파일에서 로그 로드"""
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                entry = LogEntry.from_line(line)
                if entry:
                    self.add_entry(entry)
    
    def get_level_summary(self) -> Dict[str, int]:
        """로그 레벨별 개수 반환"""
        return dict(Counter(entry.level for entry in self.entries))
    
    def get_source_summary(self) -> Dict[str, int]:
        """소스 파일별 로그 개수 반환"""
        return dict(Counter(entry.source for entry in self.entries))
    
    def get_error_messages(self) -> List[LogEntry]:
        """에러 메시지만 필터링"""
        return [entry for entry in self.entries if entry.level == 'ERROR']
    
    def get_recent_entries(self, hours: int = 1) -> List[LogEntry]:
        """최근 N시간 내 로그 엔트리 반환"""
        cutoff_time = datetime.now() - timedelta(hours=hours)
        return [entry for entry in self.entries if entry.timestamp >= cutoff_time]
    
    def print_analysis(self):
        """분석 결과 출력"""
        print(f"\n=== 로그 분석 결과 ===")
        print(f"총 로그 엔트리: {len(self.entries):,}개")
        
        print(f"\n레벨별 분포:")
        for level, count in self.get_level_summary().items():
            print(f"  {level}: {count:,}개")
        
        print(f"\n소스별 분포:")
        for source, count in sorted(self.get_source_summary().items()):
            print(f"  {source}: {count:,}개")
        
        errors = self.get_error_messages()
        if errors:
            print(f"\n최근 에러 메시지 (최대 5개):")
            for error in errors[-5:]:
                print(f"  {error.timestamp}: {error.message}")

# 사용 예제 (샘플 데이터)
analyzer = LogAnalyzer()

# 샘플 로그 엔트리 추가
sample_logs = [
    "2024-01-20 10:30:45 [INFO] main.py: Application started",
    "2024-01-20 10:31:00 [DEBUG] database.py: Connected to database",
    "2024-01-20 10:31:15 [ERROR] api.py: Failed to connect to external API",
    "2024-01-20 10:31:30 [WARN] cache.py: Cache miss for key 'user_123'",
    "2024-01-20 10:32:00 [INFO] main.py: Processing request"
]

for log_line in sample_logs:
    entry = LogEntry.from_line(log_line)
    if entry:
        analyzer.add_entry(entry)

analyzer.print_analysis()
```

---

## 마무리

이 튜토리얼에서는 Python dataclass의 모든 기능을 상세히 살펴보았습니다:

### 주요 학습 내용

1. **기본 개념**: 코드 간소화와 가독성 향상
2. **타입 힌트**: 명확한 데이터 구조 정의
3. **Field 함수**: 세밀한 필드 제어
4. **메서드 추가**: 비즈니스 로직 구현
5. **비교와 정렬**: 데이터 정렬 및 비교
6. **불변성**: 안전한 데이터 구조
7. **상속**: 코드 재사용성
8. **고급 기능**: 최적화와 메타데이터

### 판다스와의 연계

- DataFrame과 dataclass 간 변환
- 구조화된 데이터 분석
- 설정 관리 및 로그 분석

### 다음 단계

- Pydantic과의 차이점 이해
- 실제 프로젝트에서의 활용
- 성능 최적화 기법

Dataclass는 판다스와 함께 사용할 때 더욱 강력한 도구가 됩니다. 구조화된 데이터를 다루는 모든 상황에서 활용해보세요!
