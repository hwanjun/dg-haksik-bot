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
1 : '개발자 사정으로 메뉴는 내일부터 업로드 됩니다',
2 : '불고기당면볶음\n쌀밥\n매운무채국\n미역줄기양파볶음\n콩나물무침\n배추김치',
3 : '탕수육\n쌀밥\n일식짬뽕국\n연근조림\n실곤약야채무침\n배추김치',
4 : '순대야채볶음\n쌀밥\n재첩국\n어묵볶음\n치커리무침\n배추김치',
5 : '제육고추장볶음\n쌀밥\n유채된장국\n도토리묵야채무침\n오이양파무침\n배추김치',
6 : '주말은 쉽니다',
7 : '주말은 쉽니다',
}

lunch_menu_B = {
1 : '개발자 사정으로 메뉴는 내일부터 업로드 됩니다',
2 : '뚝배기장각닭다리죽\n쌀밥\n잡채볼조림\n야채스틱*쌈장\n양파초절이\n깍두기/요구르트',
3 : '불고기생야채비빔밥\n미역국\n치킨너겟*허니머스타드s\n과일맛젤리\n배추김치\n콜라',
4 : '스팸김치마요덮밥\n우동국물\n멘치카츠*사우전d\n푸질리샐러드\n배추김치\n쥬시쿨',
5 : '사누끼우동\n매콤불닭볶음밥\n군만두*양념장\n콘샐러드\n배추김치\n포도주스',
6 : '주말은 쉽니다',
7 : '주말은 쉽니다',
}

lunch_menu_C = {
1 : '개발자 사정으로 메뉴는 내일부터 업로드 됩니다',
2 : '돈육고추장불고기\n상추/쌈장\n햄계란구이\n미역국\n배추김치\n쌀밥\n샐러드',
3 : '닭볶음탕\n두부구이/양념\n미나리무우생채\n콩조림\n배추김치\n쌀밥\n샐러드/누룽지탕',
4 : '설렁탕/소면사리\n순대떡볶음\n물미역/초장\n음료수\n배추김치\n쌀밥\n샐러드',
5 : '날치알밥찜\n생선까스/소스\n치커리생채\n우동국지\n배추김치\n쌀밥\n샐러드',
6 : '주말은 쉽니다',
7 : '주말은 쉽니다',
}

dinner_menu_A = {
1 : '죄송합니다 ㅠㅠ 많이 이용해 주세요',
2 : '뚝배기포자만두국\n쌀밥\n단호박전*간장\n맛살야채볶음\n브로커리*초장\n배추김치',
3 : '고추장닭살야채볶음\n쌀밥\n시금치국\n우엉채볶음\n얼갈이겉절이\n배추김치',
4 : '섭산적*불갈비맛소스\n쌀밥\n콩나물국\n알감자조림\n청경채겉절이\n배추김치',
5 : '삼치레몬구이\n쌀밥\n미역국\n소시지고추장케찹볶음\n쑥갓양파무침\n배추김치',
6 : '주말은 쉽니다',
7 : '주말은 쉽니다',
}

dinner_menu_B = {
1 : '죄송합니다 ㅠㅠ 많이 이용해 주세요',
2 : '김치소면\n우동국물\n매콤꼬지어묵\n배추김치',
3 : '삼색소보로덮밥\n시금치국\n집게맛살튀김*케찹\n깍두기',
4 : '불고기볶음밥\n콩나물국\n야채크로켓*케찹\n배추김치',
5 : '호박멸치칼국수\n쌀밥\n사모사\n배추김치',
6 : '주말은 쉽니다',
7 : '주말은 쉽니다',
}

dinner_menu_C = {
1 : '죄송합니다 ㅠㅠ 많이 이용해 주세요',
2 : '소고기국밥\n만두강정\n명엽채조림\n참나물생채\n배추김치\n쌀밥',
3 : '등심돈까스/소스\n감자튀김\n야채샐러드\n크림스프\n배추김치\n쌀밥',
4 : '닭개장\n탕수육/소스\n우엉조림\n오이무침\n배추김치\n쌀밥',
5 : '짜장밥\n군만두/간장\n단배추생채\n계란파국\n배추김치\n쌀밥',
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


