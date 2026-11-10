from scs import *

#modle were you keep vareables 
def onAppStart(app):
    app.cookieR=100
    app.score=0
    app.scoreX=54

#controler were you chang them/ interact with code 

def cheackhit(app, x, y):
    if (abs(200-x )<app.cookieR and abs(200-y )<app.cookieR):
        print("hit")
        app.cookieR-=10
        app.score+=1
def onMousePress(app, x, y):
    cheackhit(app, x,y)
    app.scoreX right =

        
def onMouseRelease(app, x, y):
    app.cookieR=100



#view the product just shapes  
def redrawAll(app):
        drawCircle(200,200,app.cookieR, fill='saddlebrown')
        drawLabel(app.score, app.scoreX, 32, size=80)
def main():
    runApp(400,400)
    
main()