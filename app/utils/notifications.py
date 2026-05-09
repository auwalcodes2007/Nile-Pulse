from flask_mail import Message
from flask import render_template, current_app
from ..extensions import mail
import logging
from threading import Thread

# Set up logging for failed emails (US 6.1 requirement)
logging.basicConfig(filename='email_errors.log', level=logging.ERROR)

def send_async_email(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            # US 6.1: Failed attempts are logged, but system keeps running
            logging.error(f"Failed to send email: {str(e)}")

def send_order_update_email(order, template, subject):
    """
    Universal notification helper.
    US 6.1 & 6.2: Handles receipts and status updates.
    """
    msg = Message(
        subject=f"Nile Pulse: {subject} (Order #{order.id})",
        recipients=[order.customer.email]
    )
    # We pass the order object so the template can loop through order.items
    msg.html = render_template(f"emails/{template}.html", order=order)

    app = current_app._get_current_object()
    Thread(target=send_async_email, args=(app, msg)).start()
