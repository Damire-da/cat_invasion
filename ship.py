import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        """Инициализирует корабль и задаёт его начальную позицию."""
        self.screen = screen
        self.ai_settings = ai_settings

        #Загрузка изображения корабля и получение прямогульника.
        self.image = pygame.image.load('D:\\alien_invasion\images\mouse.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #Каждый новый корабль появляется у нижнего края экрана.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    
        #Сохранение координат корабля,чтобы реализовать передвижение в разные стороны
        self.centerX = float(self.rect.centerx)
        self.centerY = float(self.rect.centery)

        #Флаги перемещения
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    
    def update(self):
        """Обновляет позицию корабля с учётом флага"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerX += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerX -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.centerY -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centerY += self.ai_settings.ship_speed_factor
        #Обновление атрибута rect на основании self.center
        self.rect.centerx = self.centerX
        self.rect.centery = self.centerY


    def blitme(self):
        """Рисует корабль в текущей позиции."""

        self.screen.blit(self.image, self.rect)