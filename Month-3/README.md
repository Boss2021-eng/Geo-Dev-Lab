# Month 3: Geospatial Python Automation
## Week 10

- Loaded, inspected, joined and visualised the Month 3 starter datasets using GeoPandas.
- Developed and executed `my_explore.py` as part of the independent challenge, using my Month 1 Lagos administrative and health facility dataset ([Lagos_Health_and_LGA.gpkg](https://github.com/Boss2021-eng/Geo-Dev-Lab/blob/main/week%203/Lagos_Health_and_LGA.gpkg))
- Extracted and processed the health facility data from Month 1, successfully saving all 2,320 facilities in EPSG:4326 ([facilities_independent.gpkg](https://github.com/Boss2021-eng/Geo-Dev-Lab/blob/main/Month-3/Week-10/Independent_challenge/files/facilities_independent.gpkg)) using ([my_points.py](https://github.com/Boss2021-eng/Geo-Dev-Lab/blob/main/Month-3/Week-10/Independent_challenge/my_points.py))
- Enriched the Lagos LGA shapefile from Week 2 with estimated population data from the LGA population CSV. Successfully performed a left join, matching all 20 LGAs using  ([my_join.py](https://github.com/Boss2021-eng/Geo-Dev-Lab/blob/main/Month-3/Week-10/Independent_challenge/my_join.py))
- Created a map showing Lagos LGA boundaries and the first 20 healthcare facilities to avoid overcrowding ([lagos_facilities_map.png](https://github.com/Boss2021-eng/Geo-Dev-Lab/blob/main/Month-3/Week-10/Independent_challenge/files/lagos_facilities_map.png)) using ([my_make_map.py](https://github.com/Boss2021-eng/Geo-Dev-Lab/blob/main/Month-3/Week-10/Independent_challenge/my_make_map.py))

## Week 12:
- Loaded and inspected Landsat 8 Collection 2 Level-2 (L2SP) imagery for Lagos using my_inspect.py. Worked with scene LC08_L2SP_191055_20261104_20261116_02_T1, acquired on 4 November 2026, covering WRS-2 Path 191 and Row 055.

- Examined Landsat scene metadata, including acquisition date, processing level, spatial resolution, spectral bands and surface reflectance properties using my_inspect.py.

- Generated a Normalized Difference Water Index (NDWI) map using Landsat 8 Bands 3 (Green) and 5 (Near Infrared), applying surface reflectance scaling factors and using my_index.py and myplot.py for index calculation and visualization.

- Loaded and inspected SRTM 1 Arc-Second Global Digital Elevation Model (DEM) data for Lagos to examine elevation characteristics.

- Performed zonal statistical analysis on the Lagos DEM to derive elevation statistics and calculate mean elevation values across health facility locations.


- Performed zonal statistical analysis on the Lagos DEM to derive elevation statistics and calculate mean elevation across health facility locations.
