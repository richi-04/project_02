from django.shortcuts import render
from django.http import HttpResponse
from .models import blog
from django.core.paginator import Paginator

# Create your views here.
def post(request):
    allpost = blog.objects.all()
    paginator = Paginator(allpost, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog.html', {'page_obj':page_obj})
