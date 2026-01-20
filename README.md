# Transaction Cleanup Demo (Batch Processing)

This project demonstrates a **reusable batch pipeline** for cleaning messy financial transaction spreadsheets into **analysis-ready Excel files**.

The focus is not on a single file, but on **processing multiple raw transaction files with consistent rules**, similar to real client work on platforms like Upwork.

------

## Problem

Real-world financial spreadsheets (bank statements, expense reports, transaction logs) often contain:

- Merged cells (e.g. one date spanning multiple transactions)
- Mixed date formats
- Amounts stored as text (`$123`, `(300)`, `USD 800`, etc.)
- Repeated headers inside the data
- Subtotal / Total rows mixed with transactions
- Empty separator rows and visual formatting noise

Such files look readable to humans, but are **not suitable for analysis or system import**.

------

## Input

- Multiple raw Excel files (`.xlsx`)
- Each file may contain inconsistent formatting and noise
- Raw files are **never modified** and are treated as the source of truth

Example input files:

```
data/raw/
├── demo1_raw.xlsx
├── demo2_raw.xlsx
└── demo3_raw.xlsx
```

------

## Output

Each raw file is converted into a clean Excel file with:

- One row per transaction
- Standardized schema
- Numeric amounts
- Explicit currency
- No summary or formatting noise

Output schema:

| Column        | Description                            |
| ------------- | -------------------------------------- |
| `date`        | Standardized date (YYYY-MM-DD)         |
| `description` | Cleaned transaction description        |
| `amount`      | Numeric amount (expenses are negative) |
| `currency`    | Extracted or inferred currency         |
| `notes`       | Additional notes (if available)        |
| `source_file` | Original source file name              |

Example output location:

```
data/clean/
├── demo1_clean.xlsx
├── demo2_clean.xlsx
└── demo3_clean.xlsx
```

------

## Pipeline Overview

The cleaning process is implemented as a **modular pipeline**, where each step solves a specific real-world data issue:

1. Normalize column headers
2. Expand merged cells (forward-fill dates)
3. Remove noise rows (empty rows, repeated headers, subtotal/total)
4. Parse and standardize dates
5. Parse amounts and extract currency
6. Enforce final schema and add source metadata

Each rule is implemented as an independent function for clarity and reuse.

------

## Design Notes

- Dates are **only forward-filled when missing due to merged cells**.
   Rows without a reliable date signal are intentionally left blank to avoid fabricating data.
- Original raw values (e.g. text amounts) are preserved alongside parsed numeric fields for traceability.
- The pipeline is designed to be **extensible**, allowing new rules or file formats to be added with minimal changes.

## Project Structure

```
transaction-cleanup-demo/
├── data/
│   ├── raw/        # original input files (never modified)
│   ├── interim/    # optional intermediate stage
│   └── clean/      # cleaned output files
├── src/
│   ├── config.py        # schema and normalization constants
│   ├── clean_rules.py  # core cleaning rules (pipeline)
│   ├── io_utils.py     # file I/O helpers
│   └── run_cleaning.py # pipeline entry point
├── screenshots/
└── README.md
```

------

## How to Run

```bash
python -m src.run_cleaning
```

The script processes all files in `data/raw/` and writes cleaned files to `data/clean/`.

------

## Why This Demo

This project is designed to reflect **real client work**, not toy datasets:

- Batch processing instead of single-file scripts
- Clear separation between raw data and cleaned results
- Explicit, explainable cleaning rules
- Easy to extend for new files or formats

------

## Notes

- This demo focuses on **data cleaning and normalization**, not financial analysis.
- The same pipeline can be applied to new transaction files with similar structure.