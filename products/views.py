from django.shortcuts import render_to_response, HttpResponse
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from BlogProj.tasks import send_confirmation_email
from .models import Product
# Create your views here.

@method_decorator(csrf_exempt)
def index(request):
	products=Product.objects.all()
	context = {
	"products": products,
	}
	template = "products.html"
	return render_to_response(template,context,context_instance=RequestContext(request))

def submit(request):
	if request.method == 'POST':
		post = request.POST.get('post')
		email = request.POST.get('email')

		return HttpResponse(
			json.dumps({"something":email, "moreofit":"moreeeeeee"}),
			content_type="application/json"
			)
	else:
		return HttpResponse(
			json.dumps({"nothing to see": "this isn't happening"}),
			content_type="application/json"
			)