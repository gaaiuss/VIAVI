# JSON to CSV Converter

This Python application merges multiple `.json` files into a single file, 
flattens nested data, formats GPON serial numbers, and exports 
the data to a `.csv` file using a configurable column order.

---

## Latest Release

[Realese](https://github.com/gaaiuss/VIAVI/releases/tag/v1.0.0)

---

## Download

[Direct download of the latest version](https://github.com/gaaiuss/VIAVI/releases/download/v1.0.0/VIAVI.OLP-39.Report.Generator.exe)

---

## Features

- **Merge JSON files** from selected existing files
- **Format GPON serial numbers** (4 ASCII + 4 HEX)
- **Flatten nested JSON** using dot notation
- **Write CSV with ordered columns** based on a config csv file

---

## Requirements

- Python **3.10+**
- All the modules required are detailed in `requirements.txt`

---

## Column Configuration

Your `resource/config.csv` should define the column order for the output CSV:

```csv
column,order
test.id,1
results.deviceName,2
results.data.gpon.ontSerialNumber,3
...
