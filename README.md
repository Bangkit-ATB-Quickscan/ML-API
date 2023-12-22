# ML API

## Trigger the ML function from the model and get the API prediction endpoint :
This is a python code, so make sure you have python installed on your system.

## Requirement
1. Make new project with billing account on gcp
2. Go to google cloud storage and make bucket with name _atbq_bucket_
3. On the bucket make folder with name _predict_uploads/_
4. Go to **IAM >> Service Account** and **create service account**, and then give role as **google cloud storage object admin**
5. Click the service account name that lates you create, go ro **KEYS** tab and **add keys**, pict **JSON** and **CREATE**
6. After finish download, upload keys to folder clone **ML API** and change name to **atbq-credentials.json**
7. Training ML Model with export to .h5, or yo can download [atbq_modelfix.h5 here](https://drive.google.com/drive/folders/1RDpPszoPxDN93UQch5IMWlWGncT7zTAz?usp=sharing)

## Project Structure

```
atbq_modelfix.h5
    |--atbq-credentials.json
    |--main.py
    |--requirements.txt
    |--README.md
    |--.python-version
    |--.gitignore
    |--.python-version
```

## Step To Deploy
1. Clone the Repository:
   ```bash
   git clone https://github.com/Bangkit-ATB-Quickscan/ML-API.git
2. Navigate to the Project Directory:
   ```bash
   cd predict
3. Install Dependencies:
   ```bash
   pip install -r requirements.txt
5. Run the api:
   ```bash
   python main.py
6. By default, the server will run on the localhost with the port 5000, open follow to view it in your browser.
   ```bash
   http://localhost:5000
8. If it shows 'OK' then you have successfully run the predict api.
9. Then deploy predict api to cloud.

   