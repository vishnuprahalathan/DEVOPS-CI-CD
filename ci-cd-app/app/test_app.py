from app import app

def test_health_check():
    tester = app.test_client()
    response = tester.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"
