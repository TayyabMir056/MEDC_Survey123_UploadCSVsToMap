import os
import json
from IPython.display import display
import arcgis
from arcgis.gis import GIS,ContentManager
from arcgis.mapping import WebMap

#Enter portal details
gis= GIS(url="", username="", password ="")

wm_Z1 = WebMap()
folderpath = r'M:\Planning\GIS\GIS Staff\Tayyab\Hussam\DSS per users\CSVs Per User\Zone 1'
zone1Areas=os.listdir(folderpath)

#Loop through all the csvs in the mentioned folder, and add them in the GIS as layers, publish them, and add them to the above created web map
for areacsv in zone1Areas:
    if areacsv!='.cekey':#Ignore Lock files
        csv_file=folderpath+'\\'+areacsv
        csv_item= gis.content.add({'type':'CSV'},csv_file)
        lyr=csv_item.publish()
        wm_Z3.add_layer(lyr)
        
#Set Map properties and save.
web_map_properties = {'title':'Zone 1 - GMT Distribution Substations Routine check MAP',
                     'snippet':'',
                     'tags':'MEDC'}
web_map_item = wm_Z3.save(item_properties=web_map_properties)
