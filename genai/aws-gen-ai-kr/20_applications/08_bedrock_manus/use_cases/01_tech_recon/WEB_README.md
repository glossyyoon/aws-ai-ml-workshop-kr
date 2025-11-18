# Tech Recon 웹 인터페이스

터미널 대신 웹 브라우저에서 Tech Recon 프로젝트를 실행하고 모니터링할 수 있는 웹 애플리케이션입니다.

## 주요 기능

- **실시간 로그 스트리밍**: WebSocket을 통해 실행 과정을 실시간으로 확인
- **Part1/Part2 실행**: 웹 UI에서 버튼 클릭으로 실행
- **파일 다운로드**: 생성된 artifacts 파일들을 개별 또는 ZIP으로 다운로드
- **시각적 모니터링**: 실행 상태, 로그 수, 파일 수 등을 한눈에 확인

## 설치 방법

### 1. 필요한 패키지 설치

```bash
# 프로젝트 디렉토리로 이동
cd /home/sagemaker-user/jiyunp/aws-ai-ml-workshop-kr/genai/aws-gen-ai-kr/20_applications/08_bedrock_manus/use_cases/01_tech_recon

# 웹 애플리케이션 패키지 설치
pip install -r requirements_web.txt
```

또는 기존 가상환경을 사용하는 경우:

```bash
# 가상환경 활성화
source .venv/bin/activate

# 패키지 설치
pip install flask flask-socketio python-socketio
```

### 2. 환경 변수 설정

기존 `.env` 파일이 설정되어 있어야 합니다. (AWS Bedrock 등의 API 키)

## How to Run

### Method 1: Using Start Script (Recommended)

```bash
# Navigate to project directory
cd /home/sagemaker-user/jiyunp/aws-ai-ml-workshop-kr/genai/aws-gen-ai-kr/20_applications/08_bedrock_manus/use_cases/01_tech_recon

# Run the start script
./start_web.sh
```

### Method 2: Manual Execution

```bash
# Navigate to project directory
cd /home/sagemaker-user/jiyunp/aws-ai-ml-workshop-kr/genai/aws-gen-ai-kr/20_applications/08_bedrock_manus/use_cases/01_tech_recon

# Activate virtual environment
source .venv/bin/activate

# Install required packages (first time only)
pip install flask flask-socketio python-socketio

# Run web server
python web_app.py
```

When the web server starts, you'll see this message:

```
============================================================
Tech Recon Web Application
============================================================
Server starting at: http://localhost:5000
Press Ctrl+C to stop the server
============================================================
```

## 사용 방법

### 1. 웹 브라우저 접속

```
http://localhost:5000
```

로컬에서 실행 중이므로 브라우저에서 위 주소로 접속합니다.

### 2. 실행

1. **Part1 실행** 또는 **Part2 실행** 버튼 클릭
2. 확인 대화상자에서 "확인" 클릭
3. 실시간 로그 화면에서 진행 상황 확인

### 3. 로그 모니터링

- **실시간 로그**: 왼쪽 패널에서 실시간으로 로그 확인
- **자동 스크롤**: 기본적으로 활성화되어 있으며, 토글 가능
- **로그 지우기**: "로그 지우기" 버튼으로 화면 정리
- **색상 코딩**:
  - 🔵 파란색: Reasoning (추론 과정)
  - 🟡 노란색: Tool Use (도구 사용)
  - 🟢 녹색: Tool Result (도구 실행 결과)
  - 🔴 빨간색: Error (오류)
  - ⚪ 흰색: 일반 텍스트

### 4. 파일 다운로드

#### 개별 파일 다운로드
- 오른쪽 패널의 "생성된 파일" 섹션에서 파일별 "다운로드" 버튼 클릭

#### 전체 파일 다운로드 (ZIP)
- **Part1 전체**: Part1에서 생성된 모든 파일을 ZIP으로 다운로드
- **Part2 전체**: Part2에서 생성된 모든 파일을 ZIP으로 다운로드
- **모든 파일 다운로드**: Part1과 Part2 전체를 하나의 ZIP으로 다운로드

## 화면 구성

### 상단 헤더
- 프로젝트 제목과 설명

### 왼쪽 패널 (로그 섹션)
- 실행 상태 표시 (대기 중 / 실행 중 / 완료 / 오류)
- 실시간 로그 화면
- 로그 제어 버튼 (지우기, 자동 스크롤)

### 오른쪽 패널 (제어판)
- **통계**: 로그 엔트리 수, 생성된 파일 수
- **실행 제어**: Part1/Part2 실행 버튼
- **파일 다운로드**: 전체 다운로드 버튼
- **생성된 파일 목록**: 파일 이름, 크기, Part 구분, 개별 다운로드

### 하단 우측
- 연결 상태 표시 (연결됨 / 연결 끊김)

## 기술 스택

- **Backend**: Flask, Flask-SocketIO
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **실시간 통신**: WebSocket (Socket.IO)
- **비동기 처리**: Python asyncio

## API 엔드포인트

### REST API
- `GET /`: 메인 페이지
- `POST /api/start`: 실행 시작
- `GET /api/status`: 현재 상태 조회
- `GET /api/logs`: 로그 조회
- `GET /api/files`: 파일 목록 조회
- `GET /api/download/<path>`: 개별 파일 다운로드
- `GET /api/download-all/<part>`: 전체 파일 ZIP 다운로드

### WebSocket Events
- `connect`: 클라이언트 연결
- `disconnect`: 클라이언트 연결 해제
- `log`: 로그 메시지 전송 (서버 → 클라이언트)
- `status`: 상태 변경 전송 (서버 → 클라이언트)

## 주의사항

1. **방화벽**: 포트 5000이 열려있어야 합니다
2. **동시 실행**: 한 번에 하나의 Part만 실행 가능
3. **브라우저 호환성**: 최신 버전의 Chrome, Firefox, Safari, Edge 권장
4. **네트워크**: 로컬 네트워크에서만 접근 가능 (0.0.0.0:5000)

## 트러블슈팅

### 연결이 안 될 때
```bash
# 포트 사용 확인
lsof -i :5000

# 프로세스 종료
kill -9 <PID>
```

### 패키지 오류
```bash
# 패키지 재설치
pip install --upgrade flask flask-socketio python-socketio
```

### 로그가 표시되지 않을 때
- 브라우저 개발자 도구 (F12) 콘솔에서 에러 확인
- WebSocket 연결 상태 확인 (하단 우측 표시)

## 기존 터미널 방식과 비교

| 항목 | 터미널 방식 | 웹 인터페이스 |
|------|------------|--------------|
| 실행 | `python main.py` | 브라우저에서 버튼 클릭 |
| 로그 확인 | 터미널 출력 | 웹 페이지 실시간 표시 |
| 파일 다운로드 | 직접 파일 탐색 | 웹에서 버튼 클릭 |
| 상태 모니터링 | 수동 확인 | 실시간 통계 표시 |
| 접근성 | 로컬 터미널만 | 브라우저에서 접근 가능 |

## 라이선스

이 프로젝트는 원본 Tech Recon 프로젝트의 라이선스를 따릅니다.

## 문의

문제가 발생하거나 기능 개선 제안이 있으시면 이슈를 등록해주세요.
