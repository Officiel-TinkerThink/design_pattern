import json
from typing import Dict

class Flyweight:
    def __init__(self, intrinsic_state: str):
        self._intrinsic_state = intrinsic_state

    def operation(self, extrinsic_state: str) -> str:
        s = json.dumps(self._intrinsic_state)
        u = json.dumps(extrinsic_state)
        print(f"Flyweight: Displaying Intrinsic State: ({s}), Extrinsic State: ({u}) state.", end="")

class FlyweightFactory:
    _flyweights: Dict[str, Flyweight] = {}

    def __init__(self, initial_flyweights: list[Dict]) -> None:
        for state in initial_flyweights:
            self._flyweights[self.get_key(state)] = Flyweight(state)

    def get_key(self, state: Dict) -> str:
        return "_".join(sorted(state.values()))

    def get_flyweight(self, intrinsic_state: Dict) -> Flyweight:
        key = self.get_key(intrinsic_state)
        if not self._flyweights.get(key):
            print("FlyweightFactory: Can't find a flyweight, creating new one.")
            self._flyweights[key] = Flyweight(intrinsic_state)
        else:
            print("FlyweightFactory: Reusing existing flyweight.")
        return self._flyweights[key]

    def list_flyweights(self) -> None:
        count = len(self._flyweights)
        print(f"FlyweightFactory: I have {count} flyweights:")
        print("\n".join(map(str, self._flyweights.keys())), end="")


def add_car_to_police_database(
    factory: FlyweightFactory,
    plates: str,
    owner: str,
    brand: str,
    model: str,
    color: str,
) -> None:
    print("\nClient: Adding a car to database.")
    flyweight = factory.get_flyweight({
        "brand": brand,
        "model": model,
        "color": color
    })

    flyweight.operation(f"{plates}, {owner}")


if __name__ == "__main__":
    factory = FlyweightFactory([
        {"brand": "Chevrolet", "model": "Camaro2018", "color": "pink"},
        {"brand": "Mercedes Benz", "model": "C300", "color": "black"},
        {"brand": "Mercedes Benz", "model": "C500", "color": "red"},
        {"brand": "BMW", "model": "M5", "color": "red"},
        {"brand": "BMW", "model": "X6", "color": "white"},
    ])
    factory.list_flyweights()

    add_car_to_police_database(
        factory,
        "CL234IR",
        "James Doe",
        "BMW",
        "M5",
        "red",
    )

    add_car_to_police_database(
        factory,
        "CL234IR",
        "James Doe",
        "BMW",
        "X1",
        "red",
    )

    factory.list_flyweights()