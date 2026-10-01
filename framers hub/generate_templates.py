import os

TEMPLATES = {
    'farmer_products.html': '''{% extends 'backend/base.html' %}
{% block title %}My Products - UzhavarHub{% endblock %}
{% block content %}
<div style="background: var(--surface); padding: 2rem; border-radius: 12px; border: 1px solid var(--border);">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem;">
        <h2 style="color: white;">My Products</h2>
        <a href="{% url 'farmer_add_product' %}" class="btn" style="width: auto;">Add New Product</a>
    </div>
    {% if products %}
    <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 1.5rem;">
        {% for product in products %}
        <div style="background: var(--bg-color); border: 1px solid var(--border); border-radius: 8px; padding: 1.5rem;">
            <h3 style="color: white; margin-bottom: 0.5rem;">{{ product.commodity }}</h3>
            <p style="color: var(--text-muted); margin-bottom: 1rem;">Location: {{ product.location }}</p>
            <p style="color: var(--text-muted);">Status: {% if hasattr product 'listing' and product.listing.is_active %}Active{% else %}Inactive{% endif %}</p>
        </div>
        {% endfor %}
    </div>
    {% else %}
    <p style="color: var(--text-muted);">You have no products listed.</p>
    {% endif %}
</div>
{% endblock %}''',

    'farmer_add_product.html': '''{% extends 'backend/base.html' %}
{% block title %}Add Product - UzhavarHub{% endblock %}
{% block content %}
<div class="auth-wrapper">
    <div class="auth-card" style="max-width: 600px;">
        <div class="auth-header">
            <h2>Add New Product</h2>
            <p>List a new crop on the marketplace</p>
        </div>
        <form method="POST">
            {% csrf_token %}
            <h4 style="color: white; margin: 1.5rem 0 1rem;">Product Details</h4>
            {{ product_form.as_p }}
            <h4 style="color: white; margin: 1.5rem 0 1rem;">Listing Pricing</h4>
            {{ listing_form.as_p }}
            <h4 style="color: white; margin: 1.5rem 0 1rem;">Inventory</h4>
            {{ inventory_form.as_p }}
            <button type="submit" class="btn" style="margin-top: 2rem;">Add Product</button>
        </form>
    </div>
</div>
<script>
    document.querySelectorAll('input, select, textarea').forEach(el => {
        if(el.type !== 'checkbox' && el.type !== 'radio') {
            el.classList.add('form-control');
        }
    });
</script>
{% endblock %}''',

    'product_details.html': '''{% extends 'backend/base.html' %}
{% block title %}{{ listing.product.commodity }} - UzhavarHub{% endblock %}
{% block content %}
<div style="background: var(--surface); padding: 2rem; border-radius: 12px; border: 1px solid var(--border);">
    <h2 style="color: white; margin-bottom: 1rem;">{{ listing.product.commodity }}</h2>
    <p style="color: var(--primary); font-size: 1.5rem; font-weight: bold; margin-bottom: 2rem;">₹{{ listing.selling_price_per_kg }} per kg</p>
    <div style="color: var(--text-muted); line-height: 1.6;">
        <p><strong>Farmer:</strong> {{ listing.product.farmer.user.username }}</p>
        <p><strong>Location:</strong> {{ listing.product.location }}</p>
        <p><strong>Available:</strong> {{ listing.product.inventory.available_quantity }} kg</p>
        <p style="margin-top: 1rem;">{{ listing.product.description }}</p>
    </div>
    <form action="{% url 'add_to_cart' listing.id %}" method="POST" style="margin-top: 2rem; display: flex; gap: 1rem;">
        {% csrf_token %}
        <input type="number" name="quantity" value="1" min="1" max="{{ listing.product.inventory.available_quantity }}" class="form-control" style="width: 100px;">
        <button type="submit" class="btn" style="width: auto;">Add to Cart</button>
    </form>
</div>
{% endblock %}''',

    'cart.html': '''{% extends 'backend/base.html' %}
{% block title %}Shopping Cart - UzhavarHub{% endblock %}
{% block content %}
<div style="background: var(--surface); padding: 2rem; border-radius: 12px; border: 1px solid var(--border);">
    <h2 style="color: white; margin-bottom: 2rem;">Your Cart</h2>
    {% if cart and cart.items.exists %}
    <table style="width: 100%; text-align: left; border-collapse: collapse; color: var(--text);">
        <tr style="border-bottom: 1px solid var(--border);">
            <th style="padding: 1rem;">Product</th>
            <th style="padding: 1rem;">Price</th>
            <th style="padding: 1rem;">Quantity</th>
            <th style="padding: 1rem;">Total</th>
        </tr>
        {% for item in cart.items.all %}
        <tr style="border-bottom: 1px solid var(--border);">
            <td style="padding: 1rem;">{{ item.listing.product.commodity }}</td>
            <td style="padding: 1rem;">₹{{ item.listing.selling_price_per_kg }}</td>
            <td style="padding: 1rem;">{{ item.quantity }} kg</td>
            <td style="padding: 1rem;">₹{{ item.subtotal }}</td>
        </tr>
        {% endfor %}
    </table>
    <div style="margin-top: 2rem; text-align: right;">
        <a href="{% url 'checkout' %}" class="btn" style="display: inline-block; width: auto; padding: 1rem 2rem;">Proceed to Checkout</a>
    </div>
    {% else %}
    <p style="color: var(--text-muted);">Your cart is empty.</p>
    {% endif %}
</div>
{% endblock %}''',

    'checkout.html': '''{% extends 'backend/base.html' %}
{% block title %}Checkout - UzhavarHub{% endblock %}
{% block content %}
<div class="auth-wrapper">
    <div class="auth-card" style="max-width: 600px;">
        <h2 style="color: white; margin-bottom: 2rem; text-align: center;">Checkout</h2>
        <form method="POST">
            {% csrf_token %}
            <p style="color: var(--text); margin-bottom: 1.5rem; text-align: center;">Simulating Payment Gateway...</p>
            <button type="submit" class="btn">Pay & Confirm Order</button>
        </form>
    </div>
</div>
{% endblock %}''',

    'order_history.html': '''{% extends 'backend/base.html' %}
{% block title %}Orders - UzhavarHub{% endblock %}
{% block content %}
<div style="background: var(--surface); padding: 2rem; border-radius: 12px; border: 1px solid var(--border);">
    <h2 style="color: white; margin-bottom: 2rem;">Orders</h2>
    {% if orders %}
    <div style="display: grid; gap: 1.5rem;">
        {% for order in orders %}
        <div style="background: var(--bg-color); border: 1px solid var(--border); border-radius: 8px; padding: 1.5rem;">
            <h3 style="color: white; margin-bottom: 1rem;">Order #{{ order.id }}</h3>
            <p style="color: var(--text-muted);">Date: {{ order.created_at|date }}</p>
            <p style="color: var(--text-muted); margin-bottom: 1rem;">Total: <strong style="color: var(--primary);">₹{{ order.total_amount }}</strong></p>
            <p style="color: white;">Items:</p>
            <ul style="color: var(--text-muted); margin-left: 1.5rem; margin-top: 0.5rem;">
                {% for item in order.items.all %}
                <li>{{ item.product.commodity }} - {{ item.quantity }}kg</li>
                {% endfor %}
            </ul>
        </div>
        {% endfor %}
    </div>
    {% else %}
    <p style="color: var(--text-muted);">No orders found.</p>
    {% endif %}
</div>
{% endblock %}'''
}

for name, content in TEMPLATES.items():
    path = os.path.join('backend/templates/backend', name)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print('Templates created!')
