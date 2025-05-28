# 🐼 Pandas 완전 정복 튜토리얼

## Pandas 초중급에서 중고급으로 도약하는 단테 가이드

> **📁 데이터셋 준비**: 튜토리얼을 시작하기 전에 `datasets` 폴더에서 `python create_all_datasets.py`를 실행하여 예제 데이터를 생성하세요.

---

## 📚 목차

- [🐼 Pandas 완전 정복 튜토리얼](#-pandas-완전-정복-튜토리얼)
  - [Pandas 초중급에서 중고급으로 도약하는 단테 가이드](#pandas-초중급에서-중고급으로-도약하는-단테-가이드)
  - [📚 목차](#-목차)
  - [기본편](#기본편)
    - [Pandas 소개 및 설치](#pandas-소개-및-설치)
      - [설치 및 임포트](#설치-및-임포트)
    - [Series와 DataFrame 기초](#series와-dataframe-기초)
      - [Series 생성과 기본 조작](#series-생성과-기본-조작)
      - [Series의 기본 속성과 메서드](#series의-기본-속성과-메서드)
      - [DataFrame 생성과 기본 조작](#dataframe-생성과-기본-조작)
      - [DataFrame의 기본 정보 확인](#dataframe의-기본-정보-확인)
    - [데이터 읽기/쓰기](#데이터-읽기쓰기)
      - [CSV 파일 다루기](#csv-파일-다루기)
      - [Excel 파일 다루기](#excel-파일-다루기)
    - [기본 데이터 조작](#기본-데이터-조작)
      - [컬럼 선택과 추가](#컬럼-선택과-추가)
      - [행 선택과 필터링](#행-선택과-필터링)
      - [정렬](#정렬)
  - [중급편](#중급편)
    - [고급 인덱싱과 선택](#고급-인덱싱과-선택)
      - [.loc와 .iloc 활용](#loc와-iloc-활용)
      - [조건부 선택과 query 메서드](#조건부-선택과-query-메서드)
    - [데이터 정제와 변환](#데이터-정제와-변환)
      - [결측값 처리](#결측값-처리)
      - [데이터 타입 변환](#데이터-타입-변환)
      - [apply와 map 함수 활용](#apply와-map-함수-활용)
    - [그룹화와 집계](#그룹화와-집계)
      - [기본 그룹화](#기본-그룹화)
      - [다중 그룹화와 집계](#다중-그룹화와-집계)
      - [transform과 filter 활용](#transform과-filter-활용)
    - [데이터 병합과 결합](#데이터-병합과-결합)
      - [merge 함수 활용](#merge-함수-활용)
      - [concat 함수 활용](#concat-함수-활용)
  - [최신기능편](#최신기능편)
    - [PyArrow 백엔드 활용](#pyarrow-백엔드-활용)
    - [고급 문자열 처리](#고급-문자열-처리)
    - [시계열 데이터 고급 처리](#시계열-데이터-고급-처리)
    - [성능 최적화 기법](#성능-최적화-기법)
      - [메모리 최적화](#메모리-최적화)
      - [벡터화 연산 활용](#벡터화-연산-활용)
      - [eval과 query를 이용한 성능 향상](#eval과-query를-이용한-성능-향상)
  - [🎯 실전 프로젝트: 종합 데이터 분석](#-실전-프로젝트-종합-데이터-분석)
  - [📝 마무리 및 추가 학습 가이드](#-마무리-및-추가-학습-가이드)
    - [핵심 포인트 정리](#핵심-포인트-정리)
    - [다음 단계 학습 추천](#다음-단계-학습-추천)
    - [실무 팁](#실무-팁)
  - [📊 Plotly를 활용한 데이터 시각화](#-plotly를-활용한-데이터-시각화)
    - [Plotly 설치 및 기본 설정](#plotly-설치-및-기본-설정)
    - [기본 차트 생성](#기본-차트-생성)
    - [판매 데이터 시각화](#판매-데이터-시각화)
    - [주식 데이터 시각화](#주식-데이터-시각화)
    - [센서 데이터 시각화](#센서-데이터-시각화)
    - [고객 분석 시각화](#고객-분석-시각화)
    - [대시보드 스타일 종합 차트](#대시보드-스타일-종합-차트)
    - [인터랙티브 기능 활용](#인터랙티브-기능-활용)
    - [Plotly 차트 저장하기](#plotly-차트-저장하기)
    - [📊 시각화 팁](#-시각화-팁)

---

## 기본편

### Pandas 소개 및 설치

Pandas는 Python에서 가장 강력한 데이터 분석 라이브러리입니다. 구조화된 데이터를 효율적으로 처리하고 분석할 수 있는 도구를 제공합니다.

#### 설치 및 임포트

```python
# 설치 (터미널에서)
# pip install pandas numpy

# 기본 임포트
import pandas as pd
import numpy as np

# 버전 확인
print(f"Pandas 버전: {pd.__version__}")
print(f"NumPy 버전: {np.__version__}")
```

### Series와 DataFrame 기초

#### Series 생성과 기본 조작

Series는 pandas의 1차원 데이터 구조입니다. 인덱스가 있는 배열이라고 생각하면 됩니다.

```python
# 다양한 방법으로 Series 생성
# 1. 리스트로부터 생성
s1 = pd.Series([1, 3, 5, 7, 9])
print("기본 Series:")
print(s1)

# 2. 인덱스를 지정하여 생성
s2 = pd.Series([10, 20, 30, 40, 50], 
               index=['a', 'b', 'c', 'd', 'e'])
print("\n인덱스가 있는 Series:")
print(s2)

# 3. 딕셔너리로부터 생성
data_dict = {'서울': 9776000, '부산': 3419000, '대구': 2438000}
s3 = pd.Series(data_dict)
print("\n딕셔너리로부터 생성한 Series:")
print(s3)
```

#### Series의 기본 속성과 메서드

```python
# Series의 기본 정보
print(f"데이터 타입: {s3.dtype}")
print(f"인덱스: {s3.index}")
print(f"값들: {s3.values}")
print(f"크기: {s3.size}")
print(f"모양: {s3.shape}")

# 기본 통계 정보
print(f"\n기본 통계:")
print(f"평균: {s3.mean():,.0f}")
print(f"최댓값: {s3.max():,.0f}")
print(f"최솟값: {s3.min():,.0f}")
```

#### DataFrame 생성과 기본 조작

DataFrame은 pandas의 2차원 데이터 구조로, 여러 개의 Series가 결합된 형태입니다.

```python
# 실제 데이터셋 불러오기
df = pd.read_csv('datasets/employees.csv')
print("직원 정보 DataFrame:")
print(df)

# 인덱스 설정
df_indexed = df.set_index('이름')
print("\n이름을 인덱스로 설정한 DataFrame:")
print(df_indexed.head())
```

#### DataFrame의 기본 정보 확인

```python
# DataFrame 기본 정보
print("DataFrame 정보:")
print(f"모양: {df.shape}")
print(f"컬럼: {list(df.columns)}")
print(f"인덱스: {list(df.index)}")
print(f"데이터 타입:\n{df.dtypes}")

# 처음 몇 행과 마지막 몇 행 확인
print("\n처음 3행:")
print(df.head(3))

print("\n마지막 2행:")
print(df.tail(2))

# 기본 통계 정보
print("\n기본 통계 정보:")
print(df.describe())
```

### 데이터 읽기/쓰기

#### CSV 파일 다루기

```python
# 제품 데이터 읽기
df_products = pd.read_csv('datasets/products.csv')
print("제품 데이터:")
print(df_products.head())

# 다양한 읽기 옵션
df_custom = pd.read_csv('datasets/products.csv', 
                       usecols=['product_name', 'category', 'price'],  # 특정 컬럼만
                       nrows=10)  # 처음 10행만
print("\n커스텀 읽기:")
print(df_custom)

# 도시 데이터도 읽어보기
df_cities = pd.read_csv('datasets/cities.csv')
print("\n도시 데이터:")
print(df_cities)
```

#### Excel 파일 다루기

```python
# Excel 파일로 저장
df.to_excel('datasets/employee_data.xlsx', index=False, sheet_name='직원정보')

# Excel 파일 읽기
try:
    df_from_excel = pd.read_excel('datasets/employee_data.xlsx', sheet_name='직원정보')
    print("Excel에서 읽은 데이터:")
    print(df_from_excel)
except ImportError:
    print("Excel 파일을 읽으려면 openpyxl 또는 xlrd 패키지가 필요합니다.")
    print("pip install openpyxl 로 설치하세요.")
```

### 기본 데이터 조작

#### 컬럼 선택과 추가

```python
# 단일 컬럼 선택 (Series 반환)
names = df['이름']
print("이름 컬럼:")
print(names)
print(f"타입: {type(names)}")

# 여러 컬럼 선택 (DataFrame 반환)
subset = df[['이름', '연봉']]
print("\n이름과 연봉:")
print(subset)
print(f"타입: {type(subset)}")

# 새 컬럼 추가
df['연봉_만원'] = df['연봉'] / 10000
df['고연봉자'] = df['연봉'] > 4000

print("\n새 컬럼이 추가된 DataFrame:")
print(df)
```

#### 행 선택과 필터링

```python
# 조건을 이용한 필터링
high_salary = df[df['연봉'] > 4000]
print("연봉 4000만원 이상인 직원:")
print(high_salary)

# 여러 조건 조합
seoul_high_salary = df[(df['도시'] == '서울') & (df['연봉'] > 3000)]
print("\n서울에 거주하고 연봉이 3000만원 이상인 직원:")
print(seoul_high_salary)

# isin() 메서드 사용
major_cities = df[df['도시'].isin(['서울', '부산', '대구'])]
print("\n주요 도시 거주자:")
print(major_cities)
```

#### 정렬

```python
# 단일 컬럼으로 정렬
df_sorted_age = df.sort_values('나이')
print("나이순 정렬:")
print(df_sorted_age)

# 여러 컬럼으로 정렬
df_sorted_multi = df.sort_values(['도시', '연봉'], ascending=[True, False])
print("\n도시별, 연봉 내림차순 정렬:")
print(df_sorted_multi)

# 인덱스로 정렬
df_sorted_index = df.sort_index()
print("\n인덱스 정렬:")
print(df_sorted_index)
```

---

## 중급편

### 고급 인덱싱과 선택

#### .loc와 .iloc 활용

```python
# 판매 데이터 불러오기 (중급편 데이터셋)
df_sales = pd.read_csv('datasets/sales_data.csv')
df_sales['date'] = pd.to_datetime(df_sales['date'])
df_sales = df_sales.set_index('date')

print("판매 데이터 (고급 인덱싱 예제):")
print(df_sales.head())

# .loc 사용 (라벨 기반)
print("\n.loc 사용 예제:")
print("특정 날짜의 데이터:")
print(df_sales.loc['2024-01-01'])

print("\n날짜 범위와 특정 컬럼:")
print(df_sales.loc['2024-01-01':'2024-01-05', ['region', 'product', 'total_amount']])

# .iloc 사용 (위치 기반)
print("\n.iloc 사용 예제:")
print("처음 5행, 처음 3컬럼:")
print(df_sales.iloc[:5, :3])

print("\n특정 위치의 값들:")
print(df_sales.iloc[[0, 2, 4], [1, 3, 5]])
```

#### 조건부 선택과 query 메서드

```python
# 복잡한 조건 필터링
condition = (df_sales['quantity'] > 10) & (df_sales['total_amount'] > 50000) & (df_sales['region'] == '서울')
filtered_df = df_sales[condition]
print("복잡한 조건 필터링 결과 (서울, 수량>10, 금액>50000):")
print(filtered_df.head())

# query 메서드 사용 (더 읽기 쉬운 방법)
query_result = df_sales.query('quantity > 10 and total_amount > 50000 and region == "서울"')
print("\nquery 메서드 사용 결과:")
print(query_result.head())

# 변수를 사용한 query
min_quantity = 15
min_amount = 100000
query_with_vars = df_sales.query('quantity > @min_quantity and total_amount > @min_amount')
print(f"\n변수를 사용한 query (수량 > {min_quantity}, 금액 > {min_amount}):")
print(query_with_vars.head())
```

### 데이터 정제와 변환

#### 결측값 처리

```python
# 결측값이 포함된 판매 데이터 사용
df_missing = df_sales.copy()

print("결측값 정보:")
print(df_missing.isnull().sum())

# 결측값 확인
print("\n결측값이 있는 행:")
print(df_missing[df_missing.isnull().any(axis=1)].head())

# 결측값 처리 방법들
# 1. 결측값 제거
df_dropped = df_missing.dropna()
print(f"\n결측값 제거 후 크기: {df_dropped.shape}")

# 2. 특정 컬럼의 결측값만 제거
df_dropped_subset = df_missing.dropna(subset=['salesperson'])
print(f"salesperson 컬럼 결측값만 제거 후 크기: {df_dropped_subset.shape}")

# 3. 결측값 채우기
df_filled = df_missing.fillna({
    'salesperson': '미지정',  # 문자열로 채우기
    'unit_price': df_missing['unit_price'].median(),  # 중앙값으로 채우기
    'customer_type': '일반'  # 기본값으로 채우기
})
print("\n결측값을 채운 후:")
print(df_filled.isnull().sum())

# 4. 전진/후진 채우기
df_ffill = df_missing.fillna(method='ffill')  # 앞의 값으로 채우기
df_bfill = df_missing.fillna(method='bfill')  # 뒤의 값으로 채우기
```

#### 데이터 타입 변환

```python
# 데이터 타입 확인
print("현재 데이터 타입:")
print(df_advanced.dtypes)

# 데이터 타입 변환
df_converted = df_advanced.copy()
df_converted['C'] = df_converted['C'].astype('float64')
df_converted['D'] = df_converted['D'].astype('category')

print("\n변환 후 데이터 타입:")
print(df_converted.dtypes)

# 카테고리 데이터의 장점
print(f"\n메모리 사용량 비교:")
print(f"원본 D 컬럼: {df_advanced['D'].memory_usage(deep=True)} bytes")
print(f"카테고리 D 컬럼: {df_converted['D'].memory_usage(deep=True)} bytes")
```

#### apply와 map 함수 활용

```python
# apply 함수 사용
def categorize_value(x):
    if x > 1:
        return 'High'
    elif x > 0:
        return 'Medium'
    else:
        return 'Low'

df_advanced['A_category'] = df_advanced['A'].apply(categorize_value)
print("apply 함수 적용 결과:")
print(df_advanced[['A', 'A_category']].head())

# lambda 함수와 함께 사용
df_advanced['B_squared'] = df_advanced['B'].apply(lambda x: x**2)
print("\nlambda 함수 적용 결과:")
print(df_advanced[['B', 'B_squared']].head())

# DataFrame 전체에 apply 적용
numeric_cols = ['A', 'B', 'C']
df_normalized = df_advanced[numeric_cols].apply(lambda x: (x - x.mean()) / x.std())
print("\n정규화된 데이터:")
print(df_normalized.head())
```

### 그룹화와 집계

#### 기본 그룹화

```python
# 실제 판매 데이터 사용
print("판매 데이터:")
print(df_sales.head(10))

# 기본 그룹화
region_group = df_sales.groupby('region')
print("\n지역별 평균 판매량:")
print(region_group['quantity'].mean())

print("\n지역별 총 매출:")
print(region_group['total_amount'].sum())

# 제품별 그룹화
product_group = df_sales.groupby('product')
print("\n제품별 평균 단가:")
print(product_group['unit_price'].mean())
```

#### 다중 그룹화와 집계

```python
# 다중 그룹화
multi_group = df_sales.groupby(['region', 'product'])
print("지역별, 제품별 집계:")
print(multi_group.agg({
    'quantity': ['sum', 'mean'],
    'total_amount': ['sum', 'max', 'min']
}))

# 사용자 정의 집계 함수
def amount_range(x):
    return x.max() - x.min()

custom_agg = df_sales.groupby('region').agg({
    'quantity': ['mean', 'std'],
    'total_amount': ['sum', 'count', amount_range]
})
print("\n사용자 정의 집계:")
print(custom_agg)
```

#### transform과 filter 활용

```python
# transform: 그룹별 변환
sales_data['지역별_평균_판매량'] = sales_data.groupby('지역')['판매량'].transform('mean')
sales_data['평균대비_비율'] = sales_data['판매량'] / sales_data['지역별_평균_판매량']

print("transform 결과:")
print(sales_data[['지역', '판매량', '지역별_평균_판매량', '평균대비_비율']].head())

# filter: 조건에 맞는 그룹만 선택
high_sales_groups = sales_data.groupby('지역').filter(lambda x: x['매출'].sum() > 50000)
print(f"\n고매출 지역 데이터 수: {len(high_sales_groups)}")
print("고매출 지역:")
print(high_sales_groups.groupby('지역')['매출'].sum())
```

### 데이터 병합과 결합

#### merge 함수 활용

```python
# 실제 데이터셋 사용
customers = pd.read_csv('datasets/customers.csv')
orders = pd.read_csv('datasets/orders.csv')

print("고객 데이터:")
print(customers.head())
print("\n주문 데이터:")
print(orders.head())

# Inner Join (기본)
inner_merged = pd.merge(customers, orders, on='customer_id')
print("\nInner Join 결과:")
print(inner_merged)

# Left Join
left_merged = pd.merge(customers, orders, on='customer_id', how='left')
print("\nLeft Join 결과:")
print(left_merged)

# Right Join
right_merged = pd.merge(customers, orders, on='customer_id', how='right')
print("\nRight Join 결과:")
print(right_merged)

# Outer Join
outer_merged = pd.merge(customers, orders, on='customer_id', how='outer')
print("\nOuter Join 결과:")
print(outer_merged)
```

#### concat 함수 활용

```python
# concat 예제 데이터
df1 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

df2 = pd.DataFrame({
    'A': [7, 8, 9],
    'B': [10, 11, 12]
})

df3 = pd.DataFrame({
    'C': [13, 14, 15],
    'D': [16, 17, 18]
})

# 세로 연결
vertical_concat = pd.concat([df1, df2], ignore_index=True)
print("세로 연결:")
print(vertical_concat)

# 가로 연결
horizontal_concat = pd.concat([df1, df3], axis=1)
print("\n가로 연결:")
print(horizontal_concat)

# 키를 사용한 연결
keyed_concat = pd.concat([df1, df2], keys=['first', 'second'])
print("\n키를 사용한 연결:")
print(keyed_concat)
```

---

## 최신기능편

### PyArrow 백엔드 활용

PyArrow는 pandas의 성능을 크게 향상시키는 최신 백엔드입니다.

```python
# PyArrow 설치 확인 및 사용
try:
    import pyarrow as pa
    print(f"PyArrow 버전: {pa.__version__}")
    
    # PyArrow 백엔드 Series 생성
    arrow_series = pd.Series([-1.545, 0.211, None], dtype="float32[pyarrow]")
    print("PyArrow 백엔드 Series:")
    print(arrow_series)
    print(f"데이터 타입: {arrow_series.dtype}")
    
    # 성능 향상된 연산
    print(f"\n평균: {arrow_series.mean()}")
    print(f"합계: {arrow_series + arrow_series}")
    print(f"비교: {arrow_series > (arrow_series + 1)}")
    
    # 결측값 처리
    print(f"\n결측값 제거: {arrow_series.dropna()}")
    print(f"결측값 확인: {arrow_series.isna()}")
    print(f"결측값 채우기: {arrow_series.fillna(0)}")
    
    # 문자열 PyArrow 타입
    arrow_string_series = pd.Series(["a", "b", None], dtype=pd.ArrowDtype(pa.string()))
    print(f"\nPyArrow 문자열 Series:")
    print(arrow_string_series)
    print(f"'a'로 시작하는지 확인: {arrow_string_series.str.startswith('a')}")
    
except ImportError:
    print("PyArrow가 설치되지 않았습니다. pip install pyarrow로 설치하세요.")
```

### 고급 문자열 처리

```python
# 고객 데이터를 사용한 문자열 처리
text_data = customers[['name', 'email', 'phone', 'city']].head(10)

print("문자열 데이터:")
print(text_data)

# 문자열 메서드 체이닝
text_data['name_upper'] = text_data['name'].str.upper()
text_data['email_domain'] = text_data['email'].str.split('@').str[1]
text_data['phone_cleaned'] = text_data['phone'].str.replace('-', '')

print("\n문자열 처리 결과:")
print(text_data[['name', 'name_upper', 'email', 'email_domain', 'phone', 'phone_cleaned']])

# 정규표현식 사용
text_data['area_code'] = text_data['phone'].str.extract(r'(\d{3})-\d{4}-\d{4}')
text_data['city_suffix'] = text_data['city'].str.extract(r'(\w+)시')

print("\n정규표현식 추출 결과:")
print(text_data[['phone', 'area_code', 'city', 'city_suffix']])

# 문자열 조건 필터링
gmail_users = text_data[text_data['email'].str.contains('gmail')]
print("\nGmail 사용자:")
print(gmail_users[['name', 'email']])

# 문자열 길이와 통계
text_data['name_length'] = text_data['name'].str.len()
print(f"\n이름 길이 통계:")
print(text_data['name_length'].describe())
```

### 시계열 데이터 고급 처리

```python
# 주식 데이터 불러오기
stock_data = pd.read_csv('datasets/stock_data.csv')
stock_data['date'] = pd.to_datetime(stock_data['date'])

# 특정 종목 선택 (AAPL)
ts_data = stock_data[stock_data['symbol'] == 'AAPL'].copy()
ts_data.set_index('date', inplace=True)

print("시계열 데이터 (AAPL 주식):")
print(ts_data.head())

# 날짜/시간 속성 추출
ts_data['year'] = ts_data.index.year
ts_data['month'] = ts_data.index.month
ts_data['day_of_week'] = ts_data.index.dayofweek
ts_data['quarter'] = ts_data.index.quarter

print("\n날짜 속성 추출:")
print(ts_data[['close', 'year', 'month', 'day_of_week', 'quarter']].head())

# 리샘플링
monthly_stock = ts_data['close'].resample('M').agg({
    'open': 'first',
    'high': 'max',
    'low': 'min',
    'close': 'last'
})
print("\n월별 주가 집계:")
print(monthly_stock.head())

# 이동 평균
ts_data['close_ma_7'] = ts_data['close'].rolling(window=7).mean()
ts_data['close_ma_30'] = ts_data['close'].rolling(window=30).mean()

print("\n이동 평균:")
print(ts_data[['close', 'close_ma_7', 'close_ma_30']].head(10))

# 시차 변수 생성
ts_data['close_lag_1'] = ts_data['close'].shift(1)
ts_data['close_lag_7'] = ts_data['close'].shift(7)
ts_data['close_diff'] = ts_data['close'].diff()
ts_data['returns'] = ts_data['close'].pct_change()

print("\n시차 변수와 수익률:")
print(ts_data[['close', 'close_lag_1', 'close_diff', 'returns']].head(10))
```

### 성능 최적화 기법

#### 메모리 최적화

```python
# 메모리 사용량 확인
def memory_usage(df):
    return df.memory_usage(deep=True).sum() / 1024**2  # MB 단위

# 대용량 데이터셋 불러오기
large_data = pd.read_csv('datasets/large_dataset.csv')

print(f"원본 데이터 메모리 사용량: {memory_usage(large_data):.2f} MB")
print("원본 데이터 타입:")
print(large_data.dtypes)
print(f"데이터 크기: {large_data.shape}")

# 메모리 최적화
optimized_data = large_data.copy()
optimized_data['id'] = optimized_data['id'].astype('int32')  # int64 -> int32
optimized_data['category'] = optimized_data['category'].astype('category')  # object -> category
optimized_data['subcategory'] = optimized_data['subcategory'].astype('category')  # object -> category
optimized_data['value1'] = optimized_data['value1'].astype('float32')  # float64 -> float32
optimized_data['value2'] = optimized_data['value2'].astype('float32')  # float64 -> float32
optimized_data['value3'] = optimized_data['value3'].astype('int16')  # int64 -> int16

print(f"\n최적화된 데이터 메모리 사용량: {memory_usage(optimized_data):.2f} MB")
print("최적화된 데이터 타입:")
print(optimized_data.dtypes)

memory_reduction = (1 - memory_usage(optimized_data) / memory_usage(large_data)) * 100
print(f"메모리 사용량 감소: {memory_reduction:.1f}%")
```

#### 벡터화 연산 활용

```python
# 벡터화 vs 반복문 성능 비교
import time

# 테스트 데이터
test_data = pd.DataFrame({
    'A': np.random.randn(100000),
    'B': np.random.randn(100000)
})

# 반복문 방식 (비효율적)
start_time = time.time()
result_loop = []
for i in range(len(test_data)):
    if test_data.iloc[i]['A'] > 0:
        result_loop.append(test_data.iloc[i]['B'] * 2)
    else:
        result_loop.append(test_data.iloc[i]['B'])
loop_time = time.time() - start_time

# 벡터화 방식 (효율적)
start_time = time.time()
result_vectorized = np.where(test_data['A'] > 0, test_data['B'] * 2, test_data['B'])
vectorized_time = time.time() - start_time

print(f"반복문 방식 시간: {loop_time:.4f}초")
print(f"벡터화 방식 시간: {vectorized_time:.4f}초")
print(f"성능 향상: {loop_time/vectorized_time:.1f}배")
```

#### eval과 query를 이용한 성능 향상

```python
# eval과 query 성능 비교
large_df = pd.DataFrame({
    'A': np.random.randn(100000),
    'B': np.random.randn(100000),
    'C': np.random.randn(100000),
    'D': np.random.randn(100000)
})

# 일반적인 방법
start_time = time.time()
result_normal = large_df[(large_df['A'] > 0) & (large_df['B'] < 0.5)]
normal_time = time.time() - start_time

# query 사용
start_time = time.time()
result_query = large_df.query('A > 0 and B < 0.5')
query_time = time.time() - start_time

print(f"일반적인 방법 시간: {normal_time:.4f}초")
print(f"query 방법 시간: {query_time:.4f}초")

# eval 사용 (복잡한 계산)
start_time = time.time()
result_eval = large_df.eval('E = A + B * C - D')
eval_time = time.time() - start_time

start_time = time.time()
large_df['E_normal'] = large_df['A'] + large_df['B'] * large_df['C'] - large_df['D']
normal_calc_time = time.time() - start_time

print(f"eval 계산 시간: {eval_time:.4f}초")
print(f"일반 계산 시간: {normal_calc_time:.4f}초")
```

## 🎯 실전 프로젝트: 종합 데이터 분석

마지막으로 배운 내용을 종합하여 실전 프로젝트를 진행해보겠습니다.

```python
# 종합 실습: 전자상거래 데이터 분석
# 실제 생성된 데이터셋들을 활용

# 데이터 불러오기
customers = pd.read_csv('datasets/customers.csv')
products = pd.read_csv('datasets/products.csv')
orders = pd.read_csv('datasets/orders.csv')

# 데이터 전처리
orders['order_date'] = pd.to_datetime(orders['order_date'])
products['launch_date'] = pd.to_datetime(products['launch_date'])
customers['join_date'] = pd.to_datetime(customers['join_date'])

# 데이터 병합
full_data = orders.merge(customers, on='customer_id').merge(products, on='product_id')
full_data['total_amount'] = full_data['price'] * full_data['quantity']

print("종합 데이터 샘플:")
print(full_data.head())
print(f"\n전체 데이터 크기: {full_data.shape}")
print(f"분석 기간: {full_data['order_date'].min()} ~ {full_data['order_date'].max()}")

# 1. 월별 매출 분석
full_data['order_month'] = full_data['order_date'].dt.to_period('M')
monthly_sales = full_data.groupby('order_month')['total_amount'].agg(['sum', 'count', 'mean'])
monthly_sales.columns = ['총매출', '주문수', '평균주문금액']

print("\n월별 매출 분석:")
print(monthly_sales.head())

# 2. 카테고리별 성과 분석
category_analysis = full_data.groupby('category').agg({
    'total_amount': ['sum', 'mean'],
    'quantity': 'sum',
    'customer_id': 'nunique'
}).round(2)

category_analysis.columns = ['총매출', '평균주문금액', '총판매량', '고객수']
category_analysis['고객당_평균매출'] = (category_analysis['총매출'] / category_analysis['고객수']).round(2)

print("\n카테고리별 성과 분석:")
print(category_analysis)

# 3. 고객 세그멘테이션
customer_metrics = full_data.groupby('customer_id').agg({
    'total_amount': ['sum', 'count', 'mean'],
    'order_date': ['min', 'max']
}).round(2)

customer_metrics.columns = ['총구매금액', '주문횟수', '평균주문금액', '첫구매일', '마지막구매일']
customer_metrics['구매기간'] = (customer_metrics['마지막구매일'] - customer_metrics['첫구매일']).dt.days

# RFM 분석을 위한 지표 계산
reference_date = full_data['order_date'].max()
customer_metrics['최근구매일수'] = (reference_date - customer_metrics['마지막구매일']).dt.days

# 고객 등급 분류
def classify_customer(row):
    if row['총구매금액'] > customer_metrics['총구매금액'].quantile(0.8):
        return 'VIP'
    elif row['총구매금액'] > customer_metrics['총구매금액'].quantile(0.6):
        return '우수'
    elif row['총구매금액'] > customer_metrics['총구매금액'].quantile(0.4):
        return '일반'
    else:
        return '신규'

customer_metrics['고객등급'] = customer_metrics.apply(classify_customer, axis=1)

print("\n고객 등급별 분포:")
print(customer_metrics['고객등급'].value_counts())

print("\n고객 등급별 평균 지표:")
grade_analysis = customer_metrics.groupby('고객등급').agg({
    '총구매금액': 'mean',
    '주문횟수': 'mean',
    '평균주문금액': 'mean',
    '최근구매일수': 'mean'
}).round(2)
print(grade_analysis)

# 4. 지역별 분석
region_analysis = full_data.groupby('city').agg({
    'total_amount': 'sum',
    'customer_id': 'nunique',
    'order_id': 'count'
}).round(2)

region_analysis.columns = ['총매출', '고객수', '주문수']
region_analysis['고객당_매출'] = (region_analysis['총매출'] / region_analysis['고객수']).round(2)
region_analysis['고객당_주문수'] = (region_analysis['주문수'] / region_analysis['고객수']).round(2)

print("\n지역별 분석:")
print(region_analysis.sort_values('총매출', ascending=False))

print("\n🎉 분석 완료! 이제 여러분은 pandas 중고급 사용자입니다!")
```

## 📝 마무리 및 추가 학습 가이드

### 핵심 포인트 정리

1. **기본편에서 배운 것들:**
   - Series와 DataFrame의 기본 구조와 조작
   - 데이터 읽기/쓰기의 다양한 방법
   - 기본적인 데이터 선택과 필터링

2. **중급편에서 배운 것들:**
   - .loc와 .iloc을 이용한 고급 인덱싱
   - 결측값 처리와 데이터 타입 변환
   - groupby를 이용한 강력한 집계 기능
   - merge와 concat을 이용한 데이터 결합

3. **최신기능편에서 배운 것들:**
   - PyArrow 백엔드를 통한 성능 향상
   - 고급 문자열 처리 기법
   - 시계열 데이터의 전문적 처리
   - 메모리 최적화와 성능 향상 기법

### 다음 단계 학습 추천

1. **시각화**: plotly와 pandas 연동 (아래 시각화 섹션 참고)
2. **머신러닝**: scikit-learn과 pandas 연동
3. **대용량 데이터**: Dask, Polars 등 대안 라이브러리
4. **웹 개발**: Streamlit, Dash를 이용한 대시보드 구축

### 실무 팁

- 항상 데이터의 크기와 메모리 사용량을 확인하세요
- 복잡한 연산은 작은 샘플로 먼저 테스트하세요
- 코드의 가독성을 위해 메서드 체이닝을 적절히 활용하세요
- 성능이 중요한 경우 벡터화 연산을 우선 고려하세요

---

## 📊 Plotly를 활용한 데이터 시각화

pandas와 plotly를 연동하여 인터랙티브한 시각화를 만들어보겠습니다.

### Plotly 설치 및 기본 설정

```python
# Plotly 설치 (터미널에서)
# pip install plotly

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.offline as pyo

# Jupyter Notebook에서 사용할 경우
pyo.init_notebook_mode(connected=True)
```

### 기본 차트 생성

```python
# 직원 데이터로 기본 차트 만들기
df_employees = pd.read_csv('datasets/employees.csv')

# 1. 막대 차트 - 부서별 직원 수
dept_counts = df_employees['부서'].value_counts()

fig_bar = px.bar(
    x=dept_counts.index, 
    y=dept_counts.values,
    title='부서별 직원 수',
    labels={'x': '부서', 'y': '직원 수'},
    color=dept_counts.values,
    color_continuous_scale='viridis'
)
fig_bar.show()

# 2. 산점도 - 나이와 연봉의 관계
fig_scatter = px.scatter(
    df_employees, 
    x='나이', 
    y='연봉',
    color='부서',
    size='연봉',
    hover_data=['이름'],
    title='나이와 연봉의 관계'
)
fig_scatter.show()

# 3. 박스 플롯 - 부서별 연봉 분포
fig_box = px.box(
    df_employees, 
    x='부서', 
    y='연봉',
    title='부서별 연봉 분포',
    color='부서'
)
fig_box.show()
```

### 판매 데이터 시각화

```python
# 판매 데이터 불러오기
df_sales = pd.read_csv('datasets/sales_data.csv')
df_sales['date'] = pd.to_datetime(df_sales['date'])

# 1. 시계열 차트 - 일별 매출 추이
daily_sales = df_sales.groupby('date')['total_amount'].sum().reset_index()

fig_line = px.line(
    daily_sales, 
    x='date', 
    y='total_amount',
    title='일별 매출 추이',
    labels={'date': '날짜', 'total_amount': '매출액'}
)
fig_line.update_traces(line_color='#1f77b4', line_width=2)
fig_line.show()

# 2. 파이 차트 - 지역별 매출 비중
region_sales = df_sales.groupby('region')['total_amount'].sum()

fig_pie = px.pie(
    values=region_sales.values,
    names=region_sales.index,
    title='지역별 매출 비중'
)
fig_pie.show()

# 3. 히트맵 - 지역별, 제품별 매출
pivot_data = df_sales.pivot_table(
    values='total_amount', 
    index='region', 
    columns='product', 
    aggfunc='sum'
).fillna(0)

fig_heatmap = px.imshow(
    pivot_data.values,
    x=pivot_data.columns,
    y=pivot_data.index,
    title='지역별, 제품별 매출 히트맵',
    color_continuous_scale='RdYlBu_r'
)
fig_heatmap.show()
```

### 주식 데이터 시각화

```python
# 주식 데이터 불러오기
df_stocks = pd.read_csv('datasets/stock_data.csv')
df_stocks['date'] = pd.to_datetime(df_stocks['date'])

# 1. 캔들스틱 차트 - AAPL 주가
aapl_data = df_stocks[df_stocks['symbol'] == 'AAPL'].head(100)

fig_candlestick = go.Figure(data=go.Candlestick(
    x=aapl_data['date'],
    open=aapl_data['open'],
    high=aapl_data['high'],
    low=aapl_data['low'],
    close=aapl_data['close']
))

fig_candlestick.update_layout(
    title='AAPL 주가 캔들스틱 차트',
    xaxis_title='날짜',
    yaxis_title='주가 ($)'
)
fig_candlestick.show()

# 2. 다중 선 차트 - 여러 종목 비교
fig_multi = px.line(
    df_stocks, 
    x='date', 
    y='close', 
    color='symbol',
    title='주요 종목 주가 비교'
)
fig_multi.show()

# 3. 서브플롯 - 주가와 거래량
fig_subplots = make_subplots(
    rows=2, cols=1,
    subplot_titles=('주가', '거래량'),
    vertical_spacing=0.1
)

# 주가 차트
for symbol in df_stocks['symbol'].unique():
    symbol_data = df_stocks[df_stocks['symbol'] == symbol]
    fig_subplots.add_trace(
        go.Scatter(x=symbol_data['date'], y=symbol_data['close'], 
                  name=f'{symbol} 주가', line=dict(width=2)),
        row=1, col=1
    )

# 거래량 차트
for symbol in df_stocks['symbol'].unique():
    symbol_data = df_stocks[df_stocks['symbol'] == symbol]
    fig_subplots.add_trace(
        go.Scatter(x=symbol_data['date'], y=symbol_data['volume'], 
                  name=f'{symbol} 거래량', line=dict(width=1)),
        row=2, col=1
    )

fig_subplots.update_layout(height=600, title_text="주가 및 거래량 분석")
fig_subplots.show()
```

### 센서 데이터 시각화

```python
# 센서 데이터 불러오기
df_sensors = pd.read_csv('datasets/sensor_data.csv')
df_sensors['timestamp'] = pd.to_datetime(df_sensors['timestamp'])

# 1. 시계열 다중 변수 차트
fig_sensors = make_subplots(
    rows=3, cols=1,
    subplot_titles=('온도', '습도', '기압'),
    vertical_spacing=0.08
)

# 온도
fig_sensors.add_trace(
    go.Scatter(x=df_sensors['timestamp'][:1000], y=df_sensors['temperature'][:1000],
              name='온도', line=dict(color='red')),
    row=1, col=1
)

# 습도
fig_sensors.add_trace(
    go.Scatter(x=df_sensors['timestamp'][:1000], y=df_sensors['humidity'][:1000],
              name='습도', line=dict(color='blue')),
    row=2, col=1
)

# 기압
fig_sensors.add_trace(
    go.Scatter(x=df_sensors['timestamp'][:1000], y=df_sensors['pressure'][:1000],
              name='기압', line=dict(color='green')),
    row=3, col=1
)

fig_sensors.update_layout(height=800, title_text="센서 데이터 모니터링")
fig_sensors.show()

# 2. 3D 산점도 - 온도, 습도, 기압 관계
fig_3d = px.scatter_3d(
    df_sensors.sample(1000), 
    x='temperature', 
    y='humidity', 
    z='pressure',
    color='location',
    title='온도-습도-기압 3D 관계도'
)
fig_3d.show()
```

### 고객 분석 시각화

```python
# 고객 데이터 불러오기
df_customers = pd.read_csv('datasets/customers.csv')

# 1. 히스토그램 - 나이 분포
fig_hist = px.histogram(
    df_customers, 
    x='age', 
    nbins=20,
    title='고객 나이 분포',
    color_discrete_sequence=['skyblue']
)
fig_hist.show()

# 2. 바이올린 플롯 - 멤버십 레벨별 총 구매액
fig_violin = px.violin(
    df_customers, 
    x='membership_level', 
    y='total_spent',
    title='멤버십 레벨별 총 구매액 분포',
    box=True
)
fig_violin.show()

# 3. 선버스트 차트 - 도시별, 성별, 멤버십 레벨 분포
fig_sunburst = px.sunburst(
    df_customers, 
    path=['city', 'gender', 'membership_level'],
    title='고객 세그먼트 분포'
)
fig_sunburst.show()
```

### 대시보드 스타일 종합 차트

```python
# 종합 대시보드 만들기
fig_dashboard = make_subplots(
    rows=2, cols=2,
    subplot_titles=('월별 매출', '지역별 매출', '제품별 판매량', '고객 연령 분포'),
    specs=[[{"type": "scatter"}, {"type": "bar"}],
           [{"type": "bar"}, {"type": "histogram"}]]
)

# 월별 매출
monthly_sales = df_sales.groupby(df_sales['date'].dt.to_period('M'))['total_amount'].sum()
fig_dashboard.add_trace(
    go.Scatter(x=monthly_sales.index.astype(str), y=monthly_sales.values,
              mode='lines+markers', name='월별 매출'),
    row=1, col=1
)

# 지역별 매출
region_sales = df_sales.groupby('region')['total_amount'].sum()
fig_dashboard.add_trace(
    go.Bar(x=region_sales.index, y=region_sales.values, name='지역별 매출'),
    row=1, col=2
)

# 제품별 판매량
product_qty = df_sales.groupby('product')['quantity'].sum()
fig_dashboard.add_trace(
    go.Bar(x=product_qty.index, y=product_qty.values, name='제품별 판매량'),
    row=2, col=1
)

# 고객 연령 분포
fig_dashboard.add_trace(
    go.Histogram(x=df_customers['age'], name='고객 연령'),
    row=2, col=2
)

fig_dashboard.update_layout(
    height=800, 
    title_text="비즈니스 인사이트 대시보드",
    showlegend=False
)
fig_dashboard.show()
```

### 인터랙티브 기능 활용

```python
# 드롭다운 메뉴가 있는 인터랙티브 차트
fig_interactive = go.Figure()

# 각 지역별 데이터 추가
for region in df_sales['region'].unique():
    region_data = df_sales[df_sales['region'] == region]
    daily_data = region_data.groupby('date')['total_amount'].sum()
    
    fig_interactive.add_trace(
        go.Scatter(
            x=daily_data.index,
            y=daily_data.values,
            name=region,
            visible=True if region == '서울' else False
        )
    )

# 드롭다운 메뉴 생성
dropdown_buttons = []
for i, region in enumerate(df_sales['region'].unique()):
    visibility = [False] * len(df_sales['region'].unique())
    visibility[i] = True
    
    dropdown_buttons.append(
        dict(
            label=region,
            method="update",
            args=[{"visible": visibility}]
        )
    )

fig_interactive.update_layout(
    title="지역별 매출 추이 (인터랙티브)",
    updatemenus=[
        dict(
            buttons=dropdown_buttons,
            direction="down",
            showactive=True,
            x=0.1,
            y=1.15
        )
    ]
)
fig_interactive.show()
```

### Plotly 차트 저장하기

```python
# 차트를 HTML 파일로 저장
fig_bar.write_html("부서별_직원수.html")

# 차트를 이미지로 저장 (kaleido 패키지 필요)
# pip install kaleido
try:
    fig_scatter.write_image("나이_연봉_관계.png", width=800, height=600)
    fig_pie.write_image("지역별_매출비중.pdf", width=800, height=600)
    print("차트가 성공적으로 저장되었습니다!")
except Exception as e:
    print(f"이미지 저장을 위해 kaleido 패키지를 설치하세요: pip install kaleido")
    print(f"오류: {e}")
```

### 📊 시각화 팁

1. **색상 선택**: `color_discrete_sequence`나 `color_continuous_scale`로 브랜드 컬러 적용
2. **인터랙티브 기능**: 줌, 팬, 호버 등 기본 제공되는 인터랙티브 기능 활용
3. **반응형 디자인**: `fig.update_layout(autosize=True)`로 반응형 차트 생성
4. **애니메이션**: `animation_frame` 매개변수로 시간에 따른 변화 시각화
5. **테마 적용**: `template` 매개변수로 일관된 디자인 적용

이제 여러분은 pandas와 plotly를 연동하여 인터랙티브하고 아름다운 시각화를 만들 수 있습니다! 📈✨

---

이제 여러분은 pandas를 활용하여 실무에서 마주치는 대부분의 데이터 분석 작업을 수행할 수 있습니다. 계속해서 실제 데이터로 연습하며 실력을 향상시켜 나가세요! 🚀
