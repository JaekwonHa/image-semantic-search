import os.path

import gradio as gr
import tensorflow as tf
from google.cloud import storage

def download_from_gcs(bucket_name, source_blob_name, destination_file_name):
    """Download a file from GCS bucket."""
    # 파일이 이미 존재하는지 확인
    if os.path.exists(destination_file_name):
        print(f"File {destination_file_name} already exists. Skipping download.")
        return

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)
    print(f"File {source_blob_name} downloaded to {destination_file_name}.")

bucket_name = 'practice-tensorflow'
source_blob_name = '2.build-tensorflow-model/models/my_model.h5'
destination_file_name = '/2.build-tensorflow-model/models/my_model.h5'

# GCS에서 모델을 다운로드합니다.
download_from_gcs(bucket_name, source_blob_name, destination_file_name)

# 모델을 로드합니다.
model = tf.keras.models.load_model('/2.build-tensorflow-model/models/my_model.h5')

img_height = 224
img_width = 224

# Category 정보 로드
def load_categories(list_category_cloth_path):
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)

    # Read image_paths from GCS
    blob = bucket.blob(list_category_cloth_path)
    content = blob.download_as_text()

    categories = {i: line.split()[0] for i, line in enumerate(content.split('\n')[2:-1], 1)}
    return categories

list_category_cloth_path = '2.build-tensorflow-model/data/list_category_cloth.txt'
categories = load_categories(list_category_cloth_path)

# Gradio 인터페이스를 정의합니다.
def classify_image(image):
    img = tf.image.resize(image, (img_height, img_width))
    img = img[tf.newaxis, ...]
    pred = model.predict(img)
    pred_label = categories[pred.argmax()]
    return pred_label


iface = gr.Interface(
    fn=classify_image,
    inputs=gr.inputs.Image(shape=(224, 224)),
    outputs=gr.outputs.Label(num_top_classes=len(categories)),
    capture_session=True
)
iface.launch()
