from HelloWolrd import app


def test_hello_world_should_return_200_status():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
