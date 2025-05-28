"""
Dataclass & Pydantic 데이터 시각화 예제
Plotly를 사용한 인터랙티브 차트 생성
"""

from dataclasses import dataclass, asdict
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime, date
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import random

print("=" * 60)
print("Dataclass & Pydantic 데이터 시각화 실습")
print("=" * 60)

# 1. 판매 데이터 모델 정의
@dataclass
class SalesRecord:
    """판매 기록 (Dataclass)"""
    date: date
    product: str
    quantity: int
    revenue: float
    region: str
    salesperson: str

class ProductInfo(BaseModel):
    """제품 정보 (Pydantic)"""
    id: int = Field(gt=0, description="제품 ID")
    name: str = Field(min_length=1, description="제품명")
    category: str = Field(description="카테고리")
    price: float = Field(gt=0, description="가격")
    cost: float = Field(gt=0, description="원가")
    
    @property
    def profit_margin(self) -> float:
        return ((self.price - self.cost) / self.price) * 100

# 2. 샘플 데이터 생성
print("\n1. 샘플 데이터 생성")
print("-" * 40)

# 제품 정보 생성
products = [
    ProductInfo(id=1, name="노트북", category="전자제품", price=1500000, cost=1200000),
    ProductInfo(id=2, name="마우스", category="전자제품", price=25000, cost=15000),
    ProductInfo(id=3, name="키보드", category="전자제품", price=80000, cost=50000),
    ProductInfo(id=4, name="모니터", category="전자제품", price=300000, cost=200000),
    ProductInfo(id=5, name="책상", category="가구", price=200000, cost=120000),
    ProductInfo(id=6, name="의자", category="가구", price=150000, cost=90000),
]

# 판매 기록 생성
sales_data = []
regions = ["서울", "부산", "대구", "인천", "광주"]
salespeople = ["김영업", "이판매", "박마케팅", "최세일즈", "정딜러"]

for i in range(100):
    product = random.choice(products)
    sales_data.append(SalesRecord(
        date=date(2024, random.randint(1, 12), random.randint(1, 28)),
        product=product.name,
        quantity=random.randint(1, 10),
        revenue=product.price * random.randint(1, 10),
        region=random.choice(regions),
        salesperson=random.choice(salespeople)
    ))

print(f"생성된 제품 수: {len(products)}")
print(f"생성된 판매 기록 수: {len(sales_data)}")

# 3. DataFrame 변환
print("\n2. DataFrame 변환")
print("-" * 40)

# Pydantic → DataFrame
products_df = pd.DataFrame([product.model_dump() for product in products])
products_df['profit_margin'] = [product.profit_margin for product in products]

# Dataclass → DataFrame
sales_df = pd.DataFrame([asdict(record) for record in sales_data])

print("제품 DataFrame:")
print(products_df.head())
print(f"\n판매 DataFrame 크기: {sales_df.shape}")

# 4. 시각화 생성
print("\n3. 인터랙티브 시각화 생성")
print("-" * 40)

# 4-1. 제품별 수익률 차트
fig1 = px.bar(
    products_df, 
    x='name', 
    y='profit_margin',
    color='category',
    title='제품별 수익률',
    labels={'profit_margin': '수익률 (%)', 'name': '제품명'},
    text='profit_margin'
)
fig1.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
fig1.update_layout(
    xaxis_tickangle=-45,
    height=500,
    showlegend=True
)

# 4-2. 지역별 매출 분석
region_sales = sales_df.groupby('region').agg({
    'revenue': 'sum',
    'quantity': 'sum'
}).reset_index()

fig2 = px.pie(
    region_sales,
    values='revenue',
    names='region',
    title='지역별 매출 분포',
    hover_data=['quantity']
)
fig2.update_traces(textposition='inside', textinfo='percent+label')

# 4-3. 월별 매출 트렌드
sales_df['month'] = pd.to_datetime(sales_df['date']).dt.month
monthly_sales = sales_df.groupby('month')['revenue'].sum().reset_index()

fig3 = px.line(
    monthly_sales,
    x='month',
    y='revenue',
    title='월별 매출 트렌드',
    markers=True,
    labels={'revenue': '매출 (원)', 'month': '월'}
)
fig3.update_traces(line=dict(width=3))
fig3.update_layout(
    xaxis=dict(tickmode='linear', tick0=1, dtick=1),
    height=400
)

# 4-4. 영업사원별 성과 분석
salesperson_performance = sales_df.groupby('salesperson').agg({
    'revenue': 'sum',
    'quantity': 'sum'
}).reset_index()

fig4 = px.scatter(
    salesperson_performance,
    x='quantity',
    y='revenue',
    size='revenue',
    color='salesperson',
    title='영업사원별 성과 (수량 vs 매출)',
    labels={'quantity': '판매 수량', 'revenue': '매출 (원)'},
    hover_name='salesperson'
)

# 4-5. 제품 카테고리별 상세 분석
category_analysis = sales_df.merge(
    products_df[['name', 'category']], 
    left_on='product', 
    right_on='name'
).groupby(['category', 'region']).agg({
    'revenue': 'sum',
    'quantity': 'sum'
}).reset_index()

fig5 = px.sunburst(
    category_analysis,
    path=['category', 'region'],
    values='revenue',
    title='카테고리별 지역 매출 분포'
)

