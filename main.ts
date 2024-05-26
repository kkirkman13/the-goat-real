namespace SpriteKind {
    export const mom = SpriteKind.create()
    export const monkey = SpriteKind.create()
    export const thing = SpriteKind.create()
    export const otherthing = SpriteKind.create()
}
scene.onOverlapTile(SpriteKind.mom, assets.tile`myTile5`, function (sprite, location) {
    tiles.setCurrentTilemap(tilemap`level9`)
})
scene.onOverlapTile(SpriteKind.monkey, assets.tile`myTile10`, function (sprite4, location4) {
    tiles.setCurrentTilemap(tilemap`level3`)
})
controller.player3.onButtonEvent(ControllerButton.B, ControllerButtonEvent.Pressed, function () {
    upgraded_spit = sprites.createProjectileFromSprite(assets.image`spit`, upgraded_kiwi, 100, 0)
    upgraded_spit.setKind(SpriteKind.thing)
})
controller.player2.onButtonEvent(ControllerButton.B, ControllerButtonEvent.Pressed, function () {
    dart = sprites.createProjectileFromSprite(assets.image`dart`, bad_monkey, -100, 0)
    dart.setKind(SpriteKind.otherthing)
})
scene.onOverlapTile(SpriteKind.mom, assets.tile`myTile6`, function (sprite52, location52) {
    tiles.setCurrentTilemap(tilemap`level11`)
})
sprites.onOverlap(SpriteKind.thing, SpriteKind.monkey, function (sprite8, otherSprite2) {
    game.gameOver(false)
})
scene.onOverlapTile(SpriteKind.monkey, assets.tile`myTile0`, function (sprite22, location22) {
    tiles.setCurrentTilemap(tilemap`level5`)
    sprites.destroy(bad_monkey, effects.none, 100)
    upgraded_bad_monkey = sprites.create(assets.image`monkey3`, SpriteKind.Player)
    controller.player4.moveSprite(upgraded_bad_monkey, 100, 0)
    upgraded_bad_monkey.ay = 500
    tiles.placeOnRandomTile(upgraded_bad_monkey, sprites.swamp.swampTile0)
})
controller.player2.onButtonEvent(ControllerButton.A, ControllerButtonEvent.Pressed, function () {
    bad_monkey.vy = -300
})
scene.onOverlapTile(SpriteKind.mom, assets.tile`myTile4`, function (sprite23, location23) {
    tiles.setCurrentTilemap(tilemap`level7`)
})
scene.onOverlapTile(SpriteKind.mom, assets.tile`myTile1`, function (sprite42, location42) {
    tiles.setCurrentTilemap(tilemap`level3`)
})
controller.player3.onEvent(ControllerEvent.Connected, function () {
    scene.cameraFollowSprite(upgraded_kiwi)
})
controller.player3.onButtonEvent(ControllerButton.Right, ControllerButtonEvent.Pressed, function () {
    upgraded_kiwi.setImage(assets.image`kiwi2`)
})
scene.onOverlapTile(SpriteKind.mom, assets.tile`myTile3`, function (sprite3, location3) {
    tiles.setCurrentTilemap(tilemap`level0`)
})
scene.onOverlapTile(SpriteKind.monkey, assets.tile`myTile7`, function (sprite2, location2) {
    tiles.setCurrentTilemap(tilemap`level7`)
})
scene.onOverlapTile(SpriteKind.monkey, assets.tile`myTile2`, function (sprite32, location32) {
    tiles.setCurrentTilemap(tilemap`level0`)
})
controller.player2.onButtonEvent(ControllerButton.Right, ControllerButtonEvent.Pressed, function () {
    bad_monkey.setImage(assets.image`monkey0`)
})
scene.onOverlapTile(SpriteKind.monkey, assets.tile`myTile9`, function (sprite53, location53) {
    tiles.setCurrentTilemap(tilemap`level11`)
})
controller.player4.onButtonEvent(ControllerButton.A, ControllerButtonEvent.Pressed, function () {
    upgraded_bad_monkey.vy = -300
})
controller.player2.onButtonEvent(ControllerButton.Left, ControllerButtonEvent.Pressed, function () {
    bad_monkey.setImage(assets.image`monkey`)
})
controller.player1.onButtonEvent(ControllerButton.Right, ControllerButtonEvent.Pressed, function () {
    kiwi.setImage(assets.image`kiwi`)
})
controller.player1.onButtonEvent(ControllerButton.A, ControllerButtonEvent.Pressed, function () {
    kiwi.vy = -300
})
sprites.onOverlap(SpriteKind.otherthing, SpriteKind.mom, function (sprite7, otherSprite) {
    game.gameOver(true)
})
controller.player4.onButtonEvent(ControllerButton.Left, ControllerButtonEvent.Pressed, function () {
    upgraded_bad_monkey.setImage(assets.image`monkey3`)
})
scene.onOverlapTile(SpriteKind.monkey, assets.tile`myTile8`, function (sprite5, location5) {
    tiles.setCurrentTilemap(tilemap`level9`)
})
controller.player3.onButtonEvent(ControllerButton.A, ControllerButtonEvent.Pressed, function () {
    upgraded_kiwi.vy = -300
})
controller.player1.onButtonEvent(ControllerButton.B, ControllerButtonEvent.Pressed, function () {
    spit = sprites.createProjectileFromSprite(assets.image`he`, kiwi, 100, 0)
    spit.setKind(SpriteKind.thing)
})
scene.onOverlapTile(SpriteKind.mom, assets.tile`myTile`, function (sprite6, location6) {
    tiles.setCurrentTilemap(tilemap`level19`)
    sprites.destroy(kiwi, effects.none, 100)
    upgraded_kiwi = sprites.create(assets.image`kiwi2`, SpriteKind.Player)
    controller.player3.moveSprite(upgraded_kiwi, 100, 0)
    upgraded_kiwi.ay = 500
    tiles.placeOnRandomTile(upgraded_kiwi, sprites.swamp.swampTile0)
})
controller.player4.onButtonEvent(ControllerButton.Right, ControllerButtonEvent.Pressed, function () {
    upgraded_bad_monkey.setImage(assets.image`monkey1`)
})
controller.player3.onButtonEvent(ControllerButton.Left, ControllerButtonEvent.Pressed, function () {
    upgraded_kiwi.setImage(assets.image`kiwi0`)
})
controller.player1.onButtonEvent(ControllerButton.Left, ControllerButtonEvent.Pressed, function () {
    kiwi.setImage(assets.image`kiwi1`)
})
let spit: Sprite = null
let upgraded_bad_monkey: Sprite = null
let dart: Sprite = null
let upgraded_kiwi: Sprite = null
let upgraded_spit: Sprite = null
let kiwi: Sprite = null
let bad_monkey: Sprite = null
tiles.placeOnRandomTile(bad_monkey, sprites.swamp.swampTile2)
tiles.placeOnRandomTile(kiwi, sprites.swamp.swampTile2)
scene.cameraFollowSprite(kiwi)
tiles.setCurrentTilemap(tilemap`level2`)
scene.setBackgroundImage(assets.image`forest`)
kiwi = sprites.create(assets.image`kiwi`, SpriteKind.mom)
bad_monkey = sprites.create(assets.image`monkey`, SpriteKind.monkey)
bad_monkey.setPosition(143, 99)
controller.player2.moveSprite(bad_monkey, 100, 0)
controller.player1.moveSprite(kiwi, 100, 0)
game.setGameOverMessage(false, "KO!!!! Kiwis Win!!!")
game.setGameOverMessage(true, "KO!!!! Monkeys Win!!!")
tiles.placeOnRandomTile(kiwi, sprites.swamp.swampTile3)
tiles.placeOnRandomTile(bad_monkey, sprites.swamp.swampTile2)
scene.cameraFollowSprite(kiwi)
forever(function () {
    kiwi.ay = 500
    bad_monkey.ay = 500
})
