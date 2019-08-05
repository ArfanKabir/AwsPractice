import pandas
import boto3
#name = ['InvoiceID','PayerAccountId','LinkedAccountId','RecordType','RecordID','BillingPeriodStartDate','BillingPeriodEndDate','InvoiceDate','PayerAccountName','LinkedAccountName','TaxationAddress','PayerPONumber','ProductCode','ProductName','SellerOfRecord','UsageType','Operation','RateId','ItemDescription','UsageStartDate','UsageEndDate','UsageQuantity','BlendedRate','CurrencyCode','CostBeforeTax','Credits','TaxAmount','TaxType','TotalCost']
#dtypes = {'InvoiceID': 'double', 'PayerAccountId': 'int64','LinkedAccountId': 'float64','RecordType': 'str','RecordID': 'int64','BillingPeriodStartDate': 'str','BillingPeriodEndDate': 'str','InvoiceDate': 'str','PayerAccountName': 'str','LinkedAccountName': 'str','TaxationAddress': 'str','PayerPONumber': 'str','ProductCode': 'str','ProductName': 'str','SellerOfRecord': 'str','UsageType': 'str','Operation': 'str','RateId': 'int64','ItemDescription': 'str','UsageStartDate': 'str','UsageEndDate': 'str','UsageQuantity': 'double','BlendedRate': 'double','CurrencyCode': 'str','CostBeforeTax': 'double','Credits': 'double','TaxAmount':'double','TaxType': 'str','TotalCost': 'double'}
#These are commented out because they caused more of a hassle
#Problems occur in python and the conversion when the types in the columns aren't the same (which can be pretty common because csvs don't care about the types in the columns being uniform)
s3 = boto3.client('s3',region_name = 'us-east-1');
bucketName = "arfan-athena-test-bucket";

for i in range(6):  
    parquetName = "endResult"+str(i+2)+".parquet";
    if (i == 5):
        break;
    df = pandas.read_csv('NewECSV_'+str(i+2)+'_2019.csv')#dtype = dtypes;
    df.to_parquet(parquetName);
    print("File "+str(i+2)+ " has been successfully converted");
    s3.upload_file(parquetName,bucketName,parquetName);
