# Python Dataclass 완전 가이드 - 판다스 학습자를 위한 튜토리얼

## 목차

1. [Dataclass란 무엇인가?](#1-dataclass란-무엇인가)
2. [기본 사용법](#2-기본-사용법)
3. [기본값과 타입 힌트](#3-기본값과-타입-힌트)
4. [Field 함수 활용](#4-field-함수-활용)
5. [메서드 추가하기](#5-메서드-추가하기)
6. [비교와 정렬](#6-비교와-정렬)
7. [불변 데이터 클래스](#7-불변-데이터-클래스)
8. [상속과 확장](#8-상속과-확장)
9. [고급 기능들](#9-고급-기능들)
10. [실전 예제](#10-실전-예제)

---

## 1. Dataclass란 무엇인가?

### 1.1 개념 소개

Python 3.7에서 도입된 `dataclass`는 주로 데이터를 저장하기 위한 클래스를 쉽게 만들 수 있게 해주는 데코레이터입니다. 판다스의 DataFrame이 표 형태의 데이터를 다루는 것처럼, dataclass는 구조화된 데이터 객체를 만드는 데 특화되어 있습니다.

### 1.2 왜 Dataclass를 사용해야 할까?

**기존 클래스 방식:**

```python
class Student:
    def __init__(self, name, age, grade, subjects):
        self.name = name
        self.age = age
        self.grade = grade
        self.subjects = subjects
    
    def __repr__(self):
        return f"Student(name='{self.name}', age={self.age}, grade={self.grade}, subjects={self.subjects})"
    
    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return (self.name, self.age, self.grade, self.subjects) == \
               (other.name, other.age, other.grade, other.subjects)
```

**Dataclass 방식:**

```python
from dataclasses import dataclass
from typing import List

@dataclass
class Student:
    name: str
    age: int
    grade: str
    subjects: List[str]
```

두 코드는 동일한 기능을 제공하지만, dataclass는 훨씬 간결합니다!

---

## 2. 기본 사용법

### 2.1 첫 번째 Dataclass 만들기

```python
from dataclasses import dataclass
from typing import List, Optional
import pandas as pd

@dataclass
class DataPoint:
    """데이터 분석을 위한 기본 데이터 포인트"""
    id: int
    value: float
    category: str
    timestamp: str

# 객체 생성
point1 = DataPoint(1, 23.5, "A", "2024-01-01")
point2 = DataPoint(2, 45.2, "B", "2024-01-02")

print(point1)
# 출력: DataPoint(id=1, value=23.5, category='A', timestamp='2024-01-01')

print(point1 == point2)  # False
print(point1 == DataPoint(1, 23.5, "A", "2024-01-01"))  # True
```

### 2.2 판다스와의 연동

```python
@dataclass
class SalesRecord:
    date: str
    product: str
    quantity: int
    price: float
    region: str

# 여러 레코드 생성
records = [
    SalesRecord("2024-01-01", "노트북", 5, 1200000, "서울"),
    SalesRecord("2024-01-02", "마우스", 20, 25000, "부산"),
    SalesRecord("2024-01-03", "키보드", 15, 80000, "대구"),
]

# DataFrame으로 변환
import pandas as pd
from dataclasses import asdict

df = pd.DataFrame([asdict(record) for record in records])
print(df)
```

---

## 3. 기본값과 타입 힌트

### 3.1 기본값 설정

```python
@dataclass
class AnalysisConfig:
    """데이터 분석 설정을 위한 클래스"""
    dataset_name: str
    sample_size: int = 1000
    random_state: int = 42
    test_size: float = 0.2
    normalize: bool = True
    algorithm: str = "random_forest"

# 기본값 사용
config1 = AnalysisConfig("iris_dataset")
print(config1)

# 일부 값만 변경
config2 = AnalysisConfig("wine_dataset", sample_size=500, algorithm="svm")
print(config2)
```

### 3.2 복잡한 타입 힌트

```python
from typing import Dict, List, Optional, Union
from datetime import datetime

@dataclass
class DatasetInfo:
    """데이터셋 정보를 담는 클래스"""
    name: str
    features: List[str]
    target: str
    metadata: Dict[str, Union[str, int, float]]
    created_at: datetime
    description: Optional[str] = None
    tags: List[str] = None
    
    def __post_init__(self):
        # tags가 None이면 빈 리스트로 초기화
        if self.tags is None:
            self.tags = []

# 사용 예제
dataset = DatasetInfo(
    name="customer_data",
    features=["age", "income", "education"],
    target="purchase",
    metadata={"rows": 10000, "source": "survey", "version": 1.2},
    created_at=datetime.now(),
    description="고객 구매 예측 데이터셋"
)
```

---

## 4. Field 함수 활용

### 4.1 Field 기본 사용법

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class ExperimentResult:
    """실험 결과를 저장하는 클래스"""
    experiment_id: str
    accuracy: float
    precision: float
    recall: float
    
    # 계산된 필드 (초기화에서 제외)
    f1_score: float = field(init=False)
    
    # 내부 사용 필드 (repr에서 제외)
    _internal_data: List = field(default_factory=list, repr=False)
    
    # 메타데이터 포함
    model_type: str = field(metadata={"description": "사용된 모델 타입"})
    
    def __post_init__(self):
        # F1 스코어 자동 계산
        self.f1_score = 2 * (self.precision * self.recall) / (self.precision + self.recall)

# 사용 예제
result = ExperimentResult(
    experiment_id="exp_001",
    accuracy=0.85,
    precision=0.82,
    recall=0.88,
    model_type="RandomForest"
)

print(result)
print(f"F1 Score: {result.f1_score:.3f}")
```

### 4.2 Default Factory 활용

```python
from datetime import datetime
from typing import List, Dict

@dataclass
class MLPipeline:
    """머신러닝 파이프라인 설정"""
    name: str
    
    # 가변 객체는 default_factory 사용
    steps: List[str] = field(default_factory=list)
    parameters: Dict[str, any] = field(default_factory=dict)
    
    # 현재 시간을 기본값으로
    created_at: datetime = field(default_factory=datetime.now)
    
    # 고유 ID 생성
    pipeline_id: str = field(default_factory=lambda: f"pipeline_{datetime.now().strftime('%Y%m%d_%H%M%S')}")

# 사용 예제
pipeline1 = MLPipeline("classification_pipeline")
pipeline2 = MLPipeline("regression_pipeline")

print(f"Pipeline 1 ID: {pipeline1.pipeline_id}")
print(f"Pipeline 2 ID: {pipeline2.pipeline_id}")
```

---

## 5. 메서드 추가하기

### 5.1 일반 메서드

```python
import pandas as pd
from typing import List

@dataclass
class DataAnalyzer:
    """데이터 분석을 위한 클래스"""
    data: pd.DataFrame
    target_column: str
    feature_columns: List[str] = field(default_factory=list)
    
    def __post_init__(self):
        if not self.feature_columns:
            self.feature_columns = [col for col in self.data.columns if col != self.target_column]
    
    def get_summary_stats(self) -> pd.DataFrame:
        """기본 통계 정보 반환"""
        return self.data[self.feature_columns].describe()
    
    def get_correlation_matrix(self) -> pd.DataFrame:
        """상관관계 매트릭스 반환"""
        return self.data[self.feature_columns + [self.target_column]].corr()
    
    def get_missing_values(self) -> pd.Series:
        """결측값 정보 반환"""
        return self.data.isnull().sum()
    
    def filter_by_condition(self, condition: str) -> 'DataAnalyzer':
        """조건에 따라 필터링된 새로운 분석기 반환"""
        filtered_data = self.data.query(condition)
        return DataAnalyzer(filtered_data, self.target_column, self.feature_columns.copy())

# 사용 예제
# 샘플 데이터 생성
import numpy as np

np.random.seed(42)
sample_data = pd.DataFrame({
    'age': np.random.randint(20, 80, 100),
    'income': np.random.normal(50000, 15000, 100),
    'education_years': np.random.randint(8, 20, 100),
    'purchase': np.random.choice([0, 1], 100)
})

analyzer = DataAnalyzer(sample_data, 'purchase')
print("기본 통계:")
print(analyzer.get_summary_stats())
```

### 5.2 프로퍼티와 클래스 메서드

```python
@dataclass
class ModelPerformance:
    """모델 성능 지표 클래스"""
    true_positives: int
    false_positives: int
    true_negatives: int
    false_negatives: int
    
    @property
    def accuracy(self) -> float:
        """정확도 계산"""
        total = self.true_positives + self.false_positives + self.true_negatives + self.false_negatives
        return (self.true_positives + self.true_negatives) / total
    
    @property
    def precision(self) -> float:
        """정밀도 계산"""
        return self.true_positives / (self.true_positives + self.false_positives)
    
    @property
    def recall(self) -> float:
        """재현율 계산"""
        return self.true_positives / (self.true_positives + self.false_negatives)
    
    @property
    def f1_score(self) -> float:
        """F1 스코어 계산"""
        return 2 * (self.precision * self.recall) / (self.precision + self.recall)
    
    @classmethod
    def from_confusion_matrix(cls, confusion_matrix: List[List[int]]) -> 'ModelPerformance':
        """혼동 행렬로부터 객체 생성"""
        tn, fp, fn, tp = confusion_matrix[0][0], confusion_matrix[0][1], confusion_matrix[1][0], confusion_matrix[1][1]
        return cls(tp, fp, tn, fn)
    
    def to_dict(self) -> dict:
        """딕셔너리로 변환"""
        return {
            'accuracy': self.accuracy,
            'precision': self.precision,
            'recall': self.recall,
            'f1_score': self.f1_score
        }

# 사용 예제
performance = ModelPerformance(85, 15, 90, 10)
print(f"정확도: {performance.accuracy:.3f}")
print(f"정밀도: {performance.precision:.3f}")
print(f"재현율: {performance.recall:.3f}")
print(f"F1 스코어: {performance.f1_score:.3f}")

# 혼동 행렬로부터 생성
confusion_matrix = [[90, 15], [10, 85]]
performance2 = ModelPerformance.from_confusion_matrix(confusion_matrix)
print("\n혼동 행렬로부터 생성된 성능:")
print(performance2.to_dict())
```

---

## 6. 비교와 정렬

### 6.1 기본 비교 기능

```python
@dataclass
class DataQualityScore:
    """데이터 품질 점수"""
    dataset_name: str
    completeness: float  # 완전성 (0-1)
    accuracy: float      # 정확성 (0-1)
    consistency: float   # 일관성 (0-1)
    timeliness: float    # 적시성 (0-1)
    
    @property
    def overall_score(self) -> float:
        """전체 품질 점수 계산"""
        return (self.completeness + self.accuracy + self.consistency + self.timeliness) / 4

# 비교 예제
score1 = DataQualityScore("dataset_A", 0.95, 0.88, 0.92, 0.85)
score2 = DataQualityScore("dataset_B", 0.95, 0.88, 0.92, 0.85)
score3 = DataQualityScore("dataset_C", 0.90, 0.85, 0.88, 0.80)

print(score1 == score2)  # True (모든 필드가 같음)
print(score1 == score3)  # False
```

### 6.2 커스텀 정렬 기준

```python
from dataclasses import dataclass, field

@dataclass(order=True)
class ExperimentRun:
    """실험 실행 결과"""
    # 정렬 기준이 되는 필드를 첫 번째로 배치
    sort_index: float = field(init=False, repr=False)
    
    experiment_name: str
    model_type: str
    accuracy: float
    training_time: float  # 초 단위
    memory_usage: float   # MB 단위
    
    def __post_init__(self):
        # 정확도를 기준으로 정렬 (높은 순)
        self.sort_index = -self.accuracy  # 음수로 해서 내림차순 정렬

# 실험 결과들
experiments = [
    ExperimentRun("exp_1", "RandomForest", 0.85, 120.5, 256.0),
    ExperimentRun("exp_2", "SVM", 0.92, 45.2, 128.0),
    ExperimentRun("exp_3", "NeuralNet", 0.88, 300.8, 512.0),
    ExperimentRun("exp_4", "LogisticRegression", 0.79, 15.3, 64.0),
]

# 정확도 기준으로 정렬 (높은 순)
sorted_experiments = sorted(experiments)
print("정확도 기준 정렬 결과:")
for exp in sorted_experiments:
    print(f"{exp.experiment_name}: {exp.accuracy:.3f}")
```

### 6.3 다중 기준 정렬

```python
@dataclass(order=True)
class ModelComparison:
    """모델 비교를 위한 클래스"""
    # 복합 정렬 기준
    sort_index: tuple = field(init=False, repr=False)
    
    model_name: str
    accuracy: float
    speed: float  # 예측 속도 (predictions/sec)
    memory: float  # 메모리 사용량 (MB)
    
    def __post_init__(self):
        # 1순위: 정확도 (높은 순), 2순위: 속도 (높은 순), 3순위: 메모리 (낮은 순)
        self.sort_index = (-self.accuracy, -self.speed, self.memory)

models = [
    ModelComparison("Model_A", 0.85, 1000, 256),
    ModelComparison("Model_B", 0.85, 1200, 128),  # 같은 정확도, 더 빠름, 적은 메모리
    ModelComparison("Model_C", 0.90, 800, 512),   # 더 정확함
    ModelComparison("Model_D", 0.85, 1000, 512),  # Model_A와 같지만 메모리 더 많이 사용
]

sorted_models = sorted(models)
print("모델 성능 순위:")
for i, model in enumerate(sorted_models, 1):
    print(f"{i}. {model.model_name}: 정확도={model.accuracy:.2f}, 속도={model.speed}, 메모리={model.memory}MB")
```

---

## 7. 불변 데이터 클래스

### 7.1 Frozen Dataclass

```python
@dataclass(frozen=True)
class ImmutableConfig:
    """변경 불가능한 설정 클래스"""
    model_type: str
    learning_rate: float
    batch_size: int
    epochs: int
    random_seed: int = 42
    
    def get_hyperparameters(self) -> dict:
        """하이퍼파라미터 딕셔너리 반환"""
        return {
            'learning_rate': self.learning_rate,
            'batch_size': self.batch_size,
            'epochs': self.epochs,
            'random_seed': self.random_seed
        }

# 사용 예제
config = ImmutableConfig("neural_network", 0.001, 32, 100)
print(config)

# 변경 시도 시 에러 발생
try:
    config.learning_rate = 0.01  # FrozenInstanceError 발생
except Exception as e:
    print(f"에러: {e}")

# 새로운 설정이 필요하면 새 객체 생성
new_config = ImmutableConfig("neural_network", 0.01, 32, 100)
```

### 7.2 불변성의 한계와 해결책

```python
from typing import List, Tuple

@dataclass(frozen=True)
class ImmutableExperiment:
    """불변 실험 설정"""
    name: str
    parameters: Tuple[float, ...]  # 리스트 대신 튜플 사용
    feature_names: Tuple[str, ...]
    
    @classmethod
    def from_lists(cls, name: str, parameters: List[float], feature_names: List[str]):
        """리스트로부터 불변 객체 생성"""
        return cls(name, tuple(parameters), tuple(feature_names))
    
    def with_updated_parameters(self, new_parameters: List[float]) -> 'ImmutableExperiment':
        """새로운 파라미터로 새 객체 생성"""
        return ImmutableExperiment(self.name, tuple(new_parameters), self.feature_names)

# 사용 예제
experiment = ImmutableExperiment.from_lists(
    "experiment_1", 
    [0.1, 0.2, 0.3], 
    ["feature_1", "feature_2", "feature_3"]
)

# 파라미터 업데이트 (새 객체 생성)
updated_experiment = experiment.with_updated_parameters([0.15, 0.25, 0.35])
print(f"원본: {experiment.parameters}")
print(f"업데이트: {updated_experiment.parameters}")
```

---

## 8. 상속과 확장

### 8.1 기본 상속

```python
@dataclass
class BaseModel:
    """기본 모델 클래스"""
    name: str
    created_at: str
    version: str = "1.0"
    
    def get_info(self) -> str:
        return f"{self.name} v{self.version} (생성일: {self.created_at})"

@dataclass
class ClassificationModel(BaseModel):
    """분류 모델 클래스"""
    num_classes: int
    class_names: List[str] = field(default_factory=list)
    
    def predict_proba(self, X) -> str:
        return f"{self.name}으로 {len(X)}개 샘플의 확률 예측"

@dataclass
class RegressionModel(BaseModel):
    """회귀 모델 클래스"""
    target_range: Tuple[float, float] = (0.0, 1.0)
    
    def predict(self, X) -> str:
        return f"{self.name}으로 {len(X)}개 샘플의 값 예측"

# 사용 예제
clf_model = ClassificationModel(
    name="RandomForestClassifier",
    created_at="2024-01-01",
    num_classes=3,
    class_names=["Class_A", "Class_B", "Class_C"]
)

reg_model = RegressionModel(
    name="LinearRegression",
    created_at="2024-01-02",
    target_range=(0.0, 100.0)
)

print(clf_model.get_info())
print(reg_model.get_info())
```

### 8.2 상속 시 주의사항

```python
@dataclass
class BaseExperiment:
    """기본 실험 클래스"""
    name: str
    dataset: str = "default_dataset"
    random_seed: int = 42

@dataclass
class MLExperiment(BaseExperiment):
    """머신러닝 실험 클래스"""
    # 부모 클래스에 기본값이 있으면, 자식 클래스의 새 필드도 기본값이 있어야 함
    model_type: str = "random_forest"
    cross_validation: bool = True
    
    # 부모 필드 재정의 가능
    random_seed: int = 123  # 기본값 변경

# 올바른 사용
experiment = MLExperiment("my_experiment", model_type="svm")
print(experiment)

# 필드 순서는 부모 클래스 정의 순서를 따름
print(f"Random seed: {experiment.random_seed}")  # 123 (재정의된 값)
```

---

## 9. 고급 기능들

### 9.1 Post-init 처리

```python
from datetime import datetime
from typing import Optional

@dataclass
class DataPipeline:
    """데이터 파이프라인 클래스"""
    name: str
    input_path: str
    output_path: str
    
    # 계산될 필드들
    pipeline_id: str = field(init=False)
    created_timestamp: datetime = field(init=False)
    estimated_runtime: Optional[float] = field(init=False, default=None)
    
    def __post_init__(self):
        # 파이프라인 ID 생성
        self.pipeline_id = f"{self.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        # 생성 시간 기록
        self.created_timestamp = datetime.now()
        
        # 입력 경로 기반으로 예상 실행 시간 계산 (예시)
        if "large" in self.input_path.lower():
            self.estimated_runtime = 300.0  # 5분
        elif "medium" in self.input_path.lower():
            self.estimated_runtime = 120.0  # 2분
        else:
            self.estimated_runtime = 60.0   # 1분

pipeline = DataPipeline(
    name="data_cleaning",
    input_path="/data/large_dataset.csv",
    output_path="/processed/clean_data.csv"
)

print(f"파이프라인 ID: {pipeline.pipeline_id}")
print(f"예상 실행 시간: {pipeline.estimated_runtime}초")
```

### 9.2 슬롯 사용하기

```python
@dataclass
class OptimizedDataPoint:
    """메모리 최적화된 데이터 포인트"""
    __slots__ = ['x', 'y', 'label', 'weight']
    
    x: float
    y: float
    label: str
    weight: float = 1.0

# 메모리 사용량 비교 (큰 데이터셋에서 차이가 남)
import sys

# 일반 dataclass
@dataclass
class RegularDataPoint:
    x: float
    y: float
    label: str
    weight: float = 1.0

regular_point = RegularDataPoint(1.0, 2.0, "A")
optimized_point = OptimizedDataPoint(1.0, 2.0, "A")

print(f"일반 클래스 크기: {sys.getsizeof(regular_point)} bytes")
print(f"슬롯 클래스 크기: {sys.getsizeof(optimized_point)} bytes")
```

### 9.3 메타데이터 활용

```python
from dataclasses import fields

@dataclass
class FeatureDefinition:
    """피처 정의 클래스"""
    name: str = field(metadata={"description": "피처 이름", "required": True})
    data_type: str = field(metadata={"description": "데이터 타입", "options": ["numeric", "categorical", "text"]})
    nullable: bool = field(default=False, metadata={"description": "NULL 값 허용 여부"})
    default_value: any = field(default=None, metadata={"description": "기본값"})
    validation_rule: str = field(default="", metadata={"description": "검증 규칙"})

# 메타데이터 조회
feature = FeatureDefinition("age", "numeric", False, 0, "age >= 0")

print("필드 메타데이터:")
for field_info in fields(feature):
    print(f"- {field_info.name}: {field_info.metadata.get('description', 'No description')}")
    if 'options' in field_info.metadata:
        print(f"  옵션: {field_info.metadata['options']}")
```

---

## 10. 실전 예제

### 10.1 데이터 분석 프로젝트 관리

```python
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime
import pandas as pd

@dataclass
class DataAnalysisProject:
    """데이터 분석 프로젝트 관리 클래스"""
    project_name: str
    analyst_name: str
    dataset_path: str
    
    # 자동 생성 필드들
    project_id: str = field(init=False)
    created_at: datetime = field(init=False)
    
    # 분석 설정
    target_variable: Optional[str] = None
    feature_columns: List[str] = field(default_factory=list)
    analysis_type: str = "exploratory"  # exploratory, predictive, descriptive
    
    # 결과 저장
    results: Dict[str, any] = field(default_factory=dict, repr=False)
    notes: List[str] = field(default_factory=list, repr=False)
    
    def __post_init__(self):
        self.project_id = f"proj_{self.project_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        self.created_at = datetime.now()
    
    def load_data(self) -> pd.DataFrame:
        """데이터 로드"""
        try:
            data = pd.read_csv(self.dataset_path)
            self.add_note(f"데이터 로드 완료: {data.shape[0]}행, {data.shape[1]}열")
            return data
        except Exception as e:
            self.add_note(f"데이터 로드 실패: {str(e)}")
            raise
    
    def add_note(self, note: str):
        """분석 노트 추가"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.notes.append(f"[{timestamp}] {note}")
    
    def save_result(self, key: str, value: any):
        """분석 결과 저장"""
        self.results[key] = value
        self.add_note(f"결과 저장: {key}")
    
    def get_summary(self) -> str:
        """프로젝트 요약 반환"""
        summary = f"""
프로젝트 요약:
- 이름: {self.project_name}
- 분석가: {self.analyst_name}
- 생성일: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}
- 분석 유형: {self.analysis_type}
- 타겟 변수: {self.target_variable or 'None'}
- 피처 수: {len(self.feature_columns)}
- 저장된 결과 수: {len(self.results)}
- 노트 수: {len(self.notes)}
        """
        return summary.strip()

# 사용 예제
project = DataAnalysisProject(
    project_name="customer_segmentation",
    analyst_name="김데이터",
    dataset_path="customer_data.csv",
    analysis_type="predictive",
    target_variable="segment"
)

print(project.get_summary())
project.add_note("프로젝트 시작")
project.save_result("initial_analysis", {"status": "completed"})
```

### 10.2 설정 관리 시스템

```python
from dataclasses import dataclass, field
from typing import Dict, List, Union
import json
from pathlib import Path

@dataclass
class DatabaseConfig:
    """데이터베이스 설정"""
    host: str = "localhost"
    port: int = 5432
    database: str = "analytics"
    username: str = "user"
    password: str = field(repr=False, default="password")  # 비밀번호는 출력에서 숨김

@dataclass
class ModelConfig:
    """모델 설정"""
    algorithm: str = "random_forest"
    hyperparameters: Dict[str, Union[int, float, str]] = field(default_factory=dict)
    cross_validation_folds: int = 5
    test_size: float = 0.2
    random_state: int = 42

@dataclass
class LoggingConfig:
    """로깅 설정"""
    level: str = "INFO"
    format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    file_path: str = "analysis.log"
    max_file_size: str = "10MB"

@dataclass
class AnalysisConfig:
    """전체 분석 설정"""
    project_name: str
    version: str = "1.0"
    
    # 하위 설정들
    database: DatabaseConfig = field(default_factory=DatabaseConfig)
    model: ModelConfig = field(default_factory=ModelConfig)
    logging: LoggingConfig = field(default_factory=LoggingConfig)
    
    # 추가 설정
    output_directory: str = "./output"
    enable_caching: bool = True
    parallel_processing: bool = True
    max_workers: int = 4
    
    def save_to_file(self, file_path: str):
        """설정을 JSON 파일로 저장"""
        from dataclasses import asdict
        
        config_dict = asdict(self)
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(config_dict, f, indent=2, ensure_ascii=False)
    
    @classmethod
    def load_from_file(cls, file_path: str) -> 'AnalysisConfig':
        """JSON 파일에서 설정 로드"""
        with open(file_path, 'r', encoding='utf-8') as f:
            config_dict = json.load(f)
        
        # 중첩된 설정 객체들 재생성
        if 'database' in config_dict:
            config_dict['database'] = DatabaseConfig(**config_dict['database'])
        if 'model' in config_dict:
            config_dict['model'] = ModelConfig(**config_dict['model'])
        if 'logging' in config_dict:
            config_dict['logging'] = LoggingConfig(**config_dict['logging'])
        
        return cls(**config_dict)
    
    def update_model_hyperparameters(self, **kwargs):
        """모델 하이퍼파라미터 업데이트"""
        self.model.hyperparameters.update(kwargs)

# 사용 예제
config = AnalysisConfig(
    project_name="sales_prediction",
    version="2.0"
)

# 하이퍼파라미터 설정
config.update_model_hyperparameters(
    n_estimators=100,
    max_depth=10,
    min_samples_split=5
)

# 데이터베이스 설정 변경
config.database.host = "production-db.company.com"
config.database.database = "sales_data"

print("설정 정보:")
print(f"프로젝트: {config.project_name} v{config.version}")
print(f"데이터베이스: {config.database.host}:{config.database.port}/{config.database.database}")
print(f"모델: {config.model.algorithm}")
print(f"하이퍼파라미터: {config.model.hyperparameters}")

# 설정 파일 저장/로드
config.save_to_file("analysis_config.json")
loaded_config = AnalysisConfig.load_from_file("analysis_config.json")
```

### 10.3 로그 분석 시스템

```python
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime
import re
from collections import Counter

@dataclass
class LogEntry:
    """로그 엔트리 클래스"""
    timestamp: datetime
    level: str
    message: str
    source: str = "unknown"
    
    # 파싱된 정보
    parsed_data: Dict[str, str] = field(default_factory=dict, repr=False)
    
    def __post_init__(self):
        # 메시지에서 추가 정보 파싱
        self._parse_message()
    
    def _parse_message(self):
        """메시지에서 구조화된 정보 추출"""
        # IP 주소 추출
        ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
        ip_match = re.search(ip_pattern, self.message)
        if ip_match:
            self.parsed_data['ip_address'] = ip_match.group()
        
        # HTTP 상태 코드 추출
        status_pattern = r'\b[1-5]\d{2}\b'
        status_match = re.search(status_pattern, self.message)
        if status_match:
            self.parsed_data['status_code'] = status_match.group()
        
        # 사용자 ID 추출 (user_id=123 형태)
        user_pattern = r'user_id=(\d+)'
        user_match = re.search(user_pattern, self.message)
        if user_match:
            self.parsed_data['user_id'] = user_match.group(1)

@dataclass
class LogAnalyzer:
    """로그 분석기 클래스"""
    name: str
    entries: List[LogEntry] = field(default_factory=list)
    
    # 분석 결과 캐시
    _analysis_cache: Dict[str, any] = field(default_factory=dict, repr=False)
    
    def add_entry(self, entry: LogEntry):
        """로그 엔트리 추가"""
        self.entries.append(entry)
        # 캐시 무효화
        self._analysis_cache.clear()
    
    def add_log_line(self, log_line: str, log_format: str = "default"):
        """로그 라인 파싱하여 추가"""
        if log_format == "default":
            # 기본 형태: "2024-01-01 12:00:00 INFO message"
            parts = log_line.strip().split(' ', 3)
            if len(parts) >= 4:
                timestamp_str = f"{parts[0]} {parts[1]}"
                timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
                level = parts[2]
                message = parts[3]
                
                entry = LogEntry(timestamp, level, message)
                self.add_entry(entry)
    
    def get_level_distribution(self) -> Dict[str, int]:
        """로그 레벨별 분포"""
        if 'level_dist' not in self._analysis_cache:
            levels = [entry.level for entry in self.entries]
            self._analysis_cache['level_dist'] = dict(Counter(levels))
        return self._analysis_cache['level_dist']
    
    def get_error_entries(self) -> List[LogEntry]:
        """에러 로그만 필터링"""
        return [entry for entry in self.entries if entry.level in ['ERROR', 'CRITICAL']]
    
    def get_ip_addresses(self) -> List[str]:
        """추출된 IP 주소 목록"""
        ips = []
        for entry in self.entries:
            if 'ip_address' in entry.parsed_data:
                ips.append(entry.parsed_data['ip_address'])
        return list(set(ips))  # 중복 제거
    
    def get_time_range(self) -> tuple:
        """로그 시간 범위"""
        if not self.entries:
            return None, None
        
        timestamps = [entry.timestamp for entry in self.entries]
        return min(timestamps), max(timestamps)
    
    def generate_report(self) -> str:
        """분석 보고서 생성"""
        if not self.entries:
            return "분석할 로그가 없습니다."
        
        start_time, end_time = self.get_time_range()
        level_dist = self.get_level_distribution()
        error_count = len(self.get_error_entries())
        unique_ips = len(self.get_ip_addresses())
        
        report = f"""
로그 분석 보고서: {self.name}
{'='*50}
분석 기간: {start_time} ~ {end_time}
총 로그 수: {len(self.entries)}
에러 로그 수: {error_count}
고유 IP 수: {unique_ips}

레벨별 분포:
{'-'*20}
"""
        for level, count in sorted(level_dist.items()):
            percentage = (count / len(self.entries)) * 100
            report += f"{level}: {count}개 ({percentage:.1f}%)\n"
        
        if error_count > 0:
            report += f"\n최근 에러 로그 (최대 5개):\n{'-'*30}\n"
            recent_errors = sorted(self.get_error_entries(), 
                                 key=lambda x: x.timestamp, reverse=True)[:5]
            for error in recent_errors:
                report += f"[{error.timestamp}] {error.level}: {error.message[:100]}...\n"
        
        return report

# 사용 예제
analyzer = LogAnalyzer("웹서버 로그 분석")

# 샘플 로그 데이터 추가
sample_logs = [
    "2024-01-01 10:00:00 INFO User login successful user_id=123 from 192.168.1.100",
    "2024-01-01 10:05:00 WARNING High memory usage detected",
    "2024-01-01 10:10:00 ERROR Database connection failed",
    "2024-01-01 10:15:00 INFO User logout user_id=123",
    "2024-01-01 10:20:00 ERROR 404 Not Found for /api/users from 192.168.1.200",
    "2024-01-01 10:25:00 INFO New user registration user_id=124",
]

for log_line in sample_logs:
    analyzer.add_log_line(log_line)

print(analyzer.generate_report())
print(f"\n추출된 IP 주소: {analyzer.get_ip_addresses()}")
```

---

## 마무리

이 튜토리얼에서는 Python dataclass의 기본 개념부터 고급 활용법까지 다뤘습니다. 주요 내용을 정리하면:

### 핵심 포인트

1. **간결성**: 보일러플레이트 코드 대폭 감소
2. **타입 안정성**: 타입 힌트를 통한 코드 품질 향상
3. **유연성**: 다양한 설정 옵션으로 요구사항에 맞는 클래스 생성
4. **판다스 연동**: DataFrame과의 자연스러운 데이터 교환

### 언제 사용하면 좋을까?

- 구조화된 데이터를 다룰 때
- 설정 관리가 필요할 때
- 데이터 분석 결과를 객체로 관리할 때
- API 응답이나 데이터베이스 레코드를 모델링할 때

### 다음 단계

- Pydantic과 함께 사용하여 데이터 검증 강화
- FastAPI와 연동하여 웹 API 개발
- SQLAlchemy ORM과 결합하여 데이터베이스 모델링

Dataclass는 판다스와 함께 사용할 때 특히 강력합니다. 데이터 분석 워크플로우에서 구조화된 설정 관리, 결과 저장, 메타데이터 관리 등에 활용해보세요!
