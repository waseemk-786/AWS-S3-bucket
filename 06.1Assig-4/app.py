import boto3
import streamlit as st
st.title("Listing objects in ")

file=st.file_uploader("Uplaod file")

s3=boto3.client('s3')
response = s3.create_bucket(
    Bucket='waseem'
  
)
response=s3.client.upload_file('c://Users//Waseem K//Desktop//Intership//Day2//06.1Assig-4', 'waseem', 'hello.txt')