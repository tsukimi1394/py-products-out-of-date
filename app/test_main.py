import datetime
from app.main import outdated_products
from freezegun import freeze_time
import pytest


@freeze_time("2022-02-02")
@pytest.mark.parametrize(
    "products,result",
    [
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160
                }
            ],
            ["duck"]
        ),
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 2),
                    "price": 160
                }
            ],
            []
        )
    ]
)
def test_outdated_products_frozen_date(
        products: list[dict],
        result: list[str]
) -> None:
    assert (
        outdated_products(products) == result
    ), "Result is not as expected"
