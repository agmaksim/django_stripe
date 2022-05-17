from django.urls import path
from pay.views import (CancelView, CreateCheckoutSessionView,
                       ProductLandingPageView, SuccessView)

urlpatterns = [
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path(
        'create-checkout-session/<pk>/',
        CreateCheckoutSessionView.as_view(),
        name='create-checkout-session'
        ),
    path('', ProductLandingPageView.as_view(), name='landing'),
]
