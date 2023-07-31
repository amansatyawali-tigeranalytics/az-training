# Databricks notebook source
# dbutils.fs.mount(
# source = "wasbs://container1@amancloudtraining.blob.core.windows.net",
# mount_point = "/mnt/blobstorage",
# extra_configs = {"fs.azure.account.key.amancloudtraining.blob.core.windows.net":dbutils.secrets.get('test_scope', 'storagekey')})

# COMMAND ----------

from __future__ import print_function

from pyspark.ml.regression import LinearRegressionModel
from pyspark.ml import PipelineModel

from pyspark.sql import SparkSession
from pyspark.ml.linalg import Vectors
import os

if __name__ == "__main__":

    data_inp_path = "file:///Workspace/Users/aman.satyawali@tigeranalytics.com/pyfiles/regression.txt"
    model_save_path="/mnt/blobstorage/models"


    # Create a SparkSession (Note, the config section is only for Windows!)
    spark = SparkSession.builder.appName("LinearRegression").getOrCreate()

    inputLines = spark.sparkContext.textFile(data_inp_path)
    data = inputLines.map(lambda x: x.split(",")).map(lambda x: (float(x[0]), Vectors.dense(float(x[1]))))

    # Convert this RDD to a DataFrame
    colNames = ["label", "features"]
    df = data.toDF(colNames)

    trainTest = df.randomSplit([0.5, 0.5])
    trainingDF = trainTest[0]
    testDF = trainTest[1]

    model = LinearRegressionModel.load(model_save_path)
    # pipeline = PipelineModel.load(model_save_path)

    fullPredictions = model.transform(testDF).cache()

    # Extract the predictions and the "known" correct labels.
    predictions = fullPredictions.select("prediction").rdd.map(lambda x: x[0])
    labels = fullPredictions.select("label").rdd.map(lambda x: x[0])

    # Zip them together
    predictionAndLabel = predictions.zip(labels).collect()

    # Print out the predicted and actual values for each point
    for prediction in predictionAndLabel:
      print(prediction)

