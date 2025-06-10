# docker pull karoid/konlpy:3.8-12.2.0-base-ubuntu20.04
FROM karoid/konlpy:3.8-12.2.0-base-ubuntu20.04

# 주피터 노트북 설치
RUN pip install jupyter jupyterlab notebook pandas plotly requests wordcloud

# 작업 디렉토리 설정
WORKDIR /workspace

# 주피터 노트북 포트 노출
EXPOSE 8888

# 주피터 노트북 실행
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''"]
