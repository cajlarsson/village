import pyglet
from pyglet.window import key

clk = pyglet.clock.Clock()

screen_width = 800
screen_height = 600

window = pyglet.window.Window(screen_width, screen_height)

sprite_size = 20

main_batch = pyglet.graphics.Batch()

screen_width_sprite = screen_width // sprite_size
screen_height_sprite = screen_height // sprite_size

pyglet.resource.path = ['../res']
pyglet.resource.reindex()

player_image = pyglet.resource.image('test-alien.png')
grass_image = pyglet.resource.image('grass.png')

grass_sprites = []
for i in range(screen_width_sprite*screen_height_sprite):
	y = i // screen_width_sprite
	x = i % screen_width_sprite
	grass_sprites.append(pyglet.sprite.Sprite(img=grass_image,x=x*sprite_size, y=y*sprite_size, batch=main_batch))

player = pyglet.sprite.Sprite(img=player_image,x=400,y=300,batch=main_batch)

@window.event
def on_draw():
	window.clear()
	main_batch.draw()


@window.event
def on_key_press(symbol,modifier):
	if symbol == key.LEFT and player.x > 0:
		player.set_position(player.x-20,player.y)
	if symbol == key.UP and player.y < 580:
		player.set_position(player.x,player.y+20)
	if symbol == key.RIGHT and player.x < 780:
		player.set_position(player.x+20,player.y)
	if symbol == key.DOWN and player.y > 0:
		player.set_position(player.x,player.y-20)


if __name__ == '__main__':
	pyglet.app.run()
