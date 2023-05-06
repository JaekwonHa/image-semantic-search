FROM amancevice/pandas
RUN pip3 install --upgrade pandas
RUN pip3 install --upgrade gcsfs
RUN pip3 install --upgrade argparse
RUN pip3 install scikit-learn
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /titanic/src
COPY . /titanic/src
WORKDIR /titanic/src
ENTRYPOINT ["python", "titanic_preprocess.py"]
