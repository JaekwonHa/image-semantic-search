# Stage 1: Pyspark 환경 설치
FROM python:3.11 as pyspark

WORKDIR /

# 필요한 Pyspark 관련 패키지 설치 등의 작업 수행
RUN wget https://dlcdn.apache.org/spark/spark-3.4.0/spark-3.4.0-bin-hadoop3.tgz

RUN mkdir /opt/spark
RUN tar -xvf spark-3.4.0-bin-hadoop3.tgz -C /opt/spark \
    && rm spark-3.4.0-bin-hadoop3.tgz

# Stage 2: Pyspark 어플리케이션 빌드
FROM continuumio/miniconda3

WORKDIR /

# Java 환경 구성
RUN apt update \
    && apt install default-jdk -y
ENV JAVA_HOME="/usr/lib/jvm/java-11-openjdk-amd64"

# Pyspark 환경 구성
COPY --from=pyspark /opt/spark/spark-3.4.0-bin-hadoop3 /opt/spark
ENV PATH="/opt/spark/bin:$PATH"

# Python 환경 구성
COPY environment.yaml /environment.yaml
RUN conda env create -n pyspark --file /environment.yaml
