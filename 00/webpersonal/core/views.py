from django.shortcuts import render, HttpResponse


html_base = """
    <h1>Mi web Personal</h1><h2>Portada</h2>
    <ul>
       <li><a href="/">Portada</a></li>
       <li><a href="/about-me">Acerca De</a></li>
       <li><a href="/portfolio">Portafolio</a></li>
       <li><a href="/contact">Contacto</a></li>
    </ul>
"""

# Create your views here.
def home(request):
    return render(request, "core/home.html")

def about(request):
    return HttpResponse(html_base + "<h2>About</h2><p>Esto el Acerca De</p>")

def portfolio(request):
    return HttpResponse(html_base + "<h2>Portafolio</h2><p>Esto el Portafolio</p>")

def contact(request):
    return HttpResponse(html_base + "<h2>Contacto</h2><p>mi email</p>")

