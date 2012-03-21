import pyglet
import random
from pyglet.window import key

### Init
rnd = random.Random()

clk = pyglet.clock.Clock()

screen_width = 800
screen_height = 560

window = pyglet.window.Window(screen_width, screen_height)

world_width = 100
world_height = 100

sprite_size = 20

main_batch = pyglet.graphics.Batch()

screen_width_sprite = screen_width // sprite_size
screen_height_sprite = screen_height // sprite_size

pyglet.resource.path = ['../res']
pyglet.resource.reindex()

player_image = pyglet.resource.image('test-alien.png')
grass_image = pyglet.resource.image('grass.png')
alien_image = pyglet.resource.image('alien_neg.png')

all_sprites = []

def create_alien(dt=None, aliens=None, aliens_text=None,
                 all_sprites=all_sprites):
    y = rnd.randint(0,world_height)
    x = rnd.randint(0,world_width)
    aliens.append(pyglet.sprite.Sprite(img=alien_image,x=x*sprite_size, y=y*sprite_size, batch=main_batch))
    update_text(aliens_text, "Aliens: " + str(len(aliens)))


def update_text(textobject, new_text):
    textobject.text=new_text


#def get_tile(sprite):
#    y = sprite.y
#    x = sprite.x
#    y_tile = y//sprite_size
#    x_tile = x//sprite_size
#    tile = y * screen_width_sprite + x

#    return tile


#def collide(sprite, sprite_list):
#    tile1 = get_tile(sprite)
#    for i,v in enumerate(sprite_list):
#        tile2 = get_tile(v)
#        if tile1 == tile2:
#            return i,v

#    return None,None


def shift_left(sprite_list, steps=5):
    for sprite in sprite_list:
        sprite.x -= steps*sprite_size
        

def shift_right(sprite_list, steps=5):
    for sprite in sprite_list:
        sprite.x += steps*sprite_size


def shift_up(sprite_list, steps=5):
    for sprite in sprite_list:
        sprite.y += steps*sprite_size


def shift_down(sprite_list, steps=5):
    for sprite in sprite_list:
        sprite.y -= steps*sprite_size


grass_sprites = []
for i in range(world_width*world_height):
	y = i // world_width
	x = i % world_width
	grass_sprites.append(pyglet.sprite.Sprite(img=grass_image,x=x*sprite_size, y=y*sprite_size, batch=main_batch))


aliens_text = pyglet.text.Label(text="Aliens: 0", x=400, y=545, anchor_x='center')

aliens = []
for i in range(15):
    create_alien(aliens=aliens, aliens_text=aliens_text)


player = pyglet.sprite.Sprite(img=player_image,x=0,y=0,batch=main_batch)

all_sprites += grass_sprites
all_sprites.append(player)
all_sprites += aliens

fps_display = pyglet.clock.ClockDisplay(color=(0,0,1,1))

num_aliens = len(aliens)
aliens_text = pyglet.text.Label(text="Aliens: " + str(num_aliens), x=400, y=545, anchor_x='center')

@window.event
def on_draw():
    clk.tick()
    window.clear()
    main_batch.draw()
    aliens_text.draw()
    fps_display.draw()


@window.event
def on_key_press(symbol,modifier):
    if symbol == key.LEFT:
        shift_right(all_sprites,5)
    if symbol == key.UP:
        shift_down(all_sprites,5)
    if symbol == key.RIGHT:
        shift_left(all_sprites,5)
    if symbol == key.DOWN:
        shift_up(all_sprites,5)


if __name__ == '__main__':
	pyglet.app.run()
