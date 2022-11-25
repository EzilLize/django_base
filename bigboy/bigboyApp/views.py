from django.http import HttpResponse

# Create your views here.

def index(request, name, age, interests ):
    return HttpResponse(f"{name},<br> {age}, <br>{interests},"
                            "<p><a href=""about"">about</a></p>"
                                '<a href="contact">Contact</a>'
                                                                )

def about(request):
    return HttpResponse('<h2>Обо мне</h2>' '<p>Я приехал из Казани, В школе была средняя успеваемость, однако учиться любил.</p>' 
                        '<p><a href="">Home</a></p>'
                        '<a href="contact">contact</a>')

def contact(request):
    return HttpResponse('<h2>Контакты</h2>' "<p>Github: https://github.com/EzilLize</p>"
                        '<p><a href="">Home</a></p>'
                        '<a href="about">about</a>')
