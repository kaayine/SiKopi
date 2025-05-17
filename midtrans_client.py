from midtransclient import Snap
import os
from dotenv import load_dotenv

load_dotenv()

SERVER_KEY = os.getenv("MIDTRANS_SERVER_KEY")

snap = Snap(
    is_production=False,
    server_key=SERVER_KEY
)

def create_transaction(order_id, gross_amount):
    transaction_details = {
        "transaction_details": {
            "order_id": str(order_id),
            "gross_amount": gross_amount
        }
    }
    response = snap.create_transaction(transaction_details)
    return response['token']
