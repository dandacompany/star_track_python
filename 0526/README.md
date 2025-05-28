# 🌸 아이리스 데이터셋 분석 프로젝트

이 프로젝트는 케글에서 다운로드한 아이리스 데이터셋을 사용하여 다양한 머신러닝 모델을 비교하고 최적화하는 분류 문제 해결 프로젝트입니다.

## 📁 프로젝트 구조

```
0526/
├── analysis.py                 # 메인 분석 스크립트
├── datasets/                   # 케글에서 다운로드한 데이터셋
│   ├── Iris.csv               # 아이리스 데이터셋
│   └── database.sqlite        # SQLite 데이터베이스
├── models/                     # 훈련된 모델들 (pickle 파일)
│   ├── decisiontree_model.pkl
│   ├── randomforest_model.pkl
│   ├── gradientboosting_model.pkl
│   ├── logisticregression_model.pkl
│   ├── stackingensemble_model.pkl
│   ├── scaler.pkl
│   ├── label_encoder.pkl
│   └── results_summary.pkl
├── visualizations/             # 시각화 결과 (PNG 파일)
│   ├── feature_distributions.png
│   ├── scatter_matrix.png
│   ├── boxplots.png
│   ├── model_performance_comparison.png
│   ├── confusion_matrix_best_model.png
│   └── feature_importance_best_model.png
├── iris-analysis-env/          # 가상환경
├── requirements.txt            # 필요한 패키지 목록
└── README.md                   # 이 파일
```

## 🎯 분석 목표

1. **분류 문제 해결**: 아이리스 꽃의 종류를 예측하는 다중 클래스 분류
2. **모델 비교**: Tree 계열, 로지스틱 회귀, 앙상블 모델 성능 비교
3. **하이퍼파라미터 튜닝**: RandomSearchCV를 사용한 최적화
4. **과적합 방지**: Train/Validation/Test 데이터셋 분리
5. **시각화**: Plotly를 사용한 다양한 시각화

## 🔧 사용된 모델

1. **Decision Tree**: 의사결정나무
2. **Random Forest**: 랜덤 포레스트
3. **Gradient Boosting**: 그래디언트 부스팅
4. **Logistic Regression**: 로지스틱 회귀
5. **Stacking Ensemble**: 스태킹 앙상블

## 📊 분석 결과

### 최고 성능 모델: **Gradient Boosting**

- **테스트 정확도**: 96.67%
- **최적 하이퍼파라미터**:
  - `subsample`: 0.8
  - `n_estimators`: 100
  - `max_depth`: 3
  - `learning_rate`: 0.1

### 모델별 성능 비교

| 모델 | CV 점수 | 검증 점수 | 테스트 점수 |
|------|---------|-----------|-------------|
| Decision Tree | 98.89% | 90.00% | 93.33% |
| Random Forest | 97.78% | 93.33% | 93.33% |
| **Gradient Boosting** | **98.89%** | **90.00%** | **96.67%** |
| Logistic Regression | 98.89% | 90.00% | 93.33% |
| Stacking Ensemble | 98.89% | 90.00% | 96.67% |

## 🚀 실행 방법

### 1. 가상환경 설정

```bash
# 가상환경 생성
python -m venv iris-analysis-env

# 가상환경 활성화 (macOS/Linux)
source iris-analysis-env/bin/activate

# 가상환경 활성화 (Windows)
iris-analysis-env\Scripts\activate
```

### 2. 패키지 설치

```bash
pip install -r requirements.txt
```

### 3. 분석 실행

```bash
python analysis.py
```

## 📈 생성되는 시각화

1. **특성별 분포 히스토그램**: 각 특성의 종별 분포
2. **산점도 매트릭스**: 특성 간 상관관계
3. **박스플롯**: 특성별 분포와 이상치
4. **모델 성능 비교**: CV/검증/테스트 점수 비교
5. **혼동 행렬**: 최고 성능 모델의 예측 결과
6. **특성 중요도**: 트리 기반 모델의 특성 중요도

## 🔍 주요 특징

- **과적합 방지**: 60% 훈련, 20% 검증, 20% 테스트로 데이터 분할
- **효율적인 튜닝**: GridSearch 대신 RandomSearchCV 사용 (50회 반복)
- **스케일링**: 로지스틱 회귀에만 StandardScaler 적용
- **앙상블**: 최고 성능 모델들을 조합한 스태킹 앙상블
- **모델 저장**: 모든 모델을 pickle 파일로 저장하여 재사용 가능

## 📋 데이터셋 정보

- **데이터 출처**: Kaggle (uciml/iris)
- **샘플 수**: 150개
- **특성 수**: 4개 (SepalLength, SepalWidth, PetalLength, PetalWidth)
- **클래스 수**: 3개 (Iris-setosa, Iris-versicolor, Iris-virginica)
- **클래스 분포**: 각 클래스당 50개씩 균등 분포

## 🛠️ 기술 스택

- **Python**: 3.12
- **머신러닝**: scikit-learn
- **데이터 처리**: pandas, numpy
- **시각화**: plotly, matplotlib, seaborn
- **모델 저장**: pickle
- **데이터 다운로드**: Kaggle MCP

## 📝 분석 과정

1. **데이터 로드 및 탐색**: 기본 통계, 클래스 분포, 결측값 확인
2. **데이터 전처리**: 레이블 인코딩, 데이터 분할, 스케일링
3. **모델 정의**: 4개 기본 모델과 하이퍼파라미터 그리드 설정
4. **하이퍼파라미터 튜닝**: RandomSearchCV로 최적 파라미터 탐색
5. **앙상블 생성**: 스태킹 앙상블 모델 구성
6. **성능 평가**: 테스트 데이터에서 최종 성능 측정
7. **시각화**: 다양한 차트와 그래프 생성
8. **모델 저장**: 훈련된 모델들을 pickle 파일로 저장

## 🎉 결론

Gradient Boosting 모델이 96.67%의 테스트 정확도로 최고 성능을 보였으며, 모든 모델이 90% 이상의 높은 성능을 달성했습니다. 아이리스 데이터셋의 특성상 클래스 간 구분이 명확하여 대부분의 모델에서 우수한 성능을 보였습니다.
