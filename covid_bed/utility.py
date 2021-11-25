import pickle
import requests
from .models import State, District, Hospital

def add_data_to_db(response):
    for i in response:
        state_obj, created = State.objects.get_or_create(name=i['STEIN_ID'])
        print(i)
        try:
            district_obj, created = District.objects.get_or_create(name=i['DISTRICT'])
            HAS_ICU_BEDS = str(i.get('HAS_ICU_BEDS', False)).capitalize()
            if Hospital.objects.filter(name=i['HOSPITAL_NAME']).exists():
                hospitals = Hospital.objects.get(name=i['HOSPITAL_NAME'])
                hospitals.state = state_obj
                hospitals.district = district_obj
                hospitals.contact = i.get('CONTACT', None) or i.get('HOSPITAL_NUMBER', None)
                hospitals.alternative_contact = i.get('NODAL_OFFICER_CONTACT', '104 OR 0135-2710334')
                hospitals.total_ICU = i.get('ICU_TOTAL') or i.get('ALLOCATED_ICU') or i.get('TOTAL_ICU_BEDS') or i.get(
                    'TOTAL_ICU_BEDS_AVAILABLE', 0)
                hospitals.occupied_ICU = i.get('ICU_OCCUPIED') or i.get('ADMITTED_ICU') or i.get(
                    'TOTAL_ICU_BEDS_OCCUPIED', 0)
                hospitals.vacant_ICU = i.get('ICU_AVAILABLE') or i.get('TOTAL_ICU_BEDS_AVAILABLE', 0)
                hospitals.total_general = i.get('GENERAL_TOTAL') or i.get('NONOXYGEN_BEDS_TOTAL') or i.get(
                    'TOTAL_WITHOUT_OXYGEN_BEDS_AVAILABLE') or i.get(
                    'TOTAL_BEDS_WITHOUT_OXYGEN	') or i.get('GENERAL_BEDS_TOTAL', 0)
                hospitals.occupied_general = i.get('GENERAL_OCCUPIED') or i.get(
                    'TOTAL_WITHOUT_OXYGEN_BEDS_OCCUPIED') or i.get('GENERAL_BEDS_OCCUPIED') or 0
                hospitals.vacant_general = i.get('GENERAL_AVAILABLE') or i.get('AVAILABLE_BEDS_WITHOUT_OXYGEN') or i.get(
                    'NONOXYGEN_BEDS_VACANT') or i.get(
                    'GENERAL_BEDS_AVAILABLE') or 0
                hospitals.total_oxygen_general = i.get('OXYGEN_GENERAL_TOTAL') or i.get(
                    'OXYGEN_BEDS_TOTAL') or i.get('TOTAL_OXYGEN_BEDS_AVAILABLE') or i.get(
                    'BEDS_WITH_OXYGEN_TOTAL') or i.get('TOTAL_BEDS_WITH_OXYGEN') or 0
                hospitals.occupied_oxygen_general = i.get('OXYGEN_GENERAL_OCCUPIED') or i.get(
                    'TOTAL_OXYGEN_BEDS_OCCUPIED') or 0
                hospitals.vacant_oxygen_general = i.get('OXYGEN_GENERAL_AVAILABLE') or i.get(
                    'OXYGEN_BEDS_VACANT') or i.get('BEDS_WITH_OXYGEN_AVAILABLE') or i.get(
                    'AVAILABLE_BEDS_WITH_OXYGEN') or i.get('OXYGEN_BEDS_AVAILABLE') or 0
                hospitals.total_ventilators = i.get('VENTILATOR') or i.get(
                    'TOTAL_VENTILATOR_BEDS_AVAILABLE') or i.get('VENTILATOR_TOTAL') or 0
                hospitals.total_HDU = i.get('ALLOCATED_HDU') or i.get('HDU_BEDS_TOTAL') or 0
                hospitals.occupied_HDU = i.get('ADMITTED_HDU') or i.get('HDU_BEDS_VACANT') or 0
                hospitals.vacant_HDU = i.get('BLOCKED_HDU') or 0
                hospitals.total_isolation = 0
                hospitals.occupied_isolation = 0
                hospitals.vacant_isolation = 0
                hospitals.total_NMC_reserved = 0
                hospitals.occupied_NMC_reserved = 0
                hospitals.vacant_NMC_reserved = 0
                hospitals.location = i.get('LOCATION', None)
                hospitals.lat = i.get('LAT', None)
                hospitals.long = i.get("LONG", None)
                hospitals.has_ICU_beds = HAS_ICU_BEDS
                hospitals.has_ventilators = str(i.get('HAS_VENTILATORS', False)).capitalize()
                hospitals.is_new_hospital = str(i.get('IS_NEW_HOSPITAL', False)).capitalize()
                hospitals.category = i.get('CATEGORY', None)
                hospitals.total_beds = i.get('TOTAL_BEDS') or i.get('BEDS_TOTAL') or i.get(
                    'TOTAL_BEDS_ALLOCATED_TO_COVID', 0)
                hospitals.city = i.get('CITY') or i.get('ADDRESS') or i.get('DISTRICT')
                hospitals.type = i.get('TYPE', "Private")
                hospitals.save()
            else:
                Hospital.objects.create(name=i['HOSPITAL_NAME'],
                                        state=state_obj,
                                        district=district_obj,
                                        contact=i.get('CONTACT', None) or i.get('HOSPITAL_NUMBER', None),
                                        alternative_contact=i.get('NODAL_OFFICER_CONTACT', '104 OR 0135-2710334'),
                                        total_ICU=i.get('ICU_TOTAL') or i.get('ALLOCATED_ICU') or i.get(
                                            'TOTAL_ICU_BEDS') or i.get('TOTAL_ICU_BEDS_AVAILABLE', 0),
                                        occupied_ICU=i.get('ICU_OCCUPIED') or i.get('ADMITTED_ICU') or i.get(
                                            'TOTAL_ICU_BEDS_OCCUPIED', 0),
                                        vacant_ICU=i.get('ICU_AVAILABLE') or i.get('TOTAL_ICU_BEDS_AVAILABLE', 0),
                                        total_general=i.get('GENERAL_TOTAL') or i.get('NONOXYGEN_BEDS_TOTAL') or i.get(
                                            'TOTAL_WITHOUT_OXYGEN_BEDS_AVAILABLE') or i.get(
                                            'TOTAL_BEDS_WITHOUT_OXYGEN	') or i.get('GENERAL_BEDS_TOTAL', 0),
                                        occupied_general=i.get('GENERAL_OCCUPIED') or i.get(
                                            'TOTAL_WITHOUT_OXYGEN_BEDS_OCCUPIED') or i.get('GENERAL_BEDS_OCCUPIED', 0),
                                        vacant_general=i.get('GENERAL_AVAILABLE') or i.get(
                                            'AVAILABLE_BEDS_WITHOUT_OXYGEN') or i.get('NONOXYGEN_BEDS_VACANT') or i.get(
                                            'GENERAL_BEDS_AVAILABLE', 0),
                                        total_oxygen_general=i.get('OXYGEN_GENERAL_TOTAL') or i.get(
                                            'OXYGEN_BEDS_TOTAL') or i.get('TOTAL_OXYGEN_BEDS_AVAILABLE') or i.get(
                                            'BEDS_WITH_OXYGEN_TOTAL') or i.get('TOTAL_BEDS_WITH_OXYGEN', 0),
                                        occupied_oxygen_general=i.get('OXYGEN_GENERAL_OCCUPIED') or i.get(
                                            'TOTAL_OXYGEN_BEDS_OCCUPIED', 0),
                                        vacant_oxygen_general=i.get('OXYGEN_GENERAL_AVAILABLE') or i.get(
                                            'OXYGEN_BEDS_VACANT') or i.get('BEDS_WITH_OXYGEN_AVAILABLE') or i.get(
                                            'AVAILABLE_BEDS_WITH_OXYGEN') or i.get('OXYGEN_BEDS_AVAILABLE', 0),
                                        total_ventilators=i.get('VENTILATOR') or i.get(
                                            'TOTAL_VENTILATOR_BEDS_AVAILABLE') or i.get('VENTILATOR_TOTAL', 0),
                                        total_HDU=i.get('ALLOCATED_HDU') or i.get('HDU_BEDS_TOTAL', 0),
                                        occupied_HDU=i.get('ADMITTED_HDU') or i.get('HDU_BEDS_VACANT', 0),
                                        vacant_HDU=i.get('BLOCKED_HDU', 0),
                                        total_isolation=0,
                                        occupied_isolation=0,
                                        vacant_isolation=0,
                                        total_NMC_reserved=0,
                                        occupied_NMC_reserved=0,
                                        vacant_NMC_reserved=0,
                                        location=i.get('LOCATION', None),
                                        lat=i.get('LAT', None),
                                        long=i.get("LONG", None),
                                        has_ICU_beds=HAS_ICU_BEDS,
                                        has_ventilators=str(i.get('HAS_VENTILATORS', False)).capitalize(),
                                        is_new_hospital=str(i.get('IS_NEW_HOSPITAL', False)).capitalize(),
                                        category=i.get('CATEGORY', None),
                                        total_beds=i.get('TOTAL_BEDS') or i.get('BEDS_TOTAL') or i.get(
                                            'TOTAL_BEDS_ALLOCATED_TO_COVID', 0),
                                        city=i.get('CITY') or i.get('ADDRESS') or i.get('DISTRICT'),
                                        type=i.get('TYPE', "Private"),
                                        )
        except KeyError:
            pass

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
    state_list = [Uttar_Pradesh, Andra_Pradesh, Bangaluru, bihar, chattisgarh, gandhinagar, goa, haryana, nagpur,
                  nashik, pune, rajasthan, surat, tamil_nadu, telengana, thane, uttarakhand, west_bengal, ]
    payload = {}
    headers = {}
    locations = []
    for state in state_list:
        locations.append(requests.request("GET", state, headers=headers, data=payload).json())
    # Hospital.objects.select_related('state').delete()
    for location in locations:
        add_data_to_db(location)