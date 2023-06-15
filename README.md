# practice-mlops

* 목표: image-semantic-search 어플리케이션 개발. 자동화된 MLOps 파이프라인 개발
* 기술 스택
	- tensorflow
	- kubeflow
	- spark
	- elasticsearch(vector search)
	- GCP
* advance 과제
	- offline/online 파이프라인 구분
	- DVC
	- feast
	- dataflow, autoML, Vertex AI Training
	- katib

## MLOps

### MLOps가 기본적으로 제공해야하는 기능
* 신규 '코드'가 들어왔을때 자동으로 잘 통합되어야한다. 제공이 가능해야한다
  - 학계에서 발표된 SOTA 알고리즘, 다른 방식의 피처 엔지니어링 구현
* 신규 '데이터'가 들어왔을때 자동으로 잘 통합되어야한다. 제공이 가능해야한다
  - 모델의 성능 저하로 데이터를 추가하여 모델을 재학습

### Machine learning workflow
1. 데이터 관리
2. 모델 학습
3. 모델 평가
4. 모델 배포
5. 예측 실행
6. 예측 관리

## 1.tutorial-tensorflow

* step1 
    - tensorflow 공식 래퍼런스를 통해 기본적인 tensorflow 모델링 과정을 진행해본다
* step2
	- 데이터셋 준비 deepFashion: https://mmlab.ie.cuhk.edu.hk/projects/DeepFashion.html
	- GCP 신규 계정 발급
	- 데이터셋 업로드 (GCS)
	- 데이터셋에서 옷 이미지와 필요한 레이블을 전처리
	- 사용할 모델 선정
	- 모델 학습, 파인 튜닝
	- 예측해보기
	- 모델 저장 (GCS)
    - gradio 어플리케이션 코드 작성

### 참고

* [tensorflow-tutorial](https://www.tensorflow.org/tutorials/load_data/images?hl=ko)

## 2.tutoral-kubeflow

* step1
	- local에서 파이프라인 구축
	- 모델 전처리, 학습, 파인튜닝 과정을 kubeflow로 옮기기
		+ TFX가 필수는 아님
* step2
	- GCS k8s 클러스터에 구축
	- kubeflow pipeline 설치
	- kubeflow DAG 배포, 실행

### 참고

* [[GCP] AI Platform에서 구현하는 Kubeflow Pipelines 기반 ML 학습 및 배포 예제 (Part 1/3)](https://medium.com/google-cloud-apac/gcp-ai-platform-%EC%97%90%EC%84%9C-%EA%B5%AC%ED%98%84%ED%95%98%EB%8A%94-kubeflow-pipelines-%EA%B8%B0%EB%B0%98-ml-%ED%95%99%EC%8A%B5-%EB%B0%8F-%EB%B0%B0%ED%8F%AC-%EC%98%88%EC%A0%9C-part-1-3-d49f1096d786)

## 3.tutorial-vector-search

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
	* issue
		- knn library를 찾지 못함
			+ export OPENSEARCH_JAVA_HOME=/home/tangojk0002/opensearch-2.8.0/jdk
			+ export KNN_LIB_DIR=/home/tangojk0002/opensearch-2.8.0/plugins/opensearch-knn/lib
			+ export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$KNN_LIB_DIR
		- 루프백 IP에 바인딩됨
			+ network.host: 0.0.0.0
			+ discovery.seed_hosts: ["0.0.0.0"]
		- tar 설치 과정에서 knn lib 연동에 실패하여 rpm 파일로 설치 진행
* knn search 테스트
	- sample data gs 업로드
	- sample data 벡터화
	- index 생성
	- 색인
		+ elasticsearch 7.12.1 사용
	- knn search
* 시각화 코드 작성
	- knn search 결과를 시각화 해주는 코드 작성

## 4.tutorial-spark-on-k8s

* 사전 검토
	+ spark-submit on k8s(GCP) 환경 구성
	+ Spark-submit vs Spark Operator
* 간단한 pyspark 어플리케이션 개발. local 환경에서 실행
* GCP k8s cluster 구성
* GCP Artifactory Registry 구성
* spark driver를 위한 k8s ServiceAccount 생성
* pyspark 어플리케이션 개발, image build, push
	+ 임베딩 모델은 spark executor 내부에서 로드
	+ 인덱스 이름을 파라미터로 받도록 설정
* spark-submit on k8s

## 5.image-semantic-search

* spark 어플리케이션 개발
* 임베딩 인덱싱 Kubeflow DAG 코드 작성
	* https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/pipelines/pipelines_intro_kfp.ipynb

## 6.정리
- 
- 블로그 작성. 너무 자세하게 쓰기 보다는 (영어로 하는게 좋을까?)
- 전체 시스템 구성도 작성
- 데모 페이지를 만들어서 보여주기? https://ai-demos.dev/demos/matching-engine
* 별도 Repo로 분리하는게 필요할수도. 그냥 이 repo의 이름을 image-semantic-search 로 변경하기
