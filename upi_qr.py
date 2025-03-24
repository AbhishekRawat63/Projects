import qrcode

# Input for UPI ID, Recipient Name, Amount, and Currency
upi_id = input("Enter your UPI ID: ")

# UPI URLs for PhonePe, Paytm, and Google Pay
phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

# Create QR codes
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

# Save QR codes as images
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')  # Fixed the filename here

# Show QR codes
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()

print("QR codes for PhonePe, Paytm, and Google Pay have been generated and saved.")
