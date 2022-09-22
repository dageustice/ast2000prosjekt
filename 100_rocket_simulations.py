import matplotlib.pyplot as plt
from RocketThrust import *
from tqdm import trange
# gjentar simuleringen 100 ganger for å se hvor store avvikene blir
# se RocketThrust og EngineBox for fullstendige kommentarer
n = 100
fuelburned = np.zeros(n)
fuel_left = np.zeros(n)
time = np.zeros(n)
v_1 = np.zeros(n)
a = np.zeros(n)
for i in trange(n):
    N_pos, v0, momentum, particles = \
        simulate(N, T, box, N2B_ratio, Time, dt)

    fuelburned[i], fuel_left[i], time[i], v_1[i], a_all \
        = fuel_burned(ccArea, box, momentum, fuelmass,
                      particles, rocketmass, speedboost)
    a[i] = a_all[-1]

all_info = [fuelburned, fuel_left, time, v_1, a]
texts = ["Total drivstoff forbrent", "Drivstoff igjen",
         "Tiden for hele turen", "Sluttfart",
         "Sluttakselerasjon"]
iterations = np.linspace(0, n, n)

# plotter alle resultatene langs iterasjonene
for i in range(len(all_info)):
    plt.plot(iterations, (all_info[i]/(np.mean(all_info[i])))*100-100)
    max, min = np.max(all_info[i]), np.min(all_info[i])
    mean = (max+min)/2  # misvisende/forvirrende navn
    # NB! Dette er ikke gjennomsnittet, men midten av største og minste verdi
    plusminus = (max-min)/2  # avstand fra midten til max/min
    print(texts[i], ": ", f"{mean:.0f} ± {plusminus:.0f}")
plt.legend(texts); plt.ylabel("avvik [%]"); plt.xlabel("iterasjon nr.")
plt.title("100 Resultater normalisert på gjennomsnittsresultatet")
plt.grid(); plt.show(); plt.savefig("100resultater.png")
