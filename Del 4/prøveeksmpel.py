from PIL import Image
import numpy as np


img = Image.open("sample0000.png") # Open existing png
pixels = np.array(img) # png into numpy array
width = len(pixels[0, :])
redpixs = [(255, 50, 60) for i in range(width)] # Array of red pixels
pixels[239, :] = redpixs # Insert into line 500
img2 = Image.fromarray(pixels)
img2.save("exampleWithRedLine.png") # Make new png
print(np.shape(pixels))

def grid(theta0,phi0,width,height):
    
    nx,ny=(width,height)
    FOV=70*np.pi/180

    x=np.linspace(-2*np.sin(FOV/2)/1+np.cos(FOV/2),2*np.sin(FOV/2)/1+np.cos(FOV/2),nx)
    y=np.linspace(-2*np.sin(FOV/2)/1+np.cos(FOV/2),2*np.sin(FOV/2)/1+np.cos(FOV/2),ny) 
    X,Y=np.meshgrid(x,y)
    rho = np.sqrt(X**2+Y**2)
    beta = 2 * np.arctan(rho/2)
    ledd = np.cos(beta)*np.cos(theta0)+Y/rho*np.sin(beta)*np.sin(theta0)
    theta_new = theta0 - np.arcsin(ledd)
    ledd = X*np.sin(beta)/(rho*np.sin(theta0)*np.cos(beta)-Y*np.cos(theta0)*np.sin(beta))
    phi_new = phi0 + np.arctan(ledd)
    return X,Y,theta_new,phi_new
x,y,theta,phi=grid(np.pi/2,0,640,480)





"""for i in range(width):
        for k in range(height):
            p=np.sqrt(x[i]**2+y[k]**2)
            B=2*np.arctan(p/2) #kons
            theta=theta0-np.arcsin(np.cos(B)*np.cos(theta0)+y[k]/p*np.sin(B)*np.sin(theta0))
            phi=phi0+np.arctan(x[i]*np.sin(B)/(p*np.sin(theta0)*np.cos(B)-y[k]*np.cos(theta0)*np.sin(B)))
    Ntheta,Nphi=np.meshgrid(theta,phi)
"""