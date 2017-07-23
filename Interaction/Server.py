import Global
from ServerCharacter import *
import ServerGame
from ServerPlayer import *

class Server:
    def __init__(self):
        self.inputManagers = []
        self.players  = {}
        self.games = {}    

        self.playerID = 0
        self.gameID = 0
        self.characterID = 0

        player1 = self.createPlayer()
        player2 = self.createPlayer()
        self.createGame(player1, player2)

        self.running = True

    def getPlayerID(self):
        self.playerID += 1
        return self.playerID

    def getGameID(self):
        self.gameID += 1
        return self.gameID

    def getCharacterID(self):
        self.characterID += 1
        return self.characterID

    def createPlayer(self):
        self.player = ServerPlayer(self.getPlayerID())
        self.players[self.player.uid] = self.player
        return self.player

    def associatePlayer(self, player, game, character):
        player.character = character
        player.game = game
        character.player = player
        
    def associateGame(self, game, characters):
        game.characters = characters
        for charID, character in characters.items():
            character.game = game
        Global.gameState = GameState(characters, game.projectiles)
        game.gameState = Global.gameState
    
    def createGame(self, player1, player2):
        game = ServerGame.ServerGame(self.getGameID())
        self.games[game.uid] = game

        topPos = [ServerGame.width / 2, 100]
        botPos = [ServerGame.width / 2, ServerGame.height - 100]
        character1 = ServerCharacter(self.getCharacterID(), topPos)
        character2 = ServerCharacter(self.getCharacterID(), botPos)
        characters = {
            character1.uid: character1,
            character2.uid: character2
        }

        self.associatePlayer(player1, game, character1)
        self.associatePlayer(player2, game, character2)
        
        self.associateGame(game, characters)
        return game
    
    def run(self):
        # while self.running:
            inputManagers = []

            playerID = 1
            inputManagers.append([Global.inputManager, playerID])
            
            for inputManager, playerID in inputManagers:
                self.updateInput(inputManager, playerID)
        
            for gameID, game in self.games.items():
                game.run()

    def updateInput(self, inputManager, playerID):
        player = self.players[playerID]
        if player and player.game.canUpdate():
            player.character.update(inputManager)
