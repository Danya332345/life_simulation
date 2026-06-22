"""
Тесты для класса Ecosystem.
"""

from ecosystem import Ecosystem
from organism import Organism


def test_add_and_count():
    eco = Ecosystem()
    org1 = Organism("A", 10)
    org2 = Organism("B", 20)
    eco.add_organism(org1)
    eco.add_organism(org2)
    assert len(eco.organisms) == 2
    assert eco.get_alive_count() == 2


def test_simulate_day():
    eco = Ecosystem()
    org = Organism("Тест", 0.0)
    eco.add_organism(org)
    eco.simulate_day(5.0)
    assert org.energy == 5.0
    assert org.is_alive() is True
