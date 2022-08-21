# Task 3

Zadanie 3: Zadanie na wykorzystanie Django, tworzenie zapytań, posługiwanie się formatem XML oraz JSON
Na stronie NBP Web API dostępne jest API pozwalające na pobieranie kursów walut oraz cen złota w formacie XML oraz JSON.
Napisać stronę, która po podaniu zakresu dat oraz wybraniu rodzaju waluty wypisze najdłuższy przedział czasu (w ramach podanego zakresu) w którym wybrana waluta osiągała wartości niemalejące.
Użycie Django nie jest wymagane -- można użyć innego frameworku (użycie frameworku jest wymagane).

## Setup

I suggest using virtual environments to make sure that we won't have a dependency conflict with other projects

The example virutal env is created with venv package:
https://docs.python.org/3/library/venv.html#module-venv

```bash
cd task3
python -m venv myenv
source ./task3env/bin/activate
pip install -r requirements.txt
```

## Running app

```bash
# Remember to activate your venv before running app
# source ./task3env/bin/activate
python app.py
```

App should be available on localhost:5000
