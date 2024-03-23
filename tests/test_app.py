import pytest
from flask.testing import FlaskClient
from app import app  # Adjust this import based on the actual structure of your Flask app

@pytest.fixture
def client() -> FlaskClient:
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_prediction(client: FlaskClient):
    """
    Test the /predict endpoint to ensure it returns the correct prediction format
    when valid data is posted.
    """
    # Sample input data structured according to your curl example
    data = {
        "features": [6, 148, 72, 35, 0, 33.6, 0.627, 50]
    }
    
    # Make a POST request to the /predict endpoint with the sample data
    response = client.post('/predict', json=data)
    
    # Check that the response is successful
    assert response.status_code == 200
    
    # Load the response data
    response_data = response.get_json()
    
    # Check the structure of the response to match expected format
    assert "prediction" in response_data
    assert isinstance(response_data["prediction"], list)  # Since the response wraps prediction in a list
    
    # Optionally, check the prediction value(s) if expecting specific results
    # This part is more relevant if you know what the output should be for a given input
    # Example:
    # assert response_data["prediction"] == [1]  # Or whatever your expected prediction is

