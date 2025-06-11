## Ollama Docker 컨테이너 내부 모델 관리 명령어 정리

컨테이너 이름이 기본값(ollama)일 때 기준이며, 필요에 따라 컨테이너명을 변경하여 사용하세요.

---

### **1. 모델 설치**

컨테이너 내부에서 Ollama 모델을 설치하려면 다음 명령어를 사용합니다.

```bash
docker exec -it ollama ollama pull 
```

- 예시:

  ```bash
  docker exec -it ollama ollama pull gemma3:4b
  docker exec -it ollama ollama pull qwen:7b
  docker exec -it ollama ollama pull llama3:8b
  ```

---

### **2. 모델 삭제**

설치된 모델을 삭제하려면 다음 명령어를 사용합니다.

```bash
docker exec -it ollama ollama rm 
```

- 예시:

  ```bash
  docker exec -it ollama ollama rm gemma3:4b
  docker exec -it ollama ollama rm qwen:7b
  ```

---

### **3. 모델 목록(조회)**

현재 컨테이너에 설치된 모델 목록을 확인하려면 다음 명령어를 사용합니다.

```bash
docker exec -it ollama ollama list
```

- 설치된 모든 모델과 버전을 확인할 수 있습니다.

---

### **4. 기타 참고**

- 컨테이너 이름이 다를 경우, `ollama` 대신 해당 컨테이너명을 사용하세요.
- 명령어 실행 시 컨테이너가 실행 중이어야 합니다.
- Ollama 모델명은 공식 문서 또는 `ollama list` 명령어로 확인 가능합니다.

---

### **요약 표**

| 작업      | 명령어 예시                                            |
|-----------|-------------------------------------------------------|
| 설치      | docker exec -it ollama ollama pull gemma3             |
| 삭제      | docker exec -it ollama ollama rm gemma3               |
| 목록 조회 | docker exec -it ollama ollama list                    |
