# Job Hunter Agent (AI 취업 에이전트)

CrewAI와 Gemini를 활용하여 구직 과정을 자동화해주는 AI 에이전트입니다. 채용 공고 검색부터 적합도 분석, 이력서 최적화, 기업 조사, 면접 준비까지 도와줍니다.

## 📖 목차
- [주요 기능](#-주요-기능)
- [설치 및 실행](#-설치-및-실행)
  - [필수 조건](#-필수-조건)
  - [저장소 클론](#-저장소-클론)
  - [의존성 설치](#-의존성-설치)
  - [환경 변수 설정](#-환경-변수-설정)
  - [이력서 준비](#-이력서-준비)
  - [실행](#-실행)
- [커스터마이징](#-커스터마이징)
- [트러블슈팅](#-트러블슈팅)
- [프로젝트 구조](#-프로젝트-구조)
- [결과물 (Output)](#-결과물-output)
- [주의사항](#-주의사항)

## 🚀 주요 기능

1. **채용 공고 검색 (Job Search)**: 사용자의 희망 직무, 레벨, 위치에 맞는 공고를 웹에서 검색하고 스크래핑합니다.
2. **직무 매칭 분석 (Job Matching)**: 사용자 이력서와 공고를 비교하여 적합도를 점수(1-5)로 매기고 이유를 설명합니다.
3. **최고의 공고 선정 (Job Selection)**: 분석된 공고 중 사용자의 스킬과 선호도에 가장 잘 맞는 공고를 선정합니다.
4. **이력서 최적화 (Resume Optimization)**: 선정된 공고에 맞춰 사용자 이력서를 재작성합니다. (사실을 기반으로 내용을 강조하며, 허위 사실은 추가하지 않습니다.)
5. **기업 조사 (Company Research)**: 선정된 기업의 미션, 가치, 최근 뉴스, 면접 예상 질문 등을 조사합니다.
6. **면접 준비 (Interview Prep)**: 직무, 최적화된 이력서, 기업 분석을 바탕으로 종합적인 면접 준비 가이드를 제공합니다.

## 🛠️ 설치 및 실행

### 필수 조건
- **Python 3.13 이상**: 이 프로젝트는 최신 Python 기능을 사용합니다.
- **uv (권장)**: 빠르고 효율적인 패키지 관리를 위해 `uv` 사용을 권장합니다.
- **API Keys**:
  - [Firecrawl](https://www.firecrawl.dev/) (웹 검색 및 스크래핑용)
  - [Google Gemini](https://aistudio.google.com/) (AI 모델용)

### 1. 저장소 클론
```bash
git clone <repository-url>
cd 3_job-hunter-agent
```

### 2. 의존성 설치
이 프로젝트는 `uv`를 사용하여 의존성을 관리합니다.

**uv 사용 시 (권장):**
```bash
# 가상환경 생성 및 패키지 동기화
uv sync
```

**pip 사용 시:**
```bash
pip install "crewai[google-genai,tools]>=0.152.0" "firecrawl-py>=2.16.3" "google-generativeai>=0.8.5" "python-dotenv>=1.1.1"
```

### 3. 환경 변수 설정
프로젝트 루트에 `.env` 파일을 생성하고 필요한 API 키를 입력하세요.

```env
# .env
FIRECRAWL_API_KEY=fc_...
GOOGLE_API_KEY=AIza...
# CrewAI 모델 설정 (Gemini 사용 시 필수)
MODEL=gemini/gemini-1.5-pro
```

### 4. 이력서 준비
본인의 이력서 내용을 텍스트 파일로 준비해야 합니다.
1. 프로젝트 루트 또는 `knowledge/` 폴더에 `resume.txt` 파일을 생성합니다.
2. 이력서 내용을 복사하여 붙여넣습니다. (PDF나 Word 파일이 아닌 **순수 텍스트**여야 합니다.)

### 5. 실행
```bash
python main.py
```
실행 후 터미널의 안내에 따라 다음 정보를 입력하세요:
- **Position**: 희망 직무 (예: Full Stack Developer)
- **Level**: 경력 레벨 (예: Senior, Junior)
- **Location**: 희망 근무지 (예: Remote, Seoul, Korea)

## ⚙️ 커스터마이징

이 프로젝트는 `config/` 폴더 내의 YAML 파일을 통해 쉽게 수정할 수 있습니다.

- **`config/agents.yaml`**: 에이전트의 역할(Role), 목표(Goal), 배경 이야기(Backstory)를 수정하여 에이전트의 페르소나를 변경할 수 있습니다.
- **`config/tasks.yaml`**: 각 태스크의 설명(Description)과 예상 출력(Expected Output)을 수정하여 작업의 구체적인 지시사항을 변경할 수 있습니다.

## ❓ 트러블슈팅

**Q: `FileNotFoundError: Could not find resume.txt` 오류가 발생해요.**
A: `resume.txt` 파일이 프로젝트 루트 디렉토리나 `knowledge/` 폴더 안에 있는지 확인하세요. 파일명 철자가 정확한지 확인해 주세요.

**Q: API 관련 오류가 발생해요.**
A: `.env` 파일에 `FIRECRAWL_API_KEY`와 `GOOGLE_API_KEY`가 올바르게 설정되어 있는지 확인하세요. 또한, API 사용량 한도를 초과하지 않았는지 확인해 보세요.

**Q: `uv` 명령어를 찾을 수 없어요.**
A: `uv`가 설치되어 있지 않다면 `pip install uv`로 설치하거나, `pip`를 사용하여 의존성을 설치해 주세요.

## 📂 프로젝트 구조
```
3_job-hunter-agent/
├── config/
│   ├── agents.yaml       # 에이전트 설정
│   └── tasks.yaml        # 태스크 설정
├── knowledge/
│   └── resume.txt        # (사용자 제공) 이력서 파일
├── output/               # (자동 생성) 결과물 저장소
│   ├── ranked_jobs.json
│   ├── chosen_job.json
│   ├── rewritten_resume.md
│   ├── company_research.md
│   └── interview_prep.md
├── main.py               # 메인 실행 스크립트
├── models.py             # Pydantic 데이터 모델
├── tools.py              # 커스텀 도구 (Firecrawl)
├── pyproject.toml        # 프로젝트 의존성 설정
└── README.md             # 프로젝트 문서
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
