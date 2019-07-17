import boto3
import botocore
s3 = boto3.client('s3')
s3Res = boto3.resource('s3')
flag = False
while flag == False:
        try:
                bucketName = input("Enter the name of the bucket: ")
                buckets = s3Res.buckets.all()
                for bucket in buckets:
                        if bucket.name == bucketName:
                                print("Bucket found\n")
                                flag = True
                        else:
                                print("Bucket not found, try again")
        except ClientError as e:
                if e.response['Error']['Code'] == 'Not Found':
                        print("Bucket not found")
                else:
                        print("Unexpected Error")
file1 = 'majFile.json'
file2 = 'minFile.json'
remFile1 = 'majFile-remote.json'
remFile2 = 'minFile-remote.json'
s3.download_file(bucketName,file1,remFile1)
s3.download_file(bucketName,file2,remFile2)


try:
	fileReader1 = open(remFile1, "r")
	fileReader2 = open(remFile2, "r")
	counter1 = 0
	counter2 = 0
	for i in fileReader1:
		counter1 = int(counter1) + 1
	for j in fileReader2:
		counter2 = int(counter2) + 1
	print ("The number of lines in "+remFile1+": "+str(counter1))
	print ("The number of lines in "+remFile2+": "+str(counter2))
finally:
	fileReader1.close()
	fileReader2.close()
