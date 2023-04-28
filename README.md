# practice-tensorflow

## 0.tutorial-tensorflow
> https://www.tensorflow.org/tutorials/load_data/images?hl=ko

tensorflow 공식 래퍼런스를 통해 기본적인 tensorflow 모델링 과정을 진행해본다

## 1.build-model

* step1
	- DeepFashion, DeepFashion2 데이터셋을 사용 (약 백만개)
	- 무슨 옷인지 분류하는 모델을 학습
        + 데이터셋 준비 deepFashion: https://mmlab.ie.cuhk.edu.hk/projects/DeepFashion.html
		+ 데이터셋에서 옷 이미지와 필요한 레이블을 전처리
		+ 사용할 모델 선정
		+ 모델 학습, 파인 튜닝
		+ 예측해보기
* step2
	- gradio를 붙여서 이미지를 입력으로 받고, 출력으로 무슨 옷인지 분류
* step3
	- GCP 신규 계정 발급
	- GCS에 모델 업로드
	- 모델은 어디에 띄우지? EC2에 띄워야 하나..Vertex AI ? docker image로 띄우려면 image registry도 필요하겠네..
	- github action 붙여서 새로운 코드 배포 자동화
* step4
	- GCS에 데이터셋 업로드
	- github action 붙여서 새로운 데이터셋 배포 자동화
* step5
	- 모델 전처리, 학습, 파인튜닝 과정을 kubeflow로 옮기기. (TFX는 안써도되나?)
	- github action, kubeflow 연동
