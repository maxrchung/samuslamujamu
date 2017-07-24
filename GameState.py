class GameState:
    def __init__(self, charRects, projectileRects):
        # List of (playerID, rect)
        self.charRects = charRects
        # List of (playerID, rect)
        self.projectileRects = projectileRects
        
