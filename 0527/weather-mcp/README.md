# Weather MCP Server

FastMCP v2를 사용하여 구축된 날씨 정보 MCP 서버입니다. 미국 지역의 날씨 예보와 경보 정보를 제공합니다.

## 기능

- 🌤️ **날씨 예보**: 위도/경도 기반 상세 날씨 예보
- ⚠️ **날씨 경보**: 미국 주별 활성 날씨 경보
- 📍 **위치 정보**: 주요 도시 위치 데이터
- 🔧 **고급 기능**: 리소스, 프롬프트, 컨텍스트 지원

## 설치

### 요구사항

- Python 3.10 이상
- uv 패키지 매니저 (권장)

### 설치 방법

```bash
# 저장소 클론
git clone https://github.com/weather-mcp/weather-mcp-server.git
cd weather-mcp-server

# 가상환경 생성 및 활성화
uv venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate  # Windows

# 의존성 설치
uv add fastmcp requests
```

## 사용법

### 기본 서버 실행

```bash
# STDIO 모드로 실행 (MCP 클라이언트용)
python weather_server.py

# 디버깅 모드로 실행 (웹 인터페이스)
mcp dev weather_server.py
```

### 테스트

```bash
# 서버 디버깅 모드로 테스트
mcp dev weather_server.py
```

## API 도구

### get_weather_forecast

위치의 날씨 예보를 가져옵니다.

**매개변수:**

- `latitude` (float): 위도
- `longitude` (float): 경도

**예제:**

```python
# 샌프란시스코 날씨 예보
result = await get_weather_forecast(37.7749, -122.4194)
```

### get_weather_alerts

미국 주의 날씨 경보를 가져옵니다.

**매개변수:**

- `state` (str): 미국 주 코드 (예: CA, NY)

**예제:**

```python
# 캘리포니아 날씨 경보
alerts = await get_weather_alerts("CA")
```

## Claude Desktop 연결

`~/.config/claude/claude_desktop_config.json` 파일에 다음을 추가:

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

## 개발

### 코드 포맷팅

```bash
# Black으로 코드 포맷팅
black .

# isort로 import 정렬
isort .

# mypy로 타입 검사
mypy .
```

### 테스트 실행

```bash
# pytest로 테스트 실행
pytest

# 비동기 테스트 포함
pytest -v
```

## 배포

### PyPI 패키지 빌드

```bash
# 패키지 빌드
python -m build

# PyPI에 업로드
twine upload dist/*
```

### Docker 컨테이너

```bash
# Docker 이미지 빌드
docker build -t weather-mcp .

# 컨테이너 실행
docker run -p 8000:8000 weather-mcp
```

## 라이선스

MIT License

## 기여

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 지원

- [GitHub Issues](https://github.com/weather-mcp/weather-mcp-server/issues)
- [Documentation](https://weather-mcp.readthedocs.io)
- [FastMCP Documentation](https://gofastmcp.com)

## 참고 자료

- [FastMCP 공식 문서](https://gofastmcp.com)
- [MCP 사양](https://modelcontextprotocol.io)
- [National Weather Service API](https://www.weather.gov/documentation/services-web-api)
