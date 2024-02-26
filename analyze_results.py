import os

import matplotlib.pyplot as plt


dataset_sizes = ['10', '50', '100', '200', '500', '1000', '2000', '4000']

values = []
for dataset_size in dataset_sizes:
    with open('results/{}/results.csv'.format(dataset_size), 'r') as f:
        values.append(float(f.readlines()[-1].split(',         ')[6]))

# Plotting the bar chart
plt.bar(dataset_sizes, values, color='skyblue')

# Adding labels and title
plt.xlabel('Dataset size', fontsize=16)
plt.ylabel('mAP50', fontsize=16)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)

plt.title('mAP in the last epoch as a function of dataset size', fontsize=16)


maps = values

# Display the plot
values = []
for dataset_size in dataset_sizes:
    for j in os.listdir('results/{}'.format(dataset_size)):
        try:
            values.append(float(j))
        except:
            pass

plt.figure()

plt.bar(dataset_sizes, values, color='skyblue')

# Adding labels and title
plt.xlabel('Dataset size', fontsize=16)
plt.ylabel('Training time (s)', fontsize=16)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)

plt.title('Training time as a function of dataset size', fontsize=16)

plt.show()
