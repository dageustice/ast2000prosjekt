import numpy as np
import matplotlib.pyplot as plt
import ast2000tools as ast
#ikke kodemal

# jeg lager først en funkjson for f(mu, sigma, x)
def gauss_distribution(mu, sigma, x):
    return 1/(sigma*(2*np.pi)**(1/2)) \
           * np.exp(-(1/2)*((x-mu)/sigma)**2)


# så lager jeg en funkjson for P(a<x<b)
def gauss_interval(mu, sigma, a, b):
    N = int(1e4)        # jeg velger 10 000 intervaler
    dx = (b - a) / 1e4  # størrelse på interval avhenger av a og b
    x = np.linspace(a, b, N)
    one_incident = np.zeros(len(x))
    incidents = np.zeros(len(x)-1)
    one_incident[0] = gauss_distribution(mu, sigma, x=a)
    for i in range(N-1):
        one_incident[i+1] = gauss_distribution(mu, sigma, x=x[i+1])
        incidents[i] = dx*(1/2)*(one_incident[i] + one_incident[i+1])
    return sum(incidents)


mu = 1500
sigma = 50
for i in range(1, 4):
    print(f"P({-int(i)}σ ≤ μ ≤ {int(i)}σ) = {gauss_interval(mu, sigma, mu-i*sigma, mu+i*sigma)*100:.2f}%")
