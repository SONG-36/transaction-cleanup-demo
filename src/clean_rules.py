# src/clean_rules.py

import pandas as pd
from .config import (
    STANDARD_COLUMNS,
    DEFAULT_CURRENCY,
    SUMMARY_KEYWORDS,
    DATE_OUTPUT_FORMAT,
)

def normalize_headers(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize column names and drop completely empty columns.
    """
    return df


def expand_merged_cells(df: pd.DataFrame) -> pd.DataFrame:
    """
    Forward-fill merged cells (e.g. transaction dates).
    """
    return df


def remove_noise_rows(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove empty rows, repeated header rows, and summary rows
    such as Subtotal / Total / Opening Balance.
    """
    # 1. Drop completely empty rows
    df = df.dropna(how="all")

    # 2. Remove repeated header rows
    # A repeated header row usually contains the column names themselves
    header_values = [str(col).strip().lower() for col in df.columns]

    def is_repeated_header(row) -> bool:
        row_values = [str(v).strip().lower() for v in row.values]
        return row_values == header_values

    df = df[~df.apply(is_repeated_header, axis=1)]

    # 3. Remove summary rows (Subtotal / Total / Opening Balance)
    def contains_summary_keyword(row) -> bool:
        row_text = " ".join(
            str(v).lower() for v in row.values if pd.notna(v)
        )
        return any(keyword in row_text for keyword in SUMMARY_KEYWORDS)

    df = df[~df.apply(contains_summary_keyword, axis=1)]

    # Reset index after row removal
    return df.reset_index(drop=True)


def parse_dates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Parse mixed date formats and convert to standard YYYY-MM-DD.
    """
    return df


def parse_amount_and_currency(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert amount to float and extract currency.
    """
    return df


def finalize_schema(df: pd.DataFrame, source_file: str) -> pd.DataFrame:
    """
    Rename columns, add source_file, and enforce final schema.
    """
    return df
