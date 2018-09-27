from django.http import HttpResponse
from django.utils import timezone


# from django.shortcuts import render

# Create your views here.
def post_list(request):
    """

    :param request: 실제HTTP요청에 대한 정보를 가진 객체
    :return:
    """
    current_time = timezone.now()
    # 현재 지역에 맞는 날짜시간 객체를 돌려줌

    return HttpResponse(
        '<html>'
        '<body>'
        '<h1>Post List</h1>'
        '<p>{}</p>'
        '</body>'
        '</html>'.format(
            # 날짜&시간 객체가 가진 정보를 문자열로 변환
            current_time.strftime('%Y. %m. %d<br>%H:%M:%S')
        )
    )

    # 돌려주는 형식을 http형식으로? 200이면 정상 400이면 비정상
