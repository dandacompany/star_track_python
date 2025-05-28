# Pydantic v2 완전 가이드

## 판다스를 배운 학생들을 위한 데이터 검증 및 직렬화 튜토리얼

### 목차

1. [Pydantic이란 무엇인가?](#1-pydantic이란-무엇인가)
2. [기본 모델 정의](#2-기본-모델-정의)
3. [데이터 검증](#3-데이터-검증)
4. [필드 정의와 제약조건](#4-필드-정의와-제약조건)
5. [데이터 변환과 직렬화](#5-데이터-변환과-직렬화)
6. [커스텀 검증자](#6-커스텀-검증자)
7. [중첩 모델과 복잡한 구조](#7-중첩-모델과-복잡한-구조)
8. [설정과 구성](#8-설정과-구성)
9. [JSON 스키마 생성](#9-json-스키마-생성)
10. [실전 예제](#10-실전-예제)

---

## 1. Pydantic이란 무엇인가?

### 1.1 개념 소개

Pydantic은 Python 타입 힌트를 사용하여 데이터 검증과 직렬화를 수행하는 라이브러리입니다. 판다스가 DataFrame의 데이터 타입을 관리하는 것처럼, Pydantic은 Python 객체의 데이터 타입과 유효성을 보장합니다.

### 1.2 주요 특징

1. **타입 안전성**: 런타임에서 타입 검증
2. **자동 변환**: 호환 가능한 타입 간 자동 변환
3. **상세한 에러 메시지**: 검증 실패 시 명확한 오류 정보
4. **JSON 스키마 생성**: API 문서화 지원
5. **성능**: Rust로 작성된 코어로 빠른 처리

### 1.3 설치

```bash
pip install pydantic
```

---

## 2. 기본 모델 정의

### 2.1 첫 번째 Pydantic 모델

```python
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class User(BaseModel):
    id: int
    name: str
    email: str
    age: Optional[int] = None
    created_at: datetime = datetime.now()

# 올바른 데이터로 객체 생성
user = User(
    id=1,
    name="김철수",
    email="kim@example.com",
    age=25
)
print(user)
print(f"사용자 ID: {user.id}, 이름: {user.name}")
```

### 2.2 자동 타입 변환

```python
# 문자열을 정수로 자동 변환
user = User(
    id="123",  # 문자열이지만 int로 변환됨
    name="이영희",
    email="lee@example.com",
    age="30"   # 문자열이지만 int로 변환됨
)
print(user)
print(f"ID 타입: {type(user.id)}, 나이 타입: {type(user.age)}")
```

### 2.3 검증 오류 처리

```python
from pydantic import ValidationError

try:
    # 잘못된 데이터 타입
    user = User(
        id="invalid",  # 정수로 변환할 수 없는 문자열
        name="박민수",
        email="park@example.com"
    )
except ValidationError as e:
    print("검증 오류:")
    for error in e.errors():
        print(f"- 필드: {error['loc'][0]}")
        print(f"  메시지: {error['msg']}")
        print(f"  입력값: {error['input']}")
```

---

## 3. 데이터 검증

### 3.1 기본 타입 검증

```python
from pydantic import BaseModel
from typing import List, Dict
from datetime import date

class Product(BaseModel):
    name: str
    price: float
    tags: List[str]
    metadata: Dict[str, str]
    release_date: date
    is_available: bool

# 다양한 타입의 데이터 검증
product = Product(
    name="노트북",
    price="1500000",  # 문자열 -> float 변환
    tags=["전자제품", "컴퓨터"],
    metadata={"brand": "Apple", "model": "MacBook"},
    release_date="2024-01-15",  # 문자열 -> date 변환
    is_available="true"  # 문자열 -> bool 변환
)

print(product)
print(f"가격 타입: {type(product.price)}")
print(f"출시일 타입: {type(product.release_date)}")
```

### 3.2 Union 타입과 Optional

```python
from typing import Union, Optional

class FlexibleModel(BaseModel):
    id: Union[int, str]  # 정수 또는 문자열
    value: Optional[float] = None  # 선택적 필드
    status: Union[bool, str] = "active"  # 기본값이 있는 Union

# 다양한 조합으로 테스트
examples = [
    {"id": 123, "value": 45.6},
    {"id": "ABC123", "status": True},
    {"id": 456},  # value는 None으로 설정됨
]

for data in examples:
    model = FlexibleModel(**data)
    print(f"ID: {model.id} (타입: {type(model.id).__name__})")
    print(f"값: {model.value}, 상태: {model.status}")
    print("---")
```

---

## 4. 필드 정의와 제약조건

### 4.1 Field를 사용한 제약조건

```python
from pydantic import BaseModel, Field
from typing import Annotated

class Student(BaseModel):
    name: Annotated[str, Field(min_length=2, max_length=50)]
    age: Annotated[int, Field(ge=0, le=150)]  # 0 이상 150 이하
    grade: Annotated[float, Field(ge=0.0, le=100.0)]  # 0.0 이상 100.0 이하
    email: Annotated[str, Field(pattern=r'^[^@]+@[^@]+\.[^@]+$')]  # 이메일 패턴
    student_id: Annotated[str, Field(min_length=8, max_length=8)]

# 올바른 데이터
student = Student(
    name="김학생",
    age=20,
    grade=85.5,
    email="student@university.edu",
    student_id="20240001"
)
print(student)

# 제약조건 위반 테스트
try:
    invalid_student = Student(
        name="김",  # 너무 짧음
        age=200,   # 너무 큼
        grade=105, # 범위 초과
        email="invalid-email",  # 잘못된 형식
        student_id="123"  # 너무 짧음
    )
except ValidationError as e:
    print("\n제약조건 위반:")
    for error in e.errors():
        print(f"- {error['loc'][0]}: {error['msg']}")
```

### 4.2 커스텀 필드 설정

```python
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class BlogPost(BaseModel):
    title: str = Field(..., description="블로그 포스트 제목")
    content: str = Field(..., min_length=10, description="포스트 내용")
    author: str = Field(..., description="작성자")
    views: int = Field(default=0, ge=0, description="조회수")
    published: bool = Field(default=False, description="게시 여부")
    created_at: datetime = Field(default_factory=datetime.now, description="생성 시간")
    tags: Optional[List[str]] = Field(default=None, description="태그 목록")

# 필드 정보 확인
print("BlogPost 필드 정보:")
for field_name, field_info in BlogPost.model_fields.items():
    print(f"- {field_name}: {field_info.description}")
```

---

## 5. 데이터 변환과 직렬화

### 5.1 딕셔너리와 JSON 변환

```python
from pydantic import BaseModel
import json

class Person(BaseModel):
    name: str
    age: int
    email: str

# 딕셔너리로부터 생성
data = {"name": "홍길동", "age": 30, "email": "hong@example.com"}
person = Person(**data)

# 딕셔너리로 변환
person_dict = person.model_dump()
print("딕셔너리:", person_dict)

# JSON 문자열로 변환
person_json = person.model_dump_json()
print("JSON:", person_json)

# JSON으로부터 생성
json_str = '{"name": "이순신", "age": 45, "email": "lee@example.com"}'
person_from_json = Person.model_validate_json(json_str)
print("JSON에서 생성:", person_from_json)
```

### 5.2 별칭(Alias) 사용

```python
from pydantic import BaseModel, Field

class APIResponse(BaseModel):
    user_id: int = Field(alias="userId")
    full_name: str = Field(alias="fullName")
    email_address: str = Field(alias="emailAddress")
    is_active: bool = Field(alias="isActive")

# API 응답 형태의 데이터
api_data = {
    "userId": 123,
    "fullName": "김개발자",
    "emailAddress": "dev@company.com",
    "isActive": True
}

response = APIResponse(**api_data)
print("파싱된 데이터:", response)

# 별칭으로 직렬화
serialized = response.model_dump(by_alias=True)
print("별칭으로 직렬화:", serialized)
```

### 5.3 판다스 DataFrame과의 연동

```python
import pandas as pd
from pydantic import BaseModel
from typing import List

class SalesData(BaseModel):
    product_name: str
    quantity: int
    unit_price: float
    sale_date: str
    
    @property
    def total_amount(self) -> float:
        return self.quantity * self.unit_price

# Pydantic 모델 리스트를 DataFrame으로 변환
sales_records = [
    SalesData(product_name="노트북", quantity=2, unit_price=1500000, sale_date="2024-01-15"),
    SalesData(product_name="마우스", quantity=10, unit_price=25000, sale_date="2024-01-16"),
    SalesData(product_name="키보드", quantity=5, unit_price=80000, sale_date="2024-01-17")
]

# DataFrame 생성
df = pd.DataFrame([record.model_dump() for record in sales_records])
df['total_amount'] = [record.total_amount for record in sales_records]
print("DataFrame:")
print(df)

# DataFrame에서 Pydantic 모델로 변환
def df_to_pydantic(df: pd.DataFrame, model_class) -> List[BaseModel]:
    return [model_class(**row.to_dict()) for _, row in df.iterrows()]

# 다시 Pydantic 모델로 변환
converted_records = df_to_pydantic(df[['product_name', 'quantity', 'unit_price', 'sale_date']], SalesData)
print(f"\n변환된 레코드 수: {len(converted_records)}")
```

---

## 6. 커스텀 검증자

### 6.1 Field Validator

```python
from pydantic import BaseModel, field_validator
import re

class UserAccount(BaseModel):
    username: str
    password: str
    email: str
    age: int

    @field_validator('username')
    @classmethod
    def validate_username(cls, v):
        if len(v) < 3:
            raise ValueError('사용자명은 최소 3자 이상이어야 합니다')
        if not re.match(r'^[a-zA-Z0-9_]+$', v):
            raise ValueError('사용자명은 영문, 숫자, 언더스코어만 사용 가능합니다')
        return v.lower()  # 소문자로 변환

    @field_validator('password')
    @classmethod
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError('비밀번호는 최소 8자 이상이어야 합니다')
        if not re.search(r'[A-Z]', v):
            raise ValueError('비밀번호에는 대문자가 포함되어야 합니다')
        if not re.search(r'[0-9]', v):
            raise ValueError('비밀번호에는 숫자가 포함되어야 합니다')
        return v

    @field_validator('age')
    @classmethod
    def validate_age(cls, v):
        if v < 13:
            raise ValueError('13세 이상만 가입 가능합니다')
        return v

# 테스트
try:
    user = UserAccount(
        username="TestUser123",
        password="SecurePass123",
        email="test@example.com",
        age=25
    )
    print("사용자 생성 성공:", user)
except ValidationError as e:
    for error in e.errors():
        print(f"오류: {error['msg']}")
```

### 6.2 Model Validator

```python
from pydantic import BaseModel, model_validator

class PasswordReset(BaseModel):
    password: str
    confirm_password: str
    current_password: str

    @model_validator(mode='after')
    def validate_passwords(self):
        if self.password != self.confirm_password:
            raise ValueError('비밀번호와 확인 비밀번호가 일치하지 않습니다')
        
        if self.password == self.current_password:
            raise ValueError('새 비밀번호는 현재 비밀번호와 달라야 합니다')
        
        return self

# 테스트
try:
    reset = PasswordReset(
        password="newpass123",
        confirm_password="newpass123",
        current_password="oldpass123"
    )
    print("비밀번호 재설정 성공")
except ValidationError as e:
    for error in e.errors():
        print(f"오류: {error['msg']}")
```

---

## 7. 중첩 모델과 복잡한 구조

### 7.1 중첩 모델

```python
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    postal_code: str
    country: str = "대한민국"

class Contact(BaseModel):
    phone: Optional[str] = None
    email: Optional[str] = None

class Person(BaseModel):
    name: str
    age: int
    address: Address
    contact: Contact
    friends: List[str] = []

# 중첩된 데이터 생성
person_data = {
    "name": "김철수",
    "age": 30,
    "address": {
        "street": "강남대로 123",
        "city": "서울",
        "postal_code": "06234"
    },
    "contact": {
        "phone": "010-1234-5678",
        "email": "kim@example.com"
    },
    "friends": ["이영희", "박민수"]
}

person = Person(**person_data)
print("생성된 사람:", person)
print(f"주소: {person.address.city} {person.address.street}")
print(f"연락처: {person.contact.email}")
```

### 7.2 자기 참조 모델

```python
from pydantic import BaseModel
from typing import List, Optional, ForwardRef

class TreeNode(BaseModel):
    value: str
    children: List['TreeNode'] = []
    parent: Optional['TreeNode'] = None

# 트리 구조 생성
root = TreeNode(value="root")
child1 = TreeNode(value="child1", parent=root)
child2 = TreeNode(value="child2", parent=root)
grandchild = TreeNode(value="grandchild", parent=child1)

root.children = [child1, child2]
child1.children = [grandchild]

print(f"루트: {root.value}")
print(f"자식들: {[child.value for child in root.children]}")
print(f"손자: {root.children[0].children[0].value}")
```

---

## 8. 설정과 구성

### 8.1 Model Config

```python
from pydantic import BaseModel, ConfigDict

class StrictModel(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True,  # 문자열 공백 제거
        validate_default=True,      # 기본값도 검증
        extra='forbid',            # 추가 필드 금지
        frozen=True                # 불변 객체
    )
    
    name: str
    age: int

# 테스트
try:
    # 공백이 자동으로 제거됨
    model = StrictModel(name="  김철수  ", age=30)
    print(f"이름: '{model.name}'")  # 공백이 제거됨
    
    # 불변 객체이므로 수정 불가
    # model.name = "이영희"  # 오류 발생
    
except ValidationError as e:
    print("검증 오류:", e)
```

### 8.2 별칭 생성기

```python
from pydantic import BaseModel, ConfigDict

def to_camel(string: str) -> str:
    """snake_case를 camelCase로 변환"""
    components = string.split('_')
    return components[0] + ''.join(word.capitalize() for word in components[1:])

class CamelCaseModel(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)
    
    user_name: str
    email_address: str
    phone_number: str

# 사용 예제
data = {
    "userName": "김개발자",
    "emailAddress": "dev@company.com", 
    "phoneNumber": "010-1234-5678"
}

model = CamelCaseModel(**data)
print("모델:", model)

# camelCase로 직렬화
serialized = model.model_dump(by_alias=True)
print("직렬화:", serialized)
```

---

## 9. JSON 스키마 생성

### 9.1 기본 스키마 생성

```python
from pydantic import BaseModel, Field
from typing import List, Optional
import json

class Product(BaseModel):
    id: int = Field(..., description="제품 고유 ID")
    name: str = Field(..., min_length=1, max_length=100, description="제품명")
    price: float = Field(..., gt=0, description="가격 (원)")
    category: str = Field(..., description="카테고리")
    tags: List[str] = Field(default=[], description="태그 목록")
    is_available: bool = Field(default=True, description="판매 가능 여부")
    description: Optional[str] = Field(None, description="제품 설명")

# JSON 스키마 생성
schema = Product.model_json_schema()
print("JSON 스키마:")
print(json.dumps(schema, indent=2, ensure_ascii=False))
```

### 9.2 OpenAPI 스키마 활용

```python
from pydantic import BaseModel, Field
from typing import List
from enum import Enum

class StatusEnum(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    PENDING = "pending"

class User(BaseModel):
    """사용자 정보 모델"""
    id: int = Field(..., description="사용자 ID", example=1)
    username: str = Field(..., min_length=3, max_length=20, description="사용자명", example="john_doe")
    email: str = Field(..., description="이메일 주소", example="john@example.com")
    status: StatusEnum = Field(default=StatusEnum.ACTIVE, description="계정 상태")
    roles: List[str] = Field(default=[], description="사용자 역할", example=["user", "admin"])

# 스키마 생성 및 출력
schema = User.model_json_schema()
print("OpenAPI 호환 스키마:")
print(json.dumps(schema, indent=2, ensure_ascii=False))
```

---

## 10. 실전 예제

### 10.1 API 요청/응답 모델

```python
from pydantic import BaseModel, Field, field_validator
from typing import List, Optional
from datetime import datetime
from enum import Enum

class OrderStatus(str, Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"

class OrderItem(BaseModel):
    product_id: int = Field(..., gt=0, description="제품 ID")
    product_name: str = Field(..., min_length=1, description="제품명")
    quantity: int = Field(..., gt=0, description="수량")
    unit_price: float = Field(..., gt=0, description="단가")
    
    @property
    def total_price(self) -> float:
        return self.quantity * self.unit_price

class CreateOrderRequest(BaseModel):
    customer_id: int = Field(..., gt=0, description="고객 ID")
    items: List[OrderItem] = Field(..., min_length=1, description="주문 항목")
    shipping_address: str = Field(..., min_length=10, description="배송 주소")
    notes: Optional[str] = Field(None, max_length=500, description="주문 메모")
    
    @field_validator('items')
    @classmethod
    def validate_items(cls, v):
        if not v:
            raise ValueError('주문 항목이 비어있습니다')
        return v

class OrderResponse(BaseModel):
    order_id: int = Field(..., description="주문 ID")
    customer_id: int = Field(..., description="고객 ID")
    status: OrderStatus = Field(..., description="주문 상태")
    items: List[OrderItem] = Field(..., description="주문 항목")
    total_amount: float = Field(..., description="총 금액")
    created_at: datetime = Field(..., description="주문 생성 시간")
    updated_at: datetime = Field(..., description="마지막 수정 시간")

# 사용 예제
request_data = {
    "customer_id": 123,
    "items": [
        {
            "product_id": 1,
            "product_name": "노트북",
            "quantity": 1,
            "unit_price": 1500000
        },
        {
            "product_id": 2,
            "product_name": "마우스",
            "quantity": 2,
            "unit_price": 25000
        }
    ],
    "shipping_address": "서울시 강남구 테헤란로 123, 456호",
    "notes": "문 앞에 놓아주세요"
}

# 요청 검증
try:
    order_request = CreateOrderRequest(**request_data)
    print("주문 요청 검증 성공")
    
    # 총 금액 계산
    total = sum(item.total_price for item in order_request.items)
    print(f"총 주문 금액: {total:,}원")
    
    # 응답 생성
    response = OrderResponse(
        order_id=12345,
        customer_id=order_request.customer_id,
        status=OrderStatus.PENDING,
        items=order_request.items,
        total_amount=total,
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    
    print("주문 응답:", response.model_dump_json(indent=2))
    
except ValidationError as e:
    print("검증 오류:")
    for error in e.errors():
        print(f"- {error['loc']}: {error['msg']}")
```

### 10.2 설정 파일 관리

```python
from pydantic import BaseModel, Field, field_validator
from typing import Optional, Dict, Any
import os
from pathlib import Path

class DatabaseConfig(BaseModel):
    host: str = Field(default="localhost", description="데이터베이스 호스트")
    port: int = Field(default=5432, ge=1, le=65535, description="포트 번호")
    database: str = Field(..., min_length=1, description="데이터베이스 이름")
    username: str = Field(..., min_length=1, description="사용자명")
    password: str = Field(..., min_length=1, description="비밀번호")
    
    @property
    def connection_url(self) -> str:
        return f"postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"

class RedisConfig(BaseModel):
    host: str = Field(default="localhost", description="Redis 호스트")
    port: int = Field(default=6379, ge=1, le=65535, description="포트 번호")
    password: Optional[str] = Field(default=None, description="비밀번호")
    db: int = Field(default=0, ge=0, description="데이터베이스 번호")

class AppConfig(BaseModel):
    app_name: str = Field(default="MyApp", description="애플리케이션 이름")
    debug: bool = Field(default=False, description="디버그 모드")
    secret_key: str = Field(..., min_length=32, description="비밀 키")
    database: DatabaseConfig = Field(..., description="데이터베이스 설정")
    redis: RedisConfig = Field(default_factory=RedisConfig, description="Redis 설정")
    allowed_hosts: List[str] = Field(default=["localhost"], description="허용된 호스트")
    
    @field_validator('secret_key')
    @classmethod
    def validate_secret_key(cls, v):
        if len(v) < 32:
            raise ValueError('비밀 키는 최소 32자 이상이어야 합니다')
        return v
    
    @classmethod
    def from_env(cls) -> 'AppConfig':
        """환경 변수로부터 설정 로드"""
        return cls(
            app_name=os.getenv('APP_NAME', 'MyApp'),
            debug=os.getenv('DEBUG', 'false').lower() == 'true',
            secret_key=os.getenv('SECRET_KEY', 'your-secret-key-here-must-be-32-chars'),
            database=DatabaseConfig(
                host=os.getenv('DB_HOST', 'localhost'),
                port=int(os.getenv('DB_PORT', '5432')),
                database=os.getenv('DB_NAME', 'myapp'),
                username=os.getenv('DB_USER', 'user'),
                password=os.getenv('DB_PASSWORD', 'password')
            ),
            redis=RedisConfig(
                host=os.getenv('REDIS_HOST', 'localhost'),
                port=int(os.getenv('REDIS_PORT', '6379')),
                password=os.getenv('REDIS_PASSWORD'),
                db=int(os.getenv('REDIS_DB', '0'))
            ),
            allowed_hosts=os.getenv('ALLOWED_HOSTS', 'localhost').split(',')
        )

# 사용 예제
try:
    config = AppConfig.from_env()
    print("설정 로드 성공:")
    print(f"앱 이름: {config.app_name}")
    print(f"데이터베이스 URL: {config.database.connection_url}")
    print(f"허용된 호스트: {config.allowed_hosts}")
    
except ValidationError as e:
    print("설정 검증 오류:")
    for error in e.errors():
        print(f"- {error['loc']}: {error['msg']}")
```

### 10.3 데이터 ETL 파이프라인

```python
from pydantic import BaseModel, Field, field_validator
from typing import List, Dict, Optional, Any
import pandas as pd
from datetime import datetime, date
from enum import Enum

class DataQuality(str, Enum):
    EXCELLENT = "excellent"
    GOOD = "good"
    FAIR = "fair"
    POOR = "poor"

class DataSource(BaseModel):
    name: str = Field(..., description="데이터 소스 이름")
    type: str = Field(..., description="데이터 타입 (csv, json, db 등)")
    location: str = Field(..., description="데이터 위치")
    last_updated: datetime = Field(..., description="마지막 업데이트 시간")

class DataValidationRule(BaseModel):
    column: str = Field(..., description="검증할 컬럼")
    rule_type: str = Field(..., description="규칙 타입")
    parameters: Dict[str, Any] = Field(default={}, description="규칙 매개변수")
    
    @field_validator('rule_type')
    @classmethod
    def validate_rule_type(cls, v):
        allowed_types = ['not_null', 'range', 'pattern', 'unique', 'foreign_key']
        if v not in allowed_types:
            raise ValueError(f'허용되지 않는 규칙 타입: {v}')
        return v

class DataQualityReport(BaseModel):
    source: DataSource = Field(..., description="데이터 소스")
    total_records: int = Field(..., ge=0, description="총 레코드 수")
    valid_records: int = Field(..., ge=0, description="유효한 레코드 수")
    invalid_records: int = Field(..., ge=0, description="무효한 레코드 수")
    quality_score: float = Field(..., ge=0, le=100, description="품질 점수")
    quality_level: DataQuality = Field(..., description="품질 등급")
    validation_errors: List[Dict[str, Any]] = Field(default=[], description="검증 오류")
    generated_at: datetime = Field(default_factory=datetime.now, description="보고서 생성 시간")
    
    @field_validator('invalid_records')
    @classmethod
    def validate_invalid_records(cls, v, info):
        if 'total_records' in info.data:
            total = info.data['total_records']
            if v > total:
                raise ValueError('무효한 레코드 수가 총 레코드 수를 초과할 수 없습니다')
        return v
    
    @property
    def validity_rate(self) -> float:
        if self.total_records == 0:
            return 0.0
        return (self.valid_records / self.total_records) * 100

class ETLPipeline(BaseModel):
    pipeline_id: str = Field(..., description="파이프라인 ID")
    name: str = Field(..., description="파이프라인 이름")
    sources: List[DataSource] = Field(..., description="데이터 소스 목록")
    validation_rules: List[DataValidationRule] = Field(default=[], description="검증 규칙")
    target_location: str = Field(..., description="결과 저장 위치")
    schedule: Optional[str] = Field(None, description="실행 스케줄")
    
    def validate_data(self, df: pd.DataFrame) -> DataQualityReport:
        """데이터 품질 검증"""
        total_records = len(df)
        validation_errors = []
        
        # 각 규칙에 대해 검증 수행
        for rule in self.validation_rules:
            if rule.column not in df.columns:
                validation_errors.append({
                    "rule": rule.rule_type,
                    "column": rule.column,
                    "error": "컬럼이 존재하지 않음"
                })
                continue
            
            if rule.rule_type == "not_null":
                null_count = df[rule.column].isnull().sum()
                if null_count > 0:
                    validation_errors.append({
                        "rule": "not_null",
                        "column": rule.column,
                        "error": f"{null_count}개의 NULL 값 발견"
                    })
        
        # 품질 점수 계산
        invalid_records = len(validation_errors)
        valid_records = total_records - invalid_records
        quality_score = (valid_records / total_records * 100) if total_records > 0 else 0
        
        # 품질 등급 결정
        if quality_score >= 95:
            quality_level = DataQuality.EXCELLENT
        elif quality_score >= 85:
            quality_level = DataQuality.GOOD
        elif quality_score >= 70:
            quality_level = DataQuality.FAIR
        else:
            quality_level = DataQuality.POOR
        
        return DataQualityReport(
            source=self.sources[0],  # 첫 번째 소스 사용
            total_records=total_records,
            valid_records=valid_records,
            invalid_records=invalid_records,
            quality_score=quality_score,
            quality_level=quality_level,
            validation_errors=validation_errors
        )

# 사용 예제
pipeline = ETLPipeline(
    pipeline_id="ETL001",
    name="고객 데이터 처리 파이프라인",
    sources=[
        DataSource(
            name="고객 마스터",
            type="csv",
            location="/data/customers.csv",
            last_updated=datetime.now()
        )
    ],
    validation_rules=[
        DataValidationRule(
            column="customer_id",
            rule_type="not_null"
        ),
        DataValidationRule(
            column="email",
            rule_type="not_null"
        )
    ],
    target_location="/processed/customers_clean.csv"
)

# 샘플 데이터로 테스트
sample_data = pd.DataFrame({
    'customer_id': [1, 2, None, 4],
    'name': ['김철수', '이영희', '박민수', '최지영'],
    'email': ['kim@test.com', None, 'park@test.com', 'choi@test.com']
})

report = pipeline.validate_data(sample_data)
print("데이터 품질 보고서:")
print(f"총 레코드: {report.total_records}")
print(f"유효 레코드: {report.valid_records}")
print(f"품질 점수: {report.quality_score:.1f}%")
print(f"품질 등급: {report.quality_level}")
print(f"유효성 비율: {report.validity_rate:.1f}%")

if report.validation_errors:
    print("\n검증 오류:")
    for error in report.validation_errors:
        print(f"- {error['column']}: {error['error']}")
```

---

## 마무리

이 튜토리얼에서는 Pydantic v2의 핵심 기능들을 상세히 살펴보았습니다:

### 주요 학습 내용

1. **기본 모델**: 타입 안전성과 자동 변환
2. **데이터 검증**: 강력한 타입 검증과 제약조건
3. **필드 정의**: Field를 통한 세밀한 제어
4. **직렬화**: JSON, 딕셔너리 변환
5. **커스텀 검증**: 비즈니스 로직 구현
6. **중첩 모델**: 복잡한 데이터 구조
7. **설정 관리**: 애플리케이션 구성
8. **JSON 스키마**: API 문서화

### Dataclass vs Pydantic

- **Dataclass**: 단순한 데이터 컨테이너
- **Pydantic**: 데이터 검증과 직렬화가 필요한 경우

### 판다스와의 연계

- DataFrame ↔ Pydantic 모델 변환
- 데이터 품질 검증
- ETL 파이프라인 구축

### 실제 활용 분야

- API 개발 (FastAPI)
- 설정 파일 관리
- 데이터 파이프라인
- 데이터 검증 시스템

Pydantic은 판다스와 함께 사용할 때 데이터의 품질과 일관성을 보장하는 강력한 도구입니다!
