import Global
from ServerCharacter import *
from ServerGame import *
from ServerPlayer import *

class Server:
    def __init__(self):
        self.inputManagers = []
        
        self.player = ServerPlayer(1)
        self.players = {
            self.player.uid: self.player
        }

        self.game = ServerGame(1)
        self.games = [self.game]
        
        self.character = ServerCharacter(self.game, 1, [400.0,400.0])
        self.dummy = ServerCharacter(self.game, 2, [300.0,300.0])
        self.characters = {
            self.character.uid: self.character,
            self.dummy.uid: self.dummy
        }

        self.associatePlayer(self.player, self.game, self.character)
        self.associateGame(self.game, self.characters)

        self.running = True

    def associatePlayer(self, player, game, character):
        player.character = character
        player.game = game
        
    def associateGame(self, game, characters):
        game.characters = characters
        for charID, character in characters.items():
            character.game = game
        Global.gameState = GameState(characters)
        game.gameState = Global.gameState

    def run(self):
        # while self.running:
            self.inputManagers = []
            
            # TODO: Do this via network queue
            self.inputManagers += [Global.inputManager]

            self.updateInput()
        
            for game in self.games:
                game.run()

    def updateInput(self):
        for inputManager in self.inputManagers:
            player = self.players[inputManager.playerID]
            player.character.update(inputManager)
