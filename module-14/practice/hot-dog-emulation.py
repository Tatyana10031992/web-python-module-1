from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class Ingredient:
    name: str
    key: str
    price: float
    cost: float




