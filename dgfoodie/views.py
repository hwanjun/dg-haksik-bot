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
2 : '미트볼케찹조림\n쌀밥\n미역국\n표고버섯간장떡볶음\n열무겉절이\n배추김치',
3 : '탕수육\n쌀밥\n콩나물국\n어묵완자고추장조림\n얼갈이겉절이\n배추김치',
4 : '해물떡편완자전\n쌀밥\n닭개장\n잡채\n오이양파무침\n깍두기',
5 : '불고기당면볶음\n쌀밥\n근대국\n도토리묵야채무침\n청경채겉절이\n배추김치',
6 : '주말은 쉽니다',
7 : '주말은 쉽니다',
}

lunch_menu_B = {
1 : '준비중입니다',
2 : '불고기생야채비빔밥\n미역국\n치킨너겟*허니머스타드s\n과일맛젤리\n배추김치\n콜라',
3 : '뚝배기장각닭다리죽\n쌀밥\n고추잡채볼강정\n야채스틱*쌈장\n얼갈이겉절이\n깍두기/요구르트',
4 : '스팸김치마요덮밥\n우동국물\n멘치카츠*사우전d\n푸질리케찹볶음\n무맛김치\n쥬시쿨',
5 : '사누끼우동\n제육고추장볶음밥\n군만두*양념장\n콘샐러드\n배추김치\n포도주스',
6 : '주말은 쉽니다',
7 : '주말은 쉽니다',
}

lunch_menu_C = {
1 : '준비중입니다',
2 : '닭개장\n새송이버섯튀김/초간장\n햄감자채볶음\n참나물무침\n배추김치\n쌀밥\n샐러드/누룽지',
3 : '오징어덮밥\n치킨너겟/머스타드\n부추겉절이\n콩나물국\n배추김치\n쌀밥\n샐러드',
4 : '돈까스\n야채샐러드/모닝빵\n단무지/피클/브로콜리\n양송이스프\n배추김치\n쌀밥\n샐러드/누룽지',
5 : '쭈삼불고기\n배추전\n치커리생채\n된장국\n배추김치\n쌀밥\n샐러드',
6 : '주말은 쉽니다',
7 : '주말은 쉽니다',
}

dinner_menu_A = {
1 : '뚝배기순대국\n쌀밥\n감자전*간장\n어묵양파볶음\n부추겉절이\n깍두기',
2 : '가자미카레튀김\n쌀밥\n야채탕\n애호박나물\n풋고추된장무침\n배추김치',
3 : '고기완자조림\n쌀밥\n무채국\n두부조림\n실곤약야채무침\n배추김치',
4 : '제육고추장불고기\n쌀밥\n아욱국\n우엉채볶음\n치커리무침\n배추김치',
5 : '고추장닭살야채볶음\n쌀밥\n콩나물국\n미역줄기양파볶음\n미나리무침\n배추김치',
6 : '주말은 쉽니다',
7 : '주말은 쉽니다',
}

dinner_menu_B = {
1 : '불고기볶음밥\n미소시루\n새우까스*타르소스\n배추김치',
2 : '호박멸치칼국수\n쌀밥\n포자만두찜*초간장\n배추김치',
3 : '카레라이스\n무채국\n오징어링튀김*타르소스\n배추김치',
4 : '자장면\n감귤주스\n매콤불만두\n배추김치',
5 : '참치김치볶음덮밥*계란후라이\n콩나물국\n해시브라운*케찹\n배추김치',
6 : '주말은 쉽니다',
7 : '주말은 쉽니다',
}

dinner_menu_C = {
1 : '순대깻잎볶음\n떡볶이\n시금치무침\n계란파국\n배추김치\n쌀밥',
2 : '등뼈해장국\n메추리알장조림\n콩나물무침\n두부샐러드\n배추김치\n쌀밥',
3 : '감자수제비\n분홍소세지/케찹\n진미채볶음\n오이무침\n배추김치\n쌀밥',
4 : '짜장밥\n군만두/간장\n건새우호박볶음\n짬뽕국\n배추김치\n쌀밥',
5 : '마파두부\n춘권튀김/칠리소스\n콩조림\n쇠고기무국\n배추김치\n쌀밥',
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


