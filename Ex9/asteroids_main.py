from screen import Screen
import sys
from ship import *
from asteroid import *
from torpedo import *
import random

LIFE = 3
DEFAULT_ASTEROIDS_NUM = 5
NUM_OF_ARGUMENTS = 1
REMOVE_LIFE_TITLE = "BANG! You just lost a life!"
REMOVE_LIFE_MSG = "Try to fly more carefully. We can't guarantee that " \
                  "Heaven exists..."
ACCELERATION_FACTOR = 2
TORPEDO_LIMIT = 15
TWENTY_POINTS = 20
FIFTY_POINTS = 50
ONE_HUNDRED_POINTS = 100
MSG_TITLE_ASTROIDS_DESTROYED = "You won!"
MSG_ASTROIDS_DESTROYED = "You saved the world from being destroyed by " \
                         "asteroids. Way to go!"
MSG_TITLE_SHIP_DIED = "You lost :( "
MSG_SHIP_DIED = "There's less of a chance of you becoming a millonaire than" \
                " there is of getting hit on the head by a passing " \
                "asteroid. " \
                "BUT, you were hit by THREE asteorids, so you just " \
                "increased your chance of winning the lottery by THREE!"
MSG_TITLE_QUIT = "Are you sure you want to leave?"
MSG_QUIT = "Thank you for flying by! We hope you come back and play \
            again soon!"


def random_location():
    """This function generates a random number according
    to the boundries of the screen."""
    x = random.randint(Screen.SCREEN_MIN_X, Screen.SCREEN_MAX_X)
    y = random.randint(Screen.SCREEN_MIN_Y, Screen.SCREEN_MAX_Y)
    return x, y


