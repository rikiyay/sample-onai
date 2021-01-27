#!/usr/bin/env python

# import packages
import os
import glob
import json
import numpy as np
import pandas as pd

# glob image paths from the data folder
images = glob.glob("./data/Retina/train-all/*.npy")
# read label.csv
labels = pd.read_csv("./data/Retina/labels.csv")

# generate a small dict that contains image id, label, and pixel values for each image
records = []
for i, path in enumerate(images):
   img = np.load(path)
   lab = int(labels[labels.filename == os.path.basename(path)].label.values)
   dic = {"id": i, "label": lab, "data": img.tolist()}
   records.append(dic)

# create a dictionary to be dumped into sample.json
data = {
   "date_of_execution": "20210126",
   "query": "TBD",
   "format": "RGB",
   "records": records
   }

# dump the dictionary into a json file
with open(f'./code/importer.json', 'w') as outfile:
    json.dump(data, outfile)