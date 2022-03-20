import matplotlib.pyplot as plt

ax = plt.axes()

ax.arrow(0.0, 0.0, 3.0, 1.0, head_width=0.2, head_length=0.3, fc='lightblue', ec='lightblue', label='v1')
ax.arrow(0.0, 0.0, 6.0, 2.0, head_width=0.2, head_length=0.3, fc='lightblue', ec='lightblue', label='v2')
ax.arrow(0.0, 0.0, 4.0, 8.0, head_width=0.2, head_length=0.3, fc='orange', ec='orange', label='v3')
ax.legend()

plt.grid()

plt.xlim(0,10)
plt.ylim(0,10)

plt.title('Figure 1.3.6',fontsize=10)

plt.savefig('problem1.3.6.png', bbox_inches='tight')
plt.show()
plt.close()
