from scs import *

# Model: where you keep variables
def onAppStart(app):
    app.cookieR = 100
    app.score = 0
    app.scoreX = 54


# Controller: where you change variables and handle interactions
def cheackhit(app, x, y):
    if abs(200 - x) < app.cookieR and abs(200 - y) < app.cookieR:
        print("hit")
        app.cookieR -= 10
        app.score += 1


def onMousePress(app, x, y):
    cheackhit(app, x, y)


def onMouseRelease(app, x, y):
    app.cookieR = 100


# View: draw the shapes
def redrawAll(app):
    drawCircle(200, 200, app.cookieR, fill="saddlebrown")
    drawLabel(app.score, app.scoreX, 32, size=80)


def main():
    runApp(400, 400)


main()