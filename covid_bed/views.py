from django.utils import timezone
from django.shortcuts import render
from .models import Hospital, District, State
import folium


# def get_api_data():
#     url = "https://coronabeds.jantasamvad.org/covid-info.js?callback=?"  # delhi
#
#     payload = {}
#     headers = {}
#
#     response = requests.request("GET", url, headers=headers, data=payload)
#     return response
# Create your views here.
def index(request):
    """

    :param request:
    :return:
    """
    # url = "https://api.covidbedsindia.in/v1/storages/609fc7dde75f9ccdd696eb35/Uttar%20Pradesh"
    # response = get_api_data()
    # url_list = ['https://coronabeds.jantasamvad.org/covid-info.js?callback=?',]
    # async with aiohttp.ClientSession() as client:
    #     tasks=[]
    #     for url in url_list:
    #         task = asyncio.ensure_future(fetch(client,url))
    #         tasks.append(task)
    #     result = await asyncio.gather(*tasks)
    #
    # task = asyncio.ensure_future(get_api_data())
    # print(response.text)
    # await asyncio.wait([task,])
    # response=api_data()
    # print(response)
    # api_data()
    states = State.objects.values('name', )
    lat = 20.5937
    long = 78.9629
    map = folium.Map(location=(lat,long),zoom_start=4)
    states_total = dict()
    update_date = timezone.now()
    for state in states:
        hospitals = Hospital.objects.select_related('state').filter(state__name=state['name']).order_by('-total_ICU')
        print(hospitals.count())
        total_beds = 0
        for hospital in hospitals:
            update_date = hospital.update_date
            if hospital.total_beds == 0:
                if hospital.total_ICU:
                    total_beds += hospital.total_ICU
                if hospital.total_HDU:
                    total_beds += hospital.total_HDU
                if hospital.total_ICU:
                    total_beds += hospital.total_ICU
                if hospital.total_general:
                    total_beds += hospital.total_general
                if hospital.total_oxygen_general:
                    total_beds += hospital.total_oxygen_general
                if hospital.total_isolation:
                    total_beds += hospital.total_isolation
            else:
                total_beds += hospital.total_beds
        states_total.update({state['name']: total_beds})
    context = {
        'hospitals': states_total,
        'states': states,
        'update_date': update_date,
        "map": map._repr_html_(),
    }
    return render(request, 'covid_bed/index.html', context)


def hospital_list_view(request, state: str):
    """
    :param request:
    :param state:
    :return:
    """
    hospitals = Hospital.objects.select_related('state').filter(state__name=state).order_by('-total_beds')
    total_hospitals = hospitals.count()
    context = {
        'hospitals_list': hospitals,
        'total_hospitals': total_hospitals
    }
    return render(request, 'covid_bed/hospital_list.html', context)


def about(request):
    """
    :param request:
    :return:
    """
    return render(request, 'covid_bed/about.html')
