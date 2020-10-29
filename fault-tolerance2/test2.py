import os
import json

dir="cpu"
files=os.listdir(dir)

i=0
for file in files:
    print(file)
    filepath=os.path.join(dir,file)
    with open(filepath, "r") as f:
        items = json.load(f)
        for item in items:
            print(item["current_time"])
            print(item["cpu_percent"])
            i+=1
    # print(data)
print(i)