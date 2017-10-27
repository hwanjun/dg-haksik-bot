from django.http import JsonResponse

def keyboard(request):

    return JsonResponse({
        'type' : 'buttons',
        'buttons' : ['학생식당', '교직원식당']
    })