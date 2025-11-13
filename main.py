# main.py 
from cmu_graphics import*
from UI.loginPage import LoginPage
from UI.terminal import terminal

def onAppStart(app):
    # LoginPage Initialization
    app.loginPage = LoginPage()
    app.terminal = terminal()
    app.screen = 'login' 
    

    
def redrawAll(app):
    if app.screen == 'login':
        app.loginPage.draw(app)
    elif app.screen == 'terminal':
        app.terminal.draw(app)
        
def onMousePress(app, mouseX, mouseY):
    if app.screen == 'login':
        app.loginPage.loginMousePress(mouseX, mouseY, app)
    if app.screen  == 'terminal':
        pass
         

def onKeyPress(app, key):
    app.loginPage.loginKeyPress(key, app)

runApp(app.width, app.height)
