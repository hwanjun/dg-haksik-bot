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
2 : '치킨볼강정\n쌀밥\n콩나물국\n잡채\n양배추오이무침\n배추김치',
3 : '순대야채볶음\n쌀밥\n재첩국\n미니사각어묵볶음\n얼갈이겉절이\n배추김치',
4 : '포크볼케찹조림\n쌀밥\n순두부찌개\n우엉채볶음\n콩나물무침\n배추김치',
5 : '불고기당면볶음\n쌀밥\n근대국\n미역줄기양파볶음\n참나물무침\n배추김치',
6 : '주말은 쉽니다',
7 : '주말은 쉽니다',
}

lunch_menu_B = {
1 : '준비중입니다',
2 : '전주비빔밥*계란후라이\n콩나물국\n턱편고기완자*불갈비맛소스\n천사채샐러드\n배추김치\n사과주스',
3 : '뚝배기설렁탕\n쌀밥\n미니생선까스*타르소스\n미니사각어묵볶음\n얼갈이겉절이\n깍두기/요구르트',
4 : '매콤불닭에그덮밥\n얼갈이국\n소시지구이*허니머스타드s\n콘샐러드\n배추김치\n쥬시쿨',
5 : '토마토소스스파게티\n파일애플볶음밥\n우동국물\n카레코로케1EA*케찹\n양상추샐러드*키위D\n배추김치/포도주스',
6 : '주말은 쉽니다',
7 : '주말은 쉽니다',
}

lunch_menu_C = {
1 : '준비중입니다',
2 : '돈육김치볶음\n비엔나야채볶음\n두부샐러드\n물만두국\n배추김치\n쌀밥\n누룽지탕',
3 : '설렁탕/소면사리\n순대떡볶음\n샹배추부추무침\n음료수\n배추김치\n쌀밥\n샐러드/누룽지탕',
4 : '김치볶음밥/계란후라이\n야채고로케\n물미역초무침\n콩나물국\n배추김치\n쌀밥\n샐러드/누룽지탕',
5 : '등뼈해장국\n한식잡채\n치커리생채\n오징어젓갈무침\n배추김치\n쌀밥\n샐러드/누룽지탕',
6 : '주말은 쉽니다',
7 : '주말은 쉽니다',
}

dinner_menu_A = {
1 : '준비중입니다',
2 : '오징어볶음\n쌀밥\n호박채맑은국\n잡채\n쑥갓양파무침\n배추김치',
3 : '닭살당면볶음\n쌀밥\n시금치국\n올방개묵*참깨드레싱\n청경채겉절이\n배추김치',
4 : '제육불고기\n쌀밥\n무채국\n맛살야채볶음n미역초무침\n배추김치',
5 : '비엔나케찹조림\n쌀밥\n수제비국\n부들어묵볶음\n오이양파무침\n배추김치',
6 : '주말은 쉽니다',
7 : '주말은 쉽니다',
}

dinner_menu_B = {
1 : '준비중입니다',
2 : '자장덮밥\n캐플주스\n비빔춘권\n배추김치',
3 : '제육고추장볶음밥\n시금치국\n야채크로켓*케찹\n배추김치',
4 : '참치마요덮밥\n무채국\n타코야끼\n배추김치',
5 : '사누끼우동\n김가루주먹밥\n포자만두찜*초간장\n배추김치',
6 : '주말은 쉽니다',
7 : '주말은 쉽니다',
}

dinner_menu_C = {
1 : '준비중입니다',
2 : '함박스테이크\n감자튀김\n야채샐러드\n크림스프\n배추김치\n쌀밥',
3 : '부대찌개/라면사리\n탕수육/소스\n돌나물/초장\n멸치땅콩조림\n배추김치\n쌀밥',
4 : '매운돼지갈비찜\n두부구이/양념\n콩나물무침\n연근조림\n배추김치\n쌀밥',
5 : '오므라이스/소스\n만두강정\n참나물생채\n우동국\n배추김치\n쌀밥',
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


