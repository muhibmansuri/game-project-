
# Mock Data for our E-commerce Store
products = [
    {"id": 1, "name": "Wireless Headphones", "price": 2999, "image": "🎧", "desc": "Noise cancelling, 20h battery"},
    {"id": 2, "name": "Smart Watch", "price": 4500, "image": "⌚", "desc": "Health tracking, GPS included"},
    {"id": 3, "name": "Gaming Mouse", "price": 1200, "image": "🖱️", "desc": "RGB lights, high DPI"},
    {"id": 4, "name": "Mechanical Keyboard", "price": 3500, "image": "⌨️", "desc": "Blue switches, compact design"},
    {"id": 5, "name": "Laptop Stand", "price": 800, "image": "💻", "desc": "Aluminum alloy, adjustable"},
    {"id": 6, "name": "USB-C Hub", "price": 1500, "image": "🔌", "desc": "HDMI, 3x USB 3.0, SD Card"},
]

# In-memory cart for simplicity (Normally this would be in a DB or Session)
# Structure: { "session_id": { "item_id": quantity } }
# Since this is a simple demo, we will use a global cart for the user
cart = {}

def get_products():
    return products

def get_product(id):
    for p in products:
        if p['id'] == id:
            return p
    return None

def add_to_cart(id):
    if id in cart:
        cart[id] += 1
    else:
        cart[id] = 1
    return get_cart_details()

def remove_from_cart(id):
    if id in cart:
        del cart[id]
    return get_cart_details()

def update_quantity(id, change):
    if id in cart:
        cart[id] += change
        if cart[id] <= 0:
            del cart[id]
    return get_cart_details()

def get_cart_details():
    items = []
    total = 0
    count = 0
    
    for pid, qty in cart.items():
        product = get_product(pid)
        if product:
            total += product['price'] * qty
            count += qty
            items.append({
                "product": product,
                "quantity": qty,
                "subtotal": product['price'] * qty
            })
            
    return {
        "items": items,
        "total": total,
        "count": count
    }

def clear_cart():
    cart.clear()
    return True
