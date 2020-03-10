import requests
import copy
def get_component_range() :
    payload = 'range'
    print("*** payload ",payload)
    r= requests.get('http://localhost:5000/component',params=payload)
    # create a list from the response object
    range = list(r.json().values())[0]
    retData ={}
    for item in range:
        retData.update({item[0]:item[1]})
    print("*** retData ",retData)

    return retData
