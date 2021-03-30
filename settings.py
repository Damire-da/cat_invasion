class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (255, 182, 193)
        self.ship_speed_factor = 1.5

        # Параметры пуль
        self.bullet_height = 10
        self.bullet_width = 3
        self.bullet_color = 60, 60, 60
        self.bullet_speed_factor = 1