from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_items():
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == [{"item_id": "item_1"}, {"item_id": "item_2"}]

def test_read_item():
    response = client.get("/items/item_1")
    assert response.status_code == 200
    assert response.json() == {"item_id": "item_1"}

def test_create_item():
    response = client.post("/items", json={"name": "new_item"})
    assert response.status_code == 200
    assert response.json() == {"name": "new_item"}

def test_update_item():
    response = client.put("/items/item_1", json={"name": "updated_item"})
    assert response.status_code == 200
    assert response.json() == {"item_id": "item_1", "name": "updated_item"}

def test_delete_item():
    response = client.delete("/items/item_1")
    assert response.status_code == 200
    assert response.json() == {"message": "Item item_1 has been deleted"}
