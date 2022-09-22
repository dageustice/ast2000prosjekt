from RocketThrust import *
n = 100
fuelburned = np.zeros(n)
fuel_left = np.zeros(n)
time = np.zeros(n)
v_1 = np.zeros(n)
a = np.zeros(n)
for i in trange(n):
    N_pos, v0, momentum, particles = \
        simulate(N, T, box, N2B_ratio, Time, dt)
    # simulerer en enkelt boks

    fuelburned[i], fuel_left[i], time[i], v_1[i], a_all \
        = fuel_burned(ccArea, box, momentum, fuelmass,
                      particles, rocketmass, speedboost)
    a[i] = a_all[-1]

all_info = [fuelburned, fuel_left, time, v_1, a]
texts = ["Total drivstoff forbrent:", "Drivstoff igjen: ",
         "Tiden for hele turen: ", "Sluttfart: ",
         "Sluttakselerasjon: "]
iterations = np.linspace(0, n, n)

for i in range(len(all_info)):
    plt.plot(iterations, all_info[i]/(np.mean(all_info[i])))
    max, min = np.max(all_info[i]), np.min(all_info[i])
    mean = (max+min)/2
    plusminus = (max-min)/2
    print(texts[i], f"{mean:.0f} ± {plusminus:.0f}")
plt.grid(); plt.show()
