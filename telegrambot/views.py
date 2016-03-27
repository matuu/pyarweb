from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from .pyarbot import moderate


class BotMessage(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(BotMessage, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        moderate(request)
        return HttpResponse(status=200)

