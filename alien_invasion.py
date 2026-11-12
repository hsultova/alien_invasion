import random
import sys
import pygame

from time import sleep

from alien import Alien
from button import Button
from scoreboard import Scoreboard
from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    # ------Setup------
    def __init__(self) -> None:
        """Initialize the game and create game resources."""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.stats = GameStats(self.settings)
        self.scoreboard = Scoreboard(self.screen, self.settings, self.stats)

        self.ship = Ship(self.screen, self.settings)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self.alien_bullets = pygame.sprite.Group()
        self.alien_fire_timer = 0

        self._create_fleet()

        self._alien_fire()

        self.game_active = False
        self.play_button = Button(self.screen, self.settings, "Play")

    def _create_fleet(self):
        """Create the fleet of aliens."""
        new_alien = Alien(self.screen, self.settings)
        alien_width, alien_height = new_alien.rect.size

        current_x, current_y = 2 * alien_width, 4 * alien_height
        while current_y < (self.settings.screen_height - self.settings.fleet_bottom_margin * alien_height):
            while current_x < (self.settings.screen_width - self.settings.fleet_side_margin * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width 
            current_x = 2 * alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position: int, y_position: int):
        """Create an alien and place it in the row."""
        new_alien = Alien(self.screen, self.settings)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    # ------Main loop------
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_alien_bullets()
                self._update_aliens()
                self._alien_fire()

            self._update_screen()
            self.clock.tick(self.settings.framerate)

    # ------Input------
    def _check_events(self):
        """Handling keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stats.write_high_score()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                self._check_play_button(mouse_position)

    def _check_keydown_events(self, event: pygame.Event):
        """Respond to keypresses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._ship_fire()
        elif event.key ==  pygame.K_p:
            self.reset_game()
            pygame.mouse.set_visible(False)
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event: pygame.Event):
        """Respond to keyreleases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_play_button(self, mouse_position):
        """Start a new game when the player click Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_position)
        if button_clicked and not self.game_active:
            self.reset_game()
            pygame.mouse.set_visible(False)

    # ------Updating------
    def _update_bullets(self):
        """Update position of bullets and remove bullets that have disappeared of the screen"""
        self.bullets.update()        

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)       

        self._check_bullet_alien_collisions()       

    def _update_alien_bullets(self):
        """Update position of alien bullets and remove bullets that have disappeared of the screen"""
        self.alien_bullets.update()

        for bullet in self.alien_bullets.copy():
            if bullet.rect.bottom >= self.settings.screen_height:
                self.bullets.remove(bullet)

        self._check_bullet_ship_collisions()

    def _update_aliens(self):
        """Check if the fleet is at an edge and update the positions of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()

    # ------Actions------
    def _ship_fire(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self.screen, self.settings, self.ship.rect.midtop[0], self.ship.rect.top, self.settings.bullet_speed, self.settings.bullet_color)
            self.bullets.add(new_bullet)

    def _alien_fire(self):
        """Randomly fire bullets from aliens."""
        self.alien_fire_timer += self.clock.get_time()
        if self.alien_fire_timer > self.settings.alien_fire_ms and self.aliens:
            number_of_shooters = self.settings.shooters
            while number_of_shooters > 0:
                shooter = random.choice(self.aliens.sprites())
                new_bullet = Bullet(self.screen, self.settings, shooter.rect.centerx, shooter.rect.bottom, self.settings.alien_bullet_speed, self.settings.alien_bullet_color)
                self.alien_bullets.add(new_bullet)
                self.alien_fire_timer = 0 
                number_of_shooters -= 1
       
    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ship_left > 0:
            self.reset_round()
        else:
            self.end_game()
            pygame.mouse.set_visible(True)

    # ------Collisions------   
    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:      
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.scoreboard.prep_score()
            self.scoreboard.check_high_score()
        
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            self.stats.level += 1
            self.scoreboard.prep_level()

    def _check_bullet_ship_collisions(self):
        """Respond to bullet-ship collisions."""
        if pygame.sprite.spritecollideany(self.ship, self.alien_bullets):
            self._ship_hit()
    
    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break 

    # ------Game state------
    def reset_round(self):
        """Reset the game state to start a new round after the ship is hit."""
        self.stats.ship_left -= 1
        self.scoreboard.prep_ships()
        self.bullets.empty()
        self.aliens.empty()

        self._create_fleet()
        self.ship.cente_ship()
        #Pause
        sleep(1)

    def reset_game(self):
        """Reset the game state to start a new game."""
        self.settings.initialize_dynamic_settings()
        self.stats.reset_stats()
        self.scoreboard.prep_images()

        self.game_active = True
        self.bullets.empty()
        self.aliens.empty()

        self._create_fleet()
        self.ship.cente_ship()

    def end_game(self): 
        """End the game and reset the game state."""
        self.stats.reset_stats()
        self.bullets.empty()
        self.aliens.empty()
        
        self.game_active = False

    # ------Drawing------
    def _update_screen(self):
        """Update images on the screen and flip to the new screen."""
        self.screen.fill(self.settings.background_color)      
        self.ship.draw()
        self.aliens.draw(self.screen)
        for bullet in self.bullets.sprites():
            bullet.draw()

        for bullet in self.alien_bullets.sprites():
            bullet.draw()

        self.scoreboard.show()

        if not self.game_active:
            self.play_button.draw()

        pygame.display.flip()  

if __name__ == '__main__':
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()    