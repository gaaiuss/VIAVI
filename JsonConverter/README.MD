# 🧩 JSON to CSV Converter

This Python tool merges multiple `.json` files into a single file, 
flattens nested data, formats GPON serial numbers, and exports 
the data to a `.csv` file using a configurable column order.

---

## 📁 Project Structure

<pre> 
JsonConverter/
├── config/
│   ├── config.csv         # CSV column order definition
│   └── merged.json        # (auto-generated) Merged JSON
├── resource/
│   └── *.json             # Input JSON files
├── output/
│   └── output.csv         # (auto-generated) Final CSV output
├── app.py                 # Main execution script
└── README.md              # Project documentation
 </pre>


---

## 🚀 Features

- 🔁 **Merge JSON files** from a directory
- 🔧 **Format GPON serial numbers** (4 ASCII + 4 HEX)
- 📐 **Flatten nested JSON** using dot notation
- 🧾 **Write CSV with ordered columns** based on config

---

## 🔧 Requirements

- Python **3.10+**
- All the modules required are detailed in `requirements.txt`

---

## ⚙️ Column Configuration

Your `config/config.csv` should define the column order for the output CSV:

```csv
column,order
test.id,1
results.deviceName,2
results.data.gpon.ontSerialNumber,3
...
