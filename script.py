import json
import csv

with open('session_learning.json') as givenJsonFile:
    jsonData = json.load(givenJsonFile)

output_file = open('output.csv', 'w')
csvWriter = csv.writer(output_file)

count_line = 0
for patent in jsonData:
    patent_data = jsonData[patent]
    # print(patent_data)

    biblio_data = patent_data["biblio_data"]
    # print(biblio_data)

    # To print attribute names
    if count_line == 0:
        attributes = list(biblio_data.keys())
        attributes.insert(0,'S.No.')
        csvWriter.writerow(attributes)
        count_line += 1

    # application_num = str(biblio_data["application_number"])

    dataToBeAdded = biblio_data.values()
    
    # Keep only the first element in case of lists
    dataAfterModification = list()
    for attributeValues in dataToBeAdded:
        if(type(attributeValues) is list):

            if(len(attributeValues) > 0):
                attributeValues = attributeValues[0]

                if 'name' in attributeValues:
                    attributeValues = attributeValues['name']
                else:
                    attributeValues = attributeValues['assignee']

            else:
                attributeValues = "NA"
        
        elif len(attributeValues) == 0:
            attributeValues = "NA"

        dataAfterModification.append(attributeValues)
    
    dataAfterModification.insert(0,count_line)
    count_line += 1
    csvWriter.writerow(dataAfterModification)
    
output_file.close()




