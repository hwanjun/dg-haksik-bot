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
1 : '준비중입니다',
2 : '오돈불고기\n쌀밥\n매운콩나물국\n양배추쌈*쌈장\n얼갈이겉절이\n배추김치',
3 : '청양풍닭살야채볶음\n쌀밥\n시금치국\n연근조림\n오이양파무침\n배추김치',
4 : '탕수육\n쌀밥\n짬뽕국\n잡채\n치커리무침\n배추김치',
5 : '해물떡편완자전\n쌀밥\n건강닭죽\n우엉채볶음\n참나물무침\n깍두기',
6 : '주말은 쉽니다',
7 : '주말은 쉽니다',
}

lunch_menu_B = {
1 : '준비중입니다',
2 : '중화비빔밥*계란후라이\n매운콩나물국\n메밀전병2ea*간장\n천사채샐러드\n배추김치\n사과주스',
3 : '뚝배기설렁탕\n쌀밥\n감자전*간장\n잡채볼조림\n오이양파무침\n석박지/요구르트',
4 : '매콤크림소스스파게티\n쌀밥\n크림스프\n모닝빵사라다샌드위치2ea\n망고양상추샐러드*키위d\배추김치/쥬시쿨',
5 : '소금구이덮밥\n무다시마국\n치킨너겟*머스타드s\n단호박옥수수범벅\n배추김치\n포도주스',
6 : '주말은 쉽니다',
7 : '주말은 쉽니다',
}

lunch_menu_C = {
1 : '준비중입니다',
2 : '돈육고추장불고기\n상추/쌈장\n두부구이/양념\n미역국\n배추김치\n쌀밥\n누룽지탕',
3 : '등심돈까스/소스\n감자튀김\n양상추샐러드\n야채스프\n배추김치\n쌀밥\n샐러드/누룽지탕',
4 : '돼지국밥/소면사리\n김말이튀김\n도토리묵무침\n양념꺳잎지\n배추김치\n쌀밥\n샐러드',
5 : '순두부찌개\n치킨너겟/머스타드\n김구이/양념\n콩나물무침\n배추김치\n쌀밥\n샐러드',
6 : '주말은 쉽니다',
7 : '주말은 쉽니다',
}

dinner_menu_A = {
1 : '준비중입니다',
2 : '불고기\n쌀밥\n근대국\n도토리묵야채무침\n열무겉절이\n배추김치',
3 : '프리미엄동그랑땡\n쌀밥\n호박채맑은국\n어묵볶음\n실곤약야채무침\n깍두기',
4 : '뚝배기순대국\n쌀밥\n두부조림\n단호박전*간장\n부추양파겉절이\n깍두기',
5 : '돈사태떡조림\n쌀밥\n열무된장국\n맛살야채볶음\n콩나물무침\n깍두기',
6 : '주말은 쉽니다',
7 : '주말은 쉽니다',
}

dinner_menu_B = {
1 : '준비중입니다',
2 : '강황커리덮밥\n근대국\n해시브라운*케찹\n배추김치',
3 : '불고기볶음밥\n감귤주스\n매콤김말이2ea\n배추김치',
4 : '김치소면\n쌀밥\n야채크로켓*케찹\n배추김치',
5 : '함박마요덮밥\n열무된장국\n타코야끼3ea\n배추김치',
6 : '주말은 쉽니다',
7 : '주말은 쉽니다',
}

dinner_menu_C = {
1 : '준비중입니다',
2 : '닭개장\n탕수육/소스\n오이무침\n감귤\n배추김치\n쌀밥',
3 : '중화볶음밥/짜장소스/계란후라이\n치킨강정\n참나물생채\n계란파국\n배추김치\n쌀밥',
4 : '닭볶음탕\n햄계란구이\n우엉조림\n돌나물/초장\n배추김치\n쌀밥',
5 : '김치볶음밥/계란후라이\n탕수만두\n치커리생채\n미소된장국\n배추김치\n쌀밥',
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


