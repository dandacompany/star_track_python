## Ridge, Lasso 규제

**LinearRegression (선형 회귀)**  
- 가장 기본적인 회귀 방법으로, 입력 변수(피처)와 출력 변수(타깃) 사이의 선형 관계를 추정합니다.
- 손실 함수는 평균 제곱 오차(Mean Squared Error, MSE)만을 최소화합니다.
- 제약(규제)이 없기 때문에, 피처 수가 많거나 다중공선성이 존재할 때 과적합(overfitting)이 발생할 수 있습니다.

**Ridge Regression (릿지 회귀, L2 정규화)**  
- LinearRegression에 L2 규제를 추가한 모델입니다.
- 손실 함수에 회귀 계수(가중치)의 제곱합을 더해줍니다.  
  $$
  \text{Loss} = \text{MSE} + \alpha \sum_{j} w_j^2
  $$
- α(알파, 규제 강도)가 클수록 계수들이 0에 가까워집니다(완전히 0은 아님).
- 모든 피처를 사용하지만, 계수의 크기를 줄여 모델의 복잡도를 낮추고 과적합을 방지합니다.
- 변수 선택(feature selection) 기능은 없고, 변수 중요도를 완전히 0으로 만들지 않습니다.

**Lasso Regression (라쏘 회귀, L1 정규화)**  
- LinearRegression에 L1 규제를 추가한 모델입니다.
- 손실 함수에 회귀 계수의 절댓값 합을 더해줍니다.  
  $$
  \text{Loss} = \text{MSE} + \alpha \sum_{j} |w_j|
  $$
- α가 커질수록 일부 계수는 정확히 0이 되어, 불필요한 피처를 자동으로 제거하는 효과(변수 선택)가 있습니다.
- 모델이 더 간단해지고 해석이 쉬워집니다. 하지만 L1 규제 특성상 최적해가 꼭짓점(모서리)에서 발생할 확률이 높아 sparse model(희소 모델)을 만듭니다.

## 비교

| 모델             | 규제 방식 | 제약(페널티)    | 계수 0 가능성 | 변수 선택 | 과적합 방지 | scikit-learn 클래스 |
|------------------|-----------|-----------------|--------------|-----------|-------------|---------------------|
| LinearRegression | 없음      | 없음            | 없음         | 없음      | X           | LinearRegression    |
| Ridge            | L2        | $$\sum w_j^2$$  | 없음         | 없음      | O           | Ridge               |
| Lasso            | L1        | $$\sum |w_j|$$  | 있음         | 있음      | O           | Lasso               |

- Ridge는 계수를 0에 가깝게 만들지만 완전히 0으로 만들지 않음 → 변수 중요도 조정.
- Lasso는 불필요한 피처의 계수를 0으로 만들어 자동 변수 선택 효과 → 희소 모델 생성.
- 두 방법 모두 α(알파)라는 하이퍼파라미터로 규제 강도를 조절하며, α=0이면 일반 선형회귀와 동일해집니다.

## scikit-learn에서의 사용

- LinearRegression: `from sklearn.linear_model import LinearRegression`
- Ridge: `from sklearn.linear_model import Ridge`
- Lasso: `from sklearn.linear_model import Lasso`


