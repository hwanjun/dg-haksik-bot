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
1 : '다음 학기에 더욱 멋진 서비스로 찾아뵙겠습니다',
2 : '다음 학기에 더욱 멋진 서비스로 찾아뵙겠습니다',
3 : '다음 학기에 더욱 멋진 서비스로 찾아뵙겠습니다',
4 : '다음 학기에 더욱 멋진 서비스로 찾아뵙겠습니다',
5 : '다음 학기에 더욱 멋진 서비스로 찾아뵙겠습니다',
6 : '주말은 쉽니다',
7 : '주말은 쉽니다',
}

lunch_menu_B = {
1 : '다음 학기에 더욱 멋진 서비스로 찾아뵙겠습니다',
2 : '다음 학기에 더욱 멋진 서비스로 찾아뵙겠습니다',
3 : '다음 학기에 더욱 멋진 서비스로 찾아뵙겠습니다',
4 : '다음 학기에 더욱 멋진 서비스로 찾아뵙겠습니다',
5 : '다음 학기에 더욱 멋진 서비스로 찾아뵙겠습니다',
6 : '주말은 쉽니다',
7 : '주말은 쉽니다',
}

lunch_menu_C = {
1 : '다음 학기에 더욱 멋진 서비스로 찾아뵙겠습니다',
2 : '다음 학기에 더욱 멋진 서비스로 찾아뵙겠습니다',
3 : '다음 학기에 더욱 멋진 서비스로 찾아뵙겠습니다',
4 : '다음 학기에 더욱 멋진 서비스로 찾아뵙겠습니다',
5 : '다음 학기에 더욱 멋진 서비스로 찾아뵙겠습니다',
6 : '주말은 쉽니다',
7 : '주말은 쉽니다',
}

dinner_menu_A = {
1 : '(__)',
2 : '(__)',
3 : '(__)',
4 : '(__)',
5 : '(__)',
6 : '주말은 쉽니다',
7 : '주말은 쉽니다',
}

dinner_menu_B = {
1 : '(__)',
2 : '(__)',
3 : '(__)',
4 : '(__)',
5 : '(__)',
6 : '주말은 쉽니다',
7 : '주말은 쉽니다',
}

dinner_menu_C = {
1 : '(__)',
2 : '(__)',
3 : '(__)',
4 : '(__)',
5 : '(__)',
6 : '주말은 쉽니다',
7 : '주말은 쉽니다',
}

def get_menu(cafeteria_name): ##각 메뉴의 점심과 저녁 메세지 표현
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

@csrf_exempt  ##post방식 사용에 따른 CSRF Token 에러 제거
def message(request): ##keyboard에 대한 응답 message
    message = ((request.body).decode('utf-8'))
    return_json_str = json.loads(message)
    cafeteria_name = return_json_str['content']
    today_date = datetime.date.today().strftime("%m월 %d일")

    return JsonResponse({
        'message': {
            'text': today_date + '의 ' + cafeteria_name + " 메뉴입니다.\n" + get_menu(cafeteria_name)
        },
        'keyboard': {
            'type': 'buttons',
            'buttons': ['학생식당-가마(3500원)', '학생식당-인터쉐프(5000원)', '교직원(5000원)']
        }
    })


