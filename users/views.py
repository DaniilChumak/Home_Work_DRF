from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter

from users.models import Payment
from users.serializers import PaymentSerializer
from rest_framework.generics import ListAPIView


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    """Настроили фильтрацию"""
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['paid_lesson', 'paid_course', 'payment_method']
    ordering_fields = ['-date_of_payment']