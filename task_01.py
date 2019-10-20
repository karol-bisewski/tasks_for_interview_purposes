def to_postcode(x: int):
    x = str(x)
    return f'{x[0:2]}-{x[2:]}'


def get_postcodes_between(a: str, b: str):
    a = int(a.replace('-', ''))
    b = int(b.replace('-', ''))
    return [to_postcode(x) for x in range(a+1, b)]


print(get_postcodes_between("79-900", "80-155"))
