import os, psycopg2
from flask import Flask, render_template, request, url_for, redirect
from dotenv import load_dotenv
from flask_bootstrap import Bootstrap5
from flask_classful import FlaskView, route
from helpers import db_queries, get_context
app = Flask(__name__, template_folder='templates')
bootstrap = Bootstrap5(app) 


class home_view(FlaskView):
    route_base = '/'
    def get(self):
        return render_template('home.html')

class warehouses_view(FlaskView):
    route_base = '/varehus'
    def get(self):
        table_objects = db_queries('SELECT * from Warehouse', False)
        return render_template('warehouse_view.html', **get_context(table_objects, "Warehouses", False))    

# @app.route('/varehus')
# def get_warehouses():
#     return render_template('table_view.html', table_objects = db_queries('SELECT * from Warehouse', False), type = "Warehouses" )

class items_view(FlaskView):
    route_base = '/varer'
    query_dictonary = {
        "post_filter_items":"""
            SELECT  n.item_id, i.item_name, n.number_of_items,  i.price, W.warehouse_name,  c.category_name, s.supplier_name
                            FROM Inventory n
                            INNER JOIN Warehouse W USING(warehouse_id)
                            INNER JOIN Item i USING(item_id)
                            INNER JOIN Supplier s USING(supplier_id)
                            LEFT JOIN Category c USING(category_id)
            """,
            
        "get_items":"""SELECT i.item_id, i.item_name, i.price, c.category_name, s.supplier_name
                                   FROM Item i
                                    INNER JOIN Supplier s USING(supplier_id)
                                    LEFT JOIN Category c USING(category_id)
            """,
        "get_items_by_supplier":"""SELECT i.item_id, i.item_name, i.price, c.category_name
                                   FROM Item i
                                    INNER JOIN Supplier s USING(supplier_id)
                                    LEFT JOIN Category c USING(category_id)
        """,
        "get_warehouses_with_item":""" 
            SELECT w.warehouse_name, w.adress, w.city, n.number_of_items
            FROM Inventory n
                INNER JOIN Warehouse w USING(warehouse_id)
            WHERE n.item_id = %s
            """,
        "get_supplier_info":"""
            SELECT s.supplier_name, s.phone, s.email, c.contact_name, c.phone as contact_phone, c.email as contact_email
            FROM Supplier s
                INNER JOIN Contact_person c USING(contact_person_id)
            WHERE s.supplier_id = %s
        """
        
    }
    
    def post(self):
        get_items_query =  self.query_dictonary["post_filter_items"]
            
        form_inputs = [request.form['select-warehouse'], request.form['select-supplier']]
        match form_inputs:
            case [x,y] if x != "" and y != "":
                print("x:", x, "y",y)
                query = get_items_query + " WHERE n.warehouse_id = %s and i.supplier_id = %s"  
                query_params= [x,y]
                print("👍 both params ")
             
            case [x, ""] if x != "":
                query = get_items_query + " WHERE n.warehouse_id = %s" 
                query_params =  [x]
                print("👍param 1 ")
                
            case ["", y] if y != "":
                print("👍param 2 ")
                return redirect(f'/varer/supplier/{y}')
            case ["",""]| _: 
                print("❌")
                return self.get()              
    
        table_objects = db_queries(query, query_params)
        

        return render_template('table_view.html', **get_context(table_objects, "Items", False))
    
    def get(self):
        table_objects = db_queries(self.query_dictonary["get_items"], False)
        print(table_objects)
        return render_template('table_view.html', **get_context(table_objects, "Items", False))
    
    @route('/<id>')
    def get_item_info(self, id):
        table_objects = db_queries(self.query_dictonary["get_warehouses_with_item"], [id])
        item_info = db_queries(self.query_dictonary["get_items"] + "WHERE item_id = %s", [id])
        return render_template('table_view.html', **get_context(table_objects, "Items", item_info))
   
    @route('/supplier/<supplier_id>')
    def get_item_by_supplier(self, supplier_id):
        table_objects = db_queries(self.query_dictonary["get_items_by_supplier"] + " WHERE i.supplier_id = %s", [supplier_id])
        supplier_info = db_queries(self.query_dictonary["get_supplier_info"], [supplier_id])
        return render_template('table_view.html', **get_context(table_objects, "Items", supplier_info))
        
        
items_view.register(app) 
warehouses_view.register(app)