# Azure MLE training assignment

This is a flask app that gets the objects present in a certain container, in the Azure storage account. Then serves it to a URL through a Flask app

## Clone the repository

Install from GitHub:

```bash
git clone https://github.com/amansatyawali-tigeranalytics/az-training.git
cd az-training
git checkout master
```

## Creating Environment

```
conda env create --file env.txt
```

## Setup AZ login

Get connections string from Azure AD
```
export AZURE_STORAGE_CONNECTION_STRING="<connections string>"
```

## Run flask app

```
python home.py
```

## To access the app

Go to url - http://172.174.35.216:5000/