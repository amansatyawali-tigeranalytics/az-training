# Databricks notebook source
from __future__ import print_function

from pyspark.ml.regression import LinearRegression

from pyspark.sql import SparkSession
from pyspark.ml.linalg import Vectors
import os

if __name__ == "__main__":

    data_inp_path = "file:///Workspace/Users/aman.satyawali@tigeranalytics.com/pyfiles/regression.txt"
    data_save_path = "file:///Workspace/Users/aman.satyawali@tigeranalytics.com/pyfiles/regression_new.txt"

    # Create a SparkSession (Note, the config section is only for Windows!)
    spark = SparkSession.builder.appName("LinearRegression").getOrCreate()

    inputLines = spark.sparkContext.textFile(data_inp_path)


