import pygame

class Keyboard:
    def __init__(self):
        self.currentKeyStates = None
        self.previousKeyStates = None
    def processInput(self):
        self.previousKeyStates = self.currentKeyStates
        self.currentKeyStates = pygame.key.get_pressed()
    def isKeyDown(self, keyCode):
        if self.currentKeyStates is None or self.previousKeyStates is None:
            return False
        return self.currentKeyStates[keyCode] == True
    def isKeyPressed(self, keyCode):
        if self.currentKeyStates is None or self.previousKeyStates is None:
            return False
        return self.currentKeyStates[keyCode] == True and self.previousKeyStates[keyCode] == False

class InputStream:
    def __init__(self):
        self.keyboard = Keyboard()
    def processInput(self):
        self.keyboard.processInput()