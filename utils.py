#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from pdf2image import convert_from_path
from thirdweb import ThirdwebSDK
import os

sdk = ThirdwebSDK.from_private_key(os.getenv("PRIVATE_KEY"), "mumbai")
storage = sdk.storage

def convert_pdf_to_image(pdf_path):
    images = convert_from_path(pdf_path)
    image_path = pdf_path.replace(".pdf", ".png")
    images[0].save(image_path, "PNG")
    return image_path

def upload_to_ipfs(file_path):
    with open(file_path, "rb") as f:
        cid = storage.upload(f)
    return f"ipfs://{cid}"

