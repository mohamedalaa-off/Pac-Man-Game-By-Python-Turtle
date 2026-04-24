import turtle
import random
import winsound
from constants import SCREEN_HIGHT, SCREEN_WIDTH, CELL_SIZE, ENEMY_NUMBER
from renderer import Wall, Pellet, PowerPellet, UIPen
from actors import Player, Enemy
def init_screen():
    screen = turtle.Screen()
    screen.tracer(0)
    screen.title("Pac-Man Game")
    screen.setup(SCREEN_WIDTH + 10, SCREEN_HIGHT + 10)
    screen.bgcolor("black")
    return screen
def bind_controls(screen, player):
    screen.listen()
    keys = {
        'd' : player.turn_right,
        'D' : player.turn_right,
        'a' : player.turn_left,
        'A' : player.turn_left,
        'w' : player.turn_up,
        'W' : player.turn_up,
        's' : player.turn_down,
        'S' : player.turn_down
    }
    for key, func in keys.items():
        screen.onkeypress(func, key)
def game_loop(screen, player,  score_pen, lives_pen, pellet_pen, power_pellet_pen, player_start_x, player_start_y, enemies):
    
    score_pen.write_score(player.score, player.lives, pellet_pen.stamps, power_pellet_pen.stamps)
    lives_pen.write_lives(player.lives, pellet_pen.stamps, power_pellet_pen.stamps)
    
    for (px, py), stamp_id in list(pellet_pen.stamps.items()):
        if player.distance(px, py) < CELL_SIZE / 2 and (px , py) != (player_start_x, player_start_y):
            pellet_pen.clearstamp(stamp_id)
            del pellet_pen.stamps[(px, py)]
            player.score += 5
        elif player.distance(px, py) < CELL_SIZE / 2 and (px , py) == (player_start_x, player_start_y):
            pellet_pen.clearstamp(stamp_id)
            del pellet_pen.stamps[(px, py)]
    for (px, py), stamp_id in list(power_pellet_pen.stamps.items()):
        if player.distance(px, py) < CELL_SIZE / 2:
            winsound.PlaySound(r"E:\GitHub Projects\New\Pac-Man-Game-By-Python-Turtle\assets\pacman_eatfruit.wav", winsound.SND_ASYNC)
            power_pellet_pen.clearstamp(stamp_id)
            del power_pellet_pen.stamps[(px, py)]
            player.score += 50
            player.move_speed += 2
            screen.ontimer(player.reset_speed, 3000)
    # Update Player
    player.move()
    player.check_wall_collision()
    # Update Enemies
    for enemy in enemies:
        enemy.move()
        enemy.check_wall_collision()
        enemy.go_after_player()
        # Collision: player-enemy
        if enemy.distance(player) < CELL_SIZE / 2:
            winsound.PlaySound(r"E:\GitHub Projects\New\Pac-Man-Game-By-Python-Turtle\assets\death.wav", winsound.SND_ASYNC)
            safe_spot = []
            for pellet in pellet_pen.pellets:
                if all(enemy.distance(pellet) > CELL_SIZE * 5 for enemy in enemies):
                    safe_spot.append(pellet)
            player.goto(random.choice(safe_spot))
            player.lives -= 1
    
    # Win game - stop everything and close the game
    if len(power_pellet_pen.stamps) == 0 and len(pellet_pen.stamps) == 0:
        player.state = "stop"
        for enemy in enemies:
            enemy.hideturtle()
            enemy.state = "stop"
        screen.ontimer(screen.bye, 3000)
    # Game over - stop everything and close the game
    if player.lives == 0:
        player.state = "stop"
        player.hideturtle()
        for enemy in enemies:
            enemy.state = "stop"
        screen.ontimer(screen.bye, 3000)
    screen.update()
    screen.ontimer(lambda: game_loop(
        screen, 
        player,
        score_pen,
        lives_pen,
        pellet_pen,
        power_pellet_pen, 
        player_start_x,
        player_start_y,
        enemies
        ),
    1000 // 60
)
def main():
    screen = init_screen()
    screen.register_shape(r"E:\GitHub Projects\New\Pac-Man-Game-By-Python-Turtle\assets\pac.gif")
    screen.register_shape(r"E:\GitHub Projects\New\Pac-Man-Game-By-Python-Turtle\assets\up.gif")
    screen.register_shape(r"E:\GitHub Projects\New\Pac-Man-Game-By-Python-Turtle\assets\down.gif")
    screen.register_shape(r"E:\GitHub Projects\New\Pac-Man-Game-By-Python-Turtle\assets\left.gif")
    screen.register_shape(r"E:\GitHub Projects\New\Pac-Man-Game-By-Python-Turtle\assets\right.gif")
    screen.register_shape(r"E:\GitHub Projects\New\Pac-Man-Game-By-Python-Turtle\assets\green_enemy.gif")
    screen.register_shape(r"E:\GitHub Projects\New\Pac-Man-Game-By-Python-Turtle\assets\pink_enemy.gif")
    screen.register_shape(r"E:\GitHub Projects\New\Pac-Man-Game-By-Python-Turtle\assets\red_enemy.gif")
    screen.register_shape(r"E:\GitHub Projects\New\Pac-Man-Game-By-Python-Turtle\assets\wall.gif")
    wall_pen = Wall()
    pellet_pen = Pellet()
    power_pellet_pen = PowerPellet()
    ui_pen = UIPen()
    score_pen = UIPen()
    lives_pen = UIPen()
    wall_pen.draw()
    pellet_pen.draw()
    power_pellet_pen.draw()
    ui_pen.draw_ui_area()
    player_state_coor = random.choice(pellet_pen.pellets)
    player_start_x = player_state_coor[0]
    player_start_y = player_state_coor[1]
    player = Player(wall_pen.walls)
    player.goto(player_start_x, player_start_y)
    enemies = []
    enemy_colors = [r"E:\GitHub Projects\New\Pac-Man-Game-By-Python-Turtle\assets\green_enemy.gif",
                    r"E:\GitHub Projects\New\Pac-Man-Game-By-Python-Turtle\assets\pink_enemy.gif",
                    r"E:\GitHub Projects\New\Pac-Man-Game-By-Python-Turtle\assets\red_enemy.gif"]    
    for _ in range(ENEMY_NUMBER):
        safe_spot = []
        for pellet in pellet_pen.pellets:
            if player.distance(pellet) > CELL_SIZE * 5:
                safe_spot.append(pellet)
        enemy_start_x, enemy_start_y = random.choice(safe_spot)
        enemy = Enemy(enemy_start_x, enemy_start_y, wall_pen.walls, player)
        enemy.shape(random.choice(enemy_colors))
        enemies.append(enemy)
    winsound.PlaySound(r"E:\GitHub Projects\New\Pac-Man-Game-By-Python-Turtle\assets\pacman_beginning.wav", winsound.SND_ASYNC)
    screen.ontimer(lambda: bind_controls(screen, player), 4000)
    for enemy in enemies:
        screen.ontimer(enemy.start_move, 4000)
    game_loop(screen, player, score_pen, lives_pen, pellet_pen, power_pellet_pen , player_start_x,
            player_start_y, enemies)
    screen.mainloop()
if __name__ == "__main__":
    main()