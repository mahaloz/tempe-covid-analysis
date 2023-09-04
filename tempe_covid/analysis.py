from typing import List, Dict, Tuple, Optional, Union
from datetime import datetime
from collections import defaultdict
import statistics


def sort_by_observation_average(data: Dict[datetime,Dict[int,int]]):
    """
    Sorts the data by the average of the observations for each week.
    """
    reformatted_data = defaultdict(dict)
    for week, observations in data.items():
        obs = list(observations.values())
        date = week.strftime('%Y-%m-%d')
        reformatted_data[date]['avg'] = int(statistics.mean(obs))
        reformatted_data[date]['std'] = int(statistics.stdev(obs))
        reformatted_data[date]['max'] = max(obs)

    return sorted(reformatted_data.items(), key=lambda x: x[1]['avg'], reverse=True)