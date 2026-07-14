# 🌍 Global Warming Visualization

A Python tool for analyzing long-term weather observations from **Météo-France** and generating visualizations that highlight local climate trends.

The project processes daily weather records (temperature, precipitation and wind) and produces charts illustrating the evolution of temperatures over several decades for any weather station available in the dataset.

## Features

- 📈 Annual average temperature
- 🔥 Number of days with maximum temperature above a configurable threshold
- ❄️ Number of days with minimum temperature below a configurable threshold
- 🎨 Automatic chart generation
- 📂 Works with official Météo-France CSV datasets
- 🚀 Command-line interface

## Example graphs

The generated graphs can be used to visualize long-term climate evolution for a weather station.

Examples include:

- Annual average temperature
- Number of days where **TX > 30°C**
- Number of days where **TN < 10°C**

The repository already contains a set of generated charts in the [output](https://github.com/Julia-vga/global_warming/tree/main/output) directory.

These charts were produced using publicly available Météo-France datasets and illustrate examples of the analyses performed by this project for several French weather stations.

## Requirements

- Python 3.10+
- matplotlib

Install dependencies:

```bash
pip install matplotlib
```

## Data source

This project uses the official daily observations published by **Météo-France**.

Example dataset:

- Daily observations (RR / Temperature / Wind)
- Period: 1950–2024

Datasets are available from the [French open data portal](https://www.data.gouv.fr/datasets/donnees-climatologiques-de-base-quotidiennes).

## Usage

```bash
python main.py \
    --source Q_06_previous-1950-2024_RR-T-Vent.csv \
    --station_name NICE \
    --output results
```

### Parameters

| Argument | Description |
|----------|-------------|
| `--source` | Path to the Météo-France CSV file |
| `--station_name` | Weather station name (e.g. `NICE`, `BREST-GUIPAVAS`, `LILLE-LESQUIN`) |
| `--output` | Output directory for generated graphs |

## Generated outputs

Depending on the selected analysis, the program generates PNG files such as:

```
results/
├── annual_average_temperature.png
├── number_of_days_above_30C.png
└── number_of_days_below_10C.png
```


Current visualizations include:

- Annual average temperature
- Hot days (TX > threshold)
- Cold days (TN < threshold)

Additional visualizations can easily be added.

## Project structure

```
.
├── main.py
├── README.md
└── results/
```

## Notes

- Temperatures are expressed in **°C**.
- Daily average temperature uses the `TNTXM` field provided by Météo-France.
- Missing or invalid values are automatically ignored.

## License

This project is released under the MIT License.

## Contributing

Contributions, feature requests and bug reports are welcome.

Feel free to open an Issue or submit a Pull Request.

## Disclaimer

This project is intended for data visualization and educational purposes.

The generated charts illustrate trends present in the selected weather station observations and should not be interpreted as a complete climatological analysis on their own.
