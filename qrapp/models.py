# from io import BytesIO
#
# from django.core.files import File
# from django.db import models
# from PIL import Image
# import qrcode


# class QRModel(models.Model):
#     text = models.TextField(null=True, blank=True)
#     URL = models.URLField(max_length=255)
#     qr_code = models.ImageField(upload_to='qr_codes', blank=True)
#
#     def save(self, *args, **kwargs):
#         # Generate QR code
#         qrcode_img = qrcode.make(self.URL)  # Use the URL field to generate the QR code
#
#         # Create a white canvas and paste the QR code image on it
#         canvas = Image.new('RGB', (290, 290), 'white')
#         canvas.paste(qrcode_img, (0, 0))
#
#         # Prepare the image file name and save it to a BytesIO buffer
#         fname = f'qr_code-{self.id}.png'  # Use a unique identifier for the file name
#         buffer = BytesIO()
#         canvas.save(buffer, 'PNG')
#         buffer.seek(0)  # Rewind the buffer
#
#         # Save the QR code image to the model
#         self.qr_code.save(fname, File(buffer), save=False)
#
#         # Clean up
#         buffer.close()
#         canvas.close()
#
#         # Save the model instance
#         super().save(*args, **kwargs)
