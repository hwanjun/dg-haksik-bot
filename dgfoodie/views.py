from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json, datetime

def keyboard(request): ##키보드 정의해주기

    return JsonResponse({
        'type' : 'buttons',
        'buttons' : ['학생식당-가마(3500원)', '학생식당-인터쉐프(5000원)','교직원(5000원)']
        })

##월요일:1 화요일:2 ... 일요일:7
today_num = datetime.date.today().isocalendar()[2]

##요일별 메뉴 모음 dict
lunch_menu_A = {
1 : '',
2 : '',
3 : '불고기당면볶음\n쌀밥\n시금치국\n연근조림\n열무겉절이\n배추김치',
4 : '',
5 : '',
}

lunch_menu_B = {
1 : '',
2 : '',
3 : '순살치킨까스*양념치킨s\n쌀밥\n크림스프\n감자튀김*케찹\n삼색야채샐러드*요거트d\n배추김치/쥬시쿨',
4 : '',
5 : '',
}

lunch_menu_C = {
1 : '',
2 : '',
3 : '돌솥비빔밥\n두부조림\n물미역초무침\n된장국\n배추김치\n쌀밥\n샐러드',
4 : '',
5 : '',
}

dinner_menu_A = {
1 : '',
2 : '',
3 : '제육고추장볶음\n쌀밥\n매운콩나물국\n도토리묵야채무침\n미나리무침\n배추김치',
4 : '',
5 : '',
}

dinner_menu_B = {
1 : '',
2 : '',
3 : '함박마요덮밥\n매운콩나물국\n타코야끼3ea\n배추김치',
4 : '',
5 : '',
}

dinner_menu_C = {
1 : '',
2 : '',
3 : '돼지찌개\n치킨너겟/머스타드\n치커리생채\n양념깻잎지\n배추김치\n쌀밥',
4 : '',
5 : '',
}

##
def get_menu(cafeteria_name):
    if cafeteria_name == '학생식당-가마(3500원)':
        lunch = lunch_menu_A[today_num]
        dinner = dinner_menu_A[today_num]
        return "--------------\n"+ "<점심>\n" + lunch + "\n \n<저녁>\n" + dinner
    elif cafeteria_name == '학생식당-인터쉐프(5000원)':
        lunch = lunch_menu_B[today_num]
        dinner = dinner_menu_B[today_num]
        return "--------------\n"+ "<점심>\n" + lunch + "\n \n<저녁>\n" + dinner
    elif cafeteria_name == '교직원(5000원)':
        lunch = lunch_menu_C[today_num]
        dinner = dinner_menu_C[today_num]
        return "--------------\n"+ "<점심>\n" + lunch + "\n \n<저녁>\n" + dinner


@csrf_exempt ##post방식 사용에 따른 CSRF Token 에러 제거
##keyboard에 대한 응답 message
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

