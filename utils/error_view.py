from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render


def handler404(request,exception):
   message  = ('Path not found')
   response  = JsonResponse(data={'error':message})
   response.status_code = 404
   return response
# def handler404(request,exception):
#    return render(request,"product/404-m.html")

def handler500(request):
   message  = ('Interal server error')
   response  = JsonResponse(data={'error':message})
   response.status_code = 500
   return response