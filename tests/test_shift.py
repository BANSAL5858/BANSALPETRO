import pytest

from pump_system.models import Nozzle, Inventory, start_shift


def test_shift_sale_inventory_reduction():
    nozzles = [Nozzle(id=1, fuel_type="petrol", meter_reading=1000.0)]
    inventory = Inventory({"petrol": 500.0})
    shift = start_shift(nozzles)

    sale = shift.record_sale(inventory, nozzle_id=1, quantity=10.0, rate=100.0, payment_method="cash")

    assert sale.amount == 1000.0
    assert inventory.levels["petrol"] == pytest.approx(490.0)
    assert shift.total_amount == pytest.approx(1000.0)


def test_record_sale_insufficient_inventory():
    nozzles = [Nozzle(id=1, fuel_type="diesel", meter_reading=2000.0)]
    inventory = Inventory({"diesel": 5.0})
    shift = start_shift(nozzles)

    with pytest.raises(ValueError):
        shift.record_sale(inventory, nozzle_id=1, quantity=10.0, rate=90.0, payment_method="cash")
