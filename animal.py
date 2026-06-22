"""
Модуль, описывающий класс Animal (хищник).
"""

from organism import Organism


class Animal(Organism):
    """Класс животного, умеющего охотиться."""

    def hunt(self, prey: Organism) -> None:
        """
        Охота на другой организм.

        :param prey: организм-жертва
        """
        if not prey.is_alive():
            print(f"{self.name} не может охотиться на мёртвую {prey.name}.")
            return
        energy_gain = prey.energy
        self.eat(energy_gain)
        prey.energy = 0
        print(f"{self.name} охотился на {prey.name} и получил {energy_gain} энергии.")