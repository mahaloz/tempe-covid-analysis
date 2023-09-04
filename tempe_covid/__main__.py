import argparse

from .collection import collect_data
from .analysis import sort_by_observation_average
from .visualization import format_as_markdown_table


def main():
    parser = argparse.ArgumentParser(description="Collect and analyze Tempe COVID data", epilog="Example use: python -m tempe_covid -average --start-time 2021-08-21 --end-time 2023-08-21")
    parser.add_argument("-average", action="store_true", help="Sort the data by the average of the observations for each week")
    parser.add_argument("--start-time", type=str, default="2021-08-21", help="The start time for the data collection. Form: YYYY-MM-DD")
    parser.add_argument("--end-time", type=str, default="2023-08-21", help="The end time for the data collection. Form: YYYY-MM-DD")
    args = parser.parse_args()

    if args.average:
        data = collect_data(start_time=args.start_time, end_time=args.end_time)
        sorted_data = sort_by_observation_average(data)
        markdown_table = format_as_markdown_table(sorted_data)
        print(markdown_table)


if __name__ == "__main__":
    main()
