
# Week 3 GIS Data Processing and Data Quality Assessment

## 1. Overview

This data note summarises the Week 3 GIS data-processing activities, including coordinate reference system transformation, land-area calculation, comparison of area values, GeoPackage export, and an initial assessment of data quality.

## 2. Clipping of Dataset
The dataset contains administrative boundaries of Nigeria, Local Government Areas (LGAs) in Nigeria, and health facility locations across the country. Lagos State was selected as the study area. The national administrative boundary dataset was filtered to extract the boundary of Lagos State, which was saved as a separate shapefile.

The health facilities dataset and the shapefile containing the Local Government Area boundaries of Lagos State were subsequently clipped to the study area. The resulting dataset contains the administrative boundaries of the 20 Local Government Areas (LGAs) of Lagos State, Nigeria, alongside health facility data within the state

The dataset contains administrative boundaries for the 20 Local Government Areas (LGAs) of Lagos State, Nigeria.

## 3. Coordinate Reference System Transformation

The administrative boundary data were initially provided in the geographic coordinate reference system **WGS 84**. The data were reprojected into **WGS 84 / UTM Zone 31N**, a projected coordinate reference system suitable for measuring distances and areas in metres within the relevant geographic region.

Reprojection was carried out to ensure that area calculations were performed using projected coordinates rather than geographic longitude and latitude values.


## 4. Total Area Calculation

After reprojection, the total area of the study region was calculated from the administrative boundary geometries.

The calculated total area was:

**3,622,113,453.442364 square metres**

This is approximately:

**3,622.11 square kilometres**

The total area was calculated and compared with the area values associated with the individual LGA records as part of the validation process.

## 5. LGA Area Comparison

The following table presents the LGA names gotten from the polygon and the area compiled from external sources.  The discrepancy as seen is small

| LGA | Area (km²) | Area (m²) |
|---|---:|---:|
| Agege | 11.47768808 | 11,477,701 |
| Ajeromi-Ifelodun | 12.75628005 | 12,756,278 |
| Alimosho | 183.5597228 | 183,559,683 |
| Amuwo Odofin | 129.4427322 | 129,442,258 |
| Apapa | 20.06657372 | 20,066,577 |
| Badagry | 437.6404753 | 437,639,470 |
| Epe | 1,177.611956 | 1,177,612,505 |
| Eti-Osa | 184.3387492 | 184,337,274 |
| Ibeju-Lekki | 443.099273 | 443,102,863 |
| Ifako-Ijaiye | 33.05235308 | 33,052,346 |
| Ikeja | 46.57791885 | 46,577,861 |
| Ikorodu | 398.8690794 | 398,872,523 |
| Kosofe | 81.56483229 | 81,565,047 |
| Lagos Island | 8.59765152 | 8,597,651 |
| Lagos Mainland | 23.50310191 | 23,503,100 |
| Mushin | 16.5559956 | 16,556,008 |
| Ojo | 155.2963474 | 155,296,128 |
| Oshodi-Isolo | 44.12568968 | 44,125,762 |
| Shomolu | 11.18279279 | 11,182,804 |
| Surulere | 19.54428105 | 19,544,286 |

## 6. GeoPackage Export

The processed files were exported as GeoPackages (`.gpkg`). The layers were combined into a single layer during export.

GeoPackage is an OGC-supported format for storing geospatial data in a SQLite-based container. It can store geometry, attributes, and spatial reference information in a single file.

Although the exported file contains one combined layer, the administrative attributes remain available as separate fields.

## 7. Data Quality Assessment

### 7.1 Completeness

Completeness refers to the extent to which the required records, attributes, and geometries are present in the datasets.

The administrative boundary dataset contains 20 LGA records representing the 20 LGAs of Lagos State. The `administrative_name`, `language`, and `valid_to` fields contained no null values. Other fields contained some null values, but these were not relevant to the objectives of the analysis.

The health-facility dataset was also inspected for missing and inconsistent information. Identified issues relevant to the analysis were corrected before the spatial analysis.

### 7.2 Currency

Currency refers to how up to date the data are in relation to the date of analysis and intended use.

The datasets were obtained from different sources and represent different reference periods. The population dataset contains **2024 population estimates**, while the health-facility dataset contains **2023 records**. The available metadata do not establish the exact date when the administrative boundaries were last updated. Therefore, the datasets should not be assumed to represent the same point in time.

Although the `valid_to` field was populated for all 20 LGA records, a non-null validity date does not necessarily confirm that the boundary data are current.

### 7.3 Positional Accuracy

Positional accuracy refers to how closely the recorded geographic positions of features correspond to their true or accepted locations.

The LGA boundaries were reprojected from **WGS 84 to WGS 84 / UTM Zone 31N** to support area calculations. Reprojection changes the coordinate reference system but does not improve the original positional accuracy of the boundaries.

The corrected health-facility locations were compared visually against a base map. The locations showed little visible deviation from the corresponding mapped features, indicating general spatial consistency. However, this was a visual assessment and not a formal positional-accuracy assessment based on independent ground-truth coordinates.

### 7.4 Attribute Accuracy

Attribute accuracy refers to the correctness and consistency of the descriptive and numerical information associated with spatial features.

The administrative and health-facility datasets were inspected for missing and inconsistent attributes. Identified issues in the health-facility dataset that affected the analysis were corrected before further processing.

However, differences in data definitions, collection methods, and source metadata may affect the comparability of attributes across the administrative, health-facility, and demographic datasets.

### 7.5 Fitness for Purpose

The processed datasets are suitable for the objectives of this study, which focus on assessing the distribution of healthcare facilities in relation to population density across Lagos State. They support:

Mapping the spatial distribution of healthcare facilities across Lagos State
Calculating population density for each LGA
Determining healthcare facility availability relative to LGA population
Comparing population density with healthcare facility distribution
Identifying LGAs with relatively high population density but comparatively fewer healthcare facilities
Producing maps and statistical summaries to support the spatial assessment

Overall, the datasets are considered fit for the intended LGA-level spatial analysis.

## 8. Limitations

The analysis had the following limitations:

1. **Different data sources:** The administrative boundary, health-facility, and demographic datasets were obtained from different sources. Differences in definitions, data-collection methods, classification systems, and update cycles may affect their direct comparison.

2. **Temporal differences:** The population dataset contains 2024 population estimates, whereas the health-facility dataset contains 2023 records. Therefore, the datasets do not represent exactly the same point in time.

3. **Population estimates:** The population values are 2024 estimates rather than census counts and should therefore be interpreted as estimated population levels rather than exact population counts.

4. **Positional accuracy:** Health-facility locations were corrected and visually compared with a base map, showing little deviation. However, no independent ground-truth dataset or formal positional-accuracy test was used.

## 9. Conclusion

During Week 3, the LGA boundary dataset was reprojected from **WGS 84 to WGS 84 / UTM Zone 31N** to support area calculations. The total calculated area of the 20 LGAs was approximately **3,622.11 km²**. The processed spatial data were exported as a GeoPackage containing a single combined layer.

The administrative-name, language, and validity-date fields contained no null values across the 20 LGA records, although some non-relevant fields contained missing values. The health-facility dataset was inspected and corrected where necessary. The corrected health-facility locations were then compared visually against a base map and showed little spatial deviation, indicating general positional consistency.

Overall, the processed datasets are suitable for LGA-level mapping, health-facility aggregation, population comparison, and exploratory spatial analysis.
