# Reusable Report Generator

A flexible, Python-based report generator that works for any project type (accounting, sales, HR, or general).

## Setup Steps
1. Create a virtual environment:
   ```bash
   python -m venv venv
   # Windows:
   .\venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Update `config.yaml` for your specific project needs.
4. Place your raw CSV/Excel files in `data/raw/`.

## Running the Project
```bash
python main.py
```

## Structure
- `config.yaml`: Configuration for project name, period, and data type.
- `data/raw/`: Place your input files here.
- `output/`: PDF and Excel reports are generated here.
