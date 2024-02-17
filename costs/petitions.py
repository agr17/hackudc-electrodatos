import argparse
import datetime as dt
import os

import pandas as pd
import pvpc
import requests

FILES_PATH = "./data/marginalpdbc_2022/"


def _parse_args():
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
    return df


def get_costs_from_api(start_date, end_date):
    start_date = dt.datetime.strptime(start_date, "%Y-%m-%d")
    end_date = dt.datetime.strptime(end_date, "%Y-%m-%d")
    delta = end_date - start_date

    costs = []
    for i in range(delta.days + 1):
        day = start_date + dt.timedelta(days=i)
        r = pvpc.get_pvpc_day(day.strftime("%Y-%m-%d"))
        data = r.data.pcb.hours
        for hour, cost in data.items():
            date = day + dt.timedelta(hours=int(hour))
            costs.append([date, cost])

    df = pd.DataFrame(costs, columns=["datetime", "cost"])
    df.to_csv(f"./data/{start_date.year}_costs.csv", index=False)
    return df



def read_costs(start_date, end_date):
    start_datetime = dt.datetime.strptime(start_date, "%Y-%m-%d")
    end_datetime = dt.datetime.strptime(end_date, "%Y-%m-%d")
    start_year = start_datetime.year
    end_year = end_datetime.year

    if start_datetime >= dt.datetime(2021, 6, 1) and end_datetime <= dt.datetime(2024, 2, 17):
        dfs = []
        for year in range(start_year, end_year + 1):
            file_path = f"./data/{year}_costs.csv"
            if os.path.exists(file_path):
                dfs.append(pd.read_csv(file_path))
            else:
                return get_costs_from_api(start_date, end_date)

        df = pd.concat(dfs)
        filtered_df = df.loc[
            (df["datetime"] >= start_datetime.strftime("%Y-%m-%d %H:%M:%S"))
            & (df["datetime"] <= end_datetime.strftime("%Y-%m-%d %H:%M:%S"))
        ]
        return filtered_df
    else:
        return get_costs_from_api(start_date, end_date)


if __name__ == "__main__":
    args = _parse_args()

    df = read_costs(args.start_date, args.end_date)
    print(df.head())
    # read_data(args.start_date, args.end_date)
    # get_costs_from_api(args.start_date, args.end_date)

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
