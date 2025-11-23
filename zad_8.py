import requests
import argparse
from typing import List, Optional, Dict, Any

API_adres = "https://api.openbrewerydb.org/v1/breweries"


class Brewery:
    def __init__(self, data: Dict[str, Any]):
        self.id: str = data.get("id", "")
        self.name: str = data.get("name", "")
        self.brewery_type: str = data.get("brewery_type", "")
        self.address_1: Optional[str] = data.get("address_1")
        self.address_2: Optional[str] = data.get("address_2")
        self.address_3: Optional[str] = data.get("address_3")
        self.city: Optional[str] = data.get("city")
        self.state_province: Optional[str] = data.get("state_province")
        self.postal_code: Optional[str] = data.get("postal_code")
        self.country: Optional[str] = data.get("country")
        self.longitude: Optional[str] = data.get("longitude")
        self.latitude: Optional[str] = data.get("latitude")
        self.phone: Optional[str] = data.get("phone")
        self.website_url: Optional[str] = data.get("website_url")
        self.state: Optional[str] = data.get("state")
        self.street: Optional[str] = data.get("street")

    def __str__(self) -> str:

        address_parts = [
            self.address_1,
            self.city,
            self.state_province,
            self.postal_code,
            self.country
        ]
        full_address = ", ".join(part for part in address_parts if part)

        description = f"""
        --- Browar: {self.name} ---
        Typ: {self.brewery_type.capitalize()}
        Adres: {full_address if full_address else 'Brak adresu'}
        Strona WWW: {self.website_url if self.website_url else 'Brak'}
        Telefon: {self.phone if self.phone else 'Brak'}
        """
        return description.strip()


def get_breweries(count: int = 20, city: Optional[str] = None) -> List[Brewery]:

    params: Dict[str, Any] = {"per_page": count}

    search_info = f"pobieram pierwsze {count} browarów"


    if city:
        params["by_city"] = city
        search_info = f"filtruję wg miasta '{city}' i pobieram pierwsze {count} wyników"

    print(f"Łączę się z API: {API_adres} i {search_info}...")

    try:
        response = requests.get(API_adres, params=params)
        response.raise_for_status()

        breweries_data: List[Dict[str, Any]] = response.json()

        brewery_objects: List[Brewery] = [
            Brewery(data) for data in breweries_data
        ]

        print(f"Pobrano i utworzono {len(brewery_objects)} instancji klasy Brewery.")
        return brewery_objects

    except requests.exceptions.RequestException as e:
        return []


def main():
    parser = argparse.ArgumentParser(
        description="Skrypt pobiera dane o browarach z Open Brewery DB API, z opcjonalnym filtrowaniem po mieście."
    )

    parser.add_argument(
        "--city",
        type=str,
        default=None,
        help="Ogranicza pobierane browary do podanego miasta (np. --city=san_diego)"
    )

    args = parser.parse_args()

    browary_lista: List[Brewery] = get_breweries(count=20, city=args.city)

    if browary_lista:
        for i, browar in enumerate(browary_lista):
            print(f"\n--- OBIEKT NR {i + 1} ---")
            print(browar)



if __name__ == "__main__":
    main()