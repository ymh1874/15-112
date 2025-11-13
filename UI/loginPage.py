from cmu_graphics import*
class LoginPage:
    users = {'admin': '67112'}  # Example user database
    def __init__(self):
        self.box1Highlighted = False
        self.box2Highlighted = False
        self.background = 'assets/loginBackground.png'
        self.username = ''
        self.password = ''
        
    def addUser(self, username, password):
        LoginPage.users[username] = password

    def draw(self, app):
        
        drawImage(self.background, 0, 0, width=app.width, height=app.height)
        # first box
        drawRect(app.width*0.123047, app.height*0.344727,
             app.width*0.282552, app.height*0.067383,
            fill=rgb(110, 0, 18), border='black', borderWidth=2, opacity=80)
        if not self.box1Highlighted:
            drawLabel('Username', app.width*0.14, app.height*0.38, size=20, bold=True, fill='white', align = 'left')
        # second box
        drawRect(app.width*0.123698, app.height*0.450195,
                app.width*0.279948, app.height*0.067383,
                fill=rgb(110, 0, 18), border='black', borderWidth=2, opacity=80)
        if not self.box2Highlighted:   
            drawLabel('Password', app.width*0.14, app.height*0.485, size=20, bold=True, fill='white', align = 'left')
        
    def highlightBox(self, boxNumber, app):

        if boxNumber == 1:
            drawRect(app.width*0.123047, app.height*0.344727,
             app.width*0.282552, app.height*0.067383,
            fill=None, border='white', borderWidth=4, opacity=100)

        elif boxNumber == 2:
            drawRect(app.width*0.123698, app.height*0.450195,
                app.width*0.279948, app.height*0.067383,
                fill=None, border='white', borderWidth=4, opacity=100)


    def checkUser(self, username, password):
        return LoginPage.users.get(username) == password


