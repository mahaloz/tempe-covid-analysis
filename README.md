# tempe-covid-analysis
A project to understand Tempe's COVID wastewater data.

## Installation
```bash
git clone https://github.com/mahaloz/tempe-covid-analysis.git
python3 pip install -e ./tempe-covid-analysis
```

## Usage
On every query of the data, the data is downloaded from the City of Tempe's new [ArcGIS Data](https://www.arcgis.com/apps/dashboards/0eff3b8443d14c7d8bc7a5a37b82e6b0).
With this in mind, try not to spam this command as it is scraping the API for data.

You can query for the top 10 weeks with the highest average like so:
```bash 
$ python3 -m tempe_covid -average --start-time 2021-08-21 --end-time 2023-08-28
Week       | avg     | std     | max    
---------- | ------- | ------- | -------
2022-01-10 | 1241240 | 983742  | 2509867
2022-08-01 | 1024654 | 1972978 | 5878633
2022-01-03 | 715723  | 567821  | 1383933
2022-07-11 | 687366  | 376887  | 1386733
2022-11-28 | 666491  | 1128491 | 3419967
2022-01-17 | 591735  | 471201  | 1232450
2022-12-19 | 545787  | 395382  | 1118150
2023-08-21 | 514400  | 913580  | 2740500
2022-07-18 | 506879  | 561692  | 1766267
```

## Acknowledgements
This was created in response to a [Reddit Post](https://www.reddit.com/r/ASU/comments/1699rze/covid/) on the ASU subbreddit.
