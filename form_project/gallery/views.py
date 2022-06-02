from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView


def load_image(file):
    with open(f'gallery_tmp/{file.name}', 'wb+') as new_file:
        for chunk in file.chunks():
            new_file.write(chunk)



class GalleryView(View):
    def get(self, request):
        return render(request, 'gallery/load_image.html')

    def post(self, request):
        if request.FILES.__len__() >= 1:
            load_image(request.FILES['image'])
            return render(request, 'gallery/done.html')
        return render(request, 'gallery/load_image.html')

class DoneView(TemplateView):
    template_name = 'gallery/done.html'
