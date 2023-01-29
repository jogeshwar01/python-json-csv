import json
import csv
import datetime

def compareDatesForEvents(eventData):
    latestDate = datetime.datetime(100, 1, 1)

    for eventsDetails in eventData:
        dateOfCurrentEventString = eventsDetails['event_date']

        dateOfCurrentEventDatetime = dateOfCurrentEventString.split("-")
        year = int(dateOfCurrentEventDatetime[0])
        month = int(dateOfCurrentEventDatetime[1])
        day = int(dateOfCurrentEventDatetime[2])
        dateOfCurrentEventDatetime = datetime.datetime(year,month,day)

        if(dateOfCurrentEventDatetime > latestDate):
            latestDate = dateOfCurrentEventDatetime

    return latestDate.date()
    

with open('session_learning.json') as givenJsonFile:
    jsonData = json.load(givenJsonFile)

output_file = open('output2.csv', 'w')
csvWriter = csv.writer(output_file)

count_line = 0
for patent in jsonData:
    patent_data = jsonData[patent]
    # print(patent_data)

    biblio_data = patent_data["biblio_data"]
    register_events_data = patent_data["register_events"]
    legal_events_data = patent_data["legal_events"]
    # print(biblio_data)

    # To print attribute names
    if count_line == 0:
        attributes = list(biblio_data.keys())
        attributes.append('register_events')
        attributes.append('legal_events')
        csvWriter.writerow(attributes)
        count_line += 1

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

    # dataAfterModification.append(register_events_data['event_date'])
    # dataAfterModification.append(legal_events_data['event_date'])

    # Get latest date for register and legal events
    latestDateRegisterEvents = compareDatesForEvents(register_events_data)
    latestDateLegalEvents = compareDatesForEvents(legal_events_data)

    dataAfterModification.append(latestDateRegisterEvents)
    dataAfterModification.append(latestDateLegalEvents)

    csvWriter.writerow(dataAfterModification)
    
output_file.close()




