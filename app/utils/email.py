from flask_mail import Message
from ..extensions import mail
from threading import Thread
import logging

logging.basicConfig(filename="email_errors.log", level=logging.ERROR)

def send_async_email(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            # This prevents the thread from crashing the main process
            logging.error(f"MAIL SYSTEM CRITICAL ERROR: {e}")
            print(f"ASYNC MAIL ERROR: {e}")

def send_verification_alert(user_email, order_id, mismatches, total_items):
    from flask import current_app

    """Sends email if items exceed limit or mismatch."""
    app = current_app._get_current_object()
    msg = Message(f"Action Required: Laundry Order #{order_id}",
                  recipients=[user_email],
                  sender="mohammedauwalhassan07@gmail.com")
    
    msg.body = f"Hello, your order #{order_id} has been processed. \n\n"
    if len(mismatches) > 0:
        msg.body += "Issues found during verification:\n" + "\n".join(mismatches)

    if total_items > 30:
        msg.body += "\n\nPlease visit the laundry office as your order exceeds the 30-item limit."
    else:
        msg.body += "\n\nYour order has been verified and updated successfully. Thank you for using our services!"
    
    Thread(target=send_async_email, args=(app, msg)).start()
