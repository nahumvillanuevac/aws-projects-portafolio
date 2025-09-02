import boto3
import os
import mimetypes
from datetime import datetime

# bucket name
BUCKET_NAME = "s3-file-organizer-nahum"

# define categories
CATEGORIES = {
    "images": [".jpg", ".jpeg", ".png", ".gif"],
    "docs": [".pdf", ".docx", ".txt"],
    "videos": [".mp4", ".avi", ".mov"],
    "misc": [] # fallback
}

# Initialize S3 client
s3 = boto3.client("s3")

def get_category(filename):
    ext = os.path.splitext(filename)[1].lower()
    for category, extensions in CATEGORIES.items():
        if ext in extensions:
            return category
    return "misc"

def upload_files(local_folder):
    log_file = "upload_log.txt"
    with open(log_file, "a") as log:
        for root, _, files in os.walk(local_folder):
            for file in files:
                print("Found file:", file)
                local_path = os.path.join(root, file)
                category = get_category(file)
                s3_key = f"{category}/{file}"

                try:
                    s3.upload_file(local_path, BUCKET_NAME, s3_key)
                    url = s3.generate_presigned_url(
                        "get_object",
                        Params={"Bucket": BUCKET_NAME, "Key": s3_key},
                        ExpiresIn=3600
                    )
                    msg = f"[{datetime.now()}] Uploaded: {file} -> {s3_key} | URL: {url}\n"
                    print(msg)
                    log.write(msg)
                except Exception as e:
                    print(f"Error uploading {file}: {e}")

if __name__ == "__main__":
    folder = input("Enter local folder path: ")
    upload_files(folder)
