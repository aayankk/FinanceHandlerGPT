def main():
    print("Welcome to Finance Handler")
    
    # Ensure data directory exists
    if not os.path.exists("data"): os.makedirs("data")
    if not os.path.exists("reports"): os.makedirs("reports")
    
    # Load and process bank statement
    filename = input("Enter the bank statement filename (CSV/Excel/PDF in data/ folder): ")
    filepath = os.path.join("data", filename)
    transactions = parse_bank_statement(filepath)
    
    # Generate insights
    insights = generate_insights(transactions)
    print("\n--- Financial Insights ---\n", insights)
    
    # Generate report
    report_path = generate_report(transactions, insights)
    print(f"Report saved at: {report_path}")
    
if __name__ == "__main__":
    main()
