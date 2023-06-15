FROM conda/miniconda3:latest

WORKDIR /

# Reset to root to run installation tasks
USER 0

# 압축된 가상 환경 복사
COPY environment.tar.gz /

# 가상 환경 압축 해제
RUN mkdir -p /opt/conda/envs/pyspark \
    && tar -xzf /environment.tar.gz -C /opt/conda/envs/pyspark \
    && rm /environment.tar.gz

## 가상 환경 활성화 및 필요한 패키지 설치
##ENV PATH="/opt/conda/bin:$PATH"
#RUN conda install --name pyspark --yes --file requirements.txt
#
## 나머지 파일 및 코드 복사
#COPY . /app
#WORKDIR /app
#
## Spark-submit 명령어
#CMD spark-submit \
#    --master k8s://https://34.132.214.250 \
#    --deploy-mode cluster \
#    --name tutorial-spark-on-k8s \
#    --conf spark.executorEnv.PYTHONPATH="/opt/conda/envs/pyspark/bin/python" \
#    --conf spark.pyspark.python="/opt/conda/envs/pyspark/bin/python" \
#    --conf spark.pyspark.driver.python="/opt/conda/envs/pyspark/bin/python" \
#    --py-files /app/main.py \
#    /app/main.py
