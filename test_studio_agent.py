from studio_agent import input_node, processing_node, recommendation_node

def test_agent():
    sample_input = {
        "today": {"revenue": 1200, "cost": 800, "number_of_customers": 40},
        "yesterday": {"revenue": 1000, "cost": 700, "number_of_customers": 35}
    }
    data = input_node(sample_input)
    metrics = processing_node(data)
    output = recommendation_node(metrics)
    assert output['profit'] == 400
    assert output['profit_status'] == "positive"
    assert "CAC increased by" in output['alerts'][0]
    print("Test passed!")

if __name__ == "__main__":
    test_agent()
