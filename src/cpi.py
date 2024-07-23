import csv
import json
import os
from collections import defaultdict

import requests
from dotenv import load_dotenv

load_dotenv()

p = requests.post(
    "https://api.bls.gov/publicAPI/v2/timeseries/data/",
    data=json.dumps(
        {
            "endyear": "2024",
            "registrationkey": os.getenv("REGISTRATION_KEY"),
            "seriesid": ["CUSR0000SA0", "CUSR0000SA0L1E", "CUSR0000SETB01"],
            "startyear": "2019",
        }
    ),
    headers={"Content-type": "application/json"},
)

series = json.loads(p.text)["Results"]["series"]

dict = defaultdict(list)

file = csv.writer(open("src/data.csv", "w", newline=""))

file.writerow(
    ["Date", "All items", "All items, less food and energy", "Gasoline (all types)"]
)

for serie in series:
    for monthly_details in reversed(serie["data"]):
        dict[monthly_details["period"][1:] + "/" + monthly_details["year"]].append(
            monthly_details["value"]
        )

for date, values in dict.items():
    file.writerow(
        [
            date,
            values[0],
            values[1],
            values[2],
        ]
    )
