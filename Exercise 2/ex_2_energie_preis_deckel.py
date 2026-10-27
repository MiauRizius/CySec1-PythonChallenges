def energie_preis_deckel(prev_year: int, this_year: int, price_per_kwh: float) -> float:
    # TODO implement
    # First 80% of previous year are capped at 0.4
    # any usage beyond these 80% needs to pay the full fill of price_per_kwh
    disc_price = 0.4
    discounted = prev_year * 0.8
    if(this_year <= discounted): return round(this_year*(disc_price if price_per_kwh > disc_price else price_per_kwh), 2)
    disc_cost = discounted * (disc_price if price_per_kwh > disc_price else price_per_kwh)
    normal_cost = (this_year - discounted) * price_per_kwh
    total = disc_cost + normal_cost
    return round(total, 2)


def main() -> None:
    print(energie_preis_deckel(10000, 8000, 0.3))
    print(energie_preis_deckel(10000, 8000, 0.4))
    print(energie_preis_deckel(10000, 8000, 0.5))
    print(energie_preis_deckel(8000, 10000, 0.5))
    # Note: This is only for student-side debugging
    assert energie_preis_deckel(10000, 8000, 0.3) == 2400.0
    assert energie_preis_deckel(10000, 8000, 0.4) == 3200.0
    assert energie_preis_deckel(10000, 8000, 0.5) == 3200.0
    assert energie_preis_deckel(8000, 10000, 0.5) == 4360.0


# this only ensures that main() is called when executing python file.py
if __name__ == '__main__':
    main()
