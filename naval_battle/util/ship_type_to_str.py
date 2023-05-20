from naval_battle.util.enums.ship_type import ShipType

def ship_type_to_str(ship_type: ShipType) -> str:
    if ship_type == ShipType.SUBMARINE: 
        return "submarino"
    elif ship_type == ShipType.SMALL_SHIP:
        return "navio pequeno"
    elif ship_type == ShipType.MEDIUM_SHIP:
        return "navio médio"
    elif ship_type == ship_type.BIG_SHIP:
        return "navio grande"