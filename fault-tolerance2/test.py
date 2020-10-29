import json
import os

dir="time"
files=os.listdir(dir)

for file in files:
    filepath=os.path.join(dir,file)
    with open(filepath) as f:
        pop_data=json.load(f)
        print(pop_data)
        print(pop_data['starting_time'])
        print(pop_data['total_time'])

