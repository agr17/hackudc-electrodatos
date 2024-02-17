# SPDX-FileCopyrightText: 2024 Manuel Corujo
# SPDX-FileCopyrightText: 2024 María López
# SPDX-FileCopyrightText: 2024 Pablo Boo
# SPDX-FileCopyrightText: 2024 Ángel Regueiro
#
# SPDX-License-Identifier: MIT

import argparse
import pandas as pd


def _parse_args():
    # Parse the command-line arguments (start date and end date)
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--filename",
        type=str,
        required=True,
        help="Name of the file to be formatted",
    )
    return parser.parse_args()


def cnmc_to_csv(filename):
    df = pd.read_csv(filename, sep=";")

    cups = df["CUPS"].unique()[0]
    df = df.drop(columns=["CUPS"])
    df["Fecha"] = pd.to_datetime(df["Fecha"], format="%d/%m/%Y")
    df["datetime"] = df["Fecha"] + pd.to_timedelta(df["Hora"], unit="h")
    df["Consumo_KWh"] = df["Consumo_KWh"].str.replace(",", ".").astype(float)
    df["Metodo_obtencion"] = df["Metodo_obtencion"].replace(
        {"R": "Real", "S": "Estimado"}
    )
    df = df.rename(
        columns={
            "Fecha": "fecha",
            "Hora": "hora",
            "Consumo_KWh": "consumo",
            "Metodo_obtencion": "met_obtencion",
        }
    )

    df.to_csv(f"{filename[:-4]}_{cups}.csv", index=False)
    print(f"File {filename[:-4]}_{cups}.csv saved using new format")


if __name__ == "__main__":
    args = _parse_args()
    cnmc_to_csv(args.filename)
