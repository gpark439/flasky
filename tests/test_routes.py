from app.models.cars import Car

def test_get_cars_returns_status_200_and_empty_array(client):
    response = client.get('/cars')
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []


def test_get_one_car_with_populated_db_returns_car_json(client, six_cars):
    response = client.get("/cars/3")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 3,
        "driver": "Daniel Ricciardo",
        "team": "McLaren",
        "mass_kg": 734
    }

def test_post_one_car_creates_car_in_db(client):
    response = client.post('/cars', json = {
        "driver":"Lewis Hamilton", 
        "team":"Mercedes", 
        "mass_kg":746})
    response_body = response.get_json()
    assert response.status_code == 201
    assert "id" in response_body
    assert "msg" in response_body
    
    cars = Car.query.all()
    
    assert len(cars) == 1
    assert cars[0].driver == "Lewis Hamilton"
    assert cars[0].team == "Mercedes"
    assert cars[0].mass_kg == 746
    
def test_get_one_car_with_empty_db_returns_404(client):
    response = client.get("/cars/1")
    assert response.status_code == 404

def test_get_non_existing_car_with_populated_db_returns_404(client, three_cars):
    response = client.get("/cars/99")
    assert response.status_code == 404