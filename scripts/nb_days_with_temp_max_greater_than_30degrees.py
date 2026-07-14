import csv
from collections import defaultdict
from datetime import datetime

import matplotlib.pyplot as plt

def compute(source_file: str, weather_station_name: str, output_dir: str):
    # Nb days > 30°C per year
    jours_chauds = defaultdict(int)

    with open(source_file, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")

        for row in reader:

            if row["NOM_USUEL"] != weather_station_name:
                continue

            if row["TX"] == "":
                continue

            try:
                tx = float(row["TX"])
                annee = datetime.strptime(row["AAAAMMJJ"], "%Y%m%d").year
            except ValueError:
                continue

            if tx > 30:
                jours_chauds[annee] += 1

    annees = sorted(jours_chauds.keys())
    nb_jours = [jours_chauds[a] for a in annees]

    couleurs = [
        "red"
        for _ in annees
    ]

    fig, ax = plt.subplots(figsize=(18, 8))

    ax.bar(
        annees,
        nb_jours,
        color=couleurs,
        width=0.8
    )

    ax.set_title(f"Number of days with maximum temperature > 30°C in {weather_station_name}")
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of days")

    ax.grid(axis="y", alpha=0.3)

    # Display a tick every 5 years
    ax.set_xticks(annees[::5])
    ax.tick_params(axis="x", rotation=45)

    fig.tight_layout()
    fig.savefig(f"{output_dir}/temperatures_nice_nb_days_higher_than_30_degrees_1950_2024.png", dpi=300)