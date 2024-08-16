# from django.test import TestCase
#
# # Create your tests here.

import qrcode
from Qrcode_Create.settings import BASE_DIR
import datetime


def combine_photo(text=''):
    time_now = datetime.datetime.now()
    timestamp = datetime.datetime.timestamp(time_now)
    save_path = f"{BASE_DIR}/media/qr_code"
    # Create QR Code
    qr_code = qrcode.make(text)

    qr_code.thumbnail((400, 400))

    qr_code.save(f"{save_path}/vaucher_{timestamp}.jpg")
    return f"media/qr_code/vaucher_{timestamp}.jpg"
