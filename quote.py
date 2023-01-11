import openai
import pytesseract
import cv2
import os
import requests
import io
from PIL import Image
import numpy as np

openai.api_key = os.getenv('api_key_openai')


def image_to_text(img):
    # img=cv2.imread(rf'{img_path}')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    thresh,binary_img = cv2.threshold(gray,128,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU) 
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(binary_img)
    return text


def quote_meaning(quote:str):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"what is the meaning of this quote '{quote}' ",
    temperature=0.3,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    return response['choices'][0]['text']


def generte_quote_meaning_image(quote:str):
    generation_response = openai.Image.create(
    prompt=f"convert this '{quote}' to an image",
    n=1,
    size="512x512",
    response_format="url",
)
    generated_image_url = generation_response["data"][0]["url"]
    # generated_image_url

    img=requests.get(generated_image_url)
    realimg=Image.open(io.BytesIO(img.content))
    return np.asarray(realimg)

