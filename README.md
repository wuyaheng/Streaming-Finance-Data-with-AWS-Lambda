
# Streaming-Finance-Data-with-AWS-Lambda

## Description
In this project, I've collected one day’s worth of stock HIGH and LOW prices for each company listed below on December 1st, 2020, at a five minute interval with a Lambda function. This function is triggered every 5 minutes and places the collected data into a defined Kinesis Delivery Stream which was pointed to an S3 bucket as its destination. Then I configured AWS Glue to crawl this S3 bucket which allowed me to query the S3 files using AWS Athena to gain insight into the streamed data. The results.csv is the query output generated through Athena. Lastly, I created three graphs in the Jupyter Notebook by using the data in the results.csv file.


## Table of Contents

* [TechUsed](#TechUsed)

* [Infrastructure](#Infrastructure)

* [Configuration](#Configuration)

* [Questions](#Questions)


## TechUsed
AWS Lambda, Kinesis, Glue, Athena, S3 and Python

## Infrastructure
![Picture1](https://user-images.githubusercontent.com/52837649/102304572-c1a6a680-3f2b-11eb-9a25-bb21c21752d8.png)
1. DataTransformer: A lambda function that gathers the data.
2. DataCollector: A Kinesis stream that holds the data.
3. DataAnalyzer: A serverless process that allows us to query the S3 data.

## Configuration
Below is a screenshot of the AWS Kinesis configuration page 

![kinesis_config](https://user-images.githubusercontent.com/52837649/102305104-21ea1800-3f2d-11eb-81c0-c866ff1bcb6c.png)

## Questions
For questions about the project, please contact me at wuyaheng2016@gmail.com


