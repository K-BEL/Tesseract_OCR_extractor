import requests, os, sys

model_id = ''
api_key = ''

url = 'https://app.nanonets.com/api/v2/ObjectDetection/Model/' + model_id + '/LabelFile/'

data = {'file': open(r'C:\Users\LENOVO\Desktop\OCR_extraction\Image_extraction\img.jpg', 'rb'),    'modelId': ('', model_id)}

response = requests.post(url, auth=requests.auth.HTTPBasicAuth(api_key, ''), files=data)

print(response.text)