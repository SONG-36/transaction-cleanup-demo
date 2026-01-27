# ✅ Demo 1 · Transaction Cleanup (Before → After)

## Financial Transaction Cleanup Demo

**Excel / Bank Statement Normalization (Batch Processing)**

This project demonstrates a **production-style data cleaning pipeline** for transforming **messy financial transaction spreadsheets** into **analysis-ready tables**.

It is designed to reflect **real client work on platforms like Upwork**, where data often comes from:

* Bank exports
* Accounting systems
* Manually edited Excel files

---

## 🔴 The Problem (Before Cleaning)

Real-world transaction spreadsheets often look like this:

**Common issues in raw data:**

* Dates appear in **multiple formats**
  (`2024-01-01`, `Jan 3, 2024`, `2024.01.05`, etc.)
* Amounts stored as **text, not numbers**
  (`USD 52`, `$14.77`, `(32)`, `¥503`)
* Mixed currencies in a single column
* Merged cells (one date covering multiple rows)
* Repeated headers and visual separators
* Subtotal / balance rows mixed with transactions
* Empty rows used for visual spacing

👉 **Human-readable, but not machine-usable**

### 📌 Example: Raw Input

**Screenshot:**

```
screenshots/demo1_before_raw.png
```

(Shows mixed date formats, text-based amounts, merged cells, and noise rows)

---

## 🟢 The Result (After Cleaning)

Each raw file is converted into a **clean, standardized transaction table**.

**What the pipeline guarantees:**

* ✅ One row = one transaction
* ✅ Fully parsed numeric `amount`
* ✅ Explicit `currency` column
* ✅ Standardized date format (`YYYY-MM-DD`)
* ✅ Original raw values preserved for traceability
* ✅ Batch-processed across multiple files

### 📌 Example: Clean Output

**Screenshot:**

```
screenshots/demo1_after_clean.png
```

**Example rows:**

| date       | description         | amount | currency | notes   | source_file    |
| ---------- | ------------------- | ------ | -------- | ------- | -------------- |
| 2024-01-02 | Grocery Store       | 11.00  | UNKNOWN  | monthly | demo1_raw.xlsx |
| 2024-01-03 | Gas Station         | 52.00  | USD      | PayPal  | demo1_raw.xlsx |
| 2024-01-03 | Restaurant          | 503.00 | JPY      | bank    | demo1_raw.xlsx |
| 2024-01-05 | Online Subscription | -9.00  | UNKNOWN  | cash    | demo1_raw.xlsx |

---

## 📂 Input → Output Overview

### Input (Raw Files)

```
data/raw/
├── demo1_raw.xlsx
├── demo2_raw.xlsx
└── demo3_raw.xlsx
```

* Files may differ in formatting
* Raw files are **never modified**

### Output (Clean Files)

```
data/clean/
├── demo1_clean.xlsx
├── demo2_clean.xlsx
└── demo3_clean.xlsx
```

Each output file follows the **same schema**, making it ready for:

* Data analysis
* BI tools
* Database import
* Accounting systems

---

## ⚙️ Cleaning Pipeline (How It Works)

The pipeline is intentionally **modular and explainable**:

1. Normalize column headers
2. Forward-fill dates caused by merged cells
3. Remove noise rows (empty lines, headers, totals)
4. Parse and standardize dates
5. Parse amounts and extract currency
6. Enforce final schema
7. Attach source file metadata

Each step is implemented as an **independent rule**, not a monolithic script.

---

## 🧠 Design Decisions

### No Data Fabrication

Dates are only forward-filled when clearly caused by merged cells.

### Traceability First

Raw amount strings are preserved alongside parsed numeric values.

### Batch-Oriented

The pipeline processes **all files in `data/raw/` automatically**.

### Reusable

New files with similar structure require **no code changes**.

---

## 🏗 Project Structure

```
transaction-cleanup-demo/
├── data/
│   ├── raw/
│   ├── interim/
│   └── clean/
├── src/
│   ├── config.py
│   ├── clean_rules.py
│   ├── io_utils.py
│   └── run_cleaning.py
├── screenshots/
│   ├── demo1_before_raw.png
│   └── demo1_after_clean.png
└── README.md
```

---

## ▶ How to Run

```bash
python -m src.run_cleaning
```

All raw files are processed in batch, and cleaned files are written to `data/clean/`.

---

## 💼 Why This Demo Is Useful for Clients

This demo shows that I can:

* Handle **real messy financial data**
* Clean **multiple files consistently**
* Explain **every transformation** clearly
* Build pipelines that **scale beyond one-off scripts**

This same approach applies to:

* Bank statements
* Expense reports
* Transaction logs
* Accounting exports
