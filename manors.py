import requests
from derbyshire_places import get_place_ids_in_derbyshire

def get_manor_ids(place_id):
    url = f"https://opendomesday.org/api/1.0/place/{place_id}"
    response = requests.get(url)
    data = response.json()
    manor_ids = [manor["id"] for manor in data["manors"]]
    return manor_ids

if __name__ == "__main__":
    place_ids = get_place_ids_in_derbyshire()
    print(place_ids)

    test_place_id = place_ids[0]
    manor_ids = get_manor_ids(test_place_id)
    print("Manors in the first place:", manor_ids)