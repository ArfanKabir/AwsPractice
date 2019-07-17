# AwsPractice
Practice with AWS required for my internship at Thortech Industries in White Plains, New York over Summer 2019
These files found implement the use of the Boto3 module in Python, which allows the language to communicate with the AWS API.
These programs implement uploading, and downloading files, which then can be used to analyze said files from the an S3 bucket, like the practice.py and awsTest.py programs show. Practice.py converts a csv file (was provided before) into a json file, and then uploads that into my S3 bucket
awsTest.py takes the files that I uploaded to my s3 bucket, downloads them, and then counts the number of lines present in the downloaded files
