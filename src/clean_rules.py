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
    Remove empty rows, repeated headers, and summary rows.
    """
    return df


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
