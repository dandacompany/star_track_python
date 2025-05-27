# FastMCP v2 튜토리얼: 날씨 정보 MCP 서버 만들기

## 목차

1. [FastMCP v2 소개](#fastmcp-v2-소개)
2. [환경 설정](#환경-설정)
3. [기본 개념](#기본-개념)
4. [날씨 MCP 서버 구현](#날씨-mcp-서버-구현)
5. [서버 테스트](#서버-테스트)
6. [클라이언트 연결](#클라이언트-연결)
7. [고급 기능](#고급-기능)

## FastMCP v2 소개

FastMCP v2는 Model Context Protocol (MCP) 서버와 클라이언트를 쉽게 구축할 수 있는 Python 라이브러리입니다. MCP는 LLM이 외부 도구와 데이터에 접근할 수 있도록 하는 표준화된 프로토콜입니다.

### 주요 특징

- 🚀 **빠른 개발**: 데코레이터 기반의 간단한 API
- 🍀 **단순함**: 최소한의 보일러플레이트 코드
- 🐍 **파이썬다운**: 타입 힌트와 독스트링 자동 활용
- 🔍 **완전함**: MCP 사양의 전체 구현

## 환경 설정

### 1. 필수 요구사항

- Python 3.10 이상
- uv 패키지 매니저 (권장)

### 2. uv 설치

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.sh | iex"
```

### 3. 프로젝트 설정

```bash
# 새 프로젝트 생성
uv init weather-mcp
cd weather-mcp

# 가상환경 생성 및 활성화
uv venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate  # Windows

# FastMCP 설치
uv add fastmcp requests
```

## 기본 개념

### MCP의 핵심 구성요소

1. **Tools (도구)**: LLM이 호출할 수 있는 함수들
2. **Resources (리소스)**: LLM이 읽을 수 있는 데이터 소스
3. **Prompts (프롬프트)**: 재사용 가능한 메시지 템플릿
4. **Context (컨텍스트)**: 세션 정보와 기능에 대한 접근

### FastMCP 서버 구조

```python
from fastmcp import FastMCP

# 서버 인스턴스 생성
mcp = FastMCP("서버이름")

# 도구 정의
@mcp.tool()
def my_tool(param: str) -> str:
    """도구 설명"""
    return f"결과: {param}"

# 서버 실행
if __name__ == "__main__":
    mcp.run()
```

## 날씨 MCP 서버 구현

### 1. 기본 서버 설정

`weather_server.py` 파일을 생성합니다:

```python
from typing import Any
import requests
from fastmcp import FastMCP

# FastMCP 서버 초기화
mcp = FastMCP("weather")

# 상수 정의
NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather-app/1.0"
```

### 2. 헬퍼 함수 구현

```python
def make_nws_request(url: str) -> dict[str, Any] | None:
    """NWS API에 요청을 보내고 응답을 반환합니다."""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/geo+json"
    }
    try:
        response = requests.get(url, headers=headers, timeout=30.0)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"API 요청 오류: {e}")
        return None

def format_alert(feature: dict) -> str:
    """경보 정보를 읽기 쉬운 형태로 포맷합니다."""
    props = feature["properties"]
    return f"""
이벤트: {props.get('event', '알 수 없음')}
지역: {props.get('areaDesc', '알 수 없음')}
심각도: {props.get('severity', '알 수 없음')}
설명: {props.get('description', '설명 없음')}
지침: {props.get('instruction', '특별한 지침 없음')}
"""
```

### 3. 날씨 도구 구현

```python
@mcp.tool()
async def get_weather_alerts(state: str) -> str:
    """미국 주의 날씨 경보를 가져옵니다.
    
    Args:
        state: 미국 주 코드 (예: CA, NY)
    """
    url = f"{NWS_API_BASE}/alerts/active/area/{state}"
    data = make_nws_request(url)
    
    if not data or "features" not in data:
        return "경보를 가져올 수 없거나 경보가 없습니다."
    
    if not data["features"]:
        return "이 주에 활성 경보가 없습니다."
    
    alerts = [format_alert(feature) for feature in data["features"]]
    return "\n---\n".join(alerts)

@mcp.tool()
async def get_weather_forecast(latitude: float, longitude: float) -> str:
    """위치의 날씨 예보를 가져옵니다.
    
    Args:
        latitude: 위도
        longitude: 경도
    """
    # 먼저 예보 그리드 엔드포인트를 가져옵니다
    points_url = f"{NWS_API_BASE}/points/{latitude},{longitude}"
    points_data = make_nws_request(points_url)
    
    if not points_data:
        return "이 위치의 예보 데이터를 가져올 수 없습니다."
    
    # 포인트 응답에서 예보 URL을 가져옵니다
    forecast_url = points_data["properties"]["forecast"]
    forecast_data = make_nws_request(forecast_url)
    
    if not forecast_data:
        return "상세 예보를 가져올 수 없습니다."
    
    # 기간을 읽기 쉬운 예보로 포맷합니다
    periods = forecast_data["properties"]["periods"]
    forecasts = []
    for period in periods[:5]:  # 다음 5개 기간만 표시
        forecast = f"""
{period['name']}:
온도: {period['temperature']}°{period['temperatureUnit']}
바람: {period['windSpeed']} {period['windDirection']}
예보: {period['detailedForecast']}
"""
        forecasts.append(forecast)
    
    return "\n---\n".join(forecasts)
```

### 4. 서버 실행 코드

```python
if __name__ == "__main__":
    # 서버 초기화 및 실행
    mcp.run(transport='stdio')
```

## 서버 테스트

### 1. MCP Inspector 사용

FastMCP는 내장된 디버깅 도구를 제공합니다:

```bash
# 서버 디버깅 모드로 실행
mcp dev weather_server.py
```

브라우저에서 `http://127.0.0.1:6274`로 접속하여 Inspector 인터페이스를 사용할 수 있습니다.

### 2. 직접 테스트

```python
# test_weather.py
import asyncio
from weather_server import get_weather_alerts, get_weather_forecast

async def test_tools():
    # 도구 직접 호출 테스트
    alerts = await get_weather_alerts("CA")
    print("캘리포니아 경보:", alerts)
    
    forecast = await get_weather_forecast(37.7749, -122.4194)
    print("샌프란시스코 예보:", forecast)

if __name__ == "__main__":
    asyncio.run(test_tools())
```

## 클라이언트 연결

### 1. Claude Desktop 설정

`~/.config/claude/claude_desktop_config.json` 파일에 다음 중 하나를 추가:

#### uv 방식 (권장)

```json
{
    "mcpServers": {
        "weather": {
            "command": "uv",
            "args": [
                "--directory",
                "/절대/경로/to/weather-mcp",
                "run",
                "weather_server.py"
            ]
        }
    }
}
```

#### Python 직접 실행 방식

```json
{
    "mcpServers": {
        "weather": {
            "command": "/절대/경로/to/weather-mcp/.venv/bin/python",
            "args": [
                "/절대/경로/to/weather-mcp/weather_server.py"
            ]
        }
    }
}
```

#### Docker 방식

```json
{
    "mcpServers": {
        "weather": {
            "command": "docker",
            "args": [
                "run",
                "--rm",
                "-i",
                "weather-mcp"
            ]
        }
    }
}
```

### 2. Cursor IDE 설정

`~/.cursor/mcp.json` 파일에 다음 중 하나를 추가:

#### uv 방식 (권장)

```json
{
    "mcpServers": {
        "MCP_WEATHER": {
            "command": "uv",
            "args": [
                "--directory",
                "/절대/경로/to/weather-mcp",
                "run",
                "weather_server.py"
            ]
        }
    }
}
```

#### Python 직접 실행 방식

```json
{
    "mcpServers": {
        "MCP_WEATHER": {
            "command": "/절대/경로/to/weather-mcp/.venv/bin/python",
            "args": [
                "/절대/경로/to/weather-mcp/weather_server.py"
            ]
        }
    }
}
```

#### Docker 방식

```json
{
    "mcpServers": {
        "MCP_WEATHER": {
            "command": "docker",
            "args": [
                "run",
                "--rm",
                "-i",
                "weather-mcp"
            ]
        }
    }
}
```

### 3. 설정 방식별 장단점

| 방식 | 장점 | 단점 | 사용 시기 |
|------|------|------|-----------|
| **uv** | - 의존성 자동 관리<br>- 가상환경 자동 활성화<br>- 빠른 실행 | - uv 설치 필요 | 개발 환경 (권장) |
| **Python 직접** | - 단순한 설정<br>- 디버깅 용이 | - 가상환경 수동 관리<br>- 경로 의존성 | 로컬 개발/테스트 |
| **Docker** | - 환경 독립성<br>- 배포 용이<br>- 일관된 실행 환경 | - Docker 설치 필요<br>- 이미지 빌드 필요 | 프로덕션/배포 |

### 4. Docker 이미지 빌드 (Docker 방식 사용 시)

Docker 방식을 사용하려면 먼저 이미지를 빌드해야 합니다:

```bash
# weather-mcp 디렉토리에서 실행
cd /절대/경로/to/weather-mcp
docker build -t weather-mcp .
```

### 5. FastMCP 클라이언트 사용

```python
# client_example.py
import asyncio
from fastmcp import Client

async def test_client():
    # 서버에 연결
    async with Client("weather_server.py") as client:
        # 도구 목록 가져오기
        tools = await client.list_tools()
        print("사용 가능한 도구:", tools)
        
        # 도구 호출
        result = await client.call_tool(
            "get_weather_forecast", 
            {"latitude": 37.7749, "longitude": -122.4194}
        )
        print("예보 결과:", result.text)

if __name__ == "__main__":
    asyncio.run(test_client())
```

### 6. 설정 검증 및 테스트

#### MCP 서버 연결 테스트

```bash
# uv 방식 테스트
echo '{"jsonrpc": "2.0", "method": "initialize", "params": {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "test", "version": "1.0"}}, "id": 1}' | uv --directory /절대/경로/to/weather-mcp run weather_server.py

# Python 직접 실행 테스트
echo '{"jsonrpc": "2.0", "method": "initialize", "params": {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "test", "version": "1.0"}}, "id": 1}' | /절대/경로/to/weather-mcp/.venv/bin/python /절대/경로/to/weather-mcp/weather_server.py

# Docker 방식 테스트
echo '{"jsonrpc": "2.0", "method": "initialize", "params": {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "test", "version": "1.0"}}, "id": 1}' | docker run --rm -i weather-mcp
```

#### 성공적인 응답 예시

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "protocolVersion": "2024-11-05",
    "capabilities": {
      "experimental": {},
      "prompts": {"listChanged": false},
      "resources": {"subscribe": false, "listChanged": false},
      "tools": {"listChanged": true}
    },
    "serverInfo": {
      "name": "weather",
      "version": "1.9.1"
    }
  }
}
```

### 7. 트러블슈팅

#### 일반적인 문제와 해결방법

| 문제 | 원인 | 해결방법 |
|------|------|----------|
| `command not found: uv` | uv가 설치되지 않음 | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| `No such file or directory` | 잘못된 경로 | 절대 경로 확인 및 수정 |
| `Permission denied` | 실행 권한 없음 | `chmod +x weather_server.py` |
| `ModuleNotFoundError` | 의존성 미설치 | `uv add fastmcp requests` |
| `Docker image not found` | 이미지 미빌드 | `docker build -t weather-mcp .` |
| `Connection refused` | 서버 시작 실패 | 로그 확인 및 포트 충돌 검사 |

#### 디버깅 팁

1. **로그 확인**

   ```bash
   # Claude Desktop 로그 (macOS)
   tail -f ~/Library/Logs/Claude/mcp*.log
   
   # Cursor IDE 로그
   # Cursor > Help > Show Logs에서 확인
   ```

2. **수동 서버 실행으로 테스트**

   ```bash
   # 서버를 직접 실행하여 오류 메시지 확인
   cd /절대/경로/to/weather-mcp
   uv run weather_server.py
   ```

3. **MCP Inspector 사용**

   ```bash
   # 웹 인터페이스로 디버깅
   mcp dev weather_server.py
   # 브라우저에서 http://127.0.0.1:6274 접속
   ```

### 8. 실제 사용 예시

#### Claude Desktop에서 사용

```
사용자: "샌프란시스코의 날씨 예보를 알려주세요"

Claude: get_weather_forecast 도구를 사용하여 샌프란시스코(위도: 37.7749, 경도: -122.4194)의 날씨 예보를 가져오겠습니다.

[도구 실행 결과]
오늘 밤:
온도: 52°F
바람: 10 mph W
예보: 대체로 맑음. 최저 기온 52도 내외.

내일:
온도: 65°F
바람: 5 mph SW
예보: 맑음. 최고 기온 65도 내외.
...
```

#### Cursor IDE에서 사용

```
사용자: @MCP_WEATHER 캘리포니아에 날씨 경보가 있나요?

## 결론

이 튜토리얼에서는 FastMCP v2를 사용하여 날씨 정보를 제공하는 MCP 서버를 구축하는 방법을 배웠습니다. 주요 내용:

1. **기본 설정**: FastMCP 설치 및 프로젝트 구성
2. **도구 구현**: 날씨 경보와 예보 기능
3. **테스트**: MCP Inspector와 클라이언트를 통한 테스트
4. **고급 기능**: 리소스, 프롬프트, 컨텍스트 활용
5. **배포**: 패키징과 배포 옵션

FastMCP v2의 강력한 기능을 활용하면 LLM이 외부 데이터와 서비스에 쉽게 접근할 수 있는 도구를 빠르게 구축할 수 있습니다.

## 참고 자료

- [FastMCP 공식 문서](https://gofastmcp.com)
- [MCP 사양](https://modelcontextprotocol.io)
- [FastMCP GitHub](https://github.com/jlowin/fastmcp)
- [National Weather Service API](https://www.weather.gov/documentation/services-web-api)
