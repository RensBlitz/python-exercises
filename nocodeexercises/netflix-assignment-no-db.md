# Projectbeschrijving
Je gaat een eenvoudige CRUD-backend voor een Netflix-achtige applicatie bouwen in Python met Flask. De service draait volledig in-memory (zonder echte database), alle data is "hard coded" tijdens runtime en het wegschrijven van data is niet mogelijk. De backend biedt basisfunctionaliteit om films te beheren en gebruikersratings op te slaan.

## 0. Project opstarten in PyCharm

### Stap 1: Nieuw project aanmaken
1. Open **PyCharm**
2. Klik op **"New Project"**
3. Selecteer **"Pure Python"** als project type
4. Geef je project een naam (bijvoorbeeld: `netflix-flask-api`)
5. Kies de locatie waar je het project wilt opslaan
6. Bij **"Python Interpreter"**:
   - Selecteer **"New environment using Virtualenv"**
   - Zorg ervoor dat **Python 3.9+** is geselecteerd (bij voorkeur Python 3.11 of hoger)
7. Klik op **"Create"**

### Stap 2: Dependencies installeren
1. Open de **Terminal** in PyCharm (onderaan het scherm)
2. Zorg ervoor dat je virtual environment actief is (je ziet `(venv)` of `(netflix-flask-api)` voor je prompt)
3. Installeer Flask:
   ```bash
   pip install Flask
   ```
4. Maak een `requirements.txt` bestand aan in de root van je project:
   ```
   Flask==3.0.0
   ```

### Stap 3: Project structuur aanmaken
Maak de volgende mappenstructuur aan in je project:
```
netflix-flask-api/
├── app.py
├── requirements.txt
├── dtos/
│   └── __init__.py
├── services/
│   └── __init__.py
└── blueprints/
    └── __init__.py
```

**Tip:** Rechtermuisklik in de Project Explorer → New → Python Package om mappen met `__init__.py` aan te maken.

### Stap 4: Run configuratie instellen
1. Ga naar **Run** → **Edit Configurations**
2. Klik op **"+"** → **Python**
3. Geef een naam (bijvoorbeeld: "Flask Netflix API")
4. Bij **Script path**: selecteer je `app.py` bestand
5. Bij **Working directory**: zorg dat dit je project root is
6. Klik **OK**

Nu ben je klaar om te beginnen met de implementatie!

## 1. API-specificatie

### GET /films

**Doel:** Haalt alle films op.  
**Request:** Geen body of parameters.  
**Response (200 OK):**
```json
{
  "films": [
    {
      "id": "123",
      "titel": "Inception",
      "beschrijving": "Een droom-in-een-droom heistfilm",
      "genre": "Sci-fi",
      "releasedatum": "2010-07-16"
    },
    {
      "id": "456",
      "titel": "Parasite",
      "beschrijving": "Kritisch drama over klassenverschillen",
      "genre": "Drama",
      "releasedatum": "2019-05-30"
    }
    // …
  ]
}
```

### GET /films/<id>

**Doel:** Levert de details van één film.  
**Request:** Path-parameter `<id>`. Geen body.  
**Response (200 OK):**
```json
{
  "id": "123",
  "titel": "Inception",
  "beschrijving": "Een droom-in-een-droom heistfilm",
  "genre": "Sci-fi",
  "releasedatum": "2010-07-16",
  "gemiddeldeRating": 4.7,
  "aantalRatings": 1250
}
```

### POST /films

**Doel:** Voegt een nieuwe film toe.  
**Request:** Raw JSON met titel, beschrijving, genre, releasedatum.  
**Response (201 Created):** JSON van de toegevoegde film met gegenereerd id.  
**Logging:** In plaats van opslaan `print("New film:", film_dto.__dict__)`.

### GET /films/populair?limit=10&datum=YYYY-MM-DD

**Doel:** Toont de populairste films op een gegeven dag.  
**Request:**
- `limit` (optioneel, standaard 10)
- `datum` (optioneel, standaard vandaag)

**Response (200 OK):** JSON met datum, limit en een lijst populairsteFilms.

### POST /films/<id>/rating

**Doel:** Voegt een 1–5-sterren rating toe voor een film.  
**Request:** Raw JSON met optioneel userId, score, timestamp.  
**Response (201 Created):** JSON van de nieuwe rating.  
**Logging:** `print("New rating:", rating_dto.__dict__)`.

## 2. Over Flask

Flask is een lichtgewicht en flexibel webframework voor Python:

- **Minimalistisch:** Begin met één module en voeg alleen toe wat je nodig hebt.
- **Routing via decorators:** Definieer HTTP-routes met `@app.route` of binnen Blueprints.
- **Embedded dev-server:** Standaard ingebouwde server voor ontwikkeling.
- **Extensies:** Voeg eenvoudig functionaliteit toe via aanvullende pakketten.

## 3. Architectuur: Controller–Service–Repository pattern

In Flask implementeer je de controller-laag met Blueprints, maar het concept blijft:

**Blueprint (Controller)**  
Groepeert URL-routes en HTTP-handlers, vergelijkbaar met een controller-klasse in Java.

**Service**  
Bevat business- en CRUD-logica; beheert in-memory DTO's.

**Repository (optioneel)**  
Bij echte database komt hier data-toegang; in dit project integreer je dat in de service.

## 4. Architectuur en opbouw van de applicatie

### 4.1 DTO-laag
Definieer alleen DTO-klassen (FilmDto, RatingDto) met een `__init__`-constructor waarin je alle velden meegeeft.
Constructor (`__init__`) is de plek waar je een nieuw object initialiseert. Bijvoorbeeld in `dtos/film_dto.py`:

```python
class FilmDto:
    def __init__(self, id: str, titel: str, beschrijving: str, genre: str, releasedatum: str,
                 gemiddeldeRating: float = None, aantalRatings: int = None):
        # __init__ is de constructor: hier stel je de velden in
        self.id = id
        self.titel = titel
        self.beschrijving = beschrijving
        self.genre = genre
        self.releasedatum = releasedatum
        self.gemiddeldeRating = gemiddeldeRating
        self.aantalRatings = aantalRatings

class RatingDto:
    def __init__(self, ratingId: str, filmId: str, userId: str, score: int, timestamp: str):
        self.ratingId = ratingId
        self.filmId = filmId
        self.userId = userId
        self.score = score
        self.timestamp = timestamp
```

Maak tijdens runtime in de service hard-coded lijsten of dicts van deze DTO's om terug te sturen bij GET-verzoeken.

### 4.2 Package-structuur en __init__.py
Zorg dat iedere map een `__init__.py` heeft, bijvoorbeeld:

```
your_app/
  __init__.py
  app.py
  dtos/
    __init__.py
    film_dto.py
    rating_dto.py
  services/
    __init__.py
    film_service.py
  blueprints/
    __init__.py
    films_bp.py
```

Een (leeg) `__init__.py` maakt een map een package zodat imports werken.

### 4.3 Service-laag
In `services/film_service.py`:

Definieer `class FilmService:` met methodes:
- `get_all_films()`
- `get_film_by_id(id)`
- `add_film(film_dto)`
- `get_populaire_films(limit, datum)`
- `add_rating(film_id, rating_dto)`

Bij een POST:
```python
def add_film(self, film_dto):
    print("New film:", film_dto.__dict__)
    return film_dto
```

### 4.4 Blueprint (Controller)-laag
In `blueprints/films_bp.py`:

```python
from flask import Blueprint, request, jsonify
from services.film_service import FilmService
from dtos.film_dto import FilmDto
from dtos.rating_dto import RatingDto

# 1. Instantiëren van de service (één enkele instantie)
film_service = FilmService()

films_bp = Blueprint('films', __name__, url_prefix='/films')

@films_bp.route('/', methods=['GET'])
def get_all_films():
    films = film_service.get_all_films()
    return jsonify([f.__dict__ for f in films]), 200

@films_bp.route('/', methods=['POST'])
def create_film():
    data = request.get_json()
    film_dto = FilmDto(None, **data)
    created = film_service.add_film(film_dto)
    return jsonify(created.__dict__), 201

```

**Instantiëren:** `film_service = FilmService()` staat bovenaan, buiten de route-functies, zodat alle handlers dezelfde instantie delen.  
**Routes:** `@films_bp.route(...)` definieert welke URL naar welke functie gaat.

### Samengevat

**Instantiëren** van je service-klasse gebeurt buiten (bovenaan) de route-functies, in de module waar je de Blueprint definieert.  
**Registreren** van je routes (Blueprint) gebeurt in `app.py` via `app.register_blueprint(...)`.

Op deze manier heb je een duidelijke scheiding:

- Je service is klaar voor alle handlers,
- Je Blueprint omschrijft wát er per URL gebeurt,
- En in `app.py` zet je die Blueprint live in je app.

## 5. Registratie en opstarten in app.py

```python
from flask import Flask
from blueprints.films_bp import films_bp

app = Flask(__name__)

# Koppel alle routes uit films_bp aan je app
app.register_blueprint(films_bp)

if __name__ == '__main__':
    # Start de ingebouwde development-server op poort 8080
    app.run(debug=True, port=8080)
```

`app.register_blueprint` zorgt dat Flask alle `@films_bp.route`-handlers activeert.

## 6. Aanroepen van de API-endpoints via Postman

Gebruik basis-URL `http://localhost:8080/films`:

- **GET /** → `/films/`
- **GET /<id>** → `/films/123`
- **POST /** → `/films/` (raw JSON body; print-logging)
- **GET /populair** → `/films/populair?limit=5&datum=2025-06-10`
- **POST /<id>/rating** → `/films/123/rating` (raw JSON body; print-logging) 