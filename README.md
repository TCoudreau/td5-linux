# Rapport

[Rapport PDF (LaTeX)](https://github.com/TCoudreau/td-linux/blob/main/TD5-Rapport.pdf)

## Exercise 1: Working Directory

1.

```bash
mkdir td4
cd td4
```

2.

```bash
git init
```

3.

```bash
sudo apt-get install python3-pip
```

4.

```bash
pip3 install virtualenv
```

5.

```bash
python3 -m venv .env
```

6.

```bash
source .env/bin/activate
```

7.

```bash
pip list
```

8.

```bash
git status
```

9.

```bash
echo ".env" > .gitignore
```

10.

```bash
git status
```

11.

```bash
git add .gitignore
git commit -m "Initial commit with .gitignore"
```

## Exercise 2: Python Script

1.

```bash
pip install requests
```

2.

```python
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
```

3.

```bash
git add derbyshire_places.py
git commit -m "Add Python script for Derbyshire places"
```

## Exercise 3: Python Module

1.

```python
import requests

def get_manor_ids(place_id):
    url = f"https://opendomesday.org/api/1.0/place/{place_id}"
    response = requests.get(url)
    data = response.json()
    manor_ids = [manor["id"] for manor in data["manors"]]
    return manor_ids
```

2.

```bash
python3 manors.py
```

3.

```bash
python3
```

```python
from manors import get_manor_ids
get_manor_ids(1036)
```

4.

```python
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
```

5.

```bash
python manors.py
```

6.

```bash
git add manors.py
git commit -m "Add Python module manors.py"
```

## Exercise 4: Python Program

```bash
pip install pandas
```

```python
import requests
import pandas as pd
from derbyshire_places import get_place_ids_in_derbyshire

def get_manor_ids(place_id):
    """Return    list of manor ids for a given place id."""
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
```

```bash
git add manors.py
git commit -m "Exercice 4"
```

