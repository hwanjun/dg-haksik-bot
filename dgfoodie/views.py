from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json, datetime

def keyboard(request):

    return JsonResponse({
        'type' : 'buttons',
        'buttons' : ['학생식당-가마(3500원)', '학생식당-인터쉐프(5000원)','교직원(5000원)']
        })

def copy_menu(food_name):



def get_menu(cafeteria_name):
    if cafeteria_name == '학생식당-가마(3500원)':
        lunch = "프리미엄동그랑땡\n쌀밥\n콩나물국\n건새우무조림\n브로커리*초장\n배추김치"
        dinner = "가자미구이\n쌀밥\n호박고추장찌개\n잡채\n참나물무침\n배추김치"
        return "--------------\n"+ "<점심>\n" + lunch + "\n \n<저녁>\n" + dinner
    elif cafeteria_name == '학생식당-인터쉐프(5000원)':
        lunch = "중화비빔밥*계란후라이\n콩나물국\n메밀전병2ea*간장\n천사채샐러드\n배추김치\n사과주스"
        dinner = "매운어묵가락국수\n쌀밥\n야채크로켓2ea\n배추김치"
        return "--------------\n"+ "<점심>\n" + lunch + "\n \n<저녁>\n" + dinner
    elif cafeteria_name == '교직원(5000원)':
        lunch = "돈육고추장불고기\n상추/쌈장\n햄계란구이\n미역국\n배추김치\n쌀밥\n샐러드/누룽지탕"
        dinner = "닭볶음탕\n두부구이/양념\n돌나물/초장\n무우말랭이지\n배추김치\n쌀밥"
        return "--------------\n"+ "<점심>\n" + lunch + "\n \n<저녁>\n" + dinner


@csrf_exempt
def message(request):
    message = ((request.body).decode('utf-8'))
    return_json_str = json.loads(message)
    cafeteria_name = return_json_str['content']
    today_date = datetime.date.today().strftime("%m월 %d일")

    return JsonResponse({
        'message': {
            'text': today_date + '의 ' + cafeteria_name + " 메뉴입니다.\n" +get_menu(cafeteria_name)
        },
        'keyboard': {
            'type': 'buttons',
            'buttons': ['학생식당-가마(3500원)', '학생식당-인터쉐프(5000원)','교직원(5000원)']
        }
    })

