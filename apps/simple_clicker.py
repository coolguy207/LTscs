from scs import *

#modle were you keep vareables 
def onAppStart(app):
    app.cookieR=100
    app.score=0
    app.scoreX=5
    app.cookieX=200
    app.cookieY=200
    app.RX=350
    app.RY=350
    app.RW=50
    app.RH=50
    app.cost=10
    app.presspower=1
    app.shop="red"
#controler were you chang them/ interact with code 
def onStep(app):
    if app.cost<=app.score:
        app.shop="green"
    else:
        app.shop="red"
def cheackhit(app, x, y):
    if (abs(app.cookieX-x )<app.cookieR and abs(app.cookieY-y )<app.cookieR):
        print("hit")
        app.cookieR-=10
        app.score+=app.presspower
    if (x>app.RX and y>app.RY and y<app.RY+app.RH and x<app.RX+app.RW) and app.score>=app.cost:
        app.score-=app.cost
        print("good")
        app.cost*=2
        app.presspower+=1
def onMousePress(app, x, y):
    cheackhit(app, x,y)
    app.scoreX=5

        
def onMouseRelease(app, x, y):
    app.cookieR=100



#view the product just shapes  
def redrawAll(app):
       
        drawRect(app.RX,app.RY,app.RW,app.RH, fill=app.shop)
        drawLabel(app.cost, app.RX+20, app.RY-10, size=25, align='center')
        #cookie
        drawCircle(app.cookieX,app.cookieY,app.cookieR, fill='saddlebrown')
        
        #score
        drawLabel(app.score, app.scoreX, 32, size=80, align='left')
def main():
    runApp(400,400)
    
main()