
# 🗓️ 4-Day Machine-Learning Bootcamp

*(전처리 → 모델링 → 앙상블 → AutoML → 배포 & 실무 토픽)*

### Day 1 Regression & Pipeline

| 주제 / 알고리즘                        | 활동      | 데이터셋         | 핵심 포인트                            |
| -------------------------------- | ------- | ------------ | --------------------------------- |
| ML 워크플로 · `Pipeline` 기초          | 강의 ＋ 코드 | —            | `ColumnTransformer`, 재현성          |
| 선형 · 다중 · 다항 회귀                  | 실습      | Ames Housing | 다항 특성, 과적합                        |
| 트리 & 랜덤포레스트 회귀                   | 데모      | Bike Sharing | 편향‐분산                             |
| SVR (RBF)                        | 데모      | Bike Sharing | γ, ε-Tube                         |
| Gradient Boosting 개론             | 미니 강의   | —            | Stage-wise 학습                     |
| XGBoost · LightGBM · CatBoost 회귀 | 실습      | Bike Sharing | Leaf-wise, Cat encoding           |
| 회귀 평가지표 집중                       | 강의      | —            | MAE, RMSE, R², RMSLE              |
| **Lab #1** 주택가격 예측               | 과제    | Ames Housing | `GridSearchCV`, Ensemble baseline |

---

### Day 2 Classification · Custom Estimator · Metrics

| 주제 / 알고리즘                          | 활동     | 데이터셋           | 핵심 포인트                          |
| ---------------------------------- | ------ | -------------- | ------------------------------- |
| 분류 문제 개요 & 평가지표 (Binary · Multiclass) | 강의     | —              | Accuracy, F1, Macro-F1, ROC-AUC |
| 데이터 전처리 기초<br>· 결측치 처리<br>· 범주형 변수 인코딩 | 실습     | Telco Churn    | SimpleImputer, Label/One-Hot Encoding |
| 특성 스케일링 & 불균형 처리<br>· StandardScaler<br>· SMOTE | 실습     | Telco Churn    | MinMaxScaler, SMOTE, Class Weight |
| 전처리 파이프라인 구축                    | 실습     | Telco Churn    | ColumnTransformer, Pipeline    |
| 로지스틱 회귀 & K-NN                    | 실습     | Telco Churn    | 결정경계, 하이퍼파라미터 튜닝          |
| SVM (Linear · Kernel) ＋ PCA        | 데모     | Fashion-MNIST  | 커널 트릭, 차원 축소               |
| Naive Bayes                        | 데모     | Credit-Default | 사전·사후, 가우시안 분포             |
| 트리 기반 모델<br>· Decision Tree<br>· Random Forest | 실습     | Heart Failure  | 불순도, 앙상블 효과                |
| Boosted 트리 (XGB · LGBM · Cat)     | 실습     | Heart Failure  | AUC, Explainability             |
| **Lab #2** Churn Mini-Kaggle       | 과제 | Telco Churn    | 전체 파이프라인 구축, 모델 비교        |

---

### Day 3 Ensemble Deep-Dive

| 주제 / 알고리즘                                       | 활동   | 데이터셋          | 핵심 포인트                        |
| ----------------------------------------------- | ---- | ------------- | ----------------------------- |
| 앙상블 이론 (Bagging · Boosting · Stacking · Voting) | 강의   | —             | 편향-분산-협동                      |
| Bagging 계열<br>· Random Forest<br>· Extra Trees  | 실습   | Heart Failure | OOB Error, Feature Importance |
| Hard / Soft Voting                              | 데모   | Telco Churn   | 가중 Voting                     |
| Boosting 심화<br>· AdaBoost<br>· GBRT<br>· XGB 튜닝 | 실습   | 서울 따릉이 데이터셋 | LR, Depth, Early-Stop         |
| CatBoost 카테고리 처리                                | 데모   | Telco Churn   | Ordered Target Stats          |
| Stacking & Blending                             | 실습   | Ames Housing  | 메타 모델, K-Fold stack           |
| SHAP / Permutation 해석                           | 실습   | 서울 따릉이 데이터셋  | Global & Local Explain        |
| **Lab #3** 앙상블 경진                               | 과제 | 서울 따릉이 데이터셋  | 블렌딩 Leaderboard               |

---

### Day 4 Unsupervised · AutoML · Deployment

| 주제 / 알고리즘                               | 활동      | 데이터셋                            | 핵심 포인트                         |
| :------------------------------------------ | :-------- | :---------------------------------- | :---------------------------------- |
| PCA                                         | 실습      | Spotify Tracks                      | Variance Ratio                      |
| **이상탐지 (Anomaly Detection)**<br>· Isolation Forest<br>· One-Class SVM | **강의+실습** | **Credit-Card Fraud**               | **분포 기반 탐지, ROC-AUC**         |
| 실습 Q&A                                    | —         | —                                   | —                                   |
| K-Means & 계층적 군집                         | 데모      | Customer Personality                | Elbow, 덴드로그램                   |
| 연관 규칙 (Apriori · Eclat)                 | 데모      | Instacart Basket                    | 지지도, 향상도                      |
| AutoML 스프린트 (PyCaret · AutoGluon)       | 라이브 데모 | 서울 따릉이 데이터셋                        | 자동 스택 ＋ 리더보드               |
| Optuna Bayesian HPO                         | 코드워크  | 서울 따릉이 데이터셋                        | Trial, Pruner                       |
| 모델 배포 & 코스 종합 리뷰                    | 과제+토론 | —                                   | Streamlit, 딥러닝·시계열 Next Step |

---