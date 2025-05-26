from mcp.server.fastmcp import FastMCP
import pandas as pd
import os
import tempfile

mcp = FastMCP(
    name="csv-eda-server",
    instructions="CSV 데이터셋 탐색적 분석을 수행하는 MCP 서버"
)

@mcp.tool('load_csv', "CSV 파일 로드 및 기본 정보 표시")
async def load_csv(
    path: str,
    delimiter: str = ",",
    sample_size: int = 5
) -> dict:
    """CSV 파일을 읽고 기본 정보를 반환합니다"""
    df = pd.read_csv(path, delimiter=delimiter)

    return {
        "file_info": {
            "columns": df.columns.tolist(),
            "shape": df.shape,
            "sample": df.head(sample_size).to_dict(),
            "dtypes": df.dtypes.astype(str).to_dict()
        }
    }

@mcp.tool('describe_data', "데이터 기술 통계 생성")
async def describe_data(
    path: str,
    delimiter: str = ","
) -> dict:
    """CSV 파일을 읽고 기술 통계를 생성합니다"""
    df = pd.read_csv(path, delimiter=delimiter)
    stats = df.describe(include='all').to_dict()
    corr = df.corr(numeric_only=True).to_dict()
    return {"statistics": stats, "correlation": corr}

@mcp.tool('visualize_data', "자동화된 EDA 시각화 생성")
async def visualize_data(
    path: str,
    delimiter: str = ",",
    plot_type: str = "auto",
    output_path: str = None
) -> dict:
    """CSV 파일을 읽고 시각화를 생성합니다"""
    df = pd.read_csv(path, delimiter=delimiter)
    import plotly.express as px
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    import numpy as np

    # 모든 서브플롯을 xy 타입으로 명시적으로 지정
    fig = make_subplots(
        rows=2, 
        cols=2,
        specs=[[{"type": "xy"}, {"type": "xy"}],
               [{"type": "xy"}, {"type": "xy"}]],
        subplot_titles=["스캐터 플롯", "히스토그램", "박스 플롯", "상관관계 히트맵"]
    )
    
    # 수치형 컬럼만 선택 (최대 3개)
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns[:3]
    
    # 스캐터 플롯 - 첫 번째 서브플롯 (1,1)
    if len(numeric_cols) >= 2:
        fig.add_trace(
            go.Scatter(x=df[numeric_cols[0]], y=df[numeric_cols[1]], 
                      mode='markers', name=f'{numeric_cols[0]} vs {numeric_cols[1]}'),
            row=1, col=1
        )

    # 히스토그램 - 두 번째 서브플롯 (1,2)
    for i, col in enumerate(numeric_cols):
        fig.add_trace(
            go.Histogram(x=df[col], name=col, opacity=0.7),
            row=1, col=2
        )

    # 박스 플롯 - 세 번째 서브플롯 (2,1)
    for i, col in enumerate(numeric_cols):
        fig.add_trace(
            go.Box(y=df[col], name=col),
            row=2, col=1
        )

    # 상관관계 히트맵 - 네 번째 서브플롯 (2,2) (parcoords 대신 사용)
    if len(numeric_cols) >= 2:
        corr_matrix = df[numeric_cols].corr()
        fig.add_trace(
            go.Heatmap(
                z=corr_matrix.values,
                x=corr_matrix.columns,
                y=corr_matrix.index,
                colorscale='Viridis',
                showscale=True
            ),
            row=2, col=2
        )

    # 레이아웃 업데이트
    fig.update_layout(height=800, width=1000, title_text="EDA 시각화")
    
    # 결과 저장
    if output_path is None:
        # 임시 디렉토리에 저장
        temp_dir = tempfile.gettempdir()
        output_filename = "eda_plots.html"
        output_path = os.path.join(temp_dir, output_filename)
    
    try:
        fig.write_html(output_path)
        success = True
        message = f"EDA 플롯이 {output_path} 파일로 저장되었습니다"
    except Exception as e:
        success = False
        message = f"파일 저장 오류: {str(e)}"
        
    return {
        "message": message,
        "success": success,
        "plots": output_path if success else None
    }

