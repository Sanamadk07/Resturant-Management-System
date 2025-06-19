from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import requests

# Replace these with your own values
ESEWA_MERCHANT_CODE = "EPAYTEST"
ESEWA_VERIFY_URL = "https://rc-epay.esewa.com.np/api/epay/transaction/status/"

def pay_with_esewa(request):
    # This view renders the payment form
    context = {
        'amount': 100,
        'transaction_uuid': 'TXN12345678',
        'product_code': ESEWA_MERCHANT_CODE,
        'success_url': 'http://localhost:8000/esewa/success/',
        'failure_url': 'http://localhost:8000/esewa/failure/',
    }
    return render(request, 'payments/esewa_payment_form.html', context)

@csrf_exempt
def esewa_success(request):
    ref_id = request.GET.get('refId')
    pid = request.GET.get('oid')  # should match the transaction_uuid
    amt = request.GET.get('amt')

    payload = {
        'amt': amt,
        'rid': ref_id,
        'pid': pid,
        'scd': ESEWA_MERCHANT_CODE,
    }

    response = requests.post(ESEWA_VERIFY_URL, data=payload)

    if "<status>Success</status>" in response.text:
        return HttpResponse("✅ Payment verified successfully!")
    else:
        return HttpResponse("❌ Payment verification failed.")

def esewa_failure(request):
    return HttpResponse("❌ Payment failed or was cancelled.")
