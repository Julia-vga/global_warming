import csv
from collections import defaultdict
from datetime import datetime

import matplotlib.pyplot as plt

def compute(source_file: str, weather_station_name: str, output_dir: str):
    # Nb days < 10°C per year
    cold_days = defaultdict(int)

    with open(source_file, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")

        for row in reader:

            if row["NOM_USUEL"] != weather_station_name:
                continue

            if row["TM"] == "":
                continue

            try:
                tm = float(row["TM"])
                annee = datetime.strptime(row["AAAAMMJJ"], "%Y%m%d").year
            except ValueError:
                continue

            if tm < 10:
                cold_days[annee] += 1

    annees = sorted(cold_days.keys())
    nb_days = [cold_days[a] for a in annees]

    # Couleurs : vert jusqu'en 2003, rouge après
    couleurs = [
        "blue"
        for _ in annees
    ]

    fig, ax = plt.subplots(figsize=(18, 8))

    ax.bar(
        annees,
        nb_days,
        color=couleurs,
        width=0.8
    )

    ax.set_title("Nombre de jours avec temperature min < 10°C à Nice")
    ax.set_xlabel("Année")
    ax.set_ylabel("Nombre de jours")

    ax.grid(axis="y", alpha=0.3)

    # Une graduation tous les 5 ans
    ax.set_xticks(annees[::5])
    ax.tick_params(axis="x", rotation=45)

    fig.tight_layout()
    fig.savefig("{}/temperatures_nice_average_1950_2024.png".format(output_dir), dpi=300)