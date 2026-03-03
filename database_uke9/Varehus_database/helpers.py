import os, psycopg2
from dotenv import load_dotenv

load_dotenv()

column_names_norwegian = {  
    # Items:
    "item_id": "Id",
    "item_name": "Navn på vare",
    "price": "Pris",
    # Supplier and Contact_person:
    "supplier_name": "Leverandør",
    "phone": "Telefon",
    "contact_name": "Navn",
    # Inventory:
    "number_of_items": "Antall",
    # Warehouse:
    "warehouse_name": "Varehus",
    "adress": "Adresse",
    "city": "By",
    # Category:
    "category_name": "kategori",
    "description": "Beskrivelse"
}

def db_queries(query, query_params):
     
    conn = psycopg2.connect(port=os.getenv('DB_PORT'),
                            database=os.getenv('DB_NAME'),
                            user=os.getenv('DB_USER'),
                            password=os.getenv('DB_PASSWORD'),)
    cur = conn.cursor()
    if query_params != False:
        cur.execute(query, query_params)     
    else: 
        cur.execute(query)
        
    db_callback_col = [column_names_norwegian.get(col[0], col[0]) for col in cur.description]
    db_callback_rows = cur.fetchall() 
    cur.close()
    
    conn.close()
    return [db_callback_rows, db_callback_col]


def get_context(table_objects, type, item_info):
    default_context = {
        "table_objects": table_objects[0],
        "table_col": table_objects[1],
    }
    
    match type:
        case "Items" if item_info:    
            default_context.update({
                "item_info": item_info[0],
               
            })
                 
            return default_context
        case "Items": 
            default_context.update({
                    "type": "Items",
                    "warehouses": db_queries('SELECT warehouse_id, warehouse_name from Warehouse', False),
                    "suppliers": db_queries('SELECT supplier_id, supplier_name from Supplier', False)
                })
            return default_context
        case _:
            print("❌")