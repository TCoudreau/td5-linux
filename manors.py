import requests
import pandas as pd
from derbyshire_places import get_place_ids_in_derbyshire

def get_manor_ids(place_id):
    """Return a list of manor ids for a given place id."""
    url = f"https://opendomesday.org/api/1.0/place/{place_id}"
    response = requests.get(url)
    data = response.json()
    manor_ids = [manor["id"] for manor in data["manors"]]
    return manor_ids

def get_manor_details(manor_id):
    """Return manor details for a given manor id."""
    url = f"https://opendomesday.org/api/1.0/manor/{manor_id}"
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == "__main__":
    place_ids = get_place_ids_in_derbyshire()
    print("Place IDs:", place_ids)

    all_manor_ids = []
    for place_id in place_ids:
        manor_ids = get_manor_ids(place_id)
        all_manor_ids.extend(manor_ids)

    print("Manor IDs:", all_manor_ids)

    manor_details = [get_manor_details(manor_id) for manor_id in all_manor_ids]

    manor_data = [
        {"manor_id": manor["id"], "geld_paid": manor.get("geld", 0), "ploughs": manor.get("totalploughs", 0)}
        for manor in manor_details
    ]


    df = pd.DataFrame(manor_data)

    total_geld_paid = df["geld_paid"].sum()
    total_ploughs = df["ploughs"].sum()

    print("Total geld paid:", total_geld_paid)
    print("Total ploughs:", total_ploughs)