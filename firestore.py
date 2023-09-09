from fastapi import FastAPI
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK with your service account key JSON file
cred = credentials.Certificate("your_firestore_credentials.json")  # Replace with your Firestore credentials JSON file
firebase_admin.initialize_app(cred)

app = FastAPI()

# FastAPI Endpoints
@app.post("/items/")
async def create_item(item: dict):
    db = firestore.client()  # Initialize Firestore client
    try:
        doc_ref = db.collection("locations").add(item)
        return {"message": "Item created successfully", "id": doc_ref.id}
    except Exception as e:
        return {"error": str(e)}

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    db = firestore.client()  # Initialize Firestore client
    try:
        doc_ref = db.collection("locations").document(item_id)
        item = doc_ref.get()
        if item.exists:
            item_data = {"id": item.id, **item.to_dict()}
            return item_data
        else:
            return {"error": "Item not found"}
    except Exception as e:
        return {"error": str(e)}

@app.get("/items/")
async def read_items():
    db = firestore.client()  # Initialize Firestore client
    try:
        items = db.collection("locations").stream()
        item_list = [{"id": item.id, **item.to_dict()} for item in items]
        return item_list
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
