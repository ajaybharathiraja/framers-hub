from django.utils import timezone
from .models import Payment, Order

class PaymentService:
    @staticmethod
    def create_payment(order, amount):
        payment = Payment.objects.create(
            order=order,
            amount=amount,
            status='CREATED',
            provider='TEST_MODE'
        )
        return payment

    @staticmethod
    def verify_payment(payment_id, success=True):
        try:
            payment = Payment.objects.get(id=payment_id)
            if success:
                payment.status = 'SUCCESS'
                payment.verification_status = True
                payment.payment_timestamp = timezone.now()
                payment.save()
                
                # Update order status
                order = payment.order
                order.status = 'CONFIRMED'
                order.save()
                return True
            else:
                payment.status = 'FAILED'
                payment.save()
                return False
        except Payment.DoesNotExist:
            return False

    @staticmethod
    def refund_payment(payment_id):
        try:
            payment = Payment.objects.get(id=payment_id)
            if payment.status == 'SUCCESS':
                payment.status = 'REFUNDED'
                payment.save()
                return True
            return False
        except Payment.DoesNotExist:
            return False
