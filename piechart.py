# piechart.py
import matplotlib.pyplot as plt

# The slices will be plotted counter-clockwise.
labels = ['Apples', 'Pears', 'Bananas', 'Oranges', 'Strawberries']
sizes = [25, 25, 20, 15, 15]
colors = ['lightgreen', 'gold', 'lightskyblue', 'lightcoral', 'red']
explode = (0, 0.1, 0, 0, 0)  # only "explode" the 2nd slice
plt.figure(figsize=(5, 4))
plt.pie(sizes, explode=explode,
        labels=labels,colors=colors,
        autopct='%0.1f%%',
        shadow=True, startangle=0)
# Set aspect ratio to be equal
# so that pie is drawn as a circle.
plt.axis('equal')
plt.show()
