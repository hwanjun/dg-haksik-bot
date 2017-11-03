from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json, datetime

def keyboard(request):

    return JsonResponse({
        'type' : 'buttons',
        'buttons' : ['학생식당', '교직원','본부동']
        })

def get_menu(cafeteria_name):
    if cafeteria_name == '학생식당':
        lunch = "오돈불고기\n쌀밥\n아욱국\n미역줄기볶음\n무생채\n배추김치"
        dinner = "두부튀김양념조림\n쌀밥\n야채탕\n명엽채무침\n브로커리*초고추장\n배추김치"
        return "------------\n"+ lunch + "\n" + dinner
    elif cafeteria_name == '교직원':
        lunch = "오돈불고기\n쌀밥\n아욱국\n미역줄기볶음\n무생채\n배추김치"
        dinner = "두부튀김양념조림\n쌀밥\n야채탕\n명엽채무침\n브로커리*초고추장\n배추김치"
        return "------------\n"+ lunch + "\n" + dinner
    elif cafeteria_name == '본부동':
        lunch = "오돈불고기\n쌀밥\n아욱국\n미역줄기볶음\n무생채\n배추김치"
        dinner = "두부튀김양념조림\n쌀밥\n야채탕\n명엽채무침\n브로커리*초고추장\n배추김치"
        return "------------\n"+ lunch + "\n" + dinner


@csrf_exempt
def message(request):
    message = ((request.body).decode('utf-8'))
    return_json_str = json.loads(message)
    cafeteria_name = return_json_str['content']
    today_date = datetime.date.today().strftime("%m월 %d일")

    return JsonResponse({
        'message': {
            'text': today_date + '의' + cafeteria_name + " 메뉴입니다.\n \n" +get_menu(cafeteria_name)
        },
        'keyboard': {
            'type': 'buttons',
            'buttons': ['학생식당', '교직원','본부동']
        }
    })
