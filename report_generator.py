import matplotlib.pyplot as plt
import os

def generate_report(transactions, insights):
    """Generates a spending report as a visualization."""
    report_path = "reports/financial_report.png"
    transactions.groupby("Category")["Amount"].sum().plot(kind="bar")
    plt.title("Spending by Category")
    plt.ylabel("Amount ($)")
    plt.savefig(report_path)
    return report_path
