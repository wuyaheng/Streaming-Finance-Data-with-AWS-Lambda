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
