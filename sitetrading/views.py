from django.http import HttpResponse
from django.shortcuts import render

def home(request):
   text = """<h1>welcome to my app !</h1>"""
   return HttpResponse(text)

def about(request):
   return render(request, "sitetrading/about.html", {})


def blog_single(request):
   return render(request, "sitetrading/blog-single.html", {})

def blog(request):
   return render(request, "sitetrading/blog.html", {})
  

def contact(request):
   return render(request, "sitetrading/contact.html", {})


def index(request):
   return render(request, "sitetrading/index.html", {})


def portfolio_details(request):
   return render(request, "sitetrading/portfolio_details.html", {})




def portfolio(request):
   return render(request, "sitetrading/portfolio.html", {})



def pricing(request):
   return render(request, "sitetrading/pricing.html", {})




def services(request):
   return render(request, "sitetrading/services.html", {})




def testimonials(request):
   return render(request, "sitetrading/testimonials.html", {})
