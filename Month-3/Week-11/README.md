# Week 11: Spatial Operations

## Overview

This week focused on six major spatial operations in GeoPandas: **buffer, spatial join (count), overlay (difference), clip, dissolve, and spatial join (nearest)**.

The exercises applied these operations to Lagos administrative boundaries and health facility datasets to explore spatial relationships, measure geographic areas, identify facility accessibility and validate geographic data.

## 1. Coordinate Reference System and Area Calculation [(`my_crs.py`)](https://github.com/Boss2021-eng/Geo-Dev-Lab/blob/main/Month-3/Week-11/Independent_challenge/my_counts.py)

The Lagos administrative boundaries were projected to **EPSG:32631 (WGS 84 / UTM Zone 31N)** to enable accurate distance and area calculations in metres.

The calculated total area of Lagos was:

- **Total area: 3,619.758928 km²**

Using a projected coordinate reference system ensured that area calculations were performed using appropriate linear units rather than geographic coordinates (latitude and longitude).

## 2. Spatial Join and Facility Count [(`my_counts.py`)](https://github.com/Boss2021-eng/Geo-Dev-Lab/blob/main/Month-3/Week-11/Independent_challenge/my_counts.py)

A spatial join was performed between the health facilities and Lagos Local Government Area (LGA) boundaries to determine the number of health facilities within each LGA.

The `gpd.sjoin()` function was used to associate each health facility with its corresponding administrative boundary. The resulting dataset was grouped by LGA to calculate the facility count.

**Result:**
- Total health facilities in the original dataset: 2,320
- Facilities successfully assigned to an LGA: 2,315
- Facilities not captured: 5

The result was consistent with the facility count obtained during Month 1, providing a useful validation of the earlier analysis.

## 3. Nearest Health Facility Analysis [(`my_reach.py`)](https://github.com/Boss2021-eng/Geo-Dev-Lab/blob/main/Month-3/Week-11/Independent_challenge/my_reach.py)

The nearest spatial join (`gpd.sjoin_nearest()`) was used to identify the nearest health facility to each LGA and calculate the corresponding distance.

The analysis provided the nearest health facility and its distance from each administrative area.

### Results

| LGA | Nearest health facility | Distance (km) |
|---|---|---:|
| Agege | Mayfair Medical Center | 0.27 |
| Ajeromi-Ifelodun | Cardoso Catholic Clinic | 0.30 |
| Alimosho | Ogbomoshotedo Community Health Centre | 0.12 |
| Amuwo Odofin | Female Prison Primary Health Center | 1.70 |
| Apapa | Sacred Heart Clinic | 0.30 |
| Badagry | Sakdos Tradomedical | 0.16 |
| Epe | Papa Primary Health Care Center | 3.24 |
| Eti-Osa | Baefem Specialist Hospital | 0.77 |
| Ibeju-Lekki | Ibeju Health Center | 2.92 |
| Ifako-Ijaiye | Emerald Clinic | 0.35 |
| Ikeja | Alban Specialist Hospital | 0.17 |
| Ikorodu | Elepe Primary Health Center | 0.17 |
| Kosofe | Leye Clinic | 0.58 |
| Lagos Island | Massey Health Post | 0.08 |
| Lagos Mainland | Barry International Hospital | 0.16 |
| Mushin | Merit Medical Center | 0.26 |
| Ojo | Abodunrin Health Care Hospital | 0.41 |
| Oshodi-Isolo | Sentinel Hospital | 0.50 |
| Shomolu | Oloja Primary Health Center | 0.09 |
| Surulere | Olaniba Memorial Hospital | 0.06 |

The results showed variations in the distance to the nearest health facility across the LGAs. Epe had the highest recorded distance (3.24 km), followed by Ibeju-Lekki (2.92 km), while Surulere had the lowest (0.06 km).

This analysis provides an initial indication of the spatial proximity of health facilities to administrative areas. However, proximity alone does not establish healthcare accessibility, as factors such as road networks, travel time, facility capacity and service availability were not considered.

## 4. Geometry Validation [(`my_validity.py`)](https://github.com/Boss2021-eng/Geo-Dev-Lab/blob/main/Month-3/Week-11/Independent_challenge/my_validity.py)

The `my_validity.py` script was used to check the geometric validity of the Lagos LGA boundaries.

**Result:** All polygons were valid, with no invalid geometries detected.

This confirmed that the boundary dataset was suitable for subsequent spatial operations without requiring geometry repair.

## 5. Map Visualisation [(`my_make_map.py`)](https://github.com/Boss2021-eng/Geo-Dev-Lab/blob/main/Month-3/Week-11/Independent_challenge/my_make_map.py)

The `my_make_map.py` script was used to visualise the Lagos LGA boundaries alongside the health facility locations.

The map provided a spatial overview of the distribution of health facilities across Lagos and helped communicate the relationship between administrative boundaries and healthcare locations.

## Challenges Encountered

One of the challenges encountered was inconsistent naming conventions between datasets when attempting to join records using a common field.

To resolve this, I applied a name cleaning function to standardise, and clean the values before performing the join. This improved consistency between the datasets and enabled the spatial analysis to proceed.

## Limitations

The spatial join identified 2,315 of the 2,320 health facilities within the Lagos LGA boundaries. The remaining five facilities were not captured by the join.

This could be due to facilities located outside the administrative boundaries, inaccurate coordinate locations or points falling exactly on polygon boundaries when using the `within` predicate.

Further investigation would be required to establish the specific reasons.

Additionally, the nearest facility analysis measured straight-line distances rather than actual travel distances. Therefore, the results should be interpreted as geographic proximity rather than definitive measures of healthcare accessibility.

## How to Run from the Root Terminal

Run the following command in the project root directory:

```bash
uv run Month-3/Week-10/clip_dissolve.py
```

Replace `clip_dissolve.py` with the relevant script name when running the other exercises.

## Key Learning Outcomes

Through this week's exercises, I gained practical experience in:

- Reprojecting geographic datasets into an appropriate projected CRS for area and distance calculations.
- Using spatial joins to count features within administrative boundaries.
- Applying nearest spatial joins to identify the closest facilities and calculate distances.
- Working with buffer, overlay, clip and dissolve operations to manipulate spatial datasets.
- Validating polygon geometries before performing spatial analysis.
- Visualising spatial relationships between administrative boundaries and point datasets.

Overall, this week's exercises strengthened my understanding of how GeoPandas can be used to perform spatial analysis, manipulate geographic datasets and derive meaningful insights from location-based data.
