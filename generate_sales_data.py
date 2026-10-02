import csv
import random
from datetime import datetime, date

# Target totals matching the Power BI Reference Dashboard:
# Total Customers: 116
# Total Orders: 171
# Total Quantity: ~23,000 (23K)
# Total Sales: ~$2.25M
# Total Profit: ~$1.01M

random.seed(42)

# Named entities from reference dashboard
TOP_CUSTOMERS = [
    ("Xylona Preis", 270000, "Consumer"),
    ("Mona Khan", 200000, "Consumer"),
    ("Kim Larson", 150000, "Corporate"),
    ("Yoga Bobby", 130000, "Consumer"),
    ("Arianne Irving", 100000, "Home Office")
]

# Generate 111 additional realistic customer names (116 total)
FIRST_NAMES = [
    "Alexander", "Sophia", "Lucas", "Emma", "Liam", "Olivia", "Noah", "Ava", "Oliver", "Isabella",
    "Elijah", "Mia", "James", "Amelia", "William", "Harper", "Benjamin", "Evelyn", "Lucas", "Abigail",
    "Henry", "Emily", "Theodore", "Elizabeth", "Jack", "Mila", "Levi", "Ella", "Sebastian", "Avery",
    "Daniel", "Sofia", "Matthew", "Camila", "Samuel", "Aria", "David", "Scarlett", "Joseph", "Victoria",
    "Carter", "Madison", "Owen", "Luna", "Wyatt", "Grace", "John", "Chloe", "Jack", "Penelope",
    "Luke", "Layla", "Julian", "Riley", "Jayden", "Zoey", "Dylan", "Nora", "Grayson", "Lily",
    "Isaac", "Eleanor", "Gabriel", "Hannah", "Anthony", "Lillian", "Jaxon", "Addison", "Lincoln", "Aubrey",
    "Joshua", "Ellie", "Christopher", "Stella", "Andrew", "Natalie", "Theodore", "Zoe", "Caleb", "Leah",
    "Ryan", "Hazel", "Asher", "Violet", "Nathan", "Aurora", "Thomas", "Savannah", "Leo", "Audrey",
    "Isaiah", "Brooklyn", "Charles", "Bella", "Josiah", "Claire", "Hudson", "Skylar", "Christian", "Lucy"
]

LAST_NAMES = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
    "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
    "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson",
    "Walker", "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores",
    "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter", "Roberts"
]

all_customers = [c[0] for c in TOP_CUSTOMERS]
customer_segments = {c[0]: c[2] for c in TOP_CUSTOMERS}

# Build unique 116 customers
while len(all_customers) < 116:
    name = f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"
    if name not in customer_segments:
        all_customers.append(name)
        # Segment distribution: ~67.8% Consumer, ~18.8% Corporate, ~13.5% Home Office
        r = random.random()
        if r < 0.678:
            customer_segments[name] = "Consumer"
        elif r < 0.678 + 0.188:
            customer_segments[name] = "Corporate"
        else:
            customer_segments[name] = "Home Office"

TOP_PRODUCTS = [
    ("Power Bank Shell 5V", "Electronics", "Power Accessories", 340000),
    ("HDMI Cable 2.0 4k ca...", "Electronics", "Cables", 320000),
    ("Bamboo Folding Portable Desk", "Furniture", "Desks & Stands", 270000),
    ("Transparent Face Mask Pro", "Personal Care", "Protection", 220000),
    ("Rovtop USB Gaming Headset", "Electronics", "Gaming & Audio", 140000),
]

OTHER_PRODUCTS = [
    ("Ergonomic Mesh Chair", "Furniture", "Chairs"),
    ("Wireless Bluetooth Keyboard", "Electronics", "Peripherals"),
    ("Ultra-HD 27in Monitor", "Electronics", "Monitors"),
    ("Smart LED Desk Lamp", "Furniture", "Lighting"),
    ("Noise Cancelling Earbuds", "Electronics", "Audio"),
    ("USB-C Multi-Port Hub", "Electronics", "Accessories"),
    ("Standing Desk Converter", "Furniture", "Desks & Stands"),
    ("Heavy Duty Filing Cabinet", "Office Supplies", "Storage"),
    ("Recycled Paper Ream A4", "Office Supplies", "Paper"),
    ("High-Precision Optical Mouse", "Electronics", "Peripherals"),
    ("Adjustable Monitor Arm", "Office Supplies", "Accessories"),
    ("Mechanical Keyboard RGB", "Electronics", "Peripherals"),
    ("Tempered Glass Whiteboard", "Office Supplies", "Presentation"),
    ("Thermal Label Printer", "Electronics", "Printers"),
    ("Anti-Fatigue Comfort Mat", "Furniture", "Accessories")
]

# Cities matching reference chart
TARGET_CITIES = [
    ("Copenhagen N", 450000, 180000),
    ("Kokkedal", 320000, 110000),
    ("Ejby", 250000, 100000),
    ("Frederiksberg", 210000, 80000),
    ("Glostrup", 180000, 50000),
    ("Aarhus", 160000, 65000),
    ("Odense", 140000, 60000),
    ("Aalborg", 130000, 55000),
    ("Roskilde", 120000, 50000),
    ("Helsingor", 100000, 42000),
    ("Horsens", 90000, 40000),
    ("Kolding", 80000, 38000)
]

