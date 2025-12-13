from typing import List
from typing import Optional

class Brewery:
    def __init__(
        self,
        id: str,
        name: str,
        brewery_type: str,
        city: str,
        state: str,
        country: str,
        street: Optional[str],
        postal_code: Optional[str],
        longitude: Optional[str],
        latitude: Optional[str]
    ):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.city = city
        self.state = state
        self.country = country
        self.street = street
        self.postal_code = postal_code
        self.longitude = longitude
        self.latitude = latitude

    def __str__(self):
        return (
            f"Browar: {self.name}\n"
            f"Typ: {self.brewery_type}\n"
            f"Miasto: {self.city}, {self.state}, {self.country}\n"
            f"Adres: {self.street or '-'} {self.postal_code or ''}\n"
            f"Współrzędne: {self.latitude}, {self.longitude}\n"
        )


def fetch_breweries(city: Optional[str] = None):
    url = "https://api.openbrewerydb.org/v1/breweries"
    params = {"per_page": 20}

    if city:
        params["by_city"] = city

    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--city", type=str, help="Miasto browarów (np. Berlin)")
    args = parser.parse_args()

    data = fetch_breweries(args.city)

    breweries = [
        Brewery(
            id=b["id"],
            name=b["name"],
            brewery_type=b["brewery_type"],
            city=b["city"],
            state=b["state"],
            country=b["country"],
            street=b.get("street"),
            postal_code=b.get("postal_code"),
            longitude=b.get("longitude"),
            latitude=b.get("latitude"),
        )
        for b in data
    ]

    for brewery in breweries:
        print(brewery)


if __name__ == "__main__":
    main()