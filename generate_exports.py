import os
import json
import sqlite3
import xml.etree.ElementTree as ET
from xml.dom import minidom
from datetime import datetime, date
from decimal import Decimal

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uzhavarhub_project.settings')
import django
django.setup()

from backend.models import (
    User, FarmerProfile, CustomerProfile, Product,
    Listing, Inventory, Order, OrderItem, Payment,
    ResearchEvent, TAMSurvey
)

def custom_serializer(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError(f"Type {type(obj)} not serializable")

def generate_all_exports():
    os.makedirs('exports', exist_ok=True)
    
    # -------------------------------------------------------------
    # 1. Collect Data in Python Dictionaries
    # -------------------------------------------------------------
    users = list(User.objects.all().values('id', 'username', 'email', 'role', 'is_active', 'date_joined'))
    farmers = list(FarmerProfile.objects.all().values('id', 'user_id', 'phone', 'state', 'district', 'location', 'farming_information'))
    customers = list(CustomerProfile.objects.all().values('id', 'user_id', 'phone', 'delivery_information'))
    products = list(Product.objects.all().values('id', 'farmer_id', 'commodity', 'variety', 'grade', 'description', 'location', 'harvest_date', 'created_at'))
    listings = list(Listing.objects.all().values('id', 'product_id', 'selling_price_per_kg', 'ai_predicted_price', 'reference_market_price', 'is_active', 'created_at'))
    inventories = list(Inventory.objects.all().values('id', 'product_id', 'total_quantity', 'reserved_quantity', 'available_quantity'))
    orders = list(Order.objects.all().values('id', 'customer_id', 'total_amount', 'status', 'created_at', 'updated_at'))
    order_items = list(OrderItem.objects.all().values('id', 'order_id', 'listing_id', 'quantity', 'price_at_sale'))
    payments = list(Payment.objects.all().values('id', 'order_id', 'transaction_id', 'amount', 'status', 'provider', 'payment_timestamp', 'verification_status'))
    research_events = list(ResearchEvent.objects.all().values('id', 'user_id', 'event_type', 'metadata', 'timestamp'))
    surveys = list(TAMSurvey.objects.all().values('id', 'user_id', 'perceived_usefulness', 'perceived_ease_of_use', 'comments', 'created_at'))
    
    export_dataset = {
        "metadata": {
            "project": "UzhavarHub - Agricultural Direct Marketplace & Research Platform",
            "export_timestamp": datetime.now().isoformat(),
            "summary_counts": {
                "users": len(users),
                "farmer_profiles": len(farmers),
                "customer_profiles": len(customers),
                "products": len(products),
                "listings": len(listings),
                "inventory_records": len(inventories),
                "orders": len(orders),
                "order_items": len(order_items),
                "payments": len(payments),
                "research_events": len(research_events),
                "tam_surveys": len(surveys)
            }
        },
        "users": users,
        "farmer_profiles": farmers,
        "customer_profiles": customers,
        "products": products,
        "listings": listings,
        "inventories": inventories,
        "orders": orders,
        "order_items": order_items,
        "payments": payments,
        "research_events": research_events,
        "tam_surveys": surveys
    }
    
    # -------------------------------------------------------------
    # 2. Generate JSON File
    # -------------------------------------------------------------
    json_path = os.path.join('exports', 'uzhavarhub_data.json')
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(export_dataset, f, indent=2, default=custom_serializer, ensure_ascii=False)
    print(f"[OK] Created JSON: {json_path} ({os.path.getsize(json_path):,} bytes)")

    # -------------------------------------------------------------
    # 3. Generate XML File
    # -------------------------------------------------------------
    root = ET.Element('UzhavarHubData')
    meta_elem = ET.SubElement(root, 'Metadata')
    ET.SubElement(meta_elem, 'Project').text = export_dataset['metadata']['project']
    ET.SubElement(meta_elem, 'ExportTimestamp').text = export_dataset['metadata']['export_timestamp']
    
    counts_elem = ET.SubElement(meta_elem, 'SummaryCounts')
    for k, v in export_dataset['metadata']['summary_counts'].items():
        ET.SubElement(counts_elem, k).text = str(v)
        
    tables_map = [
        ('Users', 'User', users),
        ('FarmerProfiles', 'FarmerProfile', farmers),
        ('CustomerProfiles', 'CustomerProfile', customers),
        ('Products', 'Product', products),
        ('Listings', 'Listing', listings),
        ('Inventories', 'Inventory', inventories),
        ('Orders', 'Order', orders),
        ('OrderItems', 'OrderItem', order_items),
        ('Payments', 'Payment', payments),
        ('ResearchEvents', 'ResearchEvent', research_events),
        ('TAMSurveys', 'TAMSurvey', surveys),
    ]
    
    for section_tag, item_tag, rows in tables_map:
        section_elem = ET.SubElement(root, section_tag)
        for row in rows:
            item_elem = ET.SubElement(section_elem, item_tag)
            for col_name, val in row.items():
                col_elem = ET.SubElement(item_elem, col_name)
                if val is None:
                    col_elem.text = ""
                elif isinstance(val, dict):
                    col_elem.text = json.dumps(val, default=custom_serializer)
                elif isinstance(val, (datetime, date)):
                    col_elem.text = val.isoformat()
                elif isinstance(val, Decimal):
                    col_elem.text = str(val)
                else:
                    col_elem.text = str(val)
                    
    xml_string = ET.tostring(root, encoding='utf-8')
    pretty_xml = minidom.parseString(xml_string).toprettyxml(indent="  ")
    xml_path = os.path.join('exports', 'uzhavarhub_data.xml')
    with open(xml_path, 'w', encoding='utf-8') as f:
        f.write(pretty_xml)
    print(f"[OK] Created XML:  {xml_path} ({os.path.getsize(xml_path):,} bytes)")

    # -------------------------------------------------------------
    # 4. Generate SQL File (Standard ANSI SQL DDL & INSERTS)
    # -------------------------------------------------------------
    sql_path = os.path.join('exports', 'uzhavarhub_data.sql')
    with open(sql_path, 'w', encoding='utf-8') as f:
        f.write("-- =====================================================================\n")
        f.write("-- UzhavarHub Complete Database Export\n")
        f.write(f"-- Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("-- Database: SQLite / PostgreSQL ANSI Compatible\n")
        f.write("-- =====================================================================\n\n")
        
        # Helper to escape sql strings
        def esc(v):
            if v is None:
                return "NULL"
            if isinstance(v, bool):
                return "1" if v else "0"
            if isinstance(v, (int, float, Decimal)):
                return str(v)
            if isinstance(v, (datetime, date)):
                return f"'{v.isoformat()}'"
            if isinstance(v, dict):
                clean_json = json.dumps(v, default=custom_serializer).replace("'", "''")
                return f"'{clean_json}'"
            clean_str = str(v).replace("'", "''")
            return f"'{clean_str}'"

        # Table definitions & data dumps
        table_configs = [
            ("backend_user", users, [
                ("id", "INTEGER PRIMARY KEY"),
                ("username", "VARCHAR(150) NOT NULL"),
                ("email", "VARCHAR(254) NOT NULL"),
                ("role", "VARCHAR(10) NOT NULL"),
                ("is_active", "BOOLEAN NOT NULL"),
                ("date_joined", "DATETIME NOT NULL")
            ]),
            ("backend_farmerprofile", farmers, [
                ("id", "INTEGER PRIMARY KEY"),
                ("user_id", "INTEGER REFERENCES backend_user(id)"),
                ("phone", "VARCHAR(15)"),
                ("state", "VARCHAR(100)"),
                ("district", "VARCHAR(100)"),
                ("location", "VARCHAR(255)"),
                ("farming_information", "TEXT")
            ]),
            ("backend_customerprofile", customers, [
                ("id", "INTEGER PRIMARY KEY"),
                ("user_id", "INTEGER REFERENCES backend_user(id)"),
                ("phone", "VARCHAR(15)"),
                ("delivery_information", "TEXT")
            ]),
            ("backend_product", products, [
                ("id", "INTEGER PRIMARY KEY"),
                ("farmer_id", "INTEGER REFERENCES backend_farmerprofile(id)"),
                ("commodity", "VARCHAR(100) NOT NULL"),
                ("variety", "VARCHAR(100)"),
                ("grade", "VARCHAR(50)"),
                ("description", "TEXT"),
                ("location", "VARCHAR(255) NOT NULL"),
                ("harvest_date", "DATE"),
                ("created_at", "DATETIME NOT NULL")
            ]),
            ("backend_listing", listings, [
                ("id", "INTEGER PRIMARY KEY"),
                ("product_id", "INTEGER UNIQUE REFERENCES backend_product(id)"),
                ("selling_price_per_kg", "DECIMAL(10,2) NOT NULL"),
                ("ai_predicted_price", "DECIMAL(10,2)"),
                ("reference_market_price", "DECIMAL(10,2)"),
                ("is_active", "BOOLEAN NOT NULL"),
                ("created_at", "DATETIME NOT NULL")
            ]),
            ("backend_inventory", inventories, [
                ("id", "INTEGER PRIMARY KEY"),
                ("product_id", "INTEGER UNIQUE REFERENCES backend_product(id)"),
                ("total_quantity", "DECIMAL(10,2) NOT NULL"),
                ("reserved_quantity", "DECIMAL(10,2) NOT NULL"),
                ("available_quantity", "DECIMAL(10,2) NOT NULL")
            ]),
            ("backend_order", orders, [
                ("id", "INTEGER PRIMARY KEY"),
                ("customer_id", "INTEGER REFERENCES backend_customerprofile(id)"),
                ("total_amount", "DECIMAL(12,2) NOT NULL"),
                ("status", "VARCHAR(20) NOT NULL"),
                ("created_at", "DATETIME NOT NULL"),
                ("updated_at", "DATETIME NOT NULL")
            ]),
            ("backend_orderitem", order_items, [
                ("id", "INTEGER PRIMARY KEY"),
                ("order_id", "INTEGER REFERENCES backend_order(id)"),
                ("listing_id", "INTEGER REFERENCES backend_listing(id)"),
                ("quantity", "DECIMAL(10,2) NOT NULL"),
                ("price_at_sale", "DECIMAL(10,2) NOT NULL")
            ]),
            ("backend_payment", payments, [
                ("id", "INTEGER PRIMARY KEY"),
                ("order_id", "INTEGER UNIQUE REFERENCES backend_order(id)"),
                ("transaction_id", "VARCHAR(100)"),
                ("amount", "DECIMAL(12,2) NOT NULL"),
                ("status", "VARCHAR(20) NOT NULL"),
                ("provider", "VARCHAR(50) NOT NULL"),
                ("payment_timestamp", "DATETIME"),
                ("verification_status", "BOOLEAN NOT NULL")
            ]),
            ("backend_researchevent", research_events, [
                ("id", "INTEGER PRIMARY KEY"),
                ("user_id", "INTEGER REFERENCES backend_user(id)"),
                ("event_type", "VARCHAR(50) NOT NULL"),
                ("metadata", "TEXT"),
                ("timestamp", "DATETIME NOT NULL")
            ]),
            ("backend_tamsurvey", surveys, [
                ("id", "INTEGER PRIMARY KEY"),
                ("user_id", "INTEGER REFERENCES backend_user(id)"),
                ("perceived_usefulness", "INTEGER NOT NULL"),
                ("perceived_ease_of_use", "INTEGER NOT NULL"),
                ("comments", "TEXT"),
                ("created_at", "DATETIME NOT NULL")
            ])
        ]

        for tbl_name, rows, columns in table_configs:
            f.write(f"-- -----------------------------------------------------------------\n")
            f.write(f"-- Table structure for `{tbl_name}`\n")
            f.write(f"-- -----------------------------------------------------------------\n")
            f.write(f"DROP TABLE IF EXISTS `{tbl_name}`;\n")
            f.write(f"CREATE TABLE `{tbl_name}` (\n")
            col_defs = [f"    `{c[0]}` {c[1]}" for c in columns]
            f.write(",\n".join(col_defs))
            f.write("\n);\n\n")
            
            if rows:
                f.write(f"-- Dumping data for `{tbl_name}` ({len(rows)} records)\n")
                col_names = [c[0] for c in columns]
                cols_str = ", ".join([f"`{c}`" for c in col_names])
                
                for r in rows:
                    val_strs = [esc(r.get(c)) for c in col_names]
                    f.write(f"INSERT INTO `{tbl_name}` ({cols_str}) VALUES ({', '.join(val_strs)});\n")
                f.write("\n")
                
    print(f"[OK] Created SQL:  {sql_path} ({os.path.getsize(sql_path):,} bytes)")

if __name__ == '__main__':
    generate_all_exports()
