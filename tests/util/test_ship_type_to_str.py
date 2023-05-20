from naval_battle.util.ship_type_to_str import ship_type_to_str, ShipType


def test_submarine_to_str():
    assert "submarino" == ship_type_to_str(ShipType.SUBMARINE)


def test_small_ship_to_str():
    assert "navio pequeno" == ship_type_to_str(ShipType.SMALL_SHIP)


def test_medium_ship_to_str():
    assert "navio médio" == ship_type_to_str(ShipType.MEDIUM_SHIP)


def test_big_ship_to_str():
    assert "navio grande" == ship_type_to_str(ShipType.BIG_SHIP)
