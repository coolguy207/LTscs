from scs import *

#modle were you keep vareables 
def onAppStart(app):
    app.cookieR=100
    app.score=0
    app.scoreX=5
    app.cookieX=200
    app.cookieY=200
#controler were you chang them/ interact with code 

def cheackhit(app, x, y):
    if (abs(app.cookieX-x )<app.cookieR and abs(app.cookieY-y )<app.cookieR):
        print("hit")
        app.cookieR-=10
        app.score+=1
  
def onMousePress(app, x, y):
    cheackhit(app, x,y)
    app.scoreX=5

        
def onMouseRelease(app, x, y):
    app.cookieR=100



#view the product just shapes  
def redrawAll(app):
        drawCircle(app.cookieX,app.cookieY,app.cookieR, fill='saddlebrown')
        drawLabel(app.score, app.scoreX, 32, size=80, align='left')
def main():
    runApp(400,400)
    
main()