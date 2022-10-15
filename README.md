# Detection & Tracking platform
>무거운 짐을 로봇이 대신 들고 이동해줄 수 있도록 사용자를 따라가는 플랫폼 제작

</br>

## 1. 제작 기간 & 참여 인원
- 2020년 3월 ~ 2020년 11월
- 팀프로젝트 (팀원 3명)

</br>

## 2. 역할
카메라를 통해 이미지에서 사용자의 위치를 파악하는 역할

</br>

## 3. 사용 기술
- python
- opencv
- tensorflow
- object detection
- SORT

</br>

## 4. file 설명
### 'object_tracker.py' 
- main 실행 코드, 처음으로 카메라 가운데에 인식된 사람을 사용자로 인식하여 그 사용자의 수평방향 위치를 파악
- https://github.com/sinjy1203/object-tracker/blob/d30e566b05485518d6c7e5052f69883231e559fd/object_tracker.py#L121-L136
### 'util/login' 
- 사용자의 id를 저장하고 사용자의 수평방향 위치를 리턴
- https://github.com/sinjy1203/object-tracker/blob/master/util.py

https://github.com/theAIGuysCode/yolov3_deepsort 사용

</br>

## 5. 트러블 슈팅
### 처리 속도 문제
- cpu만으로는 연산속도가 느려서 실시간 사용자 추적이 불가능 하였다.
- 그래픽카드를 설치하여 gpu를 통한 연산으로 실시간 추적이 가능하도록 하였다.
### 사용자 구분 문제
- yolo만을 사용했을 때 이미지에서 사람을 감지하는 것은 가능했지만 여러 사람이 동시에 있을 때는 사용자만을 구별할 수 없었다.
- 사람들 중에서도 각각을 구별할 수 있도록 SORT와 yolo가 합쳐진 deepsort를 사용하여 사용자만을 구별할 수 있게 하였다.
