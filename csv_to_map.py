import os
import json
from IPython.display import display
import arcgis
from arcgis.gis import GIS,ContentManager
from arcgis.mapping import WebMap, WebScene

gis= GIS(url="", username="", password ="")

import os
from arcgis.mapping import WebMap
wm_Z3 = WebMap()
folderpath = r'M:\Planning\GIS\GIS Staff\Tayyab\Hussam\DSS per users\CSVs Per User\Zone 1'
zone1Areas=os.listdir(folderpath)
for areacsv in zone1Areas:
    if areacsv!='.cekey':
        csv_file=folderpath+'\\'+areacsv
        csv_item= gis.content.add({'type':'CSV'},csv_file)
        lyr=csv_item.publish()
        wm_Z3.add_layer(lyr)
web_map_properties = {'title':'Zone 1 - GMT Distribution Substations Routine check MAP',
                     'snippet':'',
                     'tags':'MEDC'}
web_map_item = wm_Z3.save(item_properties=web_map_properties)
