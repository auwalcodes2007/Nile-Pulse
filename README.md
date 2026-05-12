# Nile Pulse: Smart Campus Laundry System 🧺

Nile Pulse is a full-stack digital solution designed to streamline laundry operations at Nile University. It replaces manual paper trails with a real-time, automated workflow for students and staff.

**🔗 [Live Demo on Render](https://nile-pulse.onrender.com)**

---

## 🚀 Key Features
*   **Student Dashboard:** Create laundry orders, track real-time status, and view transaction history.
*   **Staff Management:** A dedicated interface for verifying items, updating order status, and managing pickups.
*   **Automated Notifications:** Asynchronous email system (using Python threading) to send receipts and status alerts.
*   **Secure Payments:** Integrated with the **Paystack API** for real-world Naira transactions.
*   **Authentication:** Secure login and registration with hashed passwords.

## 🛠️ Tech Stack
- **Backend:** Python (Flask)
- **Frontend:** HTML5, CSS3, JavaScript (Tailwind CSS)
- **Database:** PostgreSQL (Hosted on Render)
- **Real-Time Logic:** Python Threading for non-blocking email services
- **Payment Gateway:** Paystack API

## 📂 Project Structure
- `app.py`: Main entry point and route configurations.
- `models.py`: Database schemas for Users, Orders, and Items.
- `extensions.py`: Initialization for Mail, DB, and Migrations.
- `templates/`: Jinja2 templates for the UI.
- `static/`: CSS and JavaScript assets.

## ⚙️ Local Setup
1. Clone the repository:
   ```bash
   git clone [https://github.com/auwalcodes2007/Nile-Pulse.git](https://github.com/auwalcodes2007/Nile-Pulse.git)
   
2. Install dependencies: pip install -r requirements.txt
3. Set up your environment variables (`.env`):
   - `DATABASE_URL`
   - `MAIL_USERNAME` / `MAIL_PASSWORD`
   - `PAYSTACK_SECRET_KEY`
4. Run the application:
   flask run
