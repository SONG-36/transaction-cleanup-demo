# src/run_cleaning.py

from pathlib import Path
import pandas as pd

from src.clean_rules import (
    normalize_headers,
    expand_merged_cells,
    remove_noise_rows,
    parse_dates,
    parse_amount_and_currency,
    finalize_schema,
)

RAW_DIR = Path("data/raw")
CLEAN_DIR = Path("data/clean")


def clean_single_file(path: Path) -> pd.DataFrame:
    df = pd.read_excel(path)

    df = normalize_headers(df)
    df = expand_merged_cells(df)
    df = remove_noise_rows(df)
    df = parse_dates(df)
    df = parse_amount_and_currency(df)
    df = finalize_schema(df, source_file=path.name)

    return df


def main():
    CLEAN_DIR.mkdir(parents=True, exist_ok=True)

    raw_files = sorted(RAW_DIR.glob("*.xlsx"))

    if not raw_files:
        raise RuntimeError("No raw Excel files found in data/raw/")

    for raw_file in raw_files:
        print(f"Processing: {raw_file.name}")
        clean_df = clean_single_file(raw_file)

        output_path = CLEAN_DIR / raw_file.name.replace("_raw", "_clean")
        clean_df.to_excel(output_path, index=False)

        print(f"Saved: {output_path.name}")


if __name__ == "__main__":
    main()
