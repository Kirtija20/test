from fastapi import APIRouter

router = APIRouter()

@router.get("/items")
def read_items():
    return [{"item_id": "item_1"}, {"item_id": "item_2"}]

@router.get("/items/{item_id}")
def read_item(item_id: str):
    return {"item_id": item_id}

@router.post("/items")
def create_item(item: dict):
    return item

@router.put("/items/{item_id}")
def update_item(item_id: str, updated_item: dict):
    return {"item_id": item_id, **updated_item}

@router.delete("/items/{item_id}")
def delete_item(item_id: str):
    return {"message": f"Item {item_id} has been deleted"}
