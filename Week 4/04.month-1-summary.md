
# Month 1 Summary

## Spatial Question

How well are healthcare facilities distributed in relation to population across Lagos State, Nigeria?

## Spatial Join Operation

The **Summarize by Location**, a kind of spatial join operation, was used to determine the number of healthcare facilities within each of the 20 Local Government Areas (LGAs) of Lagos State. The operation summarized the healthcare facility point features by LGA and produced a facility count field based on the feature ID (`fid`), which was subsequently renamed **Health_facilities_count**.

A verification check was also carried out because some healthcare facility points were not initially captured by the spatial summary. The analysis identified 2,315 facilities automatically, while five facilities were excluded because of minor spatial shifts in their locations. These consisted of two facilities each in Eti-Osa and Ikorodu and one facility in 
Badagry. The five facilities were manually added to the corresponding LGA counts, giving a final total of **2,320 healthcare facilities**.

The **population-to-facility ratio** was then calculated by dividing the estimated population of each LGA by its number of healthcare facilities:

**Population-to-Facility Ratio = Estimated Population / Number of Healthcare Facilities**

This ratio was used to examine the relationship between population demand and healthcare facility availability as shown in the table below.

| LGA              | Estimated Population (2024) | Area (km²) | Population Density (People/km²) | Median Age | Health Facilities | Population-to-Facility Ratio |
| ---------------- | --------------------------: | ---------: | ------------------------------: | ---------: | ----------------: | ---------------------------: |
| Agege            |                   1,003,400 |       45.5 |                          22,070 |       18.5 |                79 |                    12,701.27 |
| Ajeromi-Ifelodun |                   1,734,400 |       45.3 |                          38,290 |       19.2 |                78 |                    22,235.90 |
| Alimosho         |                   2,047,000 |      185.2 |                          11,055 |       19.0 |               222 |                     9,220.72 |
| Amuwo Odofin     |                   1,318,100 |       45.5 |                          28,975 |       18.8 |               110 |                    11,982.73 |
| Apapa            |                   1,064,100 |       24.5 |                          43,400 |       20.0 |                53 |                    20,077.36 |
| Badagry          |                   1,047,600 |    2,774.7 |                             378 |       21.0 |                86 |                    12,181.40 |
| Epe              |                   1,006,700 |    3,877.3 |                             260 |       22.0 |                48 |                    20,972.92 |
| Eti-Osa          |                   1,101,400 |    1,170.0 |                             943 |       19.5 |                89 |                    12,375.28 |
| Ibeju-Lekki      |                   1,083,200 |    3,446.0 |                             314 |       20.5 |                50 |                    21,664.00 |
| Ifako-Ijaiye     |                   1,262,500 |       45.5 |                          27,700 |       18.5 |               123 |                    10,264.23 |
| Ikeja            |                   1,091,100 |      49.92 |                          21,854 |       18.5 |               170 |                     6,418.24 |
| Ikorodu          |                   1,177,600 |    1,410.0 |                             835 |       19.0 |               189 |                     6,230.69 |
| Kosofe           |                   1,665,400 |       45.5 |                          36,500 |       18.5 |               157 |                    10,607.64 |
| Lagos Island     |                   1,146,200 |        8.5 |                         135,411 |       20.0 |                61 |                    18,790.16 |
| Lagos Mainland   |                   1,231,600 |       45.5 |                          27,000 |       18.5 |                90 |                    13,684.44 |
| Mushin           |                   1,439,200 |       45.5 |                          31,600 |       18.5 |               121 |                    11,894.21 |
| Ojo              |                   1,456,800 |       45.5 |                          32,000 |       18.5 |               151 |                     9,647.68 |
| Oshodi-Isolo     |                   1,621,700 |       45.5 |                          35,600 |       18.5 |               184 |                     8,813.59 |
| Shomolu          |                   1,356,800 |       45.5 |                          29,900 |       18.5 |                80 |                    16,960.00 |
| Surulere         |                   1,691,400 |       45.5 |                          37,200 |       18.5 |               179 |                     9,449.16 |


The resulting values were classified using the **Equal Interval** classification method into four access categories: **High Access, Moderately High Access, Moderately Low Access, and Low Access**. A graduated symbology **(Equal Interval)** was then applied to visualize the spatial variation in healthcare access across Lagos State as shown in the map below

<img width="3507" height="2480" alt="Spatial Distribution of Health Facilities in relation to Population in Lagos" src="https://github.com/user-attachments/assets/5674b7c3-e0c1-417f-b92a-e4407c4cba8e" />


The files were exported as a geopackage file `Lagos_lga_and_health.gpkg`

## What Was Expected

It was expected that LGAs with larger populations  would have greater pressure on available healthcare facilities and therefore potentially show lower levels of spatial access. Conversely, areas with fewer people relative to the number of healthcare facilities were expected to have more favourable facility-to-population conditions.

The analysis was therefore intended to identify areas where the distribution of healthcare facilities appears relatively adequate in relation to population and areas where healthcare infrastructure may be comparatively strained.

## What Was Obtained

The analysis showed variation in healthcare facility access across the 20 LGAs. **Ikorodu, Alimosho, Ojo, Ikeja, and Oshodi-Isolo** were classified as having relatively high spatial healthcare access based on the population-to-facility ratio.

In contrast, **Epe and Ibeju-Lekki**, particularly in the eastern part of Lagos State, showed relatively low spatial healthcare access. This indicates that the number of healthcare facilities relative to the estimated population differs substantially between LGAs.

It is important to note that the population-to-facility ratio measures the number of people per healthcare facility rather than physical accessibility. A lower ratio indicates fewer people per facility, while a higher ratio indicates more people per facility. Therefore, the access categories describe **relative facility availability in relation to population**, rather than actual travel accessibility to healthcare facilities.

## What Surprised Me

One of the notable findings was that some highly populated LGAs, including **Alimosho**, were classified as having relatively high spatial healthcare access. This suggests that a large population does not necessarily correspond to low access when the number of healthcare facilities is considered relative to the population.

It was also unexpected that **Epe and Ibeju-Lekki**, located toward the eastern part of Lagos State, showed relatively low spatial healthcare access. This highlights that the spatial distribution of healthcare facilities does not appear to be uniform across the state and that some peripheral LGAs may have fewer facilities relative to their estimated populations.

## Data Still Needed

The current analysis measures healthcare facility availability relative to population but does not account for the physical accessibility of those facilities. Additional spatial data are therefore required to provide a more complete assessment of healthcare access.

The main data still needed are:

- **Road network data** for Lagos State to assess how easily healthcare facilities can be reached through the road system.
- **Population distribution data at a finer spatial resolution**, such as wards, census enumeration areas, or population grids, rather than relying only on LGA-level population estimates.
- **Road distance or travel-time data** to measure accessibility to healthcare facilities.
- Where available, **healthcare facility characteristics**, such as facility type, capacity, services provided, staffing, and opening status.

A potential next step is to use the road network to determine whether healthcare facilities are located within approximately **100–200 metres of accessible roads**. However, a simple 100–200 m buffer would measure proximity to roads rather than actual accessibility. A network-based distance or travel-time analysis would provide a stronger assessment because it can account for the road structure and travel routes between population locations and healthcare facilities.

## Month 1 Conclusion

The first month established a baseline measure of healthcare facility distribution across Lagos State by relating the number of healthcare facilities in each LGA to its estimated population. The analysis identified substantial spatial variation in population-to-facility ratios, with some LGAs showing relatively higher facility availability and others showing relatively lower availability. The next stage should extend the analysis from **facility availability** to **physical accessibility**, particularly through the integration of road network and population distribution data.