class GameRunner:
    """GameRunner is the main class that runs the game. It initializing the
    objects in the game, and includes all the function that control actions
    that happen on the board, (as opposed to actions related to specific
    objects), such as movement, managing crashes, drawing the shapes of the
    objects, and the game loop."""

    def __init__(self, asteroids_amnt):
        """This function initializes the score, the ship, the torpedo list, and
        the asteroids (based on the input of how many asteroids there are in
        the game."""

        self.__score = 0

        self.screen_max_x = Screen.SCREEN_MAX_X
        self.screen_max_y = Screen.SCREEN_MAX_Y
        self.screen_min_x = Screen.SCREEN_MIN_X
        self.screen_min_y = Screen.SCREEN_MIN_Y
        self.__screen = Screen()

        self.torpedo_list = []

        self.asteroid_list = []
        asteroids_amnt = self.check_asteroid_amnt(asteroids_amnt)
        for i in range(asteroids_amnt):
            self._asteroid = Asteroid(random_location()[0],
                                      random_location()[1],
                                      random.randint(-5, 5),
                                      random.randint(-5, 5))
            self.__screen.register_asteroid(self._asteroid, 3)
            self.asteroid_list.append(self._asteroid)

        self.__ship = self.create_ship()
        self.__ship_life = LIFE

    def check_asteroid_amnt(self, asteroids_amnt):
        """This function checks if the user entered a number of asteroids and
        returns the starting number of asteroids that will be in the game."""
        if len(sys.argv) == NUM_OF_ARGUMENTS + 1:
            asteroids_amnt = int(sys.argv[1])
        else:
            asteroids_amnt = DEFAULT_ASTEROIDS_NUM
        return asteroids_amnt

    def create_ship(self):
        """This function creates a ship and makes sure the ship is not in
        the location of an asteroid."""
        potential_ship = Ship(random_location()[0], random_location()[1])
        for asteroid in self.asteroid_list:
            while (asteroid.get_cord_x() != potential_ship.get_cord_x()) and (
                        asteroid.get_cord_y() != potential_ship.get_cord_y()):
                return potential_ship

    def change_location(self, x, y, speed_x, speed_y):
        """This function receives the old location of an object,and returns a
        new location."""
        delta_x = Screen.SCREEN_MAX_X - Screen.SCREEN_MIN_X
        delta_y = Screen.SCREEN_MAX_Y - Screen.SCREEN_MIN_Y
        new_cord_x = (speed_x + x - Screen.SCREEN_MIN_X) % \
                     delta_x + Screen.SCREEN_MIN_X
        new_cord_y = (speed_y + y - Screen.SCREEN_MIN_Y) % \
                     delta_y + Screen.SCREEN_MIN_Y
        return new_cord_x, new_cord_y

    def draw_ship(self):
        """This function draws out the ship and moves it (by calling
        the change_location function) according to the keys that are pressed
        by the user."""
        self.__screen.draw_ship(self.__ship.get_cord_x(),
                                self.__ship.get_cord_y(),
                                self.__ship.get_heading())
        if self.__screen.is_left_pressed():
            self.__ship.turn_right()
        if self.__screen.is_right_pressed():
            self.__ship.turn_left()
        if self.__screen.is_up_pressed():
            self.__ship.accelerate()
        new_cord_x, new_cord_y = self.change_location(self.__ship.get_cord_x(),
                    self.__ship.get_cord_y(),self.__ship.get_speed_x(),
                    self.__ship.get_speed_y())
        self.__ship.set_cord_x(new_cord_x)
        self.__ship.set_cord_y(new_cord_y)

    def draw_asteroids(self):
        """This function iterates over the asteroid list and draws the
        asteroids as they move by calling the change_location function."""
        for asteroid in self.asteroid_list:
            self.__screen.draw_asteroid(asteroid, asteroid.get_cord_x(),
                                        asteroid.get_cord_y())
            new_cord_x, new_cord_y = self.change_location(
                asteroid.get_cord_x(),
                asteroid.get_cord_y(),
                asteroid.get_speed_x(),
                asteroid.get_speed_y())
            asteroid.set_cord_x(new_cord_x)
            asteroid.set_cord_y(new_cord_y)

    def crash_ship_asteroid(self):
        """This function checks if the ship crashed into an asteroid. If it
        did, it reduces the ship's life is reduced by one."""
        for asteroid in self.asteroid_list:
            if asteroid.has_intersection(self.__ship):
                self.__screen.remove_life()
                self.__ship_life -= 1
                self.__screen.show_message(REMOVE_LIFE_TITLE, REMOVE_LIFE_MSG)
                self.__screen.unregister_asteroid(asteroid)
                self.asteroid_list.remove(asteroid)

    def crash_asteroid_torpedo(self):
        """This function manages the actions that occur if a torpedo hit an
        asteroid. These include updating the score, splitting the asteroid,
        and removing the torpedo. Each of these actions iscarried out
        by other functions that are called inside this function."""
        for asteroid in self.asteroid_list:
            for torpedo in self.torpedo_list:
                if asteroid.has_intersection(torpedo):
                    self.update_score(asteroid.get_size())
                    self.split_asteroid(asteroid, torpedo)
                    self.__screen.unregister_torpedo(torpedo)
                    self.torpedo_list.remove(torpedo)
                    return True

    def create_torpedo(self):
        """This function creates, registers, and appends to the torpedo_list
        a new torpedo."""
        angle = math.radians(self.__ship.get_heading())
        new_speed_x = self.__ship.get_speed_x() + \
                      ACCELERATION_FACTOR * math.cos(angle)
        new_speed_y = self.__ship.get_speed_y() + \
                      ACCELERATION_FACTOR * math.sin(angle)
        new_torpedo = Torpedo(self.__ship.get_cord_x(),
                              self.__ship.get_cord_y(), new_speed_x,
                              new_speed_y, self.__ship.get_heading())
        self.torpedo_list.append(new_torpedo)
        self.__screen.register_torpedo(new_torpedo)

    def draw_torpedo(self):
        """This function draws and moves the torpedos on the screen by calling
        the change_location function."""
        for torpedo in self.torpedo_list:
            self.__screen.draw_torpedo(torpedo, torpedo.get_cord_x(),
                                    torpedo.get_cord_y(),torpedo.get_heading())
            new_cord_x, new_cord_y = self.change_location(torpedo.get_cord_x(),
                                    torpedo.get_cord_y(),torpedo.get_speed_x(),
                                    torpedo.get_speed_y())
            torpedo.set_cord_x(new_cord_x)
            torpedo.set_cord_y(new_cord_y)

    def update_score(self, size):
        """This function updates the player's score whenever a torpedo hits
        an asteroid. The score is determined based upon the size of the
        asteroid that was hit."""
        if size == 3:
            self.__score += TWENTY_POINTS
        elif size == 2:
            self.__score += FIFTY_POINTS
        elif size == 1:
            self.__score += ONE_HUNDRED_POINTS

    def split_asteroid(self, asteroid, torpedo):
        """This function splits an asteroid (if it's size was either 2 or
        3) if it was hit by a torpedo, and creates two new smaller asteroids in
        it's place moving in opposite directions. In addition it removes the
        asteroid that was hit from the asteroid list and unregisters it. If
        the asteroid was already size 1, it disappears, and no new asteroids
        are created."""
        if asteroid.get_size() > 1:
            new_speed_x = (torpedo.get_speed_x() + asteroid.get_speed_x()) / \
                          (math.sqrt(((asteroid.get_speed_x()) ** 2) +
                                     (asteroid.get_speed_y()) ** 2))
            new_speed_y = (torpedo.get_speed_y() + asteroid.get_speed_y()) / \
                          (math.sqrt(((asteroid.get_speed_x()) ** 2) +
                                     (asteroid.get_speed_y()) ** 2))

            new_asteroid1 = Asteroid(asteroid.get_cord_x(),
                                     asteroid.get_cord_y(), new_speed_x,
                                     new_speed_y, asteroid.get_size() - 1)
            self.asteroid_list.append(new_asteroid1)
            self.__screen.register_asteroid(new_asteroid1,
                                            asteroid.get_size() - 1)

            new_asteroid2 = Asteroid(asteroid.get_cord_x(),
                                     asteroid.get_cord_y(), -new_speed_x,
                                     -new_speed_y, asteroid.get_size() - 1)
            self.asteroid_list.append(new_asteroid2)
            self.__screen.register_asteroid(new_asteroid2,
                                            asteroid.get_size() - 1)

        self.__screen.unregister_asteroid(asteroid)
        self.asteroid_list.remove(asteroid)

    def torpedo_life_time(self):
        """This function reduces the torpedoe's life spam (starting at 200)
        every loop of the game. Once the life spam reaches 0, the torpedo
        is removed from the torpedo list and unregistered."""
        for torpedo in self.torpedo_list:
            if torpedo.get_life_time() >= 1:
                torpedo.set_life_time(torpedo.get_life_time() - 1)
            else:
                self.__screen.unregister_torpedo(torpedo)
                self.torpedo_list.remove(torpedo)

    def torpedo_limit(self):
        """This function returns the number of torpedos that are currently in
        the game, by measuring the length of the torpedo list."""
        torpedo_num = len(self.torpedo_list)
        return torpedo_num

    def end_of_game(self):
        """This function checks if the game should end, and returns True if
        any of the three cases occur: All asteroids were destroyed, the ship
        ran out of lives, or the user requests to quit the game."""
        if len(self.asteroid_list) == 0:
            self.__screen.show_message(MSG_TITLE_ASTROIDS_DESTROYED,
                                       MSG_ASTROIDS_DESTROYED)
            return True
        elif self.__ship_life == 0:
            self.__screen.show_message(MSG_TITLE_SHIP_DIED, MSG_SHIP_DIED)
            return True
        elif self.__screen.should_end():
            self.__screen.show_message(MSG_TITLE_QUIT, MSG_QUIT)
            return True
        return False

    def _game_loop(self):
        """This function is looped through again and again throughout the
        game. Each loop it calls the functions below which draw out the
        objects, check if objects crashed, releases torpedoes, updates the
        score, and checks if the game should be over."""
        self.draw_asteroids()
        self.draw_ship()
        self.crash_ship_asteroid()
        if self.__screen.is_space_pressed() and \
                        self.torpedo_limit() < TORPEDO_LIMIT:
            self.create_torpedo()
        self.draw_torpedo()
        self.__screen.set_score(self.__score)
        self.crash_asteroid_torpedo()
        self.torpedo_life_time()
        if self.end_of_game():
            self.__screen.end_game()
            sys.exit()

    def run(self):
        self._do_loop()
        self.__screen.start_screen()

    def _do_loop(self):
        # You don't need to change this method!
        self._game_loop()

        # Set the timer to go off again
        self.__screen.update()
        self.__screen.ontimer(self._do_loop, 5)


def main(amnt):
    runner = GameRunner(amnt)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
