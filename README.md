# practice-tensorflow

## 0.tutorial-tensorflow
> https://www.tensorflow.org/tutorials/load_data/images?hl=ko

* step1 
    - tensorflow 공식 래퍼런스를 통해 기본적인 tensorflow 모델링 과정을 진행해본다

## 1.build-model

* step1
	- 데이터셋 준비 deepFashion: https://mmlab.ie.cuhk.edu.hk/projects/DeepFashion.html
	- GCP 신규 계정 발급
	- 데이터셋 업로드 (GCS)
	- 데이터셋에서 옷 이미지와 필요한 레이블을 전처리
	- 사용할 모델 선정
	- 모델 학습, 파인 튜닝
	- 예측해보기
	- 모델 저장 (GCS)
* step2
	- 모델 로드 (GCS)
	- gradio를 붙여서 이미지를 입력으로 받고, 출력으로 무슨 옷인지 분류

## 2.pipeline

* step1
	- local에서 파이프라인 구축
	- 모델 전처리, 학습, 파인튜닝 과정을 kubeflow로 옮기기. (TFX는 안써도되나?)
* step2
	- GCS k8s 클러스터에 구축
	- GCS에 gradio 앱 배포
* step3
	- github action 붙여서 새로운 코드 배포 자동화
	- github action 붙여서 새로운 데이터셋 배포 자동화

## 3.advance

* DVC, feast, offline/online 등을 해보거나 다음 프로젝트로 넘어가기
* dataflow, autoML, Vertex AI Training
* katib
 