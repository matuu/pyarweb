import json


def telegram_fix(request):
    data = json.loads(request.body.decode("latin1").replace('\n', '@'))
    data['message']['reply_to_message']['text'] = data[
        'message']['reply_to_message']['text'].replace('@', '\n')
    return data
