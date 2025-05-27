# FastMCP를 이용한 Slack MCP 서버 구축 과제

## 목차

1. [과제 개요](#과제-개요)
2. [학습 목표](#학습-목표)
3. [사전 준비사항](#사전-준비사항)
4. [Slack App 설정 가이드](#slack-app-설정-가이드)
5. [개발 환경 설정](#개발-환경-설정)
6. [구현해야 할 기능](#구현해야-할-기능)
7. [기술적 요구사항](#기술적-요구사항)
8. [과제 제출 방법](#과제-제출-방법)
9. [평가 기준](#평가-기준)
10. [참고 자료 및 힌트](#참고-자료-및-힌트)

## 과제 개요

이 과제는 **FastMCP v2**를 사용하여 **Slack API**와 연동되는 MCP(Model Context Protocol) 서버를 구축하는 것입니다.

여러분은 Slack의 주요 기능들을 MCP 도구로 구현하여 LLM(Large Language Model)이 Slack 워크스페이스와 상호작용할 수 있도록 해야 합니다.

### 과제의 핵심

- Slack API를 활용한 메시지 전송, 채널 관리, 히스토리 조회 기능 구현
- FastMCP를 이용한 MCP 서버 구축
- UTF-8 인코딩을 통한 한글 메시지 처리
- 환경 변수를 통한 안전한 토큰 관리

## 학습 목표

이 과제를 통해 다음을 학습할 수 있습니다:

1. **API 연동 경험**
   - RESTful API 사용법 이해
   - HTTP 요청/응답 처리
   - API 인증 및 권한 관리

2. **FastMCP 활용**
   - MCP 서버 구축 방법
   - 도구(Tool) 정의 및 구현
   - 비동기 프로그래밍 패턴

3. **실무 개발 스킬**
   - 환경 변수 관리
   - 에러 핸들링
   - 코드 문서화
   - 타입 힌트 활용

4. **문제 해결 능력**
   - API 문서 읽기 및 이해
   - 디버깅 및 트러블슈팅
   - 요구사항 분석 및 구현

## 사전 준비사항

### 1. 필요한 계정 및 권한

- Slack 워크스페이스 (테스트용 권장)
- Slack 워크스페이스의 관리자 권한 또는 앱 설치 권한

### 2. 개발 환경

- Python 3.10 이상
- 터미널/명령 프롬프트 사용 가능
- 텍스트 에디터 또는 IDE

### 3. 기본 지식

- Python 기본 문법
- HTTP 요청/응답 개념
- JSON 데이터 형식 이해

## Slack App 설정 가이드

### 1. Slack App 생성

1. [Slack API 페이지](https://api.slack.com/apps)에 접속
2. "Create New App" 버튼 클릭
3. "From scratch" 선택
4. 앱 이름과 개발할 워크스페이스 선택
5. "Create App" 버튼 클릭

### 2. OAuth & Permissions 설정

#### 필요한 Bot Token Scopes

다음 권한들을 Bot Token Scopes에 추가해야 합니다:

```
channels:read        # 채널 목록 조회
channels:history     # 채널 메시지 히스토리 조회
chat:write          # 메시지 전송
im:read             # DM 채널 읽기
im:write            # DM 메시지 전송
im:history          # DM 히스토리 조회
users:read          # 사용자 정보 조회
```

#### 설정 방법

1. 앱 설정 페이지에서 "OAuth & Permissions" 메뉴 선택
2. "Scopes" 섹션의 "Bot Token Scopes"에서 "Add an OAuth Scope" 클릭
3. 위의 권한들을 하나씩 추가
4. "Install App to Workspace" 버튼 클릭
5. 권한 승인 후 **Bot User OAuth Token** 복사 및 저장

### 3. 보안 주의사항

- 토큰을 코드에 직접 작성하지 말 것
- 환경 변수 또는 설정 파일을 통해 관리
- 토큰을 Git에 커밋하지 말 것

## 개발 환경 설정

### 1. uv 패키지 매니저 설치

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.sh | iex"
```

### 2. 프로젝트 초기화

```bash
# 프로젝트 생성
uv init slack-mcp
cd slack-mcp

# 가상환경 생성
uv venv

# 가상환경 활성화
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate  # Windows

# 필요한 패키지 설치
uv add fastmcp requests python-dotenv
```

### 3. 환경 변수 설정

프로젝트 루트에 `.env` 파일을 생성하고 다음과 같이 설정:

```
SLACK_BOT_TOKEN=xoxb-your-bot-token-here
```

**중요**: `.env` 파일을 `.gitignore`에 추가하여 Git에 커밋되지 않도록 해야 합니다.

## 구현해야 할 기능

### 필수 기능 (4개)

#### 1. 메시지 전송 기능

- **도구명**: `send_slack_message`
- **매개변수**:
  - `channel`: 채널 ID 또는 채널명 (예: #general, C1234567890)
  - `text`: 전송할 메시지 내용
- **기능**: 지정된 Slack 채널에 메시지 전송
- **특별 요구사항**: UTF-8 인코딩으로 한글 메시지 지원

#### 2. 채널 목록 조회 기능

- **도구명**: `get_slack_channels`
- **매개변수**: 없음
- **기능**: 접근 가능한 모든 채널 목록 조회
- **반환 정보**: 채널 ID, 이름, 공개/비공개 여부, 멤버십 상태

#### 3. 채널 메시지 히스토리 조회 기능

- **도구명**: `get_slack_channel_history`
- **매개변수**:
  - `channel_id`: 조회할 채널의 ID
  - `limit`: 조회할 메시지 수 (기본값: 10, 최대: 100)
- **기능**: 지정된 채널의 최근 메시지 히스토리 조회
- **반환 정보**: 메시지 내용, 작성자, 타임스탬프

#### 4. 다이렉트 메시지 전송 기능

- **도구명**: `send_slack_direct_message`
- **매개변수**:
  - `user_id`: 메시지를 받을 사용자의 ID
  - `text`: 전송할 메시지 내용
- **기능**: 특정 사용자에게 1:1 다이렉트 메시지 전송

### 선택 기능 (추가 점수)

#### 1. 사용자 목록 조회

- 워크스페이스의 모든 사용자 정보 조회

#### 2. 메시지 검색

- 키워드를 통한 메시지 검색 기능

#### 3. 파일 업로드

- 채널에 파일 업로드 기능

#### 4. 메시지 반응 추가

- 특정 메시지에 이모지 반응 추가

## 기술적 요구사항

### 1. 코드 구조

- **모듈화**: 기능별로 적절히 분리된 코드 구조
- **클래스 설계**: Slack API 클라이언트를 위한 클래스 구현
- **함수 분리**: 각 기능을 독립적인 함수로 구현

### 2. 코드 품질

- **타입 힌트**: 모든 함수에 타입 힌트 적용
- **독스트링**: 각 함수와 클래스에 설명 문서 작성
- **에러 핸들링**: try-except를 통한 적절한 예외 처리
- **UTF-8 인코딩**: 한글 메시지 처리를 위한 인코딩 처리

### 3. FastMCP 구현

- **서버 초기화**: FastMCP 인스턴스 생성
- **도구 등록**: @mcp.tool() 데코레이터를 사용한 도구 등록
- **비동기 처리**: async/await를 사용한 비동기 함수 구현
- **stdio transport**: 표준 입출력을 통한 통신

### 4. 환경 관리

- **python-dotenv**: 환경 변수 로드
- **토큰 보안**: 하드코딩 금지, 환경 변수 사용
- **의존성 관리**: requirements.txt 또는 pyproject.toml 작성

## 과제 제출 방법

### 1. 프로젝트 구조

제출할 프로젝트는 다음과 같은 구조를 가져야 합니다:

```
slack-mcp/
├── .env.example           # 환경 변수 템플릿 (실제 토큰 제외)
├── .gitignore            # Git 무시 파일
├── README.md             # 프로젝트 설명서
├── requirements.txt      # 의존성 목록
├── slack_api.py          # Slack API 클라이언트 구현
├── slack_mcp_server.py   # FastMCP 서버 구현
└── test_slack_mcp.py     # 테스트 코드 (선택사항)
```

### 2. README.md 필수 내용

README.md 파일에는 다음 내용이 포함되어야 합니다:

- 프로젝트 개요 및 기능 설명
- 설치 및 실행 방법
- 환경 변수 설정 방법
- 각 도구의 사용법 및 예시
- 구현 과정에서 겪은 어려움과 해결 방법
- 추가로 구현한 기능 (있는 경우)

### 3. 제출 파일 목록

1. **소스 코드**: 모든 Python 파일
2. **설정 파일**: requirements.txt, .gitignore
3. **문서**: README.md
4. **환경 변수 템플릿**: .env.example
5. **실행 결과**: 스크린샷 또는 실행 로그 (선택사항)

### 4. 제출 방식

- ZIP 파일로 압축하여 제출
- 또는 GitHub 저장소 링크 제출

## 평가 기준

### 기본 점수 (70점)

#### 1. 기능 구현 완성도 (40점)

- 메시지 전송 기능: 10점
- 채널 목록 조회 기능: 10점
- 메시지 히스토리 조회 기능: 10점
- 다이렉트 메시지 전송 기능: 10점

#### 2. 코드 품질 (20점)

- 타입 힌트 사용: 5점
- 에러 핸들링: 5점
- UTF-8 인코딩 처리: 5점
- 코드 구조와 가독성: 5점

#### 3. 문서화 (10점)

- README.md 작성: 5점
- 독스트링 작성: 5점

### 추가 점수 (30점)

#### 1. 선택 기능 구현 (15점)

- 추가 기능 1개당 5점 (최대 3개)

#### 2. 고급 구현 (10점)

- 비동기 처리 최적화: 3점
- 상세한 에러 메시지: 3점
- 사용자 친화적 출력 형식: 4점

#### 3. 창의성 및 확장성 (5점)

- 독창적인 기능 추가
- 코드 확장성 고려
- 사용자 경험 개선

### 감점 요소

- **실행되지 않는 코드**: -20점
- **환경 변수 하드코딩**: -10점
- **UTF-8 인코딩 미처리**: -10점
- **에러 핸들링 부족**: -10점
- **문서화 부족**: -5점

## 참고 자료 및 힌트

### 1. 공식 문서

- [FastMCP 공식 문서](https://gofastmcp.com)
- [Slack API 문서](https://api.slack.com/)
- [Python requests 문서](https://docs.python-requests.org/)
- [python-dotenv 문서](https://pypi.org/project/python-dotenv/)

### 2. 주요 Slack API 엔드포인트

- 메시지 전송: `POST https://slack.com/api/chat.postMessage`
- 채널 목록: `GET https://slack.com/api/conversations.list`
- 메시지 히스토리: `GET https://slack.com/api/conversations.history`
- DM 채널 열기: `POST https://slack.com/api/conversations.open`

### 3. 개발 힌트

#### HTTP 요청 헤더

```python
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json; charset=utf-8'
}
```

#### UTF-8 인코딩 처리

한글 메시지 전송 시 인코딩 문제가 발생할 수 있습니다. 적절한 인코딩 처리가 필요합니다.

#### 에러 응답 처리

Slack API는 성공 시 `"ok": true`, 실패 시 `"ok": false`와 함께 `"error"` 필드를 반환합니다.

#### DM 채널 처리

다이렉트 메시지를 보내기 위해서는 먼저 `conversations.open`으로 DM 채널을 열어야 합니다.

### 4. 자주 발생하는 문제와 해결 방법

#### Q: "missing_scope" 에러가 발생합니다

A: Slack App의 OAuth & Permissions에서 필요한 스코프가 모두 추가되었는지 확인하세요.

#### Q: 한글 메시지가 깨져서 나옵니다

A: HTTP 헤더에 `charset=utf-8`을 추가하고, 메시지 텍스트의 인코딩을 확인하세요.

#### Q: 채널 ID를 어떻게 찾나요?

A: `conversations.list` API를 사용하거나, Slack 웹/앱에서 채널 정보를 확인할 수 있습니다.

#### Q: MCP 서버가 연결되지 않습니다

A: `stdio` transport를 사용하는지 확인하고, 서버가 올바르게 실행되는지 확인하세요.

### 5. 디버깅 팁

- API 응답을 출력하여 구조 확인
- 환경 변수가 올바르게 로드되는지 확인
- 네트워크 연결 상태 확인
- Slack API 문서의 예제 응답과 비교

---

**과제 제출 마감**: [날짜를 입력하세요]  
**문의사항**: [연락처를 입력하세요]

이 과제를 통해 실제 업무에서 활용할 수 있는 Slack 연동 도구를 만들어보세요.
단순히 기능을 구현하는 것을 넘어서, 코드의 품질과 사용자 경험을 고려한 개발을 경험할 수 있을 것입니다! 🚀
