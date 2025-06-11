## 네이버 클로바 SEED GGUF 모델을 Ollama에 설치하는 방법

네이버 클로바 SEED 경량화 LLM 모델의 GGUF 파일을 Ollama에서 사용하려면 다음 절차를 따르면 됩니다.

GGUF 모델은 같은 방법으로 모두 가능합니다.

Ollama가 이미 설치되어 있다고 가정합니다.

**1. GGUF 파일 다운로드**

- Hugging Face 등에서 원하는 HyperCLOVA X SEED GGUF 파일을 다운로드합니다.
  - 예시: `HyperCLOVAX-SEED-Text-Instruct-0.5B-GGUF` 등
  - Docker 컨테이너 명령어
    - `docker compose -f docker/ollama/docker-compose.yml exec -it ollama /bin/bash`
    -

**2. 모델 폴더 준비**

- 다운로드한 GGUF 파일을 예를 들어 `~/models/hyperclova-seed-0.5b.gguf` 경로에 둡니다.

**3. Modelfile 작성**

- 모델 파일이 위치한 폴더에 `Modelfile`이라는 이름의 텍스트 파일을 생성하고 아래와 같이 작성합니다.

```
FROM ./hyperclova-seed-0.5b.gguf

TEMPLATE """{{- if .System}}
{{ .System}}
{{- end}}
Human:
{{ .Prompt }}
Assistant:
"""

SYSTEM """A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's question."""

TEMPERATURE 0.7
PARAMETER stop 
PARAMETER stop 
```

- 템플릿은 모델 구조에 따라 다를 수 있으니, 공식 문서나 비슷한 한국어 모델의 Modelfile을 참고해 조정합니다.

**4. Ollama에 모델 등록**

- 터미널에서 해당 폴더로 이동한 뒤, 아래 명령어로 모델을 등록합니다.

```
ollama create hyperclova-seed-0.5b -f Modelfile
```

- 모델명이 `hyperclova-seed-0.5b`로 등록됩니다.

**5. 모델 실행**

- 아래 명령어로 Ollama에서 모델을 실행할 수 있습니다.

```
ollama run hyperclova-seed-0.5b:latest
```

**6. 모델 목록 확인**

- 등록된 모델 목록은 다음 명령어로 확인합니다.

```
ollama list
```

---

#### 요약

GGUF 파일 다운로드 → 2. Ollama 설치 → 3. Modelfile 작성 → 4. `ollama create`로 모델 등록 → 5. `ollama run`으로 실행  
이 과정을 따르면 네이버 클로바 SEED LLM을 Ollama에서 바로 사용할 수 있습니다.

#### 자동 설정 스크립트 실행방법

```
docker compose -f docker/ollama/docker-compose.yml exec -it ollama source /custom/install.sh
```
