import matplotlib.pyplot as plt
import parseLogFile as PLF
# plt.plot([1, 2, 3, 4])
variable = 'gxmn'
params = PLF.getParams(variable)
plt.plot(params)
plt.ylabel(variable)
plt.xlabel('health check interval')
plt.show()