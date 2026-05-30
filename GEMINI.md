# GEMINI.md - 업무 말투 변환기 프로젝트 지침

이 파일은 **업무 말투 변환기(BizTalk-GeminiCLI)** 프로젝트의 아키텍처, 개발 규칙 및 워크플로우를 정의합니다. Gemini CLI 에이전트는 이 지침을 최우선으로 준수해야 합니다.

---

## 1. 프로젝트 개요 (Project Overview)

- **목적**: 사용자가 입력한 일상적인 말투를 상사, 동료, 고객 등 수신 대상에 적합한 격식 있는 업무 말투로 변환하는 서비스.
- **핵심 가치**: "완벽함보다 작동하는 서비스", "바이브 코딩 3원칙 준수".
- **기술 스택**:
  - **Backend**: Python (FastAPI), Uvicorn
  - **Frontend**: Vanilla HTML/CSS/JS
  - **AI**: Upstage Solar-Pro3, LangChain (langchain-upstage)
  - **Infrastructure**: Vercel (배포), Git/GitHub (버전 관리)

---

## 2. 개발 원칙: 바이브 코딩 3원칙

모든 작업 시 다음 원칙을 엄격히 적용합니다.

1.  **완료 기준을 먼저 정의하라**: 작업을 시작하기 전 "무엇을 만들면 끝인지" 명확한 체크리스트를 작성하고 사용자에게 확인받습니다.
2.  **조사 먼저, 구현 나중**: 새로운 라이브러리나 API(특히 Upstage/LangChain) 연동 시, 구현 전 최신 문서와 연동 방식을 먼저 조사합니다.
3.  **버그는 분석 먼저, 수정 나중**: 에러 발생 시 즉시 코드를 수정하지 않고, 발생 원인을 근본적으로 분석하여 보고한 뒤 수정을 진행합니다.

---

## 3. 디렉토리 구조 (Directory Structure)

프로젝트는 다음과 같은 구조로 구성되어야 합니다 (PRD 기준).

```text
biztalk_gemini-cli/
├── backend/                # FastAPI 서버 코드
│   ├── main.py             # 앱 진입점 및 설정
│   ├── routers/            # API 엔드포인트
│   ├── services/           # AI 변환 로직 (LangChain)
│   ├── prompts/            # 수신 대상별 템플릿
│   ├── models/             # Pydantic 스키마
│   └── requirements.txt    # 의존성 목록
├── frontend/               # 정적 웹 페이지
│   ├── index.html
│   ├── css/
│   └── js/
├── .env                    # API 키 (UPSTAGE_API_KEY)
├── .gitignore              # .env 등 민감 정보 제외
├── PRD_업무말투변환기.md     # 제품 요구사항 명세서
└── 개요서_업무말투변환기.md    # 프로그램 개요
```

---

## 4. 빌드 및 실행 가이드 (Build & Run)

### 백엔드 (Backend)
- **환경 준비**: `python -m venv venv` 후 가상환경 활성화.
- **패키지 설치**: `pip install -r backend/requirements.txt`
- **실행**: `uvicorn backend.main:app --reload --port 8000`
- **상태 확인**: `GET /health` 호출 시 `{"status": "ok"}` 응답 확인.

### 프론트엔드 (Frontend)
- `frontend/index.html` 파일을 브라우저에서 직접 열거나, VS Code Live Server 등을 사용하여 실행.

---

## 5. 개발 컨벤션 (Conventions)

- **언어**: 모든 소스 코드 주석 및 문서화는 **한국어**를 기본으로 하되, 기술 용어는 필요시 영문을 병기합니다.
- **환경 변수**: `UPSTAGE_API_KEY`는 반드시 `.env` 파일에서 관리하며, 절대 버전 관리 시스템에 노출하지 않습니다.
- **프롬프트 전략**: 수신 대상(`boss`, `colleague`, `client`, `team`)에 따라 `prompts/templates.py`에 정의된 전용 시스템 프롬프트를 사용합니다.

---

## 6. 에이전트 전용 작업 지침

- **구현 전 확인**: `context7` 도구를 사용하여 `langchain-upstage`와 `Solar-Pro3` 모델의 최신 사용법을 항상 먼저 확인하십시오.
- **보안 준수**: `my-rules.md`에 정의된 Git 관련 금지 행위 및 환경 변수 노출 금지 규칙을 절대적으로 준수하십시오.
- **보고 방식**: 5단계 이상의 복잡한 작업은 시작 전 전체 계획을 사용자에게 공유하십시오.
---
### @PRD_업무말투변환기.md 문서와 GEMINI.md 문서 항상 최신화 하기
* 모든 변경사항이 발생하면 (예를 들어 Source Code가 변경 되거나 라이브러리 버전이 변경되면) md 문서도 반드시 업데이트 합니다. 
* 구현이 완료된 사항들은 `2. 완료 체크리스트`에 모두 체크표시를 해서 완료 되었음을 반드시 표시하세요.
* `8. 단계별 구현 순서` 에서도 STEP별로 구현이 완료되면 체크표시를 해서 완료 되었음을 반드시 표시하세요.

--- 
### .env 환경변수 수정 금지
* .env 파일을 절대로 수정하지 마세요.