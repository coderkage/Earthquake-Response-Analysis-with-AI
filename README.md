# Earthquake Response Analysis with AI

This repository contains the code and datasets for analyzing earthquake responses using AI-based techniques, including Named Entity Recognition (NER) and geospatial analysis. The project leverages custom training and testing datasets, transfer learning with spaCy, and visualizations to map the severity of earthquake impacts based on extracted location data.

---

## Folder Structure


```
Project:
├───datasets
│   │   added_locs.csv
│   │   city.csv
│   │   coordinates.csv
│   │   countries.csv
│   │   jp.csv
│   │   jpgpe.csv
│   │   jpgpe1.csv
│   │   jptweets.csv
│   │   world-data-2023.csv
│   │
│   ├───test
│   │       1xjp.jsonl
│   │       2xjp.jsonl
│   │       3xjp.jsonl
│   │       4xjp.jsonl
│   │       5xjp.jsonl
│   │
│   └───train
│           1xfiltered_tagged_gpe.jsonl
│           1xtagged_gpe.jsonl
│           2xfiltered_tagged_gpe.jsonl
│           3xfiltered_tagged_gpe.jsonl
│           4xfiltered_tagged_gpe.jsonl
│           5xfiltered_tagged_gpe.jsonl
│           output.jsonl
│           output2.jsonl
│           output3.jsonl
│           output4.jsonl
│
├───main
│   │   1.ipynb
│   │   2.ipynb
│   │   3.ipynb
│   │   4.ipynb
│   │   5.ipynb
│   │   gpe.csv
│   │   hashtags.csv
│   │   loss.ipynb
│   │   loss.txt
│   │   map.ipynb
│   │   valid_gpe.csv
│   │   verified_valid_gpe.csv
│   │
│   └───model_1.2j.2
│       
│
└───maps
|       jp_locations_map.html
|       map.html
|
└───code1
|
└───code2
|
└───README.md
```


### 1. `datasets/`
Contains all the datasets and JSONL files for training and testing.

- **CSV Files:**
  - `added_locs.csv`, `city.csv`, `coordinates.csv`, `countries.csv`, `geonames.csv`: Auxiliary location datasets.
  - `jp.csv`, `jpgpe.csv`, `jptweets.csv`, `mx.csv`, `mxtweets.csv`, etc.: Specific datasets for Japan, Mexico, and other regions.
  - `tweets.csv`: Main dataset of tweets.
  - `world-data-2023.csv`: Global data for additional analysis.

- **Test Data (`test/`):**
  - `5xjp.jsonl` file: Processed final testing data of Japanese earthquake-related tweets.
  - JSONL files (`1xjp.jsonl` to `4xjp.jsonl`) backup files created on each step of test data preparation.

- **Train Data (`train/`):**
  - Tagged datasets (`1xfiltered_tagged_gpe.jsonl` to `5xfiltered_tagged_gpe.jsonl` and `output3.jsonl` to `output3.jsonl`)  backup files created on each step of train data preparation.
  - `output4.jsonl` file: Processed final training data (GPE and DISASTER tagged) for custom-NER.
 
- **Large Datasets:**
  - Due to size limits and copyright issues, we have skipped following datasets to add in the repository. They can be easily accessed from the provided links:
  - `geonames.csv` file: [geonames.org](geonames.org)
  - `tweets.csv` file: [https://www.kaggle.com/datasets/swaptr/turkey-earthquake-tweets](https://www.kaggle.com/datasets/swaptr/turkey-earthquake-tweets)

---

### 2. `main/`
Contains notebooks and related files for the primary analysis and model training/testing.

- **Notebooks:**
  - `1.ipynb`: Collects valid locations related to Turkey, Syria, and Japan.
  - `2.ipynb`: Prepares the training dataset by tagging `GPE` (Geopolitical Entity) and `DISASTER`.
  - `3.ipynb`: Implements transfer learning using spaCy’s small model on the custom NER training dataset.
  - `4.ipynb`: Prepares the testing dataset for tweets about the 2024 Noto earthquake in Japan.
  - `5.ipynb`: Performs model testing and evaluation.
  - `map.ipynb`: Plots a severity map of extracted locations using the trained model.

- **Other Files:**
  - `gpe.csv`, `valid_gpe.csv`, `verified_valid_gpe.csv`: Files containing validated and verified GPE data.
  - `hashtags.csv`: Hashtags used for tweet extraction (Turkey-Syria, 2023).
  - `loss.ipynb` & `loss.txt`: Records and visualizes model loss during training.
  - Model folder (`model_1.2j.2`): Stores trained model files.

---

### 3. `maps/`
Contains HTML files for visualized maps:
- `jp_locations_map.html`: Interactive map of all locations in Japan.
- `map.html`: Severity map based on earthquake-related tweet analysis (Japan, 2024).

---

### 4. `code1/` and `code2/`
These folders contain additional files and scripts used for experiments and background work. While not part of the primary workflow, they supported the project's development and analysis phases. Due to the complexity and extensive cross-referencing of these files, the detailed documentation of these folders can't be provided and is not necessary.

---

## Usage

### Steps to Reproduce:
1. **Data Preparation:**
   - Run `1.ipynb` to collect valid locations for analysis.
   - Use `2.ipynb` to prepare a custom training dataset by tagging GPE and DISASTER entities.

2. **Model Training:**
   - Execute `3.ipynb` to fine-tune the spaCy NER model using transfer learning.

3. **Data Testing:**
   - Use `4.ipynb` to prepare the testing dataset (e.g., tweets about the Noto earthquake).
   - Run `5.ipynb` to test the trained model and evaluate performance.

4. **Visualization:**
   - Generate severity maps using `map.ipynb` and view results in the `maps/` folder.

---

## Highlights

- **NER for Earthquake Analysis:**
  Custom NER tags (`GPE` and `DISASTER`) enhance traditional geotagging methods to extract more meaningful information from tweets.

- **Geospatial Mapping:**
  Interactive maps visualize severity and impacted areas based on tweet data.

- **Transfer Learning:**
  Leverages spaCy’s capabilities to improve model performance on earthquake-specific data.

---

## Dependencies

- Python 3.12.2
- Libraries: `spaCy`, `pandas`, `re`, `folium`, `opencage`, `geopy`, `matplotlib`, `tqdm`, `sklearn`, `seaborn`, `json` etc.

---


