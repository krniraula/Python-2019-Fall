import matplotlib.pyplot as plt
squares = [1,4,9,16,25]

fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)
#set chart title and label axes
ax.set_tital("Square Numbers", fontsize=24)
