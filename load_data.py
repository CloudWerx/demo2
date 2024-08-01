from datasets import load_dataset
from google.cloud import storage
import json
import os
import uuid


def create_text_file(content, file_name):
   with open(file_name, 'w', encoding='utf-8') as f:
       f.write(content)


def upload_to_gcs(bucket_name, source_file_name, destination_blob_name):
   """Uploads a file to the bucket."""
   storage_client = storage.Client()
   bucket = storage_client.bucket(bucket_name)
   blob = bucket.blob(destination_blob_name)


   blob.upload_from_filename(source_file_name)


   print(f"File {source_file_name} uploaded to {destination_blob_name}.")




bucket_name = "cwx-aiml-demo-2-bucket-222222"


# Load the dataset
dataset_name = "xiyuez/red-dot-design-award-product-description"
dataset = load_dataset(dataset_name, split="train")


# Prepare JSONL and text files
jsonl_file = "red_dot_design_dataset_vertex.jsonl"
text_files_dir = "red_dot_design_text_files"


os.makedirs(text_files_dir, exist_ok=True)


with open(jsonl_file, 'w') as f:
   for idx, example in enumerate(dataset):
       # Create a unique document ID
       doc_id = str(uuid.uuid4())
      
       # Create text file
       text_file_name = f"{doc_id}.txt"
       text_file_path = os.path.join(text_files_dir, text_file_name)
       create_text_file(example['text'], text_file_path)
      
       # Create the JSON object
       json_object = {
           "id": doc_id,
           "structData": {
               "product": example['product'],
               "category": example['category'],
               "description": example['description']
           },
           "content": {
               "mimeType": "text/html",
               "uri": f"gs://{bucket_name}/{text_files_dir}/{text_file_name}"
           }
       }




       # Write the JSON object as a line in the file
       f.write(json.dumps(json_object) + '\n')


# Upload JSONL file to GCS
upload_to_gcs(bucket_name, jsonl_file, f"{text_files_dir}/{jsonl_file}")


# Upload text files to GCS
for file_name in os.listdir(text_files_dir):
   local_file_path = os.path.join(text_files_dir, file_name)
   upload_to_gcs(bucket_name, local_file_path, f"{text_files_dir}/{file_name}")


print(f"Dataset transformed and uploaded to GCS bucket {bucket_name}")


# Clean up local files
os.remove(jsonl_file)
for file_name in os.listdir(text_files_dir):
   os.remove(os.path.join(text_files_dir, file_name))
os.rmdir(text_files_dir)
print("Local files removed.")
