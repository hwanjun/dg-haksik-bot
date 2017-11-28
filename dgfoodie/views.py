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
1 : '제육김치볶음\n쌀밥\n시금치국\n어묵볶음\n참나물겉절이\n깍두기',
2 : '떡갈비조림\n쌀밥\n콩나물국\n미니새송이야채볶음\n치커리무침\n배추김치',
3 : '오징어볼깐풍\n쌀밥\n근대국\n매콤두부조림\n청경채겉절이\n배추김치',
4 : '청양풍닭살야채볶음\n쌀밥\n들깨무채국\n연근조림\n오이양파무침\n배추김치',
5 : '탕수육\n쌀밥\n짬뽕국\n가지양파볶음\n실곤약야채무침\n배추김치',
6 : '주말은 쉽니다',
7 : '주말은 쉽니다',
}

lunch_menu_B = {
1 : '순살등심돈까스*데미s\n쌀밥\n크림스프\n감자튀김*케찹\n삼색야채샐러드*키위d\n배추김치/오렌지주스',
2 : '숙채비빔밥*계란후라이\n재첩국\n왕새우튀김2ea*타르소스\n콘샐러드\n배추김치\n사과주스',
3 : '뚝배기뼈다귀해장국\n쌀밥\n생선까스*타르소스\n잡채말이어묵조림\n청경채겉절이\n깍두기/요구르트',
4 : '매콤불낙볶음덮밥\n들깨무채국\n헤시브라운*케찹\n떡샐러드\n배추김치\n쥬시쿨',
5 : '오므라이스*데미그라s\n우동국물\n미니함박\n망고양상추샐러드*애플d\n배추김치\n포도주스',
6 : '주말은 쉽니다',
7 : '주말은 쉽니다',
}

lunch_menu_C = {
1 : '',
2 : '',
3 : '식당사정으로 이번주는 문을 열지 않습니다',
4 : '식당사정으로 이번주는 문을 열지 않습니다',
5 : '식당사정으로 이번주는 문을 열지 않습니다',
6 : '주말은 쉽니다',
7 : '주말은 쉽니다',
}

dinner_menu_A = {
1 : '죄송합니다 ㅠㅠ 많이 이용해 주세요',
2 : '뚝배기포자만두국\n쌀밥\n단호박전*간장\n맛살야채볶음\n브로커리*초장\n배추김치',
3 : '매콤불고기\n쌀밥\n콩가루배추국\n울방개묵*참깨드레싱\n쑥갓양파무침\n깍두기',
4 : '고기완자조림\n쌀밥\n호박고추장찌개\n우엉채볶음\n열무겉절이\n배추김치',
5 : '순대야채볶음\n쌀밥\n어묵국\n브로커리깐풍\n오이지무침\n배추김치',
6 : '주말은 쉽니다',
7 : '주말은 쉽니다',
}

dinner_menu_B = {
1 : '죄송합니다 ㅠㅠ 많이 이용해 주세요',
2 : '김치소면\n우동국물\n매콤꼬지어묵\n배추김치',
3 : '제육고추장볶음밥\n콩가루배추국\n비빔만두\n배추김치',
4 : '참치마요덮밥\n감귤주스\n타코야끼\n배추김치',
5 : '꼬치어묵우동\n쌀밥\n오징어바*머스타드S\n배추김치',
6 : '주말은 쉽니다',
7 : '주말은 쉽니다',
}

dinner_menu_C = {
1 : '',
2 : '',
3 : '다음주 월요일부터 정상 운영이라고 합니다',
4 : '다음주 월요일부터 정상 운영이라고 합니다',
5 : '다음주 월요일부터 정상 운영이라고 합니다',
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