# Monthly sales distribution for 2020:
# Jan: 0.11M, Feb: 0.07M, Mar: 0.05M, Apr: 0.17M, May: 0.23M, Jun: 0.12M, Jul: 0.26M
# Aug: 0.22M, Sep: 0.28M, Oct: 0.24M, Nov: 0.21M, Dec: 0.29M -> Total = 2.25M
MONTH_TARGETS = {
    1: 110000, 2: 70000, 3: 50000, 4: 170000, 5: 230000, 6: 120000,
    7: 260000, 8: 220000, 9: 280000, 10: 240000, 11: 210000, 12: 290000
}

# 171 Total Orders
TOTAL_ORDERS = 171
orders = [f"ORD-2020-{i:04d}" for i in range(1, TOTAL_ORDERS + 1)]

# Distribute orders across months
month_order_counts = {
    1: 9, 2: 6, 3: 5, 4: 14, 5: 18, 6: 10,
    7: 21, 8: 17, 9: 21, 10: 18, 11: 15, 12: 17
}

order_dates = {}
order_idx = 0
for m, count in month_order_counts.items():
    for _ in range(count):
        if order_idx < TOTAL_ORDERS:
            day = random.randint(1, 28)
            order_dates[orders[order_idx]] = date(2020, m, day)
            order_idx += 1

# Assign customers to orders (ensuring 116 unique customers appear)
order_customers = {}
assigned_customers = list(all_customers)
random.shuffle(assigned_customers)

for i in range(len(assigned_customers)):
    order_customers[orders[i]] = assigned_customers[i]

for i in range(len(assigned_customers), TOTAL_ORDERS):
    order_customers[orders[i]] = random.choice(all_customers)

# Build rows
rows = []
total_quantity_target = 23000
running_sales = 0
running_profit = 0
running_qty = 0

# Line items generator
item_id = 1
for ord_id in orders:
    ord_date = order_dates[ord_id]
    m = ord_date.month
    cust = order_customers[ord_id]
    segment = customer_segments[cust]
    
    # Pick city based on probability
    city_entry = random.choices(
        TARGET_CITIES,
        weights=[30, 22, 18, 15, 13, 10, 8, 8, 7, 6, 5, 4]
    )[0]
    city = city_entry[0]

    # Decide how many line items in this order (1 to 4)
    num_items = random.choices([1, 2, 3, 4], weights=[40, 35, 15, 10])[0]

    # Target monthly slice
    target_month_sales = MONTH_TARGETS[m]
    orders_in_month = month_order_counts[m]
    avg_order_sales = target_month_sales / orders_in_month

    for it in range(num_items):
        # Product selection
        if random.random() < 0.45:
            prod_info = random.choice(TOP_PRODUCTS)
            prod_name, cat, subcat, _ = prod_info
        else:
            prod_info = random.choice(OTHER_PRODUCTS)
            prod_name, cat, subcat = prod_info

        # Base price and quantity
        base_item_sales = avg_order_sales / num_items * random.uniform(0.7, 1.3)
        
        # Quantity calculation to approach ~23,000 total across all items
        qty = int(random.uniform(30, 110))
        if cat == "Personal Care" or "Cable" in prod_name or "Shell" in prod_name:
            qty = int(random.uniform(90, 220))

        unit_price = round(base_item_sales / max(1, qty), 2)
        sales = round(unit_price * qty, 2)
        
        # Profit margin: Segment based, around ~45% overall
        # Consumer ~44.8%, Home Office ~63.7% margin, Corporate ~32.2% margin
        if segment == "Consumer":
            margin = random.uniform(0.40, 0.48)
        elif segment == "Home Office":
            margin = random.uniform(0.55, 0.65)
        else:
            margin = random.uniform(0.28, 0.36)

        profit = round(sales * margin, 2)

        rows.append({
            "Order ID": ord_id,
            "Order Date": ord_date.strftime("%Y-%m-%d"),
            "Customer Name": cust,
            "Segment": segment,
            "City": city,
            "Country": "Denmark",
            "Category": cat,
            "Sub-Category": subcat,
            "Product Name": prod_name,
            "Quantity": qty,
            "Unit Price": unit_price,
            "Sales": sales,
            "Profit": profit
        })

# Fine-tune totals to match reference values closely
current_sales = sum(r["Sales"] for r in rows)
current_profit = sum(r["Profit"] for r in rows)
current_qty = sum(r["Quantity"] for r in rows)

sales_scale = 2250000.0 / current_sales
profit_scale = 1010000.0 / current_profit
qty_scale = 23000.0 / current_qty

for r in rows:
    r["Sales"] = round(r["Sales"] * sales_scale, 2)
    r["Profit"] = round(r["Profit"] * profit_scale, 2)
    r["Quantity"] = max(1, int(round(r["Quantity"] * qty_scale)))
    r["Unit Price"] = round(r["Sales"] / r["Quantity"], 2)

# Save to CSV
output_path = "Sales_Analysis_2020.csv"
fieldnames = [
    "Order ID", "Order Date", "Customer Name", "Segment", "City", 
    "Country", "Category", "Sub-Category", "Product Name", 
    "Quantity", "Unit Price", "Sales", "Profit"
]

with open(output_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

final_sales = sum(r["Sales"] for r in rows)
final_profit = sum(r["Profit"] for r in rows)
final_qty = sum(r["Quantity"] for r in rows)
final_custs = len(set(r["Customer Name"] for r in rows))
final_orders = len(set(r["Order ID"] for r in rows))

print(f"Generated {len(rows)} line items successfully!")
print(f"Total Sales:    ${final_sales:,.2f} (Target: ~2.25M)")
print(f"Total Profit:   ${final_profit:,.2f} (Target: ~1.01M)")
print(f"Total Quantity: {final_qty:,} (Target: ~23K)")
print(f"Total Orders:   {final_orders} (Target: 171)")
print(f"Total Custs:    {final_custs} (Target: 116)")
