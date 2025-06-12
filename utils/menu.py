import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firestore only once
if not firebase_admin._apps:
    cred = credentials.Certificate("restaurant-data-backend-firebase-adminsdk-fbsvc-f5cbd975ec.json")
    # path to your service key
    firebase_admin.initialize_app(cred)

db = firestore.client()

def generate_menu_from_firestore():
    """
    Fetches menu data from Firestore 'menu' collection.
    Returns a list of dish dictionaries.
    """
    menu_ref = db.collection('menu')
    docs = menu_ref.stream()

    menu = []
    for doc in docs:
        data = doc.to_dict()
        menu.append({
            "name": doc.id,
            "category": data.get("category"),
            "cuisine": data.get("cuisine"),
            "cook_time": data.get("cook_time"),
            "description": data.get("description"),
            "ingredients": data.get("ingredients", []),
            "diet": data.get("diet", [])
        })

    return menu
