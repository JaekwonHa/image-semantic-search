from pyspark.sql import SparkSession
from pyspark.sql.functions import rand

# Spark Context 생성
spark = SparkSession.builder \
    .appName("Random Number Generator") \
    .getOrCreate()

# 랜덤 숫자 생성을 위한 DataFrame 생성
df = spark.range(1000)  # 0부터 999까지의 숫자 생성

# 랜덤값 열 추가
df = df.withColumn("random_number", rand())

# 파티션 수 조정
df = df.repartition(5)

# DataFrame 출력
df.show()

# Spark Context 종료
spark.stop()
