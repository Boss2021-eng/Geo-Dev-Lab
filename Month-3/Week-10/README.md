# Week 10: Geospatial Automation and Python
## Overview
- Loaded, inspected, joined and visualised the Month 3 starter datasets using GeoPandas.
- Developed and executed `my_explore.py` as part of the independent challenge, using my Month 1 Lagos administrative and health facility dataset ([Lagos_Health_and_LGA.gpkg](https://github.com/Boss2021-eng/Geo-Dev-Lab/blob/main/week%203/Lagos_Health_and_LGA.gpkg))
- Extracted and processed the health facility data from Month 1, successfully saving all 2,320 facilities in EPSG:4326 ([facilities_independent.gpkg](https://github.com/Boss2021-eng/Geo-Dev-Lab/blob/main/Month-3/Week-10/Independent_challenge/files/facilities_independent.gpkg)) using ([my_points.py](https://github.com/Boss2021-eng/Geo-Dev-Lab/blob/main/Month-3/Week-10/Independent_challenge/my_points.py))
- Enriched the Lagos LGA shapefile from Week 2 with estimated population data from the LGA population CSV. Successfully performed a left join, matching all 20 LGAs using  ([my_join.py](https://github.com/Boss2021-eng/Geo-Dev-Lab/blob/main/Month-3/Week-10/Independent_challenge/my_join.py))
- Created a map showing Lagos LGA boundaries and the first 20 healthcare facilities to avoid overcrowding ([lagos_facilities_map.png](https://github.com/Boss2021-eng/Geo-Dev-Lab/blob/main/Month-3/Week-10/Independent_challenge/files/lagos_facilities_map.png)) using ([my_make_map.py](https://github.com/Boss2021-eng/Geo-Dev-Lab/blob/main/Month-3/Week-10/Independent_challenge/my_make_map.py))

## How to run it from the repository root
  ` uv run Month-3\Week-10\explore_layer.py`

 ## What I Found

I found GeoPandas easier to use than QGIS for data exploration and transformation because of its libraries and reproducible functions.

## What Went Wrong and How I Fixed It

While attempting to join the Lagos LGAs with the estimated population data, the code failed because one of the column names contained leading and trailing whitespace. I used Python's `.columns` attribute to inspect the actual column names, identify the whitespace issue and reference the correct column name in the merge operation. After correcting this, the merge executed successfully on the first attempt, adding the estimated population data to all 20 LGAs.
