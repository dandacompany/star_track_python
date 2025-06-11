# 임베딩 API 사용법 (OpenAI, OpenRouter)

---

## 0. 준비 : 공통 환경 세팅

```bash
# 1) Python 가상환경(선택)
python -m venv .venv && source .venv/bin/activate

# 2) 공통 패키지
pip install --upgrade openai tiktoken numpy
```

환경 변수로 API 키를 보관하는 것이 가장 안전합니다.

```bash
# 리눅스 / macOS
export OPENAI_API_KEY="sk-···"        # OpenAI용
export OPENROUTER_API_KEY="or-···"    # OpenRouter용
```

---

## 1. OpenAI 임베딩 API 사용법

| 최신 모델                    | 최대 컨텍스트      | 가격 (입력 + 출력 합산)                                    |
| ------------------------ | ------------ | -------------------------------------------------- |
| `text-embedding-3-small` | 32 K tokens  | **\$0.02 / 1 M tokens** ([platform.openai.com]) |
| `text-embedding-3-large` | 128 K tokens | \$0.13 / 1 M tokens                                |

> `text-embedding-3-small`는 이전 세대(`ada-002`) 대비 5배 더 저렴하고 품질도 높습니다.([openai.com])

### 1-1. 계정·키 만들기

1. [https://platform.openai.com](https://platform.openai.com) 에 가입
2. “API Keys” → “Create new secret key” 클릭
3. 키를 복사해 `OPENAI_API_KEY` 환경 변수에 저장

### 1-2. 최소 예제

```python
from openai import OpenAI

client = OpenAI()          # 기본 base_url = https://api.openai.com/v1
text = ["문장 A", "문장 B"]

response = client.embeddings.create(
    model="text-embedding-3-small",
    input=text
)

vectors = [obj.embedding for obj in response.data]
print(vectors[:5])      # 첫 5차원 미리보기
```

### 1-3. 비용 감 잡기

```text
문서 1 편 ＝ 500 tokens → 0.00001 $  
문서 1 000 편(500k tokens) → 0.01 $ 정도
```

* **Chunking = 512 tokens** 이하로 나누면 품질과 요금을 동시에 최적화할 수 있습니다.
* **캐싱** : 같은 문장은 한 번만 임베딩하여 재사용하세요.

---

## 2. OpenRouter (무료 / 저요금) 임베딩 API 사용법

OpenRouter는 400 + 모델을 **OpenAI호환 스키마**로 프록시합니다. 기부 기반이지만, 다수 모델이 **\$0** 또는 매우 저렴하게 풀려 있어 학생·연구용으로 인기입니다.([openrouter.ai], [openrouter.ai])

### 2-1. 계정·키 만들기

1. [https://openrouter.ai](https://openrouter.ai) 가입 (GitHub·Google OAuth 가능)
2. **Dashboard → API Keys** → 발급
3. `OPENROUTER_API_KEY` 환경 변수에 저장

### 2-2. 무료 임베딩 모델 예시

| 모델 ID (OpenRouter)               | 가격          | 특징                                        |
| -------------------------------- | ----------- | ----------------------------------------- |
| `google/gemma-3-27b-it:free`     | \$0 / token | 27 B, 다국어·128 K 컨텍스트 ([openrouter.ai]) |
| `deepseek/deepseek-r1-zero:free` | \$0 / token | RL·128 K, 영-한 품질 양호 ([openrouter.ai])  |

> 가격이 “0”이라도 • 분당 토큰 제한(보통 4 K\~10 K) • 동시 요청 제한이 존재합니다.

### 2-3. 최소 예제 (OpenAI SDK 그대로)

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",   # 중요!
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

text = ["문장 A", "문장 B"]
response = client.embeddings.create(
    model="google/gemma-3-27b-it:free",
    input=text,
    extra_headers={         # OpenRouter 권장(선택)
        "HTTP-Referer": "https://yourproject.site",
        "X-Title": "YourProject"
    }
)
vectors = [obj.embedding for obj in response.data]
```

OpenAI 코드와 다른 부분은 **`base_url`**, **모델 ID**, 그리고 일부 `extra_headers` 뿐입니다.([openrouter.ai])

### 2-4. 품질·제한 팁

* **속도** : 무료 모델은 QPS가 낮아 대량 임베딩에 시간이 걸립니다.
  → 작업을 배치 처리하고 `time.sleep()` 백오프를 넣으세요.
* **모델 다양성** : 품질이 모델마다 크게 다르므로, 소규모 벤치마크 후 채택하세요.
* **업타임** : 무료 모델은 가끔 “capacity reached”가 뜹니다. 동일 요청을 **retry** 로직으로 감싸 두면 좋습니다.

---

## 3. 두 환경을 자유롭게 전환하는 패턴

```python
import os
from openai import OpenAI

def get_client(provider: str = "openai") -> OpenAI:
    if provider == "openai":
        return OpenAI()
    elif provider == "openrouter":
        return OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY"),
        )
    else:
        raise ValueError("unknown provider")

client = get_client("openrouter")   # 또는 "openai"
```

이처럼 **팩토리 함수** 하나만 두면, 노트북·프로젝트 어디서든 손쉽게 바꿀 수 있습니다.

---

## 4. 후속 활용 : 벡터 DB에 저장하기

```python
import numpy as np
import supabase             # 예시: Supabase
...
supabase.table("embeddings").insert({
    "content": text[i],
    "embedding": np.array(vectors[i]).tolist()
}).execute()
```

벡터 DB가 없다면, **FAISS** 로 로컬 색인을 만드는 것도 간단합니다.

---

## 5. 요약 & 권장 학습 루트

1. **개념 잡기** → 토큰·Cosine 유사도·문장 단위 chunking
2. **OpenAI 소규모 실습** → 요금 체감 (문장 1000개 ≈ 0.01 \$)
3. **OpenRouter 벤치마크** → 무료 모델 품질 비교
4. **벡터 DB 통합** → 검색 + RAG 파이프라인 구축
5. **캐싱·재사용** → 학기 프로젝트 비용을 “0원대”로 유지

> 학습용이라면 먼저 OpenAI로 **정석적인 파이프라인**을 구현해 본 뒤, 같은 코드를 OpenRouter로 돌려 “비용 0원” 버전을 만들어 보는 방식을 추천합니다. 체감하기에 가장 빠른 비교 학습법입니다.

---

### 추가 참고 문헌

* OpenAI 공식 가격표 – Embeddings (실시간 업데이트) ([platform.openai.com])
* OpenRouter Quickstart & API 문서 ([openrouter.ai], [openrouter.ai])
* 무료 모델 예시 – Gemma 3 27B, DeepSeek R1 Zero ([openrouter.ai], [openrouter.ai])
