from flask_mail import Message
from flask import render_template, current_app
from ..extensions import mail
import logging
from threading import Thread

# Set up logging for failed emails (US 6.1 requirement)
logging.basicConfig(filename='email_errors.log', level=logging.ERROR)

import time

def send_async_email(app, msg):
    with app.app_context():
        retries = 3
        while retries > 0:
            try:
                mail.send(msg)
                print("Email sent successfully!")
                break # Exit loop on success
            except Exception as e:
                retries -= 1
                logging.error(f"Email failed. Retries left: {retries}. Error: {e}")
                if retries > 0:
                    time.sleep(5) # Wait 5 seconds before trying again
                else:
                    print("CRITICAL: Email failed after 3 attempts.")

def send_order_update_email(order, template, subject):
    app = current_app._get_current_object()
    
    def send_thread(app, order, template, subject):
        with app.app_context():
            try:
                # Debug print to console
                print(f"DEBUG: Attempting to send {subject} to {order.customer.email}")
                
                msg = Message(
                    subject=f"Nile Pulse: {subject} (Order #{order.id})",
                    recipients=[order.customer.email],
                    sender="mohammedauwalhassan07@gmail.com" # Explicitly add sender
                )
                msg.html = render_template(f"emails/{template}.html", order=order)
                mail.send(msg)
                print(f"DEBUG: {subject} Email Sent Successfully!")
            except Exception as e:
                logging.error(f"Failed to send email: {str(e)}")
                print(f"DEBUG EMAIL ERROR: {e}")

    Thread(target=send_thread, args=(app, order, template, subject)).start()
    