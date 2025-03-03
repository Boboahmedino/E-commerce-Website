# 🛍️ E-Commerce Website  
_A robust, full-featured eCommerce platform built with **HTML**, **CSS**, **JavaScript**, and **Django**._

---

## 🚀 Overview  
This web-based platform delivers an intuitive online shopping experience. Users can effortlessly browse products, add items to their shopping cart, complete secure payments, and track orders. Administrators have full control over product listings—adding, editing, or removing items as needed.

Key highlights include:  
- **User Authentication** with robust security measures.  
- **PayPal Payment Gateway** for secure transactions.  
- **Responsive Design** ensuring a seamless experience across all devices.  

---

## ✨ Features  
✔️ **User Authentication:** Safe and secure login system that protects sensitive user data.  
✔️ **Product Management:** Admins can add, update, and delete products easily.  
✔️ **Shopping Cart:** Users can view items, manage quantities, and see total costs before checkout.  
✔️ **Order Management:** Track order details and status post-purchase.  
✔️ **PayPal Integration:** Smooth and secure payment processing for a hassle-free checkout.  
✔️ **Responsive Layout:** Optimized for desktops, tablets, and mobile devices.  

---

## 🛠️ Technologies Used  
| **Technology**   | **Description**                                             |
|------------------|-------------------------------------------------------------|
| **Frontend**     | HTML, CSS, JavaScript                                       |
| **Backend**      | Django, Python                                              |
| **Payment**      | PayPal Payment Gateway                                      |
| **Database**     | PostgreSQL (default), MySQL (configurable in `settings.py`) |

---

## 🔧 Installation  

### ✅ Prerequisites  
Before proceeding, ensure you have the following installed:  
- **Python 3.9+**  
- **Django 5.0+**  
- **pipenv** or **virtualenv** (recommended)  

---

### 📌 Setup Instructions  

1️⃣ **Clone the repository**  
```bash
git clone https://github.com/YourUsername/ecommerce-website.git
cd ecommerce-website
```

2️⃣ **Create a virtual environment & activate it**  
```bash
python -m venv venv
# Activate on Windows:
venv\Scripts\activate
# Activate on macOS/Linux:
source venv/bin/activate
```

3️⃣ **Install dependencies**  
```bash
pip install -r requirements.txt
```

4️⃣ **Run migrations & start the server**  
```bash
python manage.py migrate
python manage.py runserver
```

5️⃣ **Access the application**  
Open your browser and visit:  
🔗 **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**  

---

## 🎯 Usage  

1️⃣ **User Registration & Login**  
   - Sign up or log in to access personalized features.  

2️⃣ **Browse & Add Products to Cart**  
   - Explore various categories and add products to your cart.  

3️⃣ **Checkout & Payment**  
   - Proceed to checkout and pay securely via PayPal.  

4️⃣ **Order Tracking**  
   - Monitor your order status in the “My Orders” section of your account.  

---

## 📁 Project Structure  
```plaintext
ecommerce-website/
├── .vscode/
├── authentication/
│   ├── views.py
│   ├── urls.py
│   └── ...
├── home/
│   ├── views.py
│   ├── urls.py
│   └── ...
├── store/
│   ├── views.py
│   ├── urls.py
│   └── ...
├── templates/
│   └── ...
└── manage.py
```

---

## ⚙️ Configuration  

- **Database**: By default, configured to use **PostgreSQL**. Update your `settings.py` for your database credentials.  
- **Static & Media Files**: Store all static files (CSS, JS) and media (images) in their respective directories.  
- **PayPal Integration**: Configure your PayPal Client ID and Client Secret in `settings.py` or via environment variables.  

---

## 👤 Author  
**Olaneye Ahmed Oladapo**  
🔗 GitHub: [boboahmedino](https://github.com/boboahmedino)  
🔗 LinkedIn: [Olaneye Ahmed Oladapo](https://www.linkedin.com/in/olaneye/)  
