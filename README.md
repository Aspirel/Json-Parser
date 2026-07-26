# 📦 JSON Parser Tool

A small desktop tool built with Python and PySide6 for inspecting and cleaning JSON files.  
It started as a personal utility to help with messy API responses and large JSON exports, and has since been refactored to be a bit more structured and easier to maintain.

The app lets you load a JSON file, pick fields you want to check, and then filter out items based on simple conditions (duplicates, empty values, null values). Results are shown in separate tabs and can be saved back out as JSON.

---

## ✨ Features

- Load and preview JSON files  
- Select which fields you want to inspect  
- Remove:
  - duplicate values  
  - empty strings  
  - null values  
- Shows results in two tabs:
  - **Matched items**  
  - **Remaining items**  
- Save filtered results to new JSON files  
- Progress bar + threaded parsing for large files  

---

## 🧠 How it works

The parsing logic is separated from the UI:

- The UI (PySide6) handles file selection, field selection, and displaying results.
- The parser module handles:
  - walking nested JSON structures  
  - checking values against a condition  
  - returning two lists: “found” and “remaining”  
- A worker thread is used so the UI doesn’t freeze during parsing.

The parser itself is intentionally simple — it recursively walks dictionaries/lists and checks values for the selected fields.

---

## 🚀 Getting Started

### Install dependencies

```bash
pip install -r requirements.txt
```

(If you don’t have a requirements file, install PySide6 manually.)

```bash
pip install PySide6
```

### Run the app

```bash
python app.py
```

---

## 📁 Project Structure

```
src/
  app.py                   // main entry point
  main.py                  // main window + UI setup
  parser_controller.py     // UI-facing parsing logic
  json_parser.py           // pure parsing functions
  workerThread.py          // background thread wrapper
  utils.py                 // small UI helpers
  Layouts/                 // PySide6 layout widgets
```

---

## 🛠 Tech Stack

- Python 3  
- PySide6 (Qt for Python)  
- Basic JSON parsing  
- Threaded background worker  

---

## 📦 Notes

This project originally started as a quick helper script and grew into a small GUI tool.  
The current version is a cleaned‑up refactor with better separation between UI and logic. It’s still intentionally lightweight — no heavy frameworks, no external dependencies beyond PySide6.

---

## 🔧 Possible Future Improvements

- Add JSON schema validation  
- Add search/filter inside the preview tab  
- Add “remove items where field contains X”  
- Add dark/light theme toggle  
- Add drag‑and‑drop file loading  
- Add support for multiple files at once  

---
