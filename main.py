# main.py 
from cmu_graphics import*
from UI.loginPage import LoginPage


def onAppStart(app):
    # LoginPage Initialization
    app.loginPage = LoginPage()
    app.screen = 'login' 
    

    
def redrawAll(app):
    if app.screen == 'login':
        app.loginPage.draw(app)
        if app.loginPage.box1Highlighted:
            app.loginPage.highlightBox(1, app)
        if app.loginPage.box2Highlighted:
            app.loginPage.highlightBox(2, app)

def onMousePress(app, mouseX, mouseY):
    if app.screen == 'login':
        if (app.width*0.123047 <= mouseX <= app.width*0.405599 and
            app.height*0.344727 <= mouseY <= app.height*0.41211):
            app.loginPage.box1Highlighted = True  
            app.loginPage.box2Highlighted = False

        elif (app.width*0.123698 <= mouseX <= app.width*0.403646 and
              app.height*0.450195 <= mouseY <= app.height*0.517578):
            app.loginPage.box2Highlighted = True
            app.loginPage.box1Highlighted = False
         

def onKeyPress(app, key):
    if app.screen == 'login':
        if key == 'Enter':
            username = app.loginPage.username
            password = app.loginPage.password
            app.loginPage.addUser(username, password)
            app.screen = 'main'
        if app.loginPage.box1Highlighted:
            if key == 'Backspace':
                app.loginPage.username = app.loginPage.username[:-1]
            elif  key.isalpha() and len(key) == 1:
                app.loginPage.username += key
runApp(app.width, app.height)
