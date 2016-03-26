from django.http import JsonResponse
from django.views.generic import View
from .pyarbot import moderate


class BotMessage(View):

    def get(self, request):
        if request.method is "POST":
            moderate(request)
        return JsonResponse({"OK"})

