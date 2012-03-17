import pyglet
import random
from pyglet.window import key

aliens_text = pyglet.text.Label(text="Aliens: 0", x=400, y=545, anchor_x='center')

def create_alien(dt=None, aliens=None):
    y = rnd.randint(0,screen_height)//sprite_size
    x = rnd.randint(0,screen_width)//sprite_size
    aliens.append(pyglet.sprite.Sprite(img=alien_image,x=x*sprite_size, y=y*sprite_size, batch=main_batch))
    aliens_text.text = "Aliens: " + str(len(aliens))

### Init

rnd = random.Random()

clk = pyglet.clock.Clock()

screen_width = 800
screen_height = 560

window = pyglet.window.Window(screen_width, screen_height)

sprite_size = 20

main_batch = pyglet.graphics.Batch()

screen_width_sprite = screen_width // sprite_size
screen_height_sprite = screen_height // sprite_size

pyglet.resource.path = ['../res']
pyglet.resource.reindex()

player_image = pyglet.resource.image('test-alien.png')
grass_image = pyglet.resource.image('grass.png')
alien_image = pyglet.resource.image('alien_neg.png')


grass_sprites = []
for i in range(screen_width_sprite*screen_height_sprite):
	y = i // screen_width_sprite
	x = i % screen_width_sprite
	grass_sprites.append(pyglet.sprite.Sprite(img=grass_image,x=x*sprite_size, y=y*sprite_size, batch=main_batch))

aliens = []
for i in range(5):
    create_alien(aliens=aliens)


player = pyglet.sprite.Sprite(img=player_image,x=0,y=0,batch=main_batch)

fps_display = pyglet.clock.ClockDisplay(color=(0,0,1,1))

#text = pyglet.text.Label(text="Village", x=400, y=545,
#                         anchor_x='center',batch=main_batch)

num_aliens = len(aliens)
aliens_text = pyglet.text.Label(text="Aliens: " + str(num_aliens), x=400, y=545, anchor_x='center')

def get_tile(sprite):
    y = sprite.y
    x = sprite.x
    y_tile = y//sprite_size
    x_tile = x//sprite_size
    tile = y * screen_width_sprite + x

    return tile


def collide(sprite, sprite_list):
    tile1 = get_tile(sprite)
    for i,v in enumerate(sprite_list):
        tile2 = get_tile(v)
        if tile1 == tile2:
            return i,v

    return None,None

    


@window.event
def on_draw():
    clk.tick()
    window.clear()
    main_batch.draw()
    aliens_text.draw()
    fps_display.draw()


@window.event
def on_key_press(symbol,modifier):
    if symbol == key.LEFT and player.x > 0:
        player.set_position(player.x-20,player.y)
    if symbol == key.UP and player.y < screen_height-sprite_size:
        player.set_position(player.x,player.y+20)
    if symbol == key.RIGHT and player.x < screen_width-sprite_size:
        player.set_position(player.x+20,player.y)
    if symbol == key.DOWN and player.y > 0:
        player.set_position(player.x,player.y-20)
    if symbol == key.SPACE:
        create_alien(aliens=aliens)

    (id, collision_sprite) = collide(player,aliens)
    if collision_sprite:
        del aliens[id]
        aliens_text.text = "Aliens: " + str(len(aliens))


def move_right(dt):
    if player.x < screen_width - sprite_size:
        player.set_position(player.x+sprite_size,player.y)

clk.schedule_interval(create_alien, 2, aliens)

if __name__ == '__main__':
	pyglet.app.run()
