import requests

def get_place_ids_in_derbyshire():
    url = "https://opendomesday.org/api/1.0/county/dby/"
    response = requests.get(url)
    data = response.json()
    place_ids = [place["id"] for place in data["places_in_county"]]
    return place_ids

if __name__ == "__main__":
    place_ids = get_place_ids_in_derbyshire()
    print(place_ids)
