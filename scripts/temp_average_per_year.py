import csv
from collections import defaultdict
from datetime import datetime

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import Normalize

def compute(source_file: str, weather_station_name: str, output_dir: str):
        # année -> somme des températures, nombre de jours
        somme = defaultdict(float)
        compteur = defaultdict(int)

        with open(source_file, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=";")

            for row in reader:

                if row["NOM_USUEL"] != weather_station_name:
                    continue

                if row["TNTXM"] == "":
                    continue

                try:
                    annee = datetime.strptime(row["AAAAMMJJ"], "%Y%m%d").year
                    temperature = float(row["TNTXM"])
                except ValueError:
                    continue

                somme[annee] += temperature
                compteur[annee] += 1

        # Calcul de la moyenne annuelle
        annees = np.array(sorted(somme.keys()))
        moyennes = np.array([somme[a] / compteur[a] for a in annees])

        fig, ax = plt.subplots(figsize=(16, 8))

        # Création des segments de la courbe
        points = np.array([annees, moyennes]).T.reshape(-1, 1, 2)
        segments = np.concatenate([points[:-1], points[1:]], axis=1)

        # Dégradé vert -> rouge
        norm = Normalize(vmin=annees.min(), vmax=annees.max())

        lc = LineCollection(
            segments,
            cmap="RdYlGn_r",
            norm=norm,
            linewidth=3
        )

        # Couleur selon l'année
        lc.set_array(annees[:-1])

        ax.add_collection(lc)

        # Points colorés
        ax.scatter(
            annees,
            moyennes,
            c=annees,
            cmap="RdYlGn_r",
            norm=norm,
            s=30,
            zorder=3
        )

        # Ajustement des axes
        ax.set_xlim(annees.min(), annees.max())
        ax.set_ylim(moyennes.min() - 0.5, moyennes.max() + 0.5)

        ax.set_title(f"Annual average temperature in {weather_station_name}")
        ax.set_xlabel("Year")
        ax.set_ylabel("Average temperature (°C)")

        ax.grid(True, alpha=0.3)

        # Barre de couleur
        cbar = fig.colorbar(lc, ax=ax)
        cbar.set_label("Year")

        fig.tight_layout()
        fig.savefig(f"{output_dir}/temperatures_{weather_station_name}_average_per_year.png", dpi=300)