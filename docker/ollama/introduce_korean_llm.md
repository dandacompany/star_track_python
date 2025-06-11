## 최근 Ollama에서 인기 많은 한국어 LLM 모델

### 대표적인 한국어 LLM 모델

- **EEVE-Korean-Instruct-10.8B (야놀자)**
  - 야놀자가 공개한 한국어 특화 LLM으로, upstage의 SOLAR-10.7B 모델을 기반으로 한국어 처리에 최적화된 어휘와 파인튜닝이 적용되었습니다.
  - 108억 파라미터로, GPT-3(1,750억 파라미터)보다는 훨씬 가볍지만, 일상적인 질의응답, 문서 요약, 간단한 생성 작업에는 충분한 성능을 보입니다.
  - Hugging Face에서 모델을 직접 다운로드하거나, Ollama에서 Modelfile로 불러와 사용할 수 있습니다.

- **Llama-2-Ko, Kollama, KoVicuna 등**
  - Llama-2, Polyglot-Ko, Vicuna 등 글로벌 베이스 모델을 한국어 데이터로 파인튜닝한 다양한 오픈소스 모델이 존재합니다.
  - 각 모델별로 파라미터 크기(7B, 13B 등)와 상업적 사용 가능 여부가 다르니, 목적에 맞게 선택하면 됩니다.

### Ollama에서 바로 쓸 수 있는 모델들

- Ollama는 Llama 3, DeepSeek, Phi-3, Qwen2 등 30개 이상의 모델을 지원하며, 최근에는 Llama 3 8B, Phi-3 Mini(4K), DeepSeek Coder(7B) 등도 인기가 높습니다.
- 한국어 특화 모델은 EEVE-Korean-Instruct-10.8B가 대표적이며, Llama-2-Ko, Kollama 등도 활용 가능합니다.

## 일반 노트북에서의 구동 가능성 및 권장 사양

- **7B~10.8B 파라미터 모델**: RAM 16GB 이상이면 무난하게 실행 가능하며, SSD 사용 시 로딩 속도와 응답성이 크게 개선됩니다.
- **Llama 3 8B**: 약 6GB RAM/VRAM으로도 동작 가능해, GPU 없이도 최신 노트북에서 충분히 구동할 수 있습니다.
- **EEVE-Korean-Instruct-10.8B**: 16GB RAM, 4코어 이상의 CPU면 실사용에 무리 없습니다. GPU가 있다면 더 빠른 응답이 가능합니다.

## 설치 및 사용법 요약

1. Ollama 설치 [Windows/Mac/Linux 지원](https://ollama.com/docs/install)

2. Docker 컨테이너 버전 설치 (권장)
   - Docker가 설치된 환경에서 더 간편하게 사용 가능
   - 예시:

     ```bash
     # Ollama 컨테이너 실행
     docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
     
     # 모델 다운로드
     docker exec -it ollama ollama pull yanolja/eeve-korean-instruct-10.8b
     
     # 모델 실행 (대화형)
     docker exec -it ollama ollama run yanolja/eeve-korean-instruct-10.8b
     ```

3. 명령어로 모델 다운로드 및 실행 (로컬 설치 시)
   - 예시:  

     ```bash
     ollama pull yanolja/eeve-korean-instruct-10.8b
     ollama run yanolja/eeve-korean-instruct-10.8b
     ```

   - 또는 Llama-2-Ko, Kollama 등 원하는 모델명으로 실행

## 기타사항

- <https://ollama.com/library> 에서 더 많은 모델들을 조회 가능합니다.
- **일반 노트북(16GB RAM 이상, SSD 권장)**에서 충분히 구동 가능하며, Ollama를 통해 설치와 사용이 매우 간편합니다.
- <https://huggingface.co/naver-hyperclovax/HyperCLOVAX-SEED-Vision-Instruct-3B> 에서 최근 네이버 클로바에서 공개한 경량 LLM 모델에 대한 정보를 얻을수 있습니다.
- <https://huggingface.co/Mungert/HyperCLOVAX-SEED-Text-Instruct-0.5B-GGUF/tree/main> 에서 GGUF(ollama에서 사용 가능한 형태) 모델을 다운로드 받을 수 있습니다.
