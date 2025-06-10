
## pm.auto_arima 주요 옵션 정리 및 설명

| 옵션명             | 기본값      | 설명                                                                                      |
|------------------|------------|-----------------------------------------------------------------------------------------|
| y                | 필수       | 입력 시계열 데이터 (array-like, Series 등)                                                |
| d                | None       | 비계절 차분 차수. 지정하지 않으면 자동으로 추정                                             |
| start_p          | 2          | AR(p) 차수 탐색 시작값                                                                   |
| max_p            | 5          | AR(p) 차수 탐색 최대값                                                                   |
| start_q          | 2          | MA(q) 차수 탐색 시작값                                                                   |
| max_q            | 5          | MA(q) 차수 탐색 최대값                                                                   |
| m                | 1          | 계절성 주기(예: 월별 데이터의 경우 12)                                                    |
| seasonal         | True       | 계절성 ARIMA(SARIMA) 모형 적용 여부                                                      |
| stepwise         | True       | Hyndman-Khandakar 알고리즘 기반 단계별 탐색 사용 여부 (False면 모든 조합 완전탐색)           |
| trace            | False      | 탐색 과정에서 모델 정보 출력 여부                                                        |
| error_action     | 'warn'     | 오류 발생 시 동작 ('warn', 'raise', 'ignore')                                            |
| suppress_warnings| False      | 경고 메시지 출력 억제 여부                                                               |
| alpha            | 0.05       | 예측 신뢰구간의 유의수준                                                                 |
| test             | 'kpss'     | 차분 차수(d) 결정 시 사용할 단위근 검정 방법 ('kpss', 'adf', 'pp' 등)                      |
| max_d            | 2          | 최대 차분 차수                                                                           |
| information_criterion | 'aic' | 모델 선택 기준 ('aic', 'bic', 'hqic', 'oob')                                             |
| n_jobs           | 1          | 병렬처리시 사용할 CPU 코어 수 (stepwise=False일 때만 적용)                                 |
| approximation    | False      | (stepwise=False일 때) 빠른 근사 알고리즘 사용 여부                                        |

- 이 외에도 SARIMA에 필요한 `start_P`, `max_P`, `start_Q`, `max_Q`, `D`, `max_D` 등 계절성 차수 관련 옵션도 존재합니다.
- 옵션에 따라 실행 속도와 결과가 크게 달라질 수 있으므로, 데이터 특성에 맞게 조정하는 것이 중요합니다.

**참고**  

- `d`, `test`, `max_d` 등은 차분의 차수를 자동으로 결정할 때 사용됩니다.
- `seasonal=True`와 `m>1`을 함께 지정하면 SARIMA 모델을 탐색합니다.
- `stepwise=False`로 설정하면 모든 조합을 완전탐색하므로 시간이 오래 걸릴 수 있습니다.
