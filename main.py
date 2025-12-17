import argparse
import sys
import os
import cv2

# YOLO 로그가 터미널에 출력되어 채점에 방해되지 않게 설정
os.environ['YOLO_VERBOSE'] = 'False'
from ultralytics import YOLO

def parse_args():
    p = argparse.ArgumentParser("CV assignment runner")
    # 1. 인자파싱
    # Sample argument usage
    p.add_argument("--input", required=True, type=str, help="path to input image")
    p.add_argument('--task', type=str, required=True, choices=['presence', 'bbox'], help='Task type')
    # p.add_argument("--output", required=True, type=str, help="path to output image")
    p.add_argument('--debug', action='store_true', help='Show image with bounding box for debugging')

    return p.parse_args()

def main():

    args = parse_args()

    # 이미지 경로 검증
    if not os.path.exists(args.input):
        # 파일이 없으면 그냥 종료
        sys.exit(1)

    # 2. 모델 로드
    # pt 파일 불러옴
    model_path = os.path.join(os.path.dirname(__file__), 'best3.pt')
    try:
        model = YOLO(model_path)
    except Exception as e:
        # 모델 로드 실패 시 종료
        sys.exit(1)

    # 3. 추론
    # conf=0.25: 신뢰도가 0.25 이상인 것만 검출 (필요시 조절해야함)
    # save=False: 이미지를 저장하지 않음
    results = model.predict(source=args.input, conf=0.25, save=False, verbose=False)

    # 결과는 리스트로 반환됨 (이미지 1장이므로 첫 번째 요소)
    result = results[0]

    if args.debug:
        # result.plot()은 바운딩 박스가 그려진 이미지(numpy 배열)를 반환
        annotated_frame = result.plot()

        # 이미지 띄우기
        cv2.imshow("Debug Result", annotated_frame)
        print("[DEBUG] 아무 키나 누르면 닫힙니다...")
        cv2.waitKey(0)  # 키 입력 대기
        cv2.destroyAllWindows()

    # 4. Task별 출력 처리
    if args.task == 'presence':
        # N Seoul Tower가 있는지를 true/false 소문자 출력
        if len(result.boxes) > 0:
            print("true")
        else:
            print("false")

    elif args.task == 'bbox':
        # 위치를 bounding box로 출력
        if len(result.boxes) > 0:
            # 가장 신뢰도가 높은 박스 1개만 선택
            # boxes.xyxy로 좌상단(x1, y1), 우하단(x2, y2) 좌표 뽑음
            box = result.boxes[0]
            x1, y1, x2, y2 = box.xyxy[0].tolist()

            # 출력 포맷: x,y,width,height
            # 좌표 계산
            x = x1
            y = y1
            w = x2 - x1
            h = y2 - y1

            #  값은 모두 정수만, 반올림, 쉼표 구분, 공백 없음
            print(f"{int(round(x))},{int(round(y))},{int(round(w))},{int(round(h))}")
        else:
            # 타워가 없을 경우 none 출력
            print("none")


    # return 0

if __name__ == "__main__":
    sys.exit(main())
