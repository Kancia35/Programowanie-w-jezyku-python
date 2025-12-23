import requests
import argparse


class Brewery:
    def __init__(
            self,
            id: str,
            name: str,
            brewery_type: str,
            street: str,
            city: str,
            state: str,
            postal_code: str,
            country: str,
            phone: str,
            website_url: str,
    ) -> None:
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country
        self.phone = phone
        self.website_url = website_url

    def __str__(self) -> str:
        return (
            f"Brewery ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Type: {self.brewery_type}\n"
            f"Address: {self.street or 'N/A'}, {self.city}, {self.state or ''} "
            f"{self.postal_code}, {self.country}\n"
            f"Phone: {self.phone or 'N/A'}\n"
            f"Website: {self.website_url or 'N/A'}\n"
            f"{'-' * 30}"
        )


def get_breweries_from_api(city: str = None) -> list:
    """
    """
    url = "https://api.openbrewerydb.org/v1/breweries"
    params = {}

    if city:
        params['by_city'] = city

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Błąd podczas pobierania danych: {response.status_code}")
        return []


def brewery_factory(breweries: list) -> list[Brewery]:
    brewery_objects = []
    for data in breweries:
        new_brewery = Brewery(
            id=data.get("id", ""),
            name=data.get("name", ""),
            brewery_type=data.get("brewery_type", ""),
            street=data.get("street", ""),
            city=data.get("city", ""),
            state=data.get("state", ""),
            postal_code=data.get("postal_code", ""),
            country=data.get("country", ""),
            phone=data.get("phone", ""),
            website_url=data.get("website_url", ""),
        )
        brewery_objects.append(new_brewery)
    return brewery_objects


def main():
    parser = argparse.ArgumentParser(description="Pobieranie informacji o browarach.")
    parser.add_argument("--city", type=str, help="Nazwa miasta, dla którego chcesz wyświetlić browary")

    args = parser.parse_args()

    breweries_raw = get_breweries_from_api(city=args.city)

    breweries = brewery_factory(breweries_raw)

    if not breweries:
        print("Nie znaleziono browarów dla podanych kryteriów.")
    else:
        for brewery in breweries[:5]:
            print(brewery)


if __name__ == "__main__":
    main()
