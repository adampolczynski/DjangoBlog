from django.shortcuts import render_to_response, HttpResponse
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from BlogProj.tasks import send_confirmation_email
from .models import Product
import json
# Create your views here.

@method_decorator(csrf_exempt)
def index(request):
	if request.method == 'POST': # while we're submitting basket
		order = request.POST.get('order')
		price = request.POST.get('price')
		email = request.POST.get('email')
		if (email != ''): # if email is not empty
			text = "You've bought items:"+order+" , for "+price
			send_confirmation_email(text, email)
		return HttpResponse(
			json.dumps({"email": email}),
			content_type="application/json"
			)
	else:
		products=Product.objects.all()
		context = {
		"products": products,
		}
		template = "products.html"
		print('oto sobie printuje GET')
		return render_to_response(template,context,context_instance=RequestContext(request))