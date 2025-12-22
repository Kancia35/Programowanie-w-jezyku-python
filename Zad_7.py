from typing import List
import requests
import argparse

URL_API = 'https://api.openbrewerydb.org/v1/breweries'


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
            f"Address: {self.street}, {self.city}, {self.state}, "
            f"{self.postal_code}, {self.country}\n"
            f"Phone: {self.phone}\n"
            f"Website: {self.website_url}\n"
        )


def get_breweries_from_api() -> list:
    response = requests.get("https://api.openbrewerydb.org/v1/breweries")
    breweries_data = response.json()
    return breweries_data


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
    breweries_raw = get_breweries_from_api()
    breweries = brewery_factory(breweries_raw)
    for brewery in breweries[:5]:
        print(brewery)


if __name__ == "__main__":
    main()