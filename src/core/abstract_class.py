class Aurum:
    def __init__(self):
        # Основные химические свойства золота
        self.name = "Gold"
        self.symbol = "Au"
        self.atomic_number = 79
        self.atomic_weight = 196.967
        self.state_at_room_temp = "Solid"
        self.melting_point_celsius = 1064.18
        
    def get_info(self):
        """Возвращает строку с базовой информацией о металле."""
        return f"Металл: {self.name} ({self.symbol}), Атомный номер: {self.atomic_number}"

    def check_melting(self, temperature):
        """Проверяет, расплавится ли золото при указанной температуре (в Цельсиях)."""
        if temperature >= self.melting_point_celsius:
            return True
        return False
