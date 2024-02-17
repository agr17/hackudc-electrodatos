import argparse
import datetime as dt
import os

import pandas as pd
import requests

FILES_PATH = "./data/marginalpdbc_2022/"


def parse_args():
    # Parse the command-line arguments (start date and end date)
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--start-date",
        type=str,
        required=True,
        help="Start date in the format YYYY-MM-DD",
    )
    parser.add_argument(
        "--end-date",
        type=str,
        required=True,
        help="End date in the format YYYY-MM-DD",
    )
    return parser.parse_args()


def read_data(start_date, end_date):
    start_date = start_date.replace("-", "")
    end_date = end_date.replace("-", "")
    costs = []
    for file in os.listdir(FILES_PATH):
        if not start_date <= file.split("_")[1][:-2] <= end_date:
            continue

        with open(os.path.join(FILES_PATH, file), "r") as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if not 1 <= i <= 24:
                    continue
                line = line[:-2].split(";")
                if len(line) != 6: # ignore lines with wrong format
                    continue
                year = line[0]
                month = line[1]
                day = line[2]
                hour = line[3]
                price = line[4]
                date = dt.datetime(int(year), int(month), int(day)) + dt.timedelta(
                    hours=int(hour)
                )
                costs.append([date, price])
    df = pd.DataFrame(costs, columns=["datetime", "price"])

    # divide price by 1000 to get €/kWh
    df["price"] = df["price"].astype(float) / 1000

    return df



def read_costs():
    args = parse_args()

    # url = "https://api.esios.ree.es/archives/3183/download_json"

    # headers = {
    #     "Accept": "application/json; application/vnd.esios-api-v1+json",
    #     "Content-Type": "application/json",
    #     "x-api-key": "6753856a894a0a3b27bb41cb7843db6f2d2eb77ab8cf3d49b7e39f7980cef700"
    # }

    # response = requests.get(url, headers=headers)
    # print(response)
    # response_json = response.json()
    # print(response_json)
    read_data(args.start_date, args.end_date)


if __name__ == "__main__":
    args = parse_args()

    read_data(args.start_date, args.end_date)
