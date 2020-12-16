
# Streaming-Finance-Data-with-AWS-Lambda

## Description
In this project, I've collected one day’s worth of stock HIGH and LOW prices for each company listed below on December 1st, 2020, at a five minute interval with a Lambda function. This function is triggered every 5 minutes and places the collected data into a defined Kinesis Delivery Stream which was pointed to an S3 bucket as its destination. Then I configured AWS Glue to crawl this S3 bucket which allowed me to query the S3 files using AWS Athena to gain insight into the streamed data. The results.csv is the query output generated through Athena. Lastly, I created three graphs in the Jupyter Notebook by using the data in the results.csv file.


## Table of Contents

* [Technology Used](#Technology Used)

* [Questions](#Questions)


## Technology Used
AWS Lambda, Kinesis, Glue, Athena, S3 and Python

## Questions
For questions about the project, please contact me at wuyaheng2016@gmail.com


