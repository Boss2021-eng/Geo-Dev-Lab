
# Week 3 GIS Data Processing and Data Quality Assessment

## 1. Overview

This document summarises the Week 3 GIS data-processing activities, including coordinate reference system transformation, land-area calculation, comparison of area values, GeoPackage export, and an initial assessment of data quality.

The dataset contains administrative boundaries for the 20 Local Government Areas (LGAs) of Lagos State, Nigeria.

## 2. Coordinate Reference System Transformation

The administrative boundary data were initially provided in the geographic coordinate reference system **WGS 84**. The data were reprojected into **WGS 84 / UTM Zone 31N**, a projected coordinate reference system suitable for measuring distances and areas in metres within the relevant geographic region.

Reprojection was carried out to ensure that area calculations were performed using projected coordinates rather than geographic longitude and latitude values.


## 3. Total Area Calculation

After reprojection, the total area of the study region was calculated from the administrative boundary geometries.

The calculated total area was:

**3,622,113,453.442364 square metres**

This is approximately:

**3,622.11 square kilometres**

The total area was calculated and compared with the area values associated with the individual LGA records as part of the validation process.

## 4. LGA Area Comparison

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

## 5. GeoPackage Export

The processed files were exported as GeoPackages (`.gpkg`). The layers were combined into a single layer during export.

GeoPackage is an OGC-supported format for storing geospatial data in a SQLite-based container. It can store geometry, attributes, and spatial reference information in a single file.

Although the exported file contains one combined layer, the administrative attributes remain available as separate fields.

## 6. Missing-Value Assessment

The following fields were inspected for missing values:

- `adm2_name1`
- `adm2_name2`
- `adm2_name3`
- `adm1_name1`
- `adm1_name2`
- `adm1_name3`
- `adm0_name1`
- `adm0_name2`
- `adm0_name3`
- `valid_to`
- `lang1`
- `lang2`
- `lang3`

Each of these fields contained **20 non-null records**, indicating that no null values were detected in these columns for the 20 LGA features examined.

This result should be interpreted as a finding about the inspected fields only. It does not, by itself, establish that all fields in the GeoPackage are complete.

## 7. Data Quality Assessment

### 7.1 Completeness

Completeness refers to the extent to which the required records, attributes, and geometries are present in the dataset.

The dataset contains 20 LGA records, corresponding to the 20 LGAs represented in the study area. The inspected administrative-name, language, and validity-date fields contained 20 non-null records each.

Therefore, the inspected fields showed no missing values. However, some fields showed null values but there were not relevant to the subject at hand.

### 7.2 Currency

Currency refers to how up to date the data are in relation to the date of the analysis and the intended application.

The available information does not establish the date on which the administrative boundaries and associated attributes were last updated. The `valid_to` field was populated for all 20 records, but a non-null value does not necessarily confirm that the data are current.


### 7.3 Positional Accuracy

Positional accuracy describes how closely the recorded geographic positions of features correspond to their true or accepted reference positions.

The data were reprojected from WGS 84 to WGS 84 / UTM Zone 31N to support area measurement. However, reprojection does not improve the original positional accuracy of the boundaries.


### 7.4 Attribute Accuracy

Attribute accuracy refers to the correctness of the descriptive and numerical information associated with each spatial feature.


### 7.5 Fitness for Purpose

Fitness for purpose refers to whether the dataset is sufficiently suitable for the intended analysis or decision-making task.

The processed LGA boundary dataset is potentially suitable for tasks such as:

- Mapping the administrative structure of Lagos State;
- Aggregating health facilities by LGA;
- Joining LGA-level population statistics;
- Performing exploratory spatial analysis;
- Calculating approximate LGA areas;
- Creating thematic maps and spatial visualisations.



**Initial assessment:** The dataset is potentially fit for general LGA-level mapping and exploratory spatial analysis, subject to verification of its source, currency, geometry quality, and attribute definitions.

## 8. Limitations

The following limitations should be considered:


## 9. Conclusion

During Week 3, the LGA boundary dataset was transformed from WGS 84 into UTM Zone 31N to support area calculations. The calculated total area was approximately 3,622.11 km². The processed data were exported as a GeoPackage containing a single combined layer.

The inspected administrative, language, and validity-date fields contained no null values across the 20 LGA records. Nevertheless, completeness, currency, positional accuracy, and attribute accuracy require further validation beyond null-value checks. The dataset may be suitable for LGA-level mapping and exploratory spatial analysis, provided that its source metadata, geometry quality, and intended use are carefully considered.
