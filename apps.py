#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import os
from utils import convert_pdf_to_image, upload_to_ipfs
from nft_minter import mint_certificate

st.title("Coursemon NFT Certificate Converter with Royalties")

uploaded_files = st.file_uploader("Upload certificate(s) (PDF)", type=["pdf"], accept_multiple_files=True)
cert_desc = st.text_area("Certificate Description (applied to all)")

if st.button("Convert & Mint NFTs"):
    if uploaded_files:
        for uploaded_file in uploaded_files:
            cert_name = os.path.splitext(uploaded_file.name)[0]
            with open(uploaded_file.name, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            image_path = convert_pdf_to_image(uploaded_file.name)
            ipfs_url = upload_to_ipfs(image_path)
            tx = mint_certificate(cert_name, cert_desc, ipfs_url)
            
            st.success(f"NFT for {cert_name} minted!")
            st.markdown(f"[View on OpenSea](https://testnets.opensea.io/assets/mumbai/{tx.receipt['contractAddress']}/{tx.id})")
    else:
        st.error("Please upload at least one certificate.")