# 4-6. 복합 대시보드
fig6 = make_subplots(
    rows=2, cols=2,
    subplot_titles=('제품별 가격', '카테고리별 매출', '월별 수량', '지역별 평균 매출'),
    specs=[[{"type": "bar"}, {"type": "pie"}],
           [{"type": "scatter"}, {"type": "bar"}]]
)

# 서브플롯 1: 제품별 가격
fig6.add_trace(
    go.Bar(x=products_df['name'], y=products_df['price'], name='가격'),
    row=1, col=1
)

# 서브플롯 2: 카테고리별 매출 (파이 차트)
category_revenue = sales_df.merge(
    products_df[['name', 'category']], 
    left_on='product', 
    right_on='name'
).groupby('category')['revenue'].sum()

fig6.add_trace(
    go.Pie(labels=category_revenue.index, values=category_revenue.values, name="카테고리"),
    row=1, col=2
)

# 서브플롯 3: 월별 수량
monthly_quantity = sales_df.groupby('month')['quantity'].sum()
fig6.add_trace(
    go.Scatter(x=monthly_quantity.index, y=monthly_quantity.values, 
               mode='lines+markers', name='수량'),
    row=2, col=1
)

# 서브플롯 4: 지역별 평균 매출
region_avg = sales_df.groupby('region')['revenue'].mean()
fig6.add_trace(
    go.Bar(x=region_avg.index, y=region_avg.values, name='평균 매출'),
    row=2, col=2
)

fig6.update_layout(height=800, title_text="종합 판매 대시보드")

# 5. 차트 저장 및 표시
print("\n4. 차트 저장")
print("-" * 40)

charts = [
    (fig1, "product_profit_margin.html", "제품별 수익률"),
    (fig2, "regional_sales.html", "지역별 매출 분포"),
    (fig3, "monthly_trend.html", "월별 매출 트렌드"),
    (fig4, "salesperson_performance.html", "영업사원별 성과"),
    (fig5, "category_sunburst.html", "카테고리별 지역 분포"),
    (fig6, "dashboard.html", "종합 대시보드")
]

for fig, filename, title in charts:
    fig.write_html(filename)
    print(f"✅ {title} → {filename}")

# 6. 데이터 요약 통계
print("\n5. 데이터 요약 통계")
print("-" * 40)

print("📊 제품 정보 요약:")
print(f"- 총 제품 수: {len(products)}개")
print(f"- 평균 가격: {products_df['price'].mean():,.0f}원")
print(f"- 평균 수익률: {products_df['profit_margin'].mean():.1f}%")

print("\n📈 판매 데이터 요약:")
print(f"- 총 거래 건수: {len(sales_data)}건")
print(f"- 총 매출: {sales_df['revenue'].sum():,.0f}원")
print(f"- 평균 거래액: {sales_df['revenue'].mean():,.0f}원")
print(f"- 총 판매 수량: {sales_df['quantity'].sum()}개")

print("\n🏆 베스트 성과:")
best_product = sales_df.groupby('product')['revenue'].sum().idxmax()
best_region = sales_df.groupby('region')['revenue'].sum().idxmax()
best_salesperson = sales_df.groupby('salesperson')['revenue'].sum().idxmax()

print(f"- 최고 매출 제품: {best_product}")
print(f"- 최고 매출 지역: {best_region}")
print(f"- 최고 성과 영업사원: {best_salesperson}")

# 7. 실시간 데이터 업데이트 시뮬레이션
print("\n6. 실시간 업데이트 시뮬레이션")
print("-" * 40)

class RealTimeSales(BaseModel):
    """실시간 판매 데이터"""
    timestamp: datetime = Field(default_factory=datetime.now)
    product_id: int = Field(gt=0)
    quantity: int = Field(gt=0)
    customer_region: str
    
    def to_sales_record(self, products: List[ProductInfo]) -> SalesRecord:
        """Pydantic 모델을 Dataclass로 변환"""
        product = next(p for p in products if p.id == self.product_id)
        return SalesRecord(
            date=self.timestamp.date(),
            product=product.name,
            quantity=self.quantity,
            revenue=product.price * self.quantity,
            region=self.customer_region,
            salesperson=random.choice(salespeople)
        )

# 실시간 데이터 시뮬레이션
realtime_data = []
for _ in range(10):
    rt_sale = RealTimeSales(
        product_id=random.choice(products).id,
        quantity=random.randint(1, 5),
        customer_region=random.choice(regions)
    )
    realtime_data.append(rt_sale)

print(f"실시간 데이터 {len(realtime_data)}건 생성")

# 실시간 데이터를 기존 형식으로 변환
new_sales = [rt.to_sales_record(products) for rt in realtime_data]
updated_sales_df = pd.concat([
    sales_df, 
    pd.DataFrame([asdict(sale) for sale in new_sales])
], ignore_index=True)

print(f"업데이트된 총 거래 건수: {len(updated_sales_df)}건")

print("\n" + "=" * 60)
print("시각화 완료!")
print("=" * 60)
print("📁 생성된 파일들:")
for _, filename, title in charts:
    print(f"  - {filename}: {title}")
print("\n💡 브라우저에서 HTML 파일을 열어 인터랙티브 차트를 확인하세요!")
print("=" * 60) 