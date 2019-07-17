import csv  
import json
import boto3
s3 = boto3.client('s3')
# Open the CSV  
with open('county_facts_kaggle.csv','r') as csvFile:
        majFile = open('majFile.json','w')        
        minFile = open('minFile.json','w')
# parse the CSV
        majCount = 0
        minCount = 0
        csvLine = csv.DictReader(csvFile)
        for line in csvLine:
                if float(line['SEX255214']) > 50:
                        majDict = {
                                "fips": line['fips'],
                                "area_name": line['area_name'],
                                "state_abbreviation": line['state_abbreviation'],
                                "Percentage of Women-owned businesses": line['SBO015207']
                             }
                        json.dump(majDict,majFile)
                        majCount = int(majCount) + 1
                        majFile.write("\n")
                else:
                        minDict = {
                                "fips": line['fips'],
                                "area_name": line['area_name'],
                                "state_abbreviation": line['state_abbreviation'],
                                "Percentage of Women-owned businesses": line['SBO015207']
                             }
                        json.dump(minDict,minFile)
                        minCount = int(minCount) + 1
                        minFile.write("\n")
        print("The number of majority counties: "+str(majCount))
        print("The number of minority counties: "+str(minCount))
        majFile.close()
        minFile.close()
        s3.upload_file('majFile.json','thortech-test-bucket','majFile.json')
        s3.upload_file('minFile.json','thortech-test-bucket','minFile.json')