@mcp.tool('advanced_visualization', "자동화 EDA 프로파일링 리포트 생성")
async def advanced_visualization(
    path: str,
    output_path: str = None,
    delimiter: str = ",",
    title: str = "자동화 EDA 리포트",
    minimal: bool = True
) -> dict:
    """pandas-profiling/ydata-profiling을 사용하여 CSV 파일의 고급 EDA 리포트를 생성합니다"""
    # 프로파일링 라이브러리 임포트 시도
    profiling_available = False
    profiling_name = None
    
    try:
        # 먼저 pandas_profiling 시도 (구 버전)
        try:
            from pandas_profiling import ProfileReport
            profiling_name = "pandas-profiling"
            profiling_available = True
        except ImportError:
            # 그 다음 ydata_profiling 시도 (새 버전)
            try:
                from ydata_profiling import ProfileReport
                profiling_name = "ydata-profiling"
                profiling_available = True
            except ImportError:
                profiling_available = False
    except Exception:
        profiling_available = False
    
    if not profiling_available:
        return {
            "message": "pandas-profiling 또는 ydata-profiling이 설치되어 있지 않습니다. 'pip install ydata-profiling'를 실행하여 설치하세요.",
            "success": False
        }
    
    # CSV 파일 로드
    df = pd.read_csv(path, delimiter=delimiter)
    
    # 출력 경로 설정
    if output_path is None:
        temp_dir = tempfile.gettempdir()
        output_filename = "profile_report.html"
        output_path = os.path.join(temp_dir, output_filename)
    else:
        # 확장자가 .html이 아니면 추가
        if not output_path.lower().endswith('.html'):
            output_path += '.html'
    
    try:
        # 프로파일 리포트 생성
        profile = ProfileReport(df, title=title, minimal=minimal)
        
        # 결과를 HTML 파일로 저장
        profile.to_file(output_path)
        
        return {
            "message": f"{profiling_name} EDA 리포트가 {output_path}에 성공적으로 저장되었습니다",
            "success": True,
            "report_path": output_path
        }
    except Exception as e:
        return {
            "message": f"리포트 생성 중 오류가 발생했습니다: {str(e)}",
            "success": False
        }

@mcp.tool('clean_data', "자동화된 데이터 클리닝 수행")
async def clean_data(
    path: str,
    output_path: str,
    delimiter: str = ",",
    missing_threshold: float = 0.3
) -> dict:
    """CSV 파일을 읽고 데이터 클리닝을 수행한 후 결과를 저장합니다"""
    df = pd.read_csv(path, delimiter=delimiter)
    
    # 결측치 처리
    missing_percent = df.isnull().mean()
    cols_to_drop = missing_percent[missing_percent > missing_threshold].index
    df = df.drop(columns=cols_to_drop)

    # 수치형 데이터 보간
    num_cols = df.select_dtypes(include='number').columns
    df[num_cols] = df[num_cols].fillna(df[num_cols].median())

    # 범주형 데이터 처리
    cat_cols = df.select_dtypes(include='object').columns
    df[cat_cols] = df[cat_cols].fillna(df[cat_cols].mode().iloc[0])

    # 이상치 제거
    z_scores = (df[num_cols] - df[num_cols].mean())/df[num_cols].std()
    df = df[(z_scores.abs() < 3).all(axis=1)]

    # 결과를 CSV 파일로 저장
    df.to_csv(output_path, index=False)

    return {
        "message": f"클리닝된 데이터가 {output_path}에 저장되었습니다",
        "rows_before": len(df),
        "columns_dropped": cols_to_drop.tolist()
    }

if __name__ == "__main__":
    print("CSV EDA MCP 서버 시작...")
    mcp.run(
        transport="stdio"
    )