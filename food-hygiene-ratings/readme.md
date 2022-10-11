## About 

This python script downloads the Food Hygiene Ratings Scheme (FHRS) Data (aka "score on the doors") from the Food Standards Agency's [website](https://data.food.gov.uk/catalog/datasets/38dd8d6a-5ab1-4f50-b753-ab33288e3200). This contains the data for the whole of the Uinted Kingdom and is updated by each local authority responsible for food hygiene. 

Since 2012, the data collected by environmental health officers for the FSA FHRS including the geographical coordinates (where stated) of all businesses/premises where food is consumed, sold or provided for all local authorties (LAs) in England, Scotland, Wales and Northern Ireland have been available online. This includes restaurants, pubs, cafes, takeaways, food vans/stalls, schools, canteens, hotels, supermarkets and other shops (e.g. garage forecourt shops, convenience stores), care homes, community centres, cafes within retail shops, nurseries and hospitals. All new businesses need to be registered with the LA at least 28 days before opening. All LAs need to upload data of recently inspected premises at least every 28 days. Frequency of inspection depends upon the hygiene rating received by the business/premises [1].

The data is downloaded as a collection of xml files that are then converted to a single csv files that contains the following buisness name, type, address as well asthe latitude and longitude. These data are national in coverage, available for public download, updated regularly, unrestricted in terms of use and free.  

## To do

* Add arguments i.e keep/remove the xmls after proceesing

[1] https://academic.oup.com/jpubhealth/article/43/4/e720/5910440


