from matplotlib import pyplot as plt

names = ['group_aaaaaaaaa']
values = [1, 10, 100]

# plt.figure(figsize=(10, 5))

# plt.subplot(132)
# plt.bar(names, values)
# plt.width=10
# plt.suptitle('Categorical Plotting')
# plt.show()

fruit_names = ['Coffee', 'Salted Caramel', 'Pistachio']
fruit_counts = [4000, 2000, 7000]

fig, ax = plt.subplots()
bar_container = ax.bar(fruit_names, fruit_counts)
ax.set(ylabel='pints sold', title='Gelato sales by flavor')
ax.bar_label(bar_container, fmt='{:,.0f}')
plt.show()