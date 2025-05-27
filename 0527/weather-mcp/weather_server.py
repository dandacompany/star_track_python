from typing import Any
import requests
from fastmcp import FastMCP

# FastMCP 서버 초기화
mcp = FastMCP("weather")

# 상수 정의
NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather-app/1.0"


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


if __name__ == "__main__":
    # 서버 초기화 및 실행
    mcp.run(transport='stdio') 