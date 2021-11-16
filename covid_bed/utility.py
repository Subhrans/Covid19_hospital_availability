import pickle
import requests


def api_data():
    Uttar_Pradesh = "https://api.covidbedsindia.in/v1/storages/609fc7dde75f9ccdd696eb35/Uttar%20Pradesh"
    Andra_Pradesh = "https://api.covidbedsindia.in/v1/storages/608982e003eef31f34d05a71/Andhra%20Pradesh"
    Bangaluru = "https://api.covidbedsindia.in/v1/storages/608982f703eef3de2bd05a72/Bengaluru"
    bihar = "https://api.covidbedsindia.in/v1/storages/60a62cf2e75f9c105696eb38/Bihar"
    chattisgarh = "https://api.covidbedsindia.in/v1/storages/6089833203eef38338d05a73/Chhattisgarh"
    delhi = "https://coronabeds.jantasamvad.org/covid-info.js?callback=?"
    gandhinagar = "https://api.covidbedsindia.in/v1/storages/608d544533382c3501cf8c96/Gandhinagar"
    goa = "https://api.covidbedsindia.in/v1/storages/60a36cb4e75f9c5d8c96eb36/Goa"
    haryana = "https://api.covidbedsindia.in/v1/storages/6089834e03eef33448d05a74/Haryana"
    nagpur = "https://api.covidbedsindia.in/v1/storages/608983e003eef32328d05a76/Nagpur"
    nashik = "https://api.covidbedsindia.in/v1/storages/608efad8423e2153ac2fd383/Nashik"
    pune = "https://api.covidbedsindia.in/v1/storages/6089822703eef30c1cd05a6e/Pune"
    rajasthan = "https://api.covidbedsindia.in/v1/storages/608983ed03eef39bb4d05a77/Rajasthan"
    surat = "https://api.covidbedsindia.in/v1/storages/6094e879423e213eb82fd384/Surat"
    tamil_nadu = "https://api.covidbedsindia.in/v1/storages/6089820e03eef3b588d05a6d/Tamil%20Nadu"
    telengana = "https://api.covidbedsindia.in/v1/storages/6089829403eef36d93d05a6f/Telangana"
    thane = "https://api.covidbedsindia.in/v1/storages/609fc78ae75f9c111f96eb34/Thane"
    uttarakhand = "https://api.covidbedsindia.in/v1/storages/608d542333382c01aecf8c95/Uttarakhand"
    west_bengal = "https://api.covidbedsindia.in/v1/storages/608983fc03eef384cad05a78/West%20Bengal"
    state_list = [Uttar_Pradesh, Andra_Pradesh, Bangaluru, bihar, chattisgarh, delhi, gandhinagar, goa, haryana, nagpur,
                  nashik, pune, rajasthan, surat, tamil_nadu, telengana, thane, uttarakhand, west_bengal]
    payload = {}
    headers = {}
    for state in state_list:
        response = requests.request("GET", state, headers=headers, data=payload).json()
        print(response)


async def fetch(client, url):
    async with client.get(url) as resp:
        assert resp.status == 200
        return await resp.json()
