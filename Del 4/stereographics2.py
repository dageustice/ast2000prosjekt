from solar_system import *
from PIL import Image
import numpy as np
from tqdm import trange


img = Image.open("sample0000.png") # Open existing png
pixels = np.array(img) # png into numpy array
width = len(pixels[0, :])
redpixs = [(255, 50, 60) for i in range(width)] # Array of red pixels
pixels[239, :] = redpixs # Insert into line 500
img2 = Image.fromarray(pixels)
img2.save("exampleWithRedLine.png") # Make new png
print(np.shape(pixels))

def grid(theta0, phi0, fil):
    img=Image.open(fil)
    pixels=np.array(img)
    nx,ny=len(pixels[0,:]),len(pixels[:,0])
    FOV = 70 * np.pi / 180
    x = np.linspace(-2 * np.sin(FOV / 2) / (1 + np.cos(FOV / 2)), 2 * np.sin(FOV / 2) / (1 + np.cos(FOV / 2)), nx)
    y = np.linspace(2 * np.sin(FOV / 2) / (1 + np.cos(FOV / 2)), -2 * np.sin(FOV / 2) / (1 + np.cos(FOV / 2)), ny)
    X, Y = np.meshgrid(x, y)
    rho = np.sqrt(X ** 2 + Y ** 2)
    beta = 2 * np.arctan(rho / 2)
    ledd = np.cos(beta) * np.cos(theta0) + Y / rho * np.sin(beta) * np.sin(theta0)
    theta_new = theta0 - np.arcsin(ledd)
    ledd = X * np.sin(beta) / (rho * np.sin(theta0) * np.cos(beta) - Y * np.cos(theta0) * np.sin(beta))
    phi_new = phi0 + np.arctan(ledd)
    return X, Y, theta_new, phi_new,nx,ny


bilde = np.load("himmelkule.npy")

theta0=np.pi/2
phi0=0
x, y, theta, phi,width,height= grid(theta0,phi0,"sample0000.png")
a = np.zeros((height, width, 3), dtype=np.uint8)

for i in range(height):
    for j in range(width):
        a[i][j] = bilde[mission.get_sky_image_pixel(theta[i][j], phi[i][j])][2:]

himmelkule = Image.fromarray(a)
himmelkule.save("himmekule.png")
