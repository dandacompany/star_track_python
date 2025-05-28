#!/usr/bin/env python3
"""
아이리스 데이터셋 분석 스크립트
- 분류 문제 해결
- 다양한 모델 비교 (Tree 계열, LogReg, 앙상블)
- 하이퍼파라미터 튜닝 (RandomSearchCV)
- 시각화 (Plotly)
- 모델 저장 (Pickle)
"""-

import pandas as pd
import numpy as np
import pickle
import os
from datetime import datetime

# 머신러닝 라이브러리
from sklearn.model_selection import train_test_split, RandomizedSearchCV, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, StackingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.pipeline import Pipeline

# 시각화 라이브러리
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.figure_factory as ff

# 경고 무시
import warnings
warnings.filterwarnings('ignore')

class IrisAnalysis:
    def __init__(self, data_path='datasets/Iris.csv'):
        """
        아이리스 분석 클래스 초기화
        """
        self.data_path = data_path
        self.df = None
        self.X = None
        self.y = None
        self.X_train = None
        self.X_val = None
        self.X_test = None
        self.y_train = None
        self.y_val = None
        self.y_test = None
        self.scaler = StandardScaler()
        self.label_encoder = LabelEncoder()
        self.models = {}
        self.best_models = {}
        self.results = {}
        
        # 결과 저장 폴더 생성
        os.makedirs('models', exist_ok=True)
        os.makedirs('visualizations', exist_ok=True)
        
    def load_and_explore_data(self):
        """
        데이터 로드 및 탐색적 데이터 분석
        """
        print("=" * 50)
        print("1. 데이터 로드 및 탐색")
        print("=" * 50)
        
        # 데이터 로드
        self.df = pd.read_csv(self.data_path)
        print(f"데이터 형태: {self.df.shape}")
        print(f"\n데이터 정보:")
        print(self.df.info())
        print(f"\n기본 통계:")
        print(self.df.describe())
        print(f"\n클래스 분포:")
        print(self.df['Species'].value_counts())
        print(f"\n결측값:")
        print(self.df.isnull().sum())
        
        # 기본 시각화
        self.create_basic_visualizations()
        
    def create_basic_visualizations(self):
        """
        기본 데이터 시각화 생성
        """
        print("\n기본 시각화 생성 중...")
        
        # 1. 특성별 분포 히스토그램
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width']
        )
        
        features = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
        positions = [(1,1), (1,2), (2,1), (2,2)]
        
        for feature, pos in zip(features, positions):
            for species in self.df['Species'].unique():
                data = self.df[self.df['Species'] == species][feature]
                fig.add_trace(
                    go.Histogram(x=data, name=f'{species}', opacity=0.7, nbinsx=15),
                    row=pos[0], col=pos[1]
                )
        
        fig.update_layout(
            title="아이리스 특성별 분포",
            height=600,
            showlegend=True
        )
        fig.write_image("visualizations/feature_distributions.png")
        print("✓ 특성별 분포 히스토그램 저장: visualizations/feature_distributions.png")
        
        # 2. 산점도 매트릭스
        fig = px.scatter_matrix(
            self.df,
            dimensions=['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm'],
            color='Species',
            title="아이리스 특성 간 상관관계"
        )
        fig.write_image("visualizations/scatter_matrix.png")
        print("✓ 산점도 매트릭스 저장: visualizations/scatter_matrix.png")
        
        # 3. 박스플롯
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width']
        )
        
        for i, feature in enumerate(features):
            row = (i // 2) + 1
            col = (i % 2) + 1
            
            for species in self.df['Species'].unique():
                data = self.df[self.df['Species'] == species][feature]
                fig.add_trace(
                    go.Box(y=data, name=f'{species}', showlegend=(i==0)),
                    row=row, col=col
                )
        
        fig.update_layout(
            title="아이리스 특성별 박스플롯",
            height=600
        )
        fig.write_image("visualizations/boxplots.png")
        print("✓ 박스플롯 저장: visualizations/boxplots.png")
        
    def prepare_data(self):
        """
        데이터 전처리 및 분할
        """
        print("\n" + "=" * 50)
        print("2. 데이터 전처리 및 분할")
        print("=" * 50)
        
        # 특성과 타겟 분리
        self.X = self.df.drop(['Id', 'Species'], axis=1)
        self.y = self.df['Species']
        
        # 레이블 인코딩
        self.y = self.label_encoder.fit_transform(self.y)
        
        # 데이터 분할: 60% train, 20% validation, 20% test
        self.X_temp, self.X_test, self.y_temp, self.y_test = train_test_split(
            self.X, self.y, test_size=0.2, random_state=42, stratify=self.y
        )
        
        self.X_train, self.X_val, self.y_train, self.y_val = train_test_split(
            self.X_temp, self.y_temp, test_size=0.25, random_state=42, stratify=self.y_temp
        )
        
        # 스케일링
        self.X_train_scaled = self.scaler.fit_transform(self.X_train)
        self.X_val_scaled = self.scaler.transform(self.X_val)
        self.X_test_scaled = self.scaler.transform(self.X_test)
        
        print(f"훈련 세트: {self.X_train.shape}")
        print(f"검증 세트: {self.X_val.shape}")
        print(f"테스트 세트: {self.X_test.shape}")
        
    def define_models(self):
        """
        모델 정의 및 하이퍼파라미터 그리드 설정
        """
        print("\n" + "=" * 50)
        print("3. 모델 정의")
        print("=" * 50)
        
        # 기본 모델들 정의
        self.models = {
            'DecisionTree': {
                'model': DecisionTreeClassifier(random_state=42),
                'params': {
                    'max_depth': [3, 5, 7, 10, None],
                    'min_samples_split': [2, 5, 10],
                    'min_samples_leaf': [1, 2, 4],
                    'criterion': ['gini', 'entropy']
                },
                'use_scaling': False
            },
            'RandomForest': {
                'model': RandomForestClassifier(random_state=42),
                'params': {
                    'n_estimators': [50, 100, 200],
                    'max_depth': [3, 5, 7, None],
                    'min_samples_split': [2, 5, 10],
                    'min_samples_leaf': [1, 2, 4]
                },
                'use_scaling': False
            },
            'GradientBoosting': {
                'model': GradientBoostingClassifier(random_state=42),
                'params': {
                    'n_estimators': [50, 100, 200],
                    'learning_rate': [0.01, 0.1, 0.2],
                    'max_depth': [3, 5, 7],
                    'subsample': [0.8, 0.9, 1.0]
                },
                'use_scaling': False
            },
            'LogisticRegression': {
                'model': LogisticRegression(random_state=42, max_iter=1000),
                'params': {
                    'C': [0.01, 0.1, 1, 10, 100],
                    'penalty': ['l1', 'l2'],
                    'solver': ['liblinear', 'saga']
                },
                'use_scaling': True
            }
        }
        
        print("정의된 모델들:")
        for name in self.models.keys():
            print(f"- {name}")
            
    def train_and_tune_models(self):
        """
        모델 훈련 및 하이퍼파라미터 튜닝
        """
        print("\n" + "=" * 50)
        print("4. 모델 훈련 및 하이퍼파라미터 튜닝")
        print("=" * 50)
        
        for name, model_info in self.models.items():
            print(f"\n{name} 모델 튜닝 중...")
            
            # 데이터 선택 (스케일링 여부에 따라)
            if model_info['use_scaling']:
                X_train = self.X_train_scaled
                X_val = self.X_val_scaled
            else:
                X_train = self.X_train
                X_val = self.X_val
            
            # RandomizedSearchCV로 하이퍼파라미터 튜닝
            random_search = RandomizedSearchCV(
                model_info['model'],
                model_info['params'],
                n_iter=50,  # 50번의 랜덤 조합 시도
                cv=5,
                scoring='accuracy',
                random_state=42,
                n_jobs=-1
            )
            
            random_search.fit(X_train, self.y_train)
            
            # 최적 모델 저장
            self.best_models[name] = random_search.best_estimator_
            
            # 검증 세트에서 성능 평가
            val_score = random_search.best_estimator_.score(X_val, self.y_val)
            
            # 교차 검증 점수
            cv_scores = cross_val_score(random_search.best_estimator_, X_train, self.y_train, cv=5)
            
            self.results[name] = {
                'best_params': random_search.best_params_,
                'best_cv_score': random_search.best_score_,
                'val_score': val_score,
                'cv_mean': cv_scores.mean(),
                'cv_std': cv_scores.std()
            }
            
            print(f"✓ 최적 파라미터: {random_search.best_params_}")
            print(f"✓ CV 점수: {random_search.best_score_:.4f}")
            print(f"✓ 검증 점수: {val_score:.4f}")
            
    def create_stacking_ensemble(self):
        """
        스태킹 앙상블 모델 생성
        """
        print("\n" + "=" * 50)
        print("5. 스태킹 앙상블 모델 생성")
        print("=" * 50)
        
        # 베이스 모델들 (스케일링이 필요한 모델과 아닌 모델 분리)
        base_models = [
            ('dt', self.best_models['DecisionTree']),
            ('rf', self.best_models['RandomForest']),
            ('gb', self.best_models['GradientBoosting'])
        ]
        
        # 메타 모델 (로지스틱 회귀)
        meta_model = LogisticRegression(random_state=42)
        
        # 스태킹 분류기 생성
        stacking_clf = StackingClassifier(
            estimators=base_models,
            final_estimator=meta_model,
            cv=5,
            stack_method='predict_proba'
        )
        
        # 훈련
        stacking_clf.fit(self.X_train, self.y_train)
        
        # 검증 세트에서 성능 평가
        val_score = stacking_clf.score(self.X_val, self.y_val)
        cv_scores = cross_val_score(stacking_clf, self.X_train, self.y_train, cv=5)
        
        self.best_models['StackingEnsemble'] = stacking_clf
        self.results['StackingEnsemble'] = {
            'best_params': 'Ensemble of best models',
            'best_cv_score': cv_scores.mean(),
            'val_score': val_score,
            'cv_mean': cv_scores.mean(),
            'cv_std': cv_scores.std()
        }
        
        print(f"✓ 스태킹 앙상블 CV 점수: {cv_scores.mean():.4f} ± {cv_scores.std():.4f}")
        print(f"✓ 스태킹 앙상블 검증 점수: {val_score:.4f}")
        
    def evaluate_models(self):
        """
        모든 모델의 최종 성능 평가
        """
        print("\n" + "=" * 50)
        print("6. 최종 모델 성능 평가")
        print("=" * 50)
        
        test_results = {}
        
        for name, model in self.best_models.items():
            # 테스트 데이터 선택
            if name == 'LogisticRegression':
                X_test = self.X_test_scaled
            else:
                X_test = self.X_test
                
            # 예측
            y_pred = model.predict(X_test)
            test_score = accuracy_score(self.y_test, y_pred)
            
            test_results[name] = {
                'test_accuracy': test_score,
                'predictions': y_pred
            }
            
            print(f"\n{name}:")
            print(f"테스트 정확도: {test_score:.4f}")
            print("분류 리포트:")
            print(classification_report(self.y_test, y_pred, 
                                      target_names=self.label_encoder.classes_))
        
        # 최고 성능 모델 찾기
        best_model_name = max(test_results.keys(), 
                             key=lambda x: test_results[x]['test_accuracy'])
        
        print(f"\n🏆 최고 성능 모델: {best_model_name}")
        print(f"테스트 정확도: {test_results[best_model_name]['test_accuracy']:.4f}")
        
        self.test_results = test_results
        self.best_model_name = best_model_name
        
        return best_model_name
        
    def create_performance_visualizations(self):
        """
        성능 비교 시각화 생성
        """
        print("\n" + "=" * 50)
        print("7. 성능 시각화 생성")
        print("=" * 50)
        
        # 1. 모델 성능 비교 바 차트
        model_names = list(self.results.keys())
        cv_scores = [self.results[name]['cv_mean'] for name in model_names]
        val_scores = [self.results[name]['val_score'] for name in model_names]
        test_scores = [self.test_results[name]['test_accuracy'] for name in model_names]
        
        fig = go.Figure(data=[
            go.Bar(name='CV Score', x=model_names, y=cv_scores),
            go.Bar(name='Validation Score', x=model_names, y=val_scores),
            go.Bar(name='Test Score', x=model_names, y=test_scores)
        ])
        
        fig.update_layout(
            title='모델 성능 비교',
            xaxis_title='모델',
            yaxis_title='정확도',
            barmode='group'
        )
        fig.write_image("visualizations/model_performance_comparison.png")
        print("✓ 모델 성능 비교 차트 저장: visualizations/model_performance_comparison.png")
        
        # 2. 혼동 행렬 (최고 성능 모델)
        best_model = self.best_models[self.best_model_name]
        if self.best_model_name == 'LogisticRegression':
            X_test = self.X_test_scaled
        else:
            X_test = self.X_test
            
        y_pred = best_model.predict(X_test)
        cm = confusion_matrix(self.y_test, y_pred)
        
        # 클래스 이름을 리스트로 변환
        class_names = list(self.label_encoder.classes_)
        
        fig = ff.create_annotated_heatmap(
            cm,
            x=class_names,
            y=class_names,
            annotation_text=cm,
            colorscale='Blues'
        )
        
        fig.update_layout(
            title=f'{self.best_model_name} 모델의 혼동 행렬',
            xaxis_title='예측값',
            yaxis_title='실제값'
        )
        fig.write_image("visualizations/confusion_matrix_best_model.png")
        print("✓ 혼동 행렬 저장: visualizations/confusion_matrix_best_model.png")
        
        # 3. 특성 중요도 (트리 기반 모델인 경우)
        if hasattr(best_model, 'feature_importances_'):
            feature_names = self.X.columns
            importances = best_model.feature_importances_
            
            fig = go.Figure(data=[
                go.Bar(x=feature_names, y=importances)
            ])
            
            fig.update_layout(
                title=f'{self.best_model_name} 모델의 특성 중요도',
                xaxis_title='특성',
                yaxis_title='중요도'
            )
            fig.write_image("visualizations/feature_importance_best_model.png")
            print("✓ 특성 중요도 차트 저장: visualizations/feature_importance_best_model.png")
        
    def save_models(self):
        """
        훈련된 모델들을 pickle 파일로 저장
        """
        print("\n" + "=" * 50)
        print("8. 모델 저장")
        print("=" * 50)
        
        # 각 모델 저장
        for name, model in self.best_models.items():
            filename = f"models/{name.lower()}_model.pkl"
            with open(filename, 'wb') as f:
                pickle.dump(model, f)
            print(f"✓ {name} 모델 저장: {filename}")
        
        # 스케일러와 레이블 인코더 저장
        with open("models/scaler.pkl", 'wb') as f:
            pickle.dump(self.scaler, f)
        print("✓ 스케일러 저장: models/scaler.pkl")
        
        with open("models/label_encoder.pkl", 'wb') as f:
            pickle.dump(self.label_encoder, f)
        print("✓ 레이블 인코더 저장: models/label_encoder.pkl")
        
        # 결과 요약 저장
        results_summary = {
            'model_results': self.results,
            'test_results': self.test_results,
            'best_model': self.best_model_name,
            'timestamp': datetime.now().isoformat()
        }
        
        with open("models/results_summary.pkl", 'wb') as f:
            pickle.dump(results_summary, f)
        print("✓ 결과 요약 저장: models/results_summary.pkl")
        
    def run_complete_analysis(self):
        """
        전체 분석 파이프라인 실행
        """
        print("🌸 아이리스 데이터셋 분석 시작 🌸")
        print(f"시작 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        try:
            self.load_and_explore_data()
            self.prepare_data()
            self.define_models()
            self.train_and_tune_models()
            self.create_stacking_ensemble()
            best_model = self.evaluate_models()
            self.create_performance_visualizations()
            self.save_models()
            
            print("\n" + "=" * 50)
            print("🎉 분석 완료!")
            print("=" * 50)
            print(f"최고 성능 모델: {best_model}")
            print(f"테스트 정확도: {self.test_results[best_model]['test_accuracy']:.4f}")
            print(f"완료 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print("\n저장된 파일들:")
            print("📁 models/ - 훈련된 모델들")
            print("📁 visualizations/ - 시각화 결과들")
            
        except Exception as e:
            print(f"❌ 오류 발생: {str(e)}")
            raise

if __name__ == "__main__":
    # 분석 실행
    analyzer = IrisAnalysis()
    analyzer.run_complete_analysis() 