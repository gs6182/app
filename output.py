import json

# ...

@app.route('/analyze_expenses', methods=['GET'])
def analyze_expenses_api():
    # ...

    # Create a dictionary with the results
    results = {
        "labels": list(category_totals.keys()),
        "datasets": [
            {
                "data": list(category_totals.values()),
                "backgroundColor": [
                    "#FF6384",
                    "#36A2EB",
                    "#FFCE56",
                    "#8BC34A",
                    "#9C27B0",
                    "#FF9800",
                    "#795548"
                ]
            }
        ]
    }

    # Return the results as JSON
    return json.dumps(results)
