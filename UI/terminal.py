from cmu_graphics import*

class terminal:
    def __init__(self):
        self.textColor = 'white'
        self.backgroundColor = 'black'
        self.textLines = [] 
        


    def draw(self, app):
        # Draw terminal background
        drawRect(0, 0, app.width, app.height, fill=self.backgroundColor)

        # Draw text lines
        lineHeight = app.height / 20  # Example line height
