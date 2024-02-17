# SPDX-FileCopyrightText: 2024 Manuel Corujo
# SPDX-FileCopyrightText: 2024 María López
# SPDX-FileCopyrightText: 2024 Pablo Boo
# SPDX-FileCopyrightText: 2024 Ángel Regueiro
#
# SPDX-License-Identifier: MIT

import datetime as dt
import pandas as pd
import argparse
import os

import src.pvpc as pvpc


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

    df = pd.DataFrame(costs, columns=["datetime", "price"])
    df.to_csv(f"./data/{start_date.year}_costs.csv", index=False)
    return df


def read_costs(start_date, end_date):
    start_datetime = dt.datetime.strptime(start_date, "%Y-%m-%d")
    end_datetime = dt.datetime.strptime(end_date, "%Y-%m-%d")
    start_year = start_datetime.year
    end_year = end_datetime.year

    if start_datetime >= dt.datetime(2021, 6, 1) and end_datetime <= dt.datetime(
        2024, 2, 17
    ):
        dfs = []
        for year in range(start_year, end_year + 1):
            file_path = f"./data/{year}_costs.csv"
            if os.path.exists(file_path):
                dfs.append(pd.read_csv(file_path))
            else:
                return get_costs_from_api(start_date, end_date)

        df = pd.concat(dfs)
        df = df.loc[
            (df["datetime"] >= start_datetime.strftime("%Y-%m-%d %H:%M:%S"))
            & (df["datetime"] <= end_datetime.strftime("%Y-%m-%d %H:%M:%S"))
        ]
        df["datetime"] = pd.to_datetime(df["datetime"])
        return df
    else:
        return get_costs_from_api(start_date, end_date)


if __name__ == "__main__":
    args = _parse_args()

    df = read_costs(args.start_date, args.end_date)
    print(df.head())
