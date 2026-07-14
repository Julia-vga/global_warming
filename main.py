import argparse
from scripts import nb_days_with_temp_max_greater_than_30degrees
from scripts import temp_average_per_year
from scripts import nb_days_with_temp_min_lower_than_10degrees

parser = argparse.ArgumentParser(
    description="Analyze Météo-France daily weather data."
)

# Input CSV file
parser.add_argument(
    "--source",
    required=True,
    help="Path to the source CSV file."
)

# Weather station name (e.g. NICE)
parser.add_argument(
    "--station_name",
    required=True,
    help="Weather station name (e.g. NICE)."
)

# Output directory
parser.add_argument(
    "--output",
    required=True,
    help="Output directory where generated files will be written."
)

args = parser.parse_args()

source = args.source
station_name = args.station_name
output_dir = args.output

print(f"Source file     : {source}")
print(f"Station name    : {station_name}")
print(f"Output directory: {output_dir}")

temp_average_per_year.compute(source, station_name, output_dir)
nb_days_with_temp_max_greater_than_30degrees.compute(source, station_name, output_dir)
nb_days_with_temp_min_lower_than_10degrees.compute(source, station_name, output_dir)
