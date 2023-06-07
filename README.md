# practice-tensorflow

## 1.tutorial-tensorflow
> https://www.tensorflow.org/tutorials/load_data/images?hl=ko

* step1 
    - tensorflow 공식 래퍼런스를 통해 기본적인 tensorflow 모델링 과정을 진행해본다

## 2.build-tensorflow-model

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

## 3.tutoral-kubeflow

* step1
	- local에서 파이프라인 구축
	- 모델 전처리, 학습, 파인튜닝 과정을 kubeflow로 옮기기. (TFX는 안써도되나?)
* step2
	- GCS k8s 클러스터에 구축
	- GCS에 gradio 앱 배포
* step3
	- github action 붙여서 새로운 코드 배포 자동화
	- github action 붙여서 새로운 데이터셋 배포 자동화

## 4.image-semantic-search

### step1
- 이미지 100개 정도를 벡터화해서 저장
- 벡터화된거 차원축소해서 클러스터링 해본다
- 최적 클러스터 개수는 실루엣점수, 그래프 사용해서 분석
	+ 근데 최적 클러스터의 개수를 구해서 어디에 쓰지? 그냥 바로 시멘틱 서치를 해보는게 의미 있지 않을까

### step2
* opensearch 구성
	* GCP VM Instance 생성(centos7)
	* opensearch 설치
	* opensearch.service 파일 생성
		- /etc/systemd/system/opensearch.sercice
	* VPC 네트워크 > 방화벽 규칙 생성 (0.0.0.0/0:9200)
	* opensearch 실행
	* opensearch 확인
		- `http://34.68.94.225:9200/_cluster/health`
* knn search 테스트
	- sample data gs 업로드
	- sample data 벡터화
	- index 생성
	- 색인
	- knn search
* 어플리케이션 로직 작성
	- knn search 결과를 다시 이미지로 보여주는 API

### step3
- 임베딩 인덱싱 pyspark 코드 작성
	+ 임베딩 모델은 spark executor 내부에서 로드
	+ spark executor는 gcp k8s에서 실행
	+ 인덱스 이름을 파라미터로 받도록 설정
- Docker 이미지로 빌드

### step4
* 임베딩 인덱싱 Kubeflow DAG 코드 작성

### step5
- 블로그 작성. 너무 자세하게 쓰기 보다는
* 별도 Repo로 분리하는게 필요할수도


## 99.advance

* DVC, feast, offline/online 등을 해보거나 다음 프로젝트로 넘어가기
* dataflow, autoML, Vertex AI Training
* katib
 