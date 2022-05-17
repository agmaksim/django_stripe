import stripe
from django.conf import settings
from django.shortcuts import redirect
#from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView

from .models import Item, Price

stripe.api_key = settings.STRIPE_SECRET_KEY
YOUR_DOMAIN = "http://127.0.0.1:8000"


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        price = Price.objects.get(id=self.kwargs["pk"])
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': price.stripe_price_id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return redirect(checkout_session.url)


class SuccessView(TemplateView):
    template_name = "success.html"


class CancelView(TemplateView):
    template_name = "cancel.html"


class ProductLandingPageView(TemplateView):
    template_name = "landing.html"

    def get_context_data(self, **kwargs):
        item = Item.objects.get(name="Stone")
        prices = Price.objects.filter(product=item)
        context = super(ProductLandingPageView,
                        self).get_context_data(**kwargs)
        context.update({
            "item": item,
            "prices": prices
        })
        return context
