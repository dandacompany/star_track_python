# CSV-EDA-MCP 사용 설명서

## 소개

CSV-EDA-MCP는 CSV 파일에 대한 탐색적 데이터 분석(EDA)을 수행하는 도구입니다. Cursor IDE 내에서 MCP(Multi-agent Conversational Protocol)를 통해 데이터 분석 작업을 쉽게 수행할 수 있습니다.

## 주요 기능

- CSV 파일 로드 및 기본 정보 표시
- 데이터 기술 통계 생성
- 자동화된 EDA 시각화 생성
- 자동화 EDA 프로파일링 리포트 생성
- 자동화된 데이터 클리닝 수행

## 설치 및 설정 가이드

### 1. 필수 패키지 설치

가상환경을 생성하고 필요한 패키지를 설치합니다:

```bash
# 가상환경 생성
python -m venv eda-mcp-env

# 가상환경 활성화 (Windows)
eda-mcp-env\Scripts\activate

# 가상환경 활성화 (Mac/Linux)
source eda-mcp-env/bin/activate

# 기본 필수 패키지 설치
pip install fastmcp pandas plotly numpy sweetviz

# 고급 EDA 리포트 생성을 위한 추가 패키지 설치 (선택사항)
pip install ydata-profiling
```

### 2. 절대 경로 확인

Cursor IDE에서 MCP 서버를 실행하려면 서버 스크립트의 절대 경로가 필요합니다:

```bash
# 현재 디렉토리의 절대 경로 확인 (Mac/Linux)
pwd

# Windows에서 절대 경로 확인
cd
```

### 3. Cursor IDE에 MCP 설정

1. Cursor IDE 열기
2. 설정(Settings) → MCP 탭 열기
3. '새 MCP 추가(Add New MCP)' 클릭
4. 다음 정보 입력:
   - 이름: CSV-EDA MCP
   - 명령어: 서버 스크립트의 절대 경로 입력

     ```
     /절대/경로/venv/bin/python /절대/경로/eda-mcp/server.py
     ```

     (Windows의 경우: `C:\절대\경로\venv\Scripts\python.exe C:\절대\경로\eda-mcp\server.py`)

### 4. MCP 서버 실행

Cursor IDE에서 명령 팔레트(Cmd/Ctrl + Shift + P)를 열고 "MCP: Connect to MCP"를 선택한 후 "CSV-EDA MCP"를 선택합니다.

## 사용 방법

### CSV 파일 로드 및 기본 정보 표시

```
load_csv 도구로 CSV 파일 로드:
- path: CSV 파일 경로
- delimiter: 구분자 (기본값: ",")
- sample_size: 샘플 크기 (기본값: 5)
```

### 데이터 기술 통계 생성

```
describe_data 도구로 데이터 기술 통계 생성:
- path: CSV 파일 경로
- delimiter: 구분자 (기본값: ",")
```

### 자동화된 EDA 시각화 생성

```
visualize_data 도구로 EDA 시각화 생성:
- path: CSV 파일 경로
- delimiter: 구분자 (기본값: ",")
- plot_type: 플롯 유형 (기본값: "auto")
- output_path: 저장 경로 (선택사항)
```

### 자동화 EDA 프로파일링 리포트 생성

```
advanced_visualization 도구로 고급 EDA 리포트 생성:
- path: CSV 파일 경로
- output_path: 저장 경로 (선택사항)
- delimiter: 구분자 (기본값: ",")
- title: 리포트 제목 (기본값: "자동화 EDA 리포트")
- minimal: 최소 리포트 생성 여부 (기본값: true)
```

### 자동화된 데이터 클리닝 수행

```
clean_data 도구로 데이터 클리닝 수행:
- path: CSV 파일 경로
- output_path: 저장 경로
- delimiter: 구분자 (기본값: ",")
- missing_threshold: 결측치 제거 임계값 (기본값: 0.3)
```

## 주요 특징

### 다양한 시각화 제공

- 스캐터 플롯: 변수 간 관계 파악
- 히스토그램: 데이터 분포 확인
- 박스 플롯: 이상치 및 분포 요약
- 상관관계 히트맵: 변수 간 상관관계 파악

### 자동화된 데이터 클리닝

- 결측치 처리: 임계값 이상의 결측치를 가진 열 제거
- 수치형 데이터 보간: 중앙값을 사용한 결측치 대체
- 범주형 데이터 처리: 최빈값을 사용한 결측치 대체
- 이상치 제거: Z-점수 기반 이상치 필터링

## 주의사항

- 가상환경 경로와 서버 스크립트의 절대 경로가 정확해야 합니다.
- 고급 EDA 리포트 생성을 위해서는 ydata-profiling 패키지 설치가 필요합니다.
- 대용량 데이터셋을 분석할 때는 처리 시간이 길어질 수 있습니다.

## 문제 해결

- MCP 연결 오류 발생 시 경로 설정을 확인하세요.
- 고급 시각화 도구 오류 시 필요한 패키지가 설치되어 있는지 확인하세요.
- plotly 관련 오류 발생 시 최신 버전으로 업데이트를 시도해보세요.
