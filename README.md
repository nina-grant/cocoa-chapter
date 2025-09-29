# Cocoa Climate Change Modeling  
[![License: MIT](https://img.shields.io/badge/Code%20License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![License: CC BY 4.0](https://img.shields.io/badge/Docs%20License-CC--BY%204.0-blue.svg)](https://creativecommons.org/licenses/by/4.0/)

This repository contains the code and supporting files used for the analyses in:  

> **Grant, N., Kiniry, J., and Aziz, F. (2025).** *Modeling the Impacts of Climate Change on Cocoa.* In: *Theobroma cacao – Past, Present and Future Insights* [Working Title]. IntechOpen. DOI: [10.5772/intechopen.1011776](http://dx.doi.org/10.5772/intechopen.1011776)  

### 🙏 Acknowledgments

Please cite the following if you use this code:

> Grant, N. (2025). Code for 'Modeling the Impacts of Climate Change on Cocoa'. Zenodo. https://doi.org/10.5281/zenodo.17229362


---

## 📖 Overview  
This repo includes scripts and notebooks used to process climate data, run crop model simulations, and analyze potential impacts of climate change on *Theobroma cacao* production. The workflow integrates NASA NEX-GDDP climate projections with the ALMANAC crop model and supporting utilities.  

---

## 📂 Repository Contents  

- **`NEX.ipynb`** – Jupyter notebook for downloading and processing NEX-GDDP CMIP6 climate data and analyzing ALMANAC output.  
- **`auto_GUI.py`** – Python script for interacting with the ALMANAC model’s GUI automatically.  
- **`failed_downloads.txt`** – Log of unsuccessful climate data downloads.  
- **`labeled_clicks.txt`** – Log file for automated GUI actions.  
- **`position_logger.py`** – Helper script to record screen positions for GUI automation.  

---

## ⚙️ Requirements  

- Python ≥ 3.8  
- Jupyter Notebook  
- Common libraries: `numpy`, `pandas`, `matplotlib`, `xarray`, `netCDF4`, `requests`, `selenium` (or similar GUI automation library)  

## 🚀 Usage

1. Open NEX.ipynb in Jupyter to reproduce data preprocessing and download routines.
2. Check failed_downloads.txt for any missing files and re-run as needed.
3. Use position_logger.py to calibrate screen positions for GUI automation. 
4. Run auto_GUI.py to automate ALMANAC model simulations (requires local installation of ALMANAC).

## 🌍 Data Sources

- NASA NEX-GDDP CMIP6 climate projections: https://www.nccs.nasa.gov/services/data-collections/land-based-products/nex-gddp
- ALMANAC crop model (Kiniry et al. 1992) available at: https://www.ars.usda.gov/plains-area/temple-tx/grassland-soil-and-water-research-laboratory/docs/193226/
