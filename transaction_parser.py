# transaction_parser.py - Parses bank statements
import pandas as pd

def parse_bank_statement(filepath):
    """Reads and processes a bank statement file (CSV or Excel)."""
    if filepath.endswith(".csv"):
        df = pd.read_csv(filepath)
    elif filepath.endswith(".xlsx"):
        df = pd.read_excel(filepath)
    else:
        raise ValueError("Unsupported file format. Please use CSV or Excel.")
    
    # Basic cleaning
    df.columns = df.columns.str.strip().str.lower()
    df = df.rename(columns={"date": "Date", "amount": "Amount", "category": "Category"})
    df["Date"] = pd.to_datetime(df["Date"])
    
    return df
