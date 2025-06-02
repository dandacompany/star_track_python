# 필요한 라이브러리 임포트
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Iris 데이터셋 로드
iris_df = px.data.iris()

# Dash 앱 초기화
# JupyterDash를 사용하면 Jupyter Notebook 내에서 앱을 실행할 수 있습니다.
# from jupyter_dash import JupyterDash
# app = JupyterDash(__name__)
app = dash.Dash(__name__)


# 앱 레이아웃 정의
app.layout = html.Div([
    html.H1("Iris 데이터셋 시각화 (Dash)"),

    html.Label("Y축으로 사용할 특징 선택:"),
    dcc.Dropdown(
        id='yaxis-column-dropdown',
        options=[{'label': col, 'value': col} for col in iris_df.columns[:-2]], # 마지막 2개 컬럼(species, species_id) 제외
        value='sepal_length', # 초기 선택값
        clearable=False
    ),

    dcc.Graph(id='iris-scatter-plot')
])

# 콜백 정의: 드롭다운 입력에 따라 그래프 업데이트
@app.callback(
    Output('iris-scatter-plot', 'figure'), # 출력: 그래프 컴포넌트의 figure 속성
    [Input('yaxis-column-dropdown', 'value')] # 입력: 드롭다운 컴포넌트의 value 속성
)
def update_graph(yaxis_column_name):
    fig = px.scatter(iris_df,
                     x='sepal_width',
                     y=yaxis_column_name, # 사용자가 선택한 컬럼을 y축으로
                     color='species',
                     title=f'Iris: Sepal Width vs {yaxis_column_name}')
    return fig

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8050)