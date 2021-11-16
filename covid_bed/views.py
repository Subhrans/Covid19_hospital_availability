from django.shortcuts import render,HttpResponse
import requests
from .utility import fetch,api_data
from .models import Hospital
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
    return render(request,'covid_bed/index.html',)
