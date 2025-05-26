# Kaggle-MCP 사용 설명서

## 소개

Kaggle-MCP는 Kaggle API를 통해 데이터셋 검색, 다운로드 및 분석을 수행할 수 있는 도구입니다. Cursor IDE 내에서 MCP(Multi-agent Conversational Protocol)를 통해 손쉽게 Kaggle 기능을 사용할 수 있습니다.

## 주요 기능

- Kaggle API 인증
- 데이터셋 목록 조회 및 검색
- 데이터셋 상세 정보 확인
- 데이터셋 다운로드
- CSV 파일 미리보기 및 분석
- Kaggle 대회 목록 조회

## 설치 및 설정 가이드

### 1. 필수 패키지 설치

가상환경을 생성하고 필요한 패키지를 설치합니다:

```bash
# 가상환경 생성
python -m venv kaggle-mcp-env

# 가상환경 활성화 (Windows)
kaggle-mcp-env\Scripts\activate

# 가상환경 활성화 (Mac/Linux)
source kaggle-mcp-env/bin/activate

# 필요 패키지 설치
pip install fastmcp pandas kaggle
```

### 2. Kaggle API 인증 정보 준비

1. [Kaggle 계정 페이지](https://www.kaggle.com/account)에 로그인
2. 'API' 섹션에서 'Create New API Token' 클릭
3. 다운로드된 `kaggle.json` 파일에 사용자명과 API 키가 포함되어 있음

### 3. 절대 경로 확인

Cursor IDE에서 MCP 서버를 실행하려면 서버 스크립트의 절대 경로가 필요합니다:

```bash
# 현재 디렉토리의 절대 경로 확인 (Mac/Linux)
pwd

# Windows에서 절대 경로 확인
cd
```

### 4. Cursor IDE에 MCP 설정

1. Cursor IDE 열기
2. 설정(Settings) → MCP 탭 열기
3. '새 MCP 추가(Add New MCP)' 클릭
4. 다음 정보 입력:
   - 이름: Kaggle MCP
   - 명령어: 서버 스크립트의 절대 경로 입력

     ```
     /절대/경로/venv/bin/python /절대/경로/kaggle-mcp/server.py
     ```

     (Windows의 경우: `C:\절대\경로\venv\Scripts\python.exe C:\절대\경로\kaggle-mcp\server.py`)

### 5. MCP 서버 실행

Cursor IDE에서 명령 팔레트(Cmd/Ctrl + Shift + P)를 열고 "MCP: Connect to MCP"를 선택한 후 "Kaggle MCP"를 선택합니다.

## 사용 방법

### 데이터셋 검색

```
list_datasets 도구로 데이터셋 검색:
- search_query: 검색어
- max_results: 최대 결과 수 (기본값: 10)
- sort_by: 정렬 기준 (기본값: "relevance")
```

### 데이터셋 다운로드

```
download_dataset 도구로 데이터셋 다운로드:
- dataset_ref: 데이터셋 참조 (형식: "소유자/데이터셋-이름")
- output_path: 저장 경로 (선택사항)
- unzip: 압축 해제 여부 (기본값: true)
```

### 데이터셋 분석

```
analyze_dataset 도구로 CSV 파일 분석:
- file_path: CSV 파일 경로
- delimiter: 구분자 (기본값: ",")
- sample_size: 샘플 크기 (기본값: 5)
```

## 주의사항

- 가상환경 경로와 서버 스크립트의 절대 경로가 정확해야 합니다.
- Kaggle API 인증 정보는 보안을 위해 안전하게 관리하세요.
- 데이터셋 분석 시 대용량 파일은 처리 시간이 오래 걸릴 수 있습니다.

## 문제 해결

- MCP 연결 오류 발생 시 경로 설정을 확인하세요.
- API 인증 오류 시 Kaggle 인증 정보가 올바른지 확인하세요.
- 패키지 관련 오류는 필요한 모든 패키지가 설치되어 있는지 확인하세요.
