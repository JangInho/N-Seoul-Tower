# N Seoul Tower

OpenCV 기반으로 이미지 내에 N서울타워(N Seoul Tower)가 있는지의 여부와 위치를 예측하는 코드를 작성하세요.
사전 학습된 모델(pretrained model)과 임의의 Python package 사용도 가능합니다.
단, 실행에 필요한 패키지는 requirements.txt에 모두 명시되어 있어야 합니다.
pip i -r requirements.txt 로 설치할 예정이며, 이 과정을 거친 후에도 실행이 되지 않는 경우 실행 불가로 0점 처리됩니다.

## N서울타워의 존재 여부
이미지 내에 객체가 존재할 경우 true 그렇지 않을 경우 false만 소문자로 출력하세요.
임의로 true 혹은 false만 출력할 경우 0점 처리합니다.

## N서울타워의 위치
이미지 내에서 객체의 위치를 x,y,width,height 형태로 한 줄로 출력하세요.
- 각 좌표는 쉼표(,)로 구분하고, 띄어쓰기 없이 모두 붙여주세요.
- 값은 모두 정수만 허용합니다. 실수값은 정수로 반올림하여 출력하세요.
- 타워가 없을 경우 소문자로 none 만 출력하세요.

# 사전 학습 모델 사용 관련 주의 사항
본 과제에서는 OpenAI API, Claude API, Google Gemini API, Llava, Qwen-VL 등 **외부 API 기반의 대규모 비전/언어 모델을 사용하여 문제를 해결하는 것은 엄격히 금지**합니다.
즉, 이미지를 외부 API 서버에 업로드하여 객체 존재 여부 또는 bounding box를 생성하는 모든 방식은 금지됩니다.

다만 아래의 방법들은 허용됩니다.
* 로컬 환경에서 직접 실행하는 오픈소스 모델 사용
  * GPU 또는 CPU에서 직접 inference 수행하는 경우
* 직접 학습한 custom detector 사용
* OpenCV 기반의 특징점, template matching, ML 활용 등 로컬 처리
* Pretrained CNN backbone 활용
즉, 이미지 데이터가 외부 서보로 전송되지 않는 방식은 허용됩니다.

위반시 처리
* 이번 과제 **전체 0점 처리**
* 필요시 로그/코드 검증 진행 (API key 사용 흔적, HTTP request 로그 등)

# 입출력 예시
## (존재 여부 확인 - presence) 입력 예시
```bash
python main.py --input path/to/image.jpg --task presence
```
- input의 인자로 이미지의 파일명(현재 폴더가 아닌 경우 경로 포함)을 명령행 인자로 입력
- 자동 채점 시 script 상에서 project 폴더 밖에 있는 다른 경로에 있는 이미지를 사용할 예정

## (존재 여부 확인 - presence) 출력 예시
```bash
true
```

## (위치 - bbox) 입력 예시 1
```bash
python main.py --input path/to/image.jpg --task bbox
```
- input의 인자로 이미지의 파일명(현재 폴더가 아닌 경우 경로 포함)을 명령행 인자로 입력
- 자동 채점 시 script 상에서 project 폴더 밖에 있는 다른 경로에 있는 이미지를 사용할 예정

## (위치 - bbox)출력 예시 1
```bash
300,200,50,150
```


## (위치 - bbox) 입력 예시 2
```bash
python main.py --input path/to/image.jpg --task bbox
```
- input의 인자로 이미지의 파일명(현재 폴더가 아닌 경우 경로 포함)을 명령행 인자로 입력
- 자동 채점 시 script 상에서 project 폴더 밖에 있는 다른 경로에 있는 이미지를 사용할 예정

## (위치 - bbox)출력 예시 2
```bash
none
```


# 과제 시작하기
1. Repository clone 하기 (<your-assignment-repo-url> 부분은 본인의 github repo 주소로 치환)
```bash
git clone <your-assignment-repo-url>
cd <your-assignment-repo>
```

2. (권장사항) Virtual environment 생성 (아래의 .venv 는 가상환경의이름이면서 venv가 위치할 경로) 
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. 필요 패키지 설치
```bash
pip install -r requirements.txt
```
- 채점을 위한 가상 환경에서 원본 requirements.txt로 필요 패키지들을 설치한 후 채점 수행
- 과제에서 requirements.txt를 수정해도 된다고 명시된 경우에만 매번 위의 명령어로 패키지들을 설치 후 채점 수행
- 만약 requirements.txt 수정 불가 과제에서 추가로 필요한 패키지가 있다면 메일로 문의

# 사용 패키지
- NumPy 2.2.6
- opencv-python 4.12.0.88

# 📦 과제 제출하기
1. 코드가 오류 없이 실행되는지 확인하세요.
2. 다양한 입력으로로 테스트해보세요.
3. 모든 요구사항을 만족하는지 검증하세요.
4. 변경사항을 Github에 ***commit***하고 ***push***하세요.
   - ⚠️ push되지 않은 내용은 채점되지 않습니다.
   - ⚠️ commit log는 사후 검증에 활용될 수 있습니다.

# 주의사항
- 채점에는 Python 3.13 버전을 사용합니다.
- main.py에서 *main* 함수를 수정하여 과제를 수행하세요.
- 과제 조건에 따라 *parse_args* 함수를 수정하여 과제를 수행하세요.
- 필요에 따라 새로운 함수나 파일을 추가하셔도 됩니다.
- *sys.exit(main())* 부분은 수정하지 마세요.
- 과제에서 명시하는 경우를 제외하고는 requirements.txt 파일을 수정하지 마세요.

# 채점 기준
- 채점시 repository를 clone 받아서, requirements.txt를 기준으로 패키지들을 설치합니다.
- main.py 파일을 명령행 인자(command-line arguments)와 함께 실행합니다.
- 출력물로 지정된 문자열 혹은 image 외에 다른 출력이 나올 경우 오답 처리 됩니다.
  - 예시) Hello가 정답인 경우
    - ❌ 대소문자 불일치: hello 는 오답 처리
  - 예시) 3이 정답인 경우: 
    - ❌ 불필요한 추가 문자열: (정답은 3) 는 오답 처리
  - 예시) 5,2가 정답인 경우: 
    - ❌ 불필요한 빈 칸: 5, 2 는 오답처리


# 📚 참고자료
- [OpenCV Documentation](https://docs.opencv.org/)
- [NumPy Documentation](https://numpy.org/doc/)
- [Python Argparse Tutorial](https://docs.python.org/3/library/argparse.html)

# 자주 발생하는 오류
1. **ImportError**: 필요한 패키지가 모두 설치되었는지 확인하세요
   ```bash
   pip install -r requirements.txt
   ```

2. **FileNotFoundError**: 입력 파일이 존재하는지, 경로가 올바른지 확인하세요

3. **Permission Error**: 출력 디렉토리에 쓰기 권한이 있는지 확인하세요

4. **Memory Error**: 큰 이미지의 경우, 청크 단위로 처리하거나 이미지 크기를 줄이는 것을 고려하세요
