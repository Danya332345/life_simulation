"""
Модуль, описывающий базовый класс Organism.
"""

class Organism:
    """Базовый класс для всех живых организмов в симуляции."""

    def __init__(self, name: str, energy: float) -> None:
        """
        Инициализирует организм.

        :param name: имя организма
        :param energy: начальный запас энергии
        """
        self.name = name
        self.energy = energy

    def eat(self, food_energy: float) -> None:
        """
        Поглощает энергию из пищи.

        :param food_energy: количество полученной энергии
        """
        if food_energy < 0:
            raise ValueError("Энергия пищи не может быть отрицательной.")
        self.energy += food_energy
        print(f"{self.name} съел и получил {food_energy} энергии.")

    def is_alive(self) -> bool:
        """Возвращает True, если организм жив (энергия > 0)."""
        return self.energy > 0

    def __str__(self) -> str:
        return f"{self.name} (энергия: {self.energy:.1f})"