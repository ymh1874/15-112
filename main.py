# main.py 
from cmu_graphics import*
from UI.loginPage import LoginPage
from UI.terminal import terminal
from UI.desktop import desktop

def onAppStart(app):
    app.loginPage = LoginPage()
    app.terminal = terminal(app)
    app.desktop = desktop(app)
    app.screen = 'terminal'  # Start with the terminal debugging screen
    

    
def redrawAll(app):
    if app.screen == 'login':
        app.loginPage.draw(app)
    elif app.screen == 'terminal':
        app.terminal.draw(app)
    elif app.screen == 'desktop':
        app.desktop.draw(app)
        
def onMousePress(app, mouseX, mouseY):
    if app.screen == 'login':
        app.loginPage.loginMousePress(mouseX, mouseY, app)
    if app.screen  == 'terminal':
        pass
         

def onKeyPress(app, key):
    if app.screen == 'login':
        app.loginPage.loginKeyPress(key, app)
    if app.screen == 'terminal':
        app.terminal.onKeyPressTerminal(key)   

runApp(app.width, app.height)
