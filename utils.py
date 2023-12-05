from exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError


def data_processing(data: dict) -> None:
    first_cup = int(data["first_cup"][:4])
    if data["titles"] < 0:
        raise NegativeTitlesError("titles cannot be negative")

    years_cup = [year for year in range(1930, 2024, 4)]
    if first_cup not in years_cup:
        raise InvalidYearCupError("there was no world cup this year")

    cup_valid = len(years_cup[years_cup.index(first_cup):])
    if data["titles"] > cup_valid:
        raise ImpossibleTitlesError(
            "impossible to have more titles than disputed cups")
