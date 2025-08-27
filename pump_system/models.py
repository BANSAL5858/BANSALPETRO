from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Dict, List
import uuid


@dataclass
class Nozzle:
    """Represents a fuel nozzle.

    Attributes:
        id: Unique identifier for the nozzle.
        fuel_type: Type of fuel dispensed by the nozzle (e.g. petrol, diesel).
        meter_reading: Current meter reading.
    """

    id: int
    fuel_type: str
    meter_reading: float = 0.0


@dataclass
class Sale:
    """Represents a single sale transaction."""

    nozzle_id: int
    fuel_type: str
    quantity: float
    rate: float
    payment_method: str
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    @property
    def amount(self) -> float:
        return self.quantity * self.rate


@dataclass
class Shift:
    """Represents a 12 hour shift."""

    id: str
    start_time: datetime
    end_time: datetime | None = None
    nozzles: Dict[int, Nozzle] = field(default_factory=dict)
    sales: List[Sale] = field(default_factory=list)

    def record_sale(self, inventory: "Inventory", nozzle_id: int, quantity: float, rate: float, payment_method: str) -> Sale:
        if nozzle_id not in self.nozzles:
            raise KeyError(f"Nozzle {nozzle_id} not found in this shift")

        nozzle = self.nozzles[nozzle_id]
        inventory.record_sale(nozzle.fuel_type, quantity)
        nozzle.meter_reading += quantity

        sale = Sale(
            nozzle_id=nozzle_id,
            fuel_type=nozzle.fuel_type,
            quantity=quantity,
            rate=rate,
            payment_method=payment_method,
        )
        self.sales.append(sale)
        return sale

    def end(self) -> None:
        self.end_time = datetime.now(timezone.utc)

    @property
    def total_amount(self) -> float:
        return sum(s.amount for s in self.sales)


class Inventory:
    """Tracks fuel inventory levels for each fuel type."""

    def __init__(self, levels: Dict[str, float] | None = None) -> None:
        self.levels: Dict[str, float] = levels.copy() if levels else {}

    def add_stock(self, fuel_type: str, quantity: float) -> None:
        self.levels[fuel_type] = self.levels.get(fuel_type, 0.0) + quantity

    def record_sale(self, fuel_type: str, quantity: float) -> None:
        available = self.levels.get(fuel_type, 0.0)
        if quantity > available:
            raise ValueError(f"Insufficient stock for {fuel_type}: have {available}, need {quantity}")
        self.levels[fuel_type] = available - quantity


def start_shift(nozzles: List[Nozzle]) -> Shift:
    """Creates a new shift for the provided list of nozzles."""
    return Shift(
        id=str(uuid.uuid4()),
        start_time=datetime.now(timezone.utc),
        nozzles={n.id: n for n in nozzles},
    )
