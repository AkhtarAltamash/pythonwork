# a = 33
# b = 200
# if a> b:
#     print("b is greater than a") # you will get an error

# a = 33
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
#
# #
# ######################
#
# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")

# ########################################
#

# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# else:
#   print("b is not greater than a")
# ###########################################
#
# a = 2
# b = 330
# print("A") if a > b else print("B")
# #
#
# ##########################################
#
#
# a = 330
# b = 330
# print("A") if a > b else print("=") if a == b else print("B")
#
#
# ###################################
#
# a = 200
# b = 33
# c = 500
# if a > b and c > a:
#   print("Both conditions are True")
#
# ###################
#
# a = 200
# b = 33
# c = 500
# if a > b or a > c:
#   print("At least one of the conditions is True")

# #################
#
# x = 41
#
# if x > 10:
#   print("Above ten,")
#   if x > 20:
#     print("and also above 20!")
#   else:
#     print("but not above 20.")
# ######################
#
#
# a = 33
# b = 200
#
# if b > a:
#   pass
#
# ###########

#
# def ReadData(fileName):
#   # Read the file, splitting by lines
#   f = open(fileName, 'r');
#   lines = f.read().splitlines();
#   f.close();
#
#   items = [];
#
#   for i in range(1, len(lines)):
#     line = lines[i].split(',');
#     itemFeatures = [];
#
#     for j in range(len(line) - 1):
#       # Convert feature value to float
#       v = float(line[j]);
#
#       # Add feature value to dict
#       itemFeatures.append(v);
#
#     items.append(itemFeatures);
#
#   shuffle(items);
#
#   return items;


# # %matplotlib inline
# import matplotlib.pyplot as plt
# import seaborn as sns; sns.set()  # for plot styling
# import numpy as np

import numpy as np
from scipy.spatial.distance import cdist


# Function to implement steps given in previous section
def kmeans(x, k, no_of_iterations):
    idx = np.random.choice(len(x), k, replace=False)
    # Randomly choosing Centroids
    centroids = x[idx, :]  # Step 1

    # finding the distance between centroids and all the data points
    distances = cdist(x, centroids, 'euclidean')  # Step 2

    # Centroid with the minimum Distance
    points = np.array([np.argmin(i) for i in distances])  # Step 3

    # Repeating the above steps for a defined number of iterations
    # Step 4
    # for _ in range(no_of_iterations):
    #     centroids = []
    #     for idx in range(k):
    #         # Updating Centroids by taking mean of Cluster it belongs to
    #         temp_cent = x[points == idx].mean(axis=0)
    #         centroids.append(temp_cent)
    #
    #     centroids = np.vstack(centroids)  # Updated Centroids
    #
    #     distances = cdist(x, centroids, 'euclidean')
    #     points = np.array([np.argmin(i) for i in distances])
    #
    # return points

    # Loading the required modules
    #
    # import numpy as np
    # from scipy.spatial.distance import cdist
    # from sklearn.datasets import load_digits
    # from sklearn.decomposition import PCA
    # from sklearn.cluster import KMeans
    # import matplotlib.pyplot as plt
    #
    # # Defining our function
    # def kmeans(x, k, no_of_iterations):
    #     idx = np.random.choice(len(x), k, replace=False)
    #     # Randomly choosing Centroids
    #     centroids = x[idx, :]  # Step 1
    #
    #     # finding the distance between centroids and all the data points
    #     distances = cdist(x, centroids, 'euclidean')  # Step 2
    #
    #     # Centroid with the minimum Distance
    #     points = np.array([np.argmin(i) for i in distances])  # Step 3
    #
    #     # Repeating the above steps for a defined number of iterations
    #     # Step 4
    #     for _ in range(no_of_iterations):
    #         centroids = []
    #         for idx in range(k):
    #             # Updating Centroids by taking mean of Cluster it belongs to
    #             temp_cent = x[points == idx].mean(axis=0)
    #             centroids.append(temp_cent)
    #
    #         centroids = np.vstack(centroids)  # Updated Centroids
    #
    #         distances = cdist(x, centroids, 'euclidean')
    #         points = np.array([np.argmin(i) for i in distances])
    #
    #     return points
    #
    #     # Load Data
    #
    # data = load_digits().data
    # pca = PCA(2)
    #
    # # Transform the data
    # df = pca.fit_transform(data)
    #
    # # Applying our function
    # label = kmeans(df, 10, 1000)
    #
    # # Visualize the results
    #
    # u_labels = np.unique(label)
    # for i in u_labels:
    #     plt.scatter(df[label == i, 0], df[label == i, 1], label=i)
    # plt.legend()
    # plt.show()