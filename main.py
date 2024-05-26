@namespace
class SpriteKind:
    mom = SpriteKind.create()
    monkey = SpriteKind.create()
    thing = SpriteKind.create()
    otherthing = SpriteKind.create()

def on_overlap_tile(sprite, location):
    tiles.set_current_tilemap(tilemap("""
        level9
    """))
scene.on_overlap_tile(SpriteKind.mom,
    assets.tile("""
        myTile5
    """),
    on_overlap_tile)

def on_overlap_tile2(sprite4, location4):
    tiles.set_current_tilemap(tilemap("""
        level3
    """))
scene.on_overlap_tile(SpriteKind.monkey,
    assets.tile("""
        myTile10
    """),
    on_overlap_tile2)

def on_player3_button_b_pressed():
    global upgraded_spit
    upgraded_spit = sprites.create_projectile_from_sprite(assets.image("""
        spit
    """), upgraded_kiwi, 100, 0)
    upgraded_spit.set_kind(SpriteKind.thing)
controller.player3.on_button_event(ControllerButton.B,
    ControllerButtonEvent.PRESSED,
    on_player3_button_b_pressed)

def on_player2_button_b_pressed():
    global dart
    dart = sprites.create_projectile_from_sprite(assets.image("""
        dart
    """), bad_monkey, -100, 0)
    dart.set_kind(SpriteKind.otherthing)
controller.player2.on_button_event(ControllerButton.B,
    ControllerButtonEvent.PRESSED,
    on_player2_button_b_pressed)

def on_on_overlap(sprite8, otherSprite2):
    game.game_over(False)
sprites.on_overlap(SpriteKind.thing, SpriteKind.monkey, on_on_overlap)

def on_overlap_tile3(sprite22, location22):
    global upgraded_bad_monkey
    tiles.set_current_tilemap(tilemap("""
        level5
    """))
    sprites.destroy(bad_monkey, effects.none, 100)
    upgraded_bad_monkey = sprites.create(assets.image("""
        monkey3
    """), SpriteKind.player)
    controller.player4.move_sprite(upgraded_bad_monkey, 100, 0)
    upgraded_bad_monkey.ay = 500
    tiles.place_on_random_tile(upgraded_bad_monkey, sprites.swamp.swamp_tile0)
scene.on_overlap_tile(SpriteKind.monkey,
    assets.tile("""
        myTile0
    """),
    on_overlap_tile3)

def on_player2_button_a_pressed():
    bad_monkey.vy = -300
controller.player2.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player2_button_a_pressed)

def on_player3_connected():
    scene.camera_follow_sprite(upgraded_kiwi)
controller.player3.on_event(ControllerEvent.CONNECTED, on_player3_connected)

def on_player3_button_right_pressed():
    upgraded_kiwi.set_image(assets.image("""
        kiwi2
    """))
controller.player3.on_button_event(ControllerButton.RIGHT,
    ControllerButtonEvent.PRESSED,
    on_player3_button_right_pressed)

def on_overlap_tile4(sprite42, location42):
    tiles.set_current_tilemap(tilemap("""
        level3
    """))
scene.on_overlap_tile(SpriteKind.mom,
    assets.tile("""
        myTile1
    """),
    on_overlap_tile4)

def on_overlap_tile5(sprite3, location3):
    tiles.set_current_tilemap(tilemap("""
        level0
    """))
scene.on_overlap_tile(SpriteKind.mom,
    assets.tile("""
        myTile3
    """),
    on_overlap_tile5)

def on_overlap_tile6(sprite2, location2):
    tiles.set_current_tilemap(tilemap("""
        level7
    """))
scene.on_overlap_tile(SpriteKind.monkey,
    assets.tile("""
        myTile7
    """),
    on_overlap_tile6)

def on_player2_button_right_pressed():
    bad_monkey.set_image(assets.image("""
        monkey0
    """))
controller.player2.on_button_event(ControllerButton.RIGHT,
    ControllerButtonEvent.PRESSED,
    on_player2_button_right_pressed)

def on_overlap_tile7(sprite5, location5):
    tiles.set_current_tilemap(tilemap("""
        level9
    """))
scene.on_overlap_tile(SpriteKind.monkey,
    assets.tile("""
        myTile8
    """),
    on_overlap_tile7)

def on_overlap_tile8(sprite52, location52):
    tiles.set_current_tilemap(tilemap("""
        level11
    """))
scene.on_overlap_tile(SpriteKind.mom,
    assets.tile("""
        myTile6
    """),
    on_overlap_tile8)

def on_player4_button_a_pressed():
    upgraded_bad_monkey.vy = -300
controller.player4.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player4_button_a_pressed)

def on_player2_button_left_pressed():
    bad_monkey.set_image(assets.image("""
        monkey
    """))
controller.player2.on_button_event(ControllerButton.LEFT,
    ControllerButtonEvent.PRESSED,
    on_player2_button_left_pressed)

def on_player1_button_right_pressed():
    kiwi.set_image(assets.image("""
        kiwi
    """))
controller.player1.on_button_event(ControllerButton.RIGHT,
    ControllerButtonEvent.PRESSED,
    on_player1_button_right_pressed)

def on_player1_button_a_pressed():
    kiwi.vy = -300
controller.player1.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player1_button_a_pressed)

def on_overlap_tile9(sprite23, location23):
    tiles.set_current_tilemap(tilemap("""
        level7
    """))
scene.on_overlap_tile(SpriteKind.mom,
    assets.tile("""
        myTile4
    """),
    on_overlap_tile9)

def on_on_overlap2(sprite7, otherSprite):
    info.player1.change_life_by(-5)
sprites.on_overlap(SpriteKind.otherthing, SpriteKind.mom, on_on_overlap2)

def on_player4_button_left_pressed():
    upgraded_bad_monkey.set_image(assets.image("""
        monkey3
    """))
controller.player4.on_button_event(ControllerButton.LEFT,
    ControllerButtonEvent.PRESSED,
    on_player4_button_left_pressed)

def on_overlap_tile10(sprite32, location32):
    tiles.set_current_tilemap(tilemap("""
        level0
    """))
scene.on_overlap_tile(SpriteKind.monkey,
    assets.tile("""
        myTile2
    """),
    on_overlap_tile10)

def on_player1_life_zero():
    game.game_over(True)
info.player1.on_life_zero(on_player1_life_zero)

def on_player3_button_a_pressed():
    upgraded_kiwi.vy = -300
controller.player3.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player3_button_a_pressed)

def on_overlap_tile11(sprite53, location53):
    tiles.set_current_tilemap(tilemap("""
        level11
    """))
scene.on_overlap_tile(SpriteKind.monkey,
    assets.tile("""
        myTile9
    """),
    on_overlap_tile11)

def on_player1_button_b_pressed():
    global spit
    spit = sprites.create_projectile_from_sprite(assets.image("""
        he
    """), kiwi, 100, 0)
    spit.set_kind(SpriteKind.thing)
controller.player1.on_button_event(ControllerButton.B,
    ControllerButtonEvent.PRESSED,
    on_player1_button_b_pressed)

def on_overlap_tile12(sprite6, location6):
    global upgraded_kiwi
    tiles.set_current_tilemap(tilemap("""
        level19
    """))
    sprites.destroy(kiwi, effects.none, 100)
    upgraded_kiwi = sprites.create(assets.image("""
        kiwi2
    """), SpriteKind.player)
    controller.player3.move_sprite(upgraded_kiwi, 100, 0)
    upgraded_kiwi.ay = 500
    tiles.place_on_random_tile(upgraded_kiwi, sprites.swamp.swamp_tile0)
scene.on_overlap_tile(SpriteKind.mom,
    assets.tile("""
        myTile
    """),
    on_overlap_tile12)

def on_player4_button_right_pressed():
    upgraded_bad_monkey.set_image(assets.image("""
        monkey1
    """))
controller.player4.on_button_event(ControllerButton.RIGHT,
    ControllerButtonEvent.PRESSED,
    on_player4_button_right_pressed)

def on_player3_button_left_pressed():
    upgraded_kiwi.set_image(assets.image("""
        kiwi0
    """))
controller.player3.on_button_event(ControllerButton.LEFT,
    ControllerButtonEvent.PRESSED,
    on_player3_button_left_pressed)

def on_player1_button_left_pressed():
    kiwi.set_image(assets.image("""kiwi1"""))
controller.player1.on_button_event(ControllerButton.LEFT,
    ControllerButtonEvent.PRESSED,
    on_player1_button_left_pressed)

spit: Sprite = None
upgraded_bad_monkey: Sprite = None
dart: Sprite = None
upgraded_kiwi: Sprite = None
upgraded_spit: Sprite = None
kiwi: Sprite = None
bad_monkey: Sprite = None
tiles.place_on_random_tile(bad_monkey, sprites.swamp.swamp_tile2)
tiles.place_on_random_tile(kiwi, sprites.swamp.swamp_tile2)
scene.camera_follow_sprite(kiwi)
tiles.set_current_tilemap(tilemap("""
    level2
"""))
scene.set_background_image(assets.image("""
    forest
"""))
kiwi = sprites.create(assets.image("""
    kiwi
"""), SpriteKind.mom)
bad_monkey = sprites.create(assets.image("""
    monkey
"""), SpriteKind.monkey)
bad_monkey.set_position(143, 99)
controller.player2.move_sprite(bad_monkey, 100, 0)
controller.player1.move_sprite(kiwi, 100, 0)
game.set_game_over_message(False, "KO!!!! Kiwi Win!!!")
game.set_game_over_message(True, "KO!!!! Monkey Win!!!")
tiles.place_on_random_tile(kiwi, sprites.swamp.swamp_tile3)
tiles.place_on_random_tile(bad_monkey, sprites.swamp.swamp_tile2)
scene.camera_follow_sprite(kiwi)

def on_forever():
    kiwi.ay = 500
    bad_monkey.ay = 500
    info.player2.set_life(5)
    info.player1.set_life(5)
    info.player3.set_life(5)
    info.player4.set_life(5)
forever(on_forever)
