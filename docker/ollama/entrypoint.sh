#!/bin/bash

# Ollama 서버 실행(백그라운드)
ollama serve &
pid=$!

# 서버가 뜰 때까지 대기
sleep 5

# 필요한 임베딩 모델 자동 설치
ollama pull nomic-embed-text
ollama pull bge-m3
ollama pull mxbai-embed-large
ollama pull gemma3:4b

# Ollama 서버 프로세스가 종료될 때까지 대기
wait $pid
