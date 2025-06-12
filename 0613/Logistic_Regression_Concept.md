## 1. 로지스틱 회귀 모델의 구조와 의미

### 1. Odds → Log-odds(=logit)

$$
\text{odds}=\frac{p}{1-p},\qquad
\text{logit}(p)=\log\!\left(\frac{p}{1-p}\right)\;.
$$

로그를 취하면 0 \~ ∞ 범위의 **odds**가 –∞ \~ ∞ 로 펼쳐져서 선형식에 직접 얹을 수 있습니다.

---

### 2. "로그-오즈가 선형" 가정

$$
\boxed{\operatorname{logit}(p)=\eta=\beta_0+\beta_1x_1+\dots+\beta_kx_k}
$$

여기서 $\eta$를 **선형 예측자(linear predictor)** 라고 부릅니다.

---

### 3-A. 선형 예측자 $\eta$를 다시 *p* 로 풀기 ― 자세한 전개

1. 선형 가정식을 지수화

   $$
   \frac{p}{1-p}=e^{\eta}.
   $$

2. 양변에 $1-p$ 를 곱해 *p* 만 남기기

   $$
   p = e^{\eta}(1-p)
   $$

3. 우변 전개 후 *p* 묶기

   $$
   p = e^{\eta} - p\,e^{\eta}
   \;\;\Longrightarrow\;\;
   p\bigl(1+e^{\eta}\bigr)=e^{\eta}
   $$

4. 양변을 $1+e^{\eta}$ 로 나누기

   $$
   p = \frac{e^{\eta}}{1+e^{\eta}}.
   $$

5. 분자·분모에 $e^{-\eta}$ 를 곱해 더 익숙한 모습으로

   $$
   \boxed{p(\eta)=\frac{1}{1+e^{-\eta}}}.
   $$

---

### 3-B. 이 식이 바로 **시그모이드(S-자) 함수**

* **수식** $\sigma(\eta)=\dfrac{1}{1+e^{-\eta}}$.
* **형태 & 직관**

  * S 모양: 왼쪽으로는 0, 오른쪽으로는 1 로 수렴
  * $\eta=0$에서 $p=0.5$ — 가운데 점
  * 기울기(미분) $ \sigma'(\eta)=\sigma(\eta)\,[1-\sigma(\eta)]$ : 0.25 로 최대

![시그모이드 함수](https://cdn.rgbitcode.com/images/2024/2/14/senspond/55/bkgB7apFELxuXq-CP.png)

위 그래프는 선형 예측자 $\eta$를 확률 영역 0–1 로 압축해 주는 모습을 보여줍니다.

---

### 4. 왜 "시그모이드여야" 하는가?

1. **확률 제약** $0\le p\le1$ 를 자연스레 만족
2. **단조증가** — $\eta$ 가 커질수록 성공 확률도 늘어야 한다는 직관과 일치
3. **해석 편의** —

   * $\eta$ 증가 1단위 ↔ **오즈(odds)가 $e^1≈2.72$ 배**
   * 경계(0,1)에 부드럽게 근접 → 극단값에서도 미분 가능

> 다른 링크함수들도 있지만, 이 세 가지 이유 때문에 로지스틱(=시그모이드) 링크가 이진반응의 '표준'이 되었습니다.

---

### 5. 정리

$$
\boxed{
P(Y=1\mid\mathbf x)=\sigma\!\bigl(\beta_0+\beta_1x_1+\dots+\beta_kx_k\bigr)
}
$$

* **출발** Odds → Log-odds
* **선형 가정** logit =$\eta$
* **역변환** $\sigma(\eta)$ → **시그모이드**
* **계수 해석** $\beta_j$ 는 오즈 1-unit log-스케일, $e^{\beta_j}$ 는 오즈비
