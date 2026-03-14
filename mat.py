
x = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
y = 1
fx = [] #lista vacía

for elemento in x:
    fx.append(elemento**4) # Parábola

print(f"F(x) = {fx}")

plt.style.use("ggplot")
plt.plot(
    x, # primero el eje X
    fx, # luego el eje Y
    )
