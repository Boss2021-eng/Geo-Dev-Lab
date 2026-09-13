# Data Sources and Data Preparation

## 1. Overview

This project uses geospatial and demographic datasets to examine the distribution of healthcare facilities in relation to population density across Lagos State, Nigeria. The datasets consist of administrative boundaries, healthcare facility locations, and LGA-level population and demographic information.

The main spatial datasets were obtained from the **Humanitarian Data Exchange (HDX)**, while the population and demographic data were obtained from the **National Bureau of Statistics (NBS)** through the Kaggle dataset listed below.

The data were processed using Python/GeoPandas and QGIS. The LGA boundary dataset was used as the spatial reference layer, while the healthcare facility data were joined to the relevant LGA using the LGA name.

---

## 2. Dataset Sources

The datasets used in this project were obtained from publicly available geospatial, health, and demographic data sources. The datasets were processed and integrated to support the analysis of healthcare facility distribution and population density across Lagos State.

| Dataset                             | Source                                                                                                                      | Format    | Features/Records | Geometry | Main Purpose                                                                                            |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------- | ---------------: | -------- | ------------------------------------------------------------------------------------------------------- |
| Lagos LGA Boundaries                | [Humanitarian Data Exchange (HDX)](https://data.humdata.org/dataset/cod-ab-nga)                                             | Shapefile |               20 | Polygon  | Defines the 20 Local Government Areas (LGAs) in Lagos State                                             |
| Lagos State Administrative Boundary | [Humanitarian Data Exchange (HDX)](https://data.humdata.org/dataset/cod-ab-nga))                                                               | Shapefile |                1 | Polygon  | Defines the overall administrative boundary of Lagos State                                              |
| Health Facilities                   | [Lagos State Health Facility Assessment Datasets – HSCL](https://doi.org/10.6084/m9.figshare.22118315)                      | CSV       |            2,320 | Point    | Contains the locations and attributes of health facilities in Lagos State                               |
| LGA Population & Demographic Data   | [National Bureau of Statistics (NBS), accessed via Kaggle](https://www.kaggle.com/datasets/favourokoli/lgas-in-lagos-state) | CSV       |               20 | None     | Provides LGA-level population, area, population density, median age, health facilities, and growth rate |


---

# 3. Lagos LGA Administrative Boundaries

### Source

The Lagos LGA administrative boundary data were obtained from the **Humanitarian Data Exchange (HDX)**. HDX provides administrative boundary datasets as part of its geospatial and humanitarian datasets. Administrative boundaries contain the names and identifiers of sub-national administrative units and are commonly used as reference layers for spatial analysis.

[Humanitarian Data Exchange]([https://centre.humdata.org/learning-path/an-introduction-to-geospatial-data/geospatial-data-geographic-information-systems/](https://data.humdata.org/dataset/cod-ab-nga))

### Dataset characteristics

* **Number of features:** 20
* **Geometry type:** Polygon
* **Administrative level:** ADM2/LGA
* **Coverage:** Lagos State, Nigeria
* **Coordinate information:** Stored in the shapefile's `.prj` file
* **Area field:** `area_sqkm`

### Key columns

| Column       | Description                          |
| ------------ | ------------------------------------ |
| `adm2_name`  | Name of the LGA                      |
| `adm2_pcode` | Administrative code for the LGA      |
| `adm1_name`  | State name                           |
| `adm1_pcode` | State administrative code            |
| `adm0_name`  | Country name                         |
| `adm0_pcode` | Country code                         |
| `area_sqkm`  | Area of the LGA in square kilometres |
| `center_lat` | Latitude of the LGA centre           |
| `center_lon` | Longitude of the LGA centre          |
| `geometry`   | LGA polygon geometry                 |

The LGA boundary layer contains **20 polygons**, representing the 20 Local Government Areas of Lagos State.

### Data gaps and limitations

The boundary dataset provides the spatial extent of the LGAs but does not contain the population variables required for the demographic analysis. Population and demographic information were therefore obtained separately and subsequently joined to the LGA boundary layer.

The boundary names must also be consistent with the population dataset when performing an attribute join. Minor differences in spelling or formatting between datasets can result in unmatched records.

---

# 4. Lagos State Administrative Boundary

A separate Lagos State administrative boundary dataset was also obtained from the Humanitarian Data Exchange.

### Dataset characteristics

* **Number of features:** 1
* **Geometry type:** Polygon
* **Coverage:** Lagos State
* **Administrative level:** ADM1

### Key columns

| Column       | Description                              |
| ------------ | ---------------------------------------- |
| `adm1_name`  | State name                               |
| `adm1_pcode` | State administrative code                |
| `adm0_name`  | Country name                             |
| `adm0_pcode` | Country code                             |
| `area_sqkm`  | Area of Lagos State in square kilometres |
| `center_lat` | Latitude of the state centre             |
| `center_lon` | Longitude of the state centre            |
| `geometry`   | Lagos State polygon                      |

This layer was used to represent the overall study-area boundary.

---

# 5. Health Facilities Dataset

The health facility data used in this project are from the **Lagos State Health Facility Assessment Datasets – HSCL**. The dataset contains **2,320 health facility records** covering Lagos State. Each record includes geographic coordinates and facility-related attributes such as LGA, ward, facility type, ownership, accessibility, and functional status.

The original dataset is available through Figshare:

**Source:** [Lagos State Health Facility Assessment Datasets – HSCL](https://doi.org/10.6084/m9.figshare.22118315)
### Dataset characteristics

* **Number of records:** 2,320
* **Number of columns:** 25
* **Format:** CSV
* **Spatial information:** Latitude, longitude and geometry
* **Study area:** Lagos State

### Key columns

| Column       | Description                          |
| ------------ | ------------------------------------ |
| `latitude`   | Latitude of the healthcare facility  |
| `longitude`  | Longitude of the healthcare facility |
| `lganame`    | LGA containing the facility          |
| `lgacode`    | LGA code                             |
| `wardname`   | Ward containing the facility         |
| `wardcode`   | Ward code                            |
| `statename`  | State name                           |
| `statecode`  | State code                           |
| `accessblty` | Accessibility information            |
| `func_stats` | Functional status of facility        |
| `category`   | Facility category                    |
| `ownership`  | Ownership of facility                |
| `type`       | Facility type                        |
| `source`     | Source information                   |
| `prmry_name` | Primary facility name                |
| `alt_name`   | Alternative facility name            |
| `geometry`   | Spatial geometry                     |

### Missing values and data-quality considerations

The health-facility dataset contains several descriptive fields that may not be populated for every facility. Therefore, missing values should be checked before performing analysis based on facility characteristics such as ownership, type, category or functional status.

The `latitude` and `longitude` fields provide the main spatial reference for the facilities. These coordinates should be checked for invalid or missing values before converting the dataset into a point layer in QGIS.

The `lganame` field was used to associate each healthcare facility with an LGA. Name-based joins can be affected by differences in spelling, abbreviations or formatting, so the resulting join should be checked for unmatched records.

---

# 6. LGA Population and Demographic Dataset

### Source

The population and demographic dataset was obtained from the **National Bureau of Statistics (NBS)** and accessed through Kaggle:

[Kaggle – LGAs in Lagos State](https://www.kaggle.com/datasets/favourokoli/lgas-in-lagos-state)

### Dataset characteristics

* **Number of records:** 20
* **Number of columns:** 7
* **Coverage:** 20 Lagos LGAs
* **Geometry:** None
* **Format:** CSV

### Key columns

| Column                            | Description                       |
| --------------------------------- | --------------------------------- |
| `LGAs`                            | Name of the Local Government Area |
| `Estimated Population 2024(Km 2)` | Estimated population for 2024     |
| `Area(Km 2)`                      | LGA area in square kilometres     |
| `Population Density(People/Km2)`  | Population density                |
| `Median Age`                      | Median age of the population      |
| `Health Facilities`               | Number of health facilities       |
| `Growth Rate(%)`                  | Population growth rate            |

The population dataset was joined to the Lagos LGA boundary layer using the **LGA name**.

---

# 7. Data Integration

The datasets were integrated to create a spatial dataset containing both geographic and demographic information for each Lagos LGA.

The main processing workflow was:

```text
Lagos LGA boundary shapefile
          |
          v
Population and demographic CSV
          |
          v
Join using LGA name
          |
          v
LGA spatial dataset with population attributes
          |
          +--------------------+
          |                    |
          v                    v
Health facilities       Population density
          |                    |
          +---------+----------+
                    |
                    v
          Spatial analysis and mapping
```

The healthcare facility dataset was associated with LGAs using the `lganame` field. The population dataset was joined to the LGA polygon layer using the `LGAs` field.

Where population density was calculated independently, the following relationship was used:

**Population Density = Population / Land Area (km²)**

---

# 8. Data Quality and Known Limitations

Several limitations should be considered when interpreting the datasets:

1. **Different data sources:** The administrative boundary, health facility, and demographic datasets were obtained from different sources. Consequently, differences exist in their definitions, data collection methods, and update cycles.

2. **Temporal differences:** The datasets represent different reference periods. The population dataset contains **2024 population estimates**, while the health facility dataset contains records from **2025**. Therefore, the population and health facility data do not represent exactly the same point in time.

3. **Missing attribute values:** Some health facility records contain missing values for selected attributes. These missing values indicate that the corresponding information was not available in the source dataset and were retained as missing during the analysis.

4. **Population estimates:** The population values represent **2024 estimates** rather than census counts. Therefore, they provide estimated population levels for each LGA and should not be interpreted as exact population counts.


---


