#Authon Huiliang

import pid_stu
import time
import matplotlib.pyplot as plt

output=10
timestep=1
x_value=0
x=[0]
y=[output]

pid = pid_stu.PID(0.2, 0.1,0.05)
pid.setSampleTime(0.1)

print output

while abs(output)>0.01:
    x.append(x_value)
    y.append(output)
    time.sleep(timestep)
    x_value += timestep
    pid.update(output)
    output = pid.output
    print output

plt.plot(x,y)
plt.show()