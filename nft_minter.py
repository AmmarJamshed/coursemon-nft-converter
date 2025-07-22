#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from thirdweb import ThirdwebSDK
from thirdweb.types.nft import NFTMetadataInput
import os
from dotenv import load_dotenv

load_dotenv()

PRIVATE_KEY = os.getenv("PRIVATE_KEY")
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")

sdk = ThirdwebSDK.from_private_key(PRIVATE_KEY, "mumbai")
contract = sdk.get_nft_collection(CONTRACT_ADDRESS)

def mint_certificate(cert_name, cert_desc, cert_image_url):
    metadata = NFTMetadataInput.from_json({
        "name": cert_name,
        "description": cert_desc,
        "image": cert_image_url
    })
    tx = contract.mint(metadata)
    return tx

