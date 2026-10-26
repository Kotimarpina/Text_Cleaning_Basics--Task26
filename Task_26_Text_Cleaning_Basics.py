"""Task 26 – Text Cleaning Basics | Veda Technology
Cleans customer text fields by trimming whitespace, collapsing repeated spaces,
standardizing capitalization, lowercasing emails, and normalizing segment labels.

Run in the folder containing customer_dirty_data.csv:
    python Task_26_Text_Cleaning_Basics.py
Or pass paths:
    python Task_26_Text_Cleaning_Basics.py input.csv output.csv

Requires: pandas (pip install pandas)
"""
import sys
from pathlib import Path
import pandas as pd

def normalize_spaces(value):
    if pd.isna(value):
        return value
    return " ".join(str(value).strip().split())

def clean_dataframe(df):
    df = df.copy()
    required = ["Customer Name", "Email", "City", "Customer Segment", "Country"]
    missing = [col for col in required if col not in df.columns]
    if missing:
        raise ValueError("Missing required columns: " + ", ".join(missing))
    df["Customer Name"] = df["Customer Name"].map(lambda v: normalize_spaces(v).title() if not pd.isna(v) else v)
    df["Email"] = df["Email"].map(lambda v: str(v).strip().lower() if not pd.isna(v) else v)
    df["City"] = df["City"].map(lambda v: normalize_spaces(v).title() if not pd.isna(v) else v)
    def segment(v):
        if pd.isna(v): return v
        value = normalize_spaces(v)
        return {"consumer":"Consumer","corporate":"Corporate","home office":"Home Office"}.get(value.casefold(), value.title())
    df["Customer Segment"] = df["Customer Segment"].map(segment)
    df["Country"] = df["Country"].map(lambda v: normalize_spaces(v).title() if not pd.isna(v) else v)
    return df

def main():
    input_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("customer_dirty_data.csv")
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("customer_cleaned_data.csv")
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    df = pd.read_csv(input_path)
    result = clean_dataframe(df)
    result.to_csv(output_path, index=False)
    print(f"Rows processed: {len(result)}")
    print(f"Cleaned data saved to: {output_path.resolve()}")

if __name__ == "__main__":
    main()
