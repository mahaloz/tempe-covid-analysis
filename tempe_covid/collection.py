import json
import datetime
from collections import defaultdict

import requests

#BASE_URL = "https://services.arcgis.com/lQySeXwbBg53XWDi/arcgis/rest/services/survey123_fac3a0c99eb642a6a36737773816d2a7_results/FeatureServer/0/query?f=json&cacheHint=true&resultOffset=0&resultRecordCount=10000&where=(collection_area%3C%3E%27Guadalupe%27%20AND%20collection_area%20IS%20NOT%20NULL)%20AND%20(week_start_date%3E%3Dtimestamp%20%272023-06-05%2007%3A00%3A00%27%20AND%20week_start_date%3C%3Dtimestamp%20%272023-09-05%2006%3A59%3A59%27)&orderByFields=week_start_date%20DESC%2Ccollection_area%20ASC&outFields=*&resultType=standard&returnGeometry=false&spatialRel=esriSpatialRelIntersects"
START_TIME_LABEL = "<START_TIME>"
# time format: YYYY-MM-DD
END_TIME_LABEL = "<END_TIME>"
DATA_POINTS_LABEL = "<DATA_POINTS>"
BASE_URL = f"https://services.arcgis.com/lQySeXwbBg53XWDi/arcgis/rest/services/survey123_fac3a0c99eb642a6a36737773816d2a7_results/FeatureServer/0/query?f=json&cacheHint=true&resultOffset=0&resultRecordCount={DATA_POINTS_LABEL}&where=(collection_area%3C%3E%27Guadalupe%27%20AND%20collection_area%20IS%20NOT%20NULL)%20AND%20(week_start_date%3E%3Dtimestamp%20%27{START_TIME_LABEL}%2007%3A00%3A00%27%20AND%20week_start_date%3C%3Dtimestamp%20%27{END_TIME_LABEL}%2006%3A59%3A59%27)&orderByFields=week_start_date%20DESC%2Ccollection_area%20ASC&outFields=*&resultType=standard&returnGeometry=false&spatialRel=esriSpatialRelIntersects"


def _construct_collection_url(start_time: str, end_time: str, data_points: int):
    return BASE_URL.replace(START_TIME_LABEL, start_time).replace(END_TIME_LABEL, end_time).replace(DATA_POINTS_LABEL, str(data_points))


def _request_data(start_time: str, end_time: str, data_points: int):
    url = _construct_collection_url(start_time, end_time, data_points)
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to collect data from {url}")

    return response.json()


#
# data parsing
#

def _parse_time(time_str: str):
    timestamp_seconds = int(time_str) / 1000
    date = datetime.datetime.utcfromtimestamp(timestamp_seconds)
    return date


def collect_data(start_time="2021-08-21", end_time="2023-09-05", data_points=1000):
    raw_data = _request_data(start_time, end_time, data_points)
    features = raw_data["features"]

    data = defaultdict(dict)
    for feature in features:
        attributes = feature["attributes"]
        collection_area = int(attributes["collection_area"][-1])
        week_start_date = _parse_time(attributes["week_start_date"])
        gene_copies_per_liter = int(attributes["gene_copies_per_liter"])
        data[week_start_date][collection_area] = gene_copies_per_liter

    return data
