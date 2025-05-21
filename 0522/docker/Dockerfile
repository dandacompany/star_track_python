FROM jupyter/datascience-notebook:latest

COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /home/jovyan/work