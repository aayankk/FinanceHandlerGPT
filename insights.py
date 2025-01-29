# insights.py - Generates financial insights
def generate_insights(transactions):
    """Analyzes transactions and provides financial insights."""
    total_spent = transactions["Amount"].sum()
    top_category = transactions.groupby("Category")["Amount"].sum().idxmax()
    
    insights = {
        "Total Spent": f"${total_spent:.2f}",
        "Top Spending Category": top_category
    }
    return insights
