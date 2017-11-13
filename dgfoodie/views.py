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
1 : '제육야채고추장볶음\n쌀밥\n미역국\n양배추쌈*쌈장\n얼갈이겉절이\n배추김치',
2 : '포크볼케찹조림\n쌀밥\n무채들깨국\n매운어묵볶음\n참나물무침\n배추김치',
3 : '넙적당면닭살야채볶음\n쌀밥\n시금치국\n미역줄기양파볶음\n열무겉절이\n배추김치',
4 : '돈채묵은지볶음\n쌀밥\n재첩국\n연두부*간장\n청경채겉절이\n깍두기',
5 : '치킨볼강정\n쌀밥\n매운콩나물국\n잡채\n오이양파무침\n배추김치',
6 : '주말은 쉽니다',
7 : '주말은 쉽니다',
}

lunch_menu_B = {
1 : '일식등심돈까스*일식s\n쌀밥\n크림스프\n감자튀김*케찹\n삼색야채샐러드*키위d\n배추김치/오렌지주스',
2 : '전주비빔밥*계란후라이\n무채들깨국\n떡편고기완자\n천사채샐러드\n배추김치\n사과주스',
3 : '뚝배기갈비탕\n쌀밥\n두부구이*양념장\n고구마맛탕\n깐마늘장아찌\n깍두기/요구르트',
4 : '매콤불닭에그덮밥\n팽이장국\n소시지구이*허니머스타드s\n콘샐러드\n배추김치\n쥬시쿨',
5 : '토마토소스스파게티\n파인애플볶음밥\n우동국물\n카레고로케1EA*케찹\n양상추샐러드*키위D\n배추김치/포도주스',
6 : '주말은 쉽니다',
7 : '주말은 쉽니다',
}

lunch_menu_C = {
1 : '순두부찌개\n야채고로케/케찹\n김구이/양념\n콩나물무침\n배추김치\n쌀밥\n샐러드',
2 : '닭개장\n탕수육/소스\n치커리생채\n계절과일\n배추김치\n쌀밥\n샐러드',
3 : '순대국밥/소면사리\n김말이튀김\n단배추생채\n콩조림\n배추김치\n쌀밥\n샐러드',
4 : '중화볶음밥/짜장소스/계란후라이\n어묵떡볶이\n우엉조림\n짬뽕국\n배추김치\n쌀밥\n샐러드',
5 : '매운돼지갈비찜\n팝콘치킨\n양배추부추무침\n양념깻잎지\n배추김치\n쌀밥\n샐러드',
6 : '주말은 쉽니다',
7 : '주말은 쉽니다',
}

dinner_menu_A = {
1 : '고등어구이\n쌀밥\n야채탕\n미니새송이버섯볶음\n브로커리*초장\n배추김치',
2 : '오징어볶음\n쌀밥\n순두부찌개\n연근조림\n쑥갓양파무침\n깍두기',
3 : '뚝배기순대국밥*소면사리\n쌀밥\n잡채볼조림\n우엉채볶음\n풋고추된장박이\n깍두기',
4 : '떡고기산적*깐풍소스\n쌀밥\n고추장수제비국\n탕평채\n오이양배추무침\n배추김치',
5 : '매콤불고기\n쌀밥\n시래기국\n단호박전*간장\n부추양파무침\n깍두기',
6 : '주말은 쉽니다',
7 : '주말은 쉽니다',
}

dinner_menu_B = {
1 : '비엔나마요덮밥\n우동국물\n매콤김말이2EA\n배추김치',
2 : '꼬치어묵우동\n쌀밥\n야채크로켓2ea\n배추김치',
3 : '자장덮밥\n캐플주스\n비빔춘권\n배추김치',
4 : '야끼우동\n우동국물\n타코야끼\n배추김치',
5 : '고추장제육볶음밥\n시래기국\n사모사\n배추김치',
6 : '주말은 쉽니다',
7 : '주말은 쉽니다',
}

dinner_menu_C = {
1 : '뚝배기김치볶음밥/계란후라이\n어묵볶음\n참나물생채\n콩나물국\n배추김치\n쌀밥',
2 : '카레라이스\n비빔만두/소스\n콘샐러드\n머묵무국\n배추김치\n쌀밥',
3 : '오므라이스\n만두강정\n두부샐러드\n우동국\n배추김치\n쌀밥',
4 : '돈육김치볶음\n두부구이/양념\n오이무침\n미역국\n배추김치\n쌀밥',
5 : '함박스테이크\n감자튀김\n야채샐러드\n크림스프\n배추김치\n쌀밥',
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


