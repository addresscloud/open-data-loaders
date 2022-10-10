#!/usr/bin/python

import requests, json, urllib.request, os
import xml.etree.ElementTree as ET
import pandas as pd

url = 'http://api.ratings.food.gov.uk/Authorities'
headers={"x-api-version":"2"}
response =requests.get(url, headers=headers)
data = response.json()

#Load JSON string into a dictionary
json_dict = (data)

#get the df just in authorities
authorities=json_dict['authorities']

#loop through the authorities and get the filename url and download
for item in authorities:
    xmlUrl = (item['FileName'])
    result = xmlUrl.rsplit('/', 1)[1]
    urllib.request.urlretrieve(xmlUrl,result)

#Create the csv
def createCsv(xml):
    tree =ET.parse(xml)
    root = tree.getroot()

    lat_rows = []
    lon_rows = []

    for elem in root.findall(".//EstablishmentDetail/Geocode"):   
        lat = getattr(elem.find('Latitude'), 'text', None)
        lon = getattr(elem.find('Longitude'), 'text', None)
        lat_rows.append (lat)
        lon_rows.append (lon)

    hyg_rows = []
    struct_rows = []
    cim_rows = []

    for elem in root.findall(".//EstablishmentDetail/Scores"):   
        hygiene = getattr(elem.find('Hygiene'), 'text', None)
        struct = getattr(elem.find('Structural'), 'text', None)
        cim = getattr(elem.find('ConfidenceInManagement'), 'text', None)
        hyg_rows.append (hygiene)
        struct_rows.append (struct)
        cim_rows.append (cim)

    #build the final dfframe
    df = pd.read_xml(xml, xpath="//EstablishmentDetail")
    #print(df.columns)
    if not 'AddressLine1' in df:
        df['AddressLine1'] = ''
    if not 'AddressLine2' in df:
        df['AddressLine2'] = ''
    if not 'AddressLine3' in df:
        df['AddressLine3'] = ''
    if not 'AddressLine4' in df:
        df['AddressLine4'] = ''
    if not 'PostCode' in df:
        df['PostCode'] = ''
    #if 'AddressLine1' in df:
    df['address'] = df[['AddressLine1','AddressLine2', 'AddressLine3','AddressLine4','PostCode']].apply(lambda x: ','.join(x.dropna()), axis=1)
    df['address'].str.lstrip(',')
    df = df[['FHRSID','BusinessName','BusinessType','address']]
    #print (df)
    df['Latitude']=lat_rows
    df['Longitude']=lon_rows
    df['Hygiene']=hyg_rows
    df['Structual']=struct_rows
    df['confidence']=cim_rows
    #df= df.drop(columns=['Scores','Geocode'], axis=1)
    output_path='fhrs_properties.csv'
    df.to_csv(output_path, mode='a', header=not os.path.exists(output_path))

# assign directory
cwd = os.getcwd()
directory = cwd
for filename in os.listdir(directory):
    xml = os.path.join(directory, filename)
    if xml.endswith('.xml'):
        createCsv(xml)




