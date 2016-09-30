from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Postear
def post_list(request):
    posts = Postear.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/post_list.html', {'posts': posts})

def detalle_articulo(request, pk):
    post = get_object_or_404(Postear, pk=pk)
    return render(request, 'blog/detalle_articulo.html', {'post': post})
