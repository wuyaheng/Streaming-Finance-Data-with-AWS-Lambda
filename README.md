# Streaming-Finance-Data-with-AWS-Lambda
## Description
In this project, I've collected one day’s worth of stock HIGH and LOW prices for each company listed below on December 1st, 2020, at a five minute interval with a Lambda function. This function is triggered every 5 minutes and places the collected data into a defined Kinesis Delivery Stream which was pointed to an S3 bucket as its destination. Then I configured AWS Glue to crawl this S3 bucket which allowed me to query the S3 files using AWS Athena to gain insight into the streamed data. The results.csv is the query output generated through Athena. Lastly, I created three graphs in the Jupyter Notebook by using the data in the results.csv file.

## Table of Contents

* [TechUsed](#TechUsed)

* [Infrastructure](#Infrastructure)

* [Questions](#Questions)


## TechUsed
AWS Lambda, Kinesis, Glue, Athena, S3 and Python

## Infrastructure
![Picture1](https://user-images.githubusercontent.com/52837649/102304572-c1a6a680-3f2b-11eb-9a25-bb21c21752d8.png)
### 1. DataTransformer<br/>
I created a lambda function as provided below to collect the data from yfinance and put into a kinesis stream.
```
import json
import boto3
import yfinance as yf

startDate = '2020-12-01'
endDate = '2020-12-02'
everyInterval = '5m'   
tickers = ['FB', 'SHOP', 'BYND', 'NFLX', 'PINS', 'SQ', 'TTD', 'OKTA', 'SNAP', 'DDOG']

kinesis = boto3.client('kinesis', "us-east-2")

def lambda_handler(event, context):
    for ticker in tickers:
        data = yf.download(ticker, start=startDate, end=endDate, interval = everyInterval)
        for Datetime, row in data.iterrows():
            record = {
              'high': row['High'],
              'low': row['Low'],
              'ts': str(Datetime), 
              'name': ticker
              }
            
            recordJSON = json.dumps(record)+"\n"
            
            kinesis.put_record(
                StreamName="STA9760F2020_stream",
                Data=recordJSON,
                PartitionKey="partitionkey"
                )
    return {
        'statusCode': 200,
        'body': json.dumps("Hello from Lambda!")
    }
```
### 2. DataCollector<br/>
I created a Kinesis stream that holds the data. Below is a screenshot of the AWS Kinesis configuration page.

![kinesis_config](https://user-images.githubusercontent.com/52837649/102305104-21ea1800-3f2d-11eb-81c0-c866ff1bcb6c.png)

### 3. DataAnalyzer<br/>
I created a serverless process that allows me to query the S3 data. Below is a screenshot of my S3 bucket. 

![screenshot_of_s3_bucket](https://user-images.githubusercontent.com/52837649/102306851-34fee700-3f31-11eb-8253-a5850c628b8d.png)

I also set up a Glue crawler so that I can run the AWS Athena queries against my data. Below is a screenshot that gives me the highest hourly stock “high” per company. 

![athena](https://user-images.githubusercontent.com/52837649/102308032-be171d80-3f33-11eb-8c96-0dcc7e401a0e.png)

## Questions
For questions about the project, please contact me at wuyaheng2016@gmail.com


