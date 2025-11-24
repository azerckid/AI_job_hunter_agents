# Job Hunter Agent (AI 취업 에이전트)

CrewAI와 Gemini를 활용하여 구직 과정을 자동화해주는 AI 에이전트입니다. 채용 공고 검색부터 적합도 분석, 이력서 최적화, 기업 조사, 면접 준비까지 도와줍니다.

## 🚀 주요 기능

1.  **채용 공고 검색 (Job Search)**: 사용자의 희망 직무, 레벨, 위치에 맞는 공고를 웹에서 검색하고 스크래핑합니다.
2.  **직무 매칭 분석 (Job Matching)**: 사용자 이력서와 공고를 비교하여 적합도를 점수(1-5)로 매기고 이유를 설명합니다.
3.  **최고의 공고 선정 (Job Selection)**: 분석된 공고 중 사용자의 스킬과 선호도에 가장 잘 맞는 공고를 선정합니다.
4.  **이력서 최적화 (Resume Optimization)**: 선정된 공고에 맞춰 사용자 이력서를 재작성합니다. (사실을 기반으로 내용을 강조하며, 허위 사실은 추가하지 않습니다.)
5.  **기업 조사 (Company Research)**: 선정된 기업의 미션, 가치, 최근 뉴스, 면접 예상 질문 등을 조사합니다.
6.  **면접 준비 (Interview Prep)**: 직무, 최적화된 이력서, 기업 분석을 바탕으로 종합적인 면접 준비 가이드를 제공합니다.

## 🛠️ 설치 및 실행

### 필수 조건
- Python 3.13 이상
- [Firecrawl](https://www.firecrawl.dev/) API Key
- Google Gemini API Key

### 1. 저장소 클론
```bash
git clone <repository-url>
cd 3_job-hunter-agent
```

### 2. 의존성 설치
이 프로젝트는 `uv`를 사용하여 패키지를 관리합니다.

```bash
# 가상환경 생성 및 패키지 동기화
uv sync
```

또는 `pip`를 사용할 경우:
```bash
pip install "crewai[google-genai,tools]>=0.152.0" "firecrawl-py>=2.16.3" "google-generativeai>=0.8.5" "python-dotenv>=1.1.1"
```

### 3. 환경 변수 설정
`.env` 파일을 생성하고 필요한 API 키를 입력하세요.

```env
# .env 예시
FIRECRAWL_API_KEY=fc_...
GOOGLE_API_KEY=AIza...
# CrewAI 모델 설정에 따라 필요한 키를 설정하세요 (예: OPENAI_API_KEY 등, 본 프로젝트는 Gemini 사용 설정됨)
```

### 4. 이력서 준비
`resume.txt` 파일을 루트 디렉토리나 `knowledge/` 폴더에 생성하고, 본인의 이력서 내용을 텍스트로 붙여넣으세요.

### 5. 실행
```bash
python main.py
```

실행 후 터미널의 안내에 따라 다음 정보를 입력하세요:
1.  **Position**: 희망 직무 (예: Full Stack Developer)
2.  **Level**: 경력 레벨 (예: Senior, Junior)
3.  **Location**: 희망 근무지 (예: Remote, Seoul, Korea)

## 📂 프로젝트 구조

```
3_job-hunter-agent/
├── config/
│   ├── agents.yaml       # 에이전트 정의 (역할, 목표, 배경)
│   └── tasks.yaml        # 태스크 정의 (설명, 예상 출력)
├── knowledge/
│   └── resume.txt        # (입력) 사용자 이력서 파일
├── output/               # (출력) 생성된 파일들이 저장되는 곳
│   ├── ranked_jobs.json
│   ├── chosen_job.json
│   ├── rewritten_resume.md
│   ├── company_research.md
│   └── interview_prep.md
├── main.py               # 메인 실행 파일 (CrewAI 설정 및 실행)
├── models.py             # 데이터 모델 (Pydantic)
├── tools.py              # 커스텀 도구 (Firecrawl 검색)
├── pyproject.toml        # 프로젝트 설정 및 의존성
└── README.md             # 프로젝트 설명서
```

## 📤 결과물 (Output)

실행이 완료되면 `output/` 폴더에 다음 파일들이 생성됩니다:

- **ranked_jobs.json**: 검색된 공고들과 매칭 점수 목록.
- **chosen_job.json**: 최종 선정된 공고의 상세 정보.
- **rewritten_resume.md**: 선정된 공고에 맞춰 최적화된 마크다운 형식의 이력서.
- **company_research.md**: 기업 분석 보고서 (개요, 미션, 면접 토픽 등).
- **interview_prep.md**: 최종 면접 준비 가이드 문서.

## ⚠️ 주의사항

- **이력서 내용**: `rewritten_resume.md`는 AI가 생성한 초안입니다. 실제 제출 전 반드시 내용을 확인하고 수정하세요.
- **API 비용**: Firecrawl 및 Gemini API 사용에 따른 비용이 발생할 수 있습니다.

---
Powered by [CrewAI](https://crewai.com) & [Gemini](https://deepmind.google/technologies/gemini/)
