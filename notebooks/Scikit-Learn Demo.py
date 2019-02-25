#!/usr/bin/env python
# coding: utf-8

# # Scikit-Learn demo

# The following code chunk is taken from:

# https://scikit-learn.org/stable/auto_examples/exercises/plot_digits_classification_exercise.html#sphx-glr-auto-examples-exercises-plot-digits-classification-exercise-py

# In[ ]:


from sklearn import datasets, neighbors, linear_model

digits = datasets.load_digits()
X_digits = digits.data / digits.data.max()
y_digits = digits.target

n_samples = len(X_digits)

X_train = X_digits[:int(.9 * n_samples)]
y_train = y_digits[:int(.9 * n_samples)]
X_test = X_digits[int(.9 * n_samples):]
y_test = y_digits[int(.9 * n_samples):]

knn = neighbors.KNeighborsClassifier()
logistic = linear_model.LogisticRegression(solver='lbfgs', max_iter=1000,
                                           multi_class='multinomial')

print('KNN score: %f' % knn.fit(X_train, y_train).score(X_test, y_test))
print('LogisticRegression score: %f'
      % logistic.fit(X_train, y_train).score(X_test, y_test))


# the following code chunk is taken from https://scikit-learn.org/stable/auto_examples/datasets/plot_digits_last_image.html#sphx-glr-auto-examples-datasets-plot-digits-last-image-py

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')

print(__doc__)


# Code source: Gaël Varoquaux
# Modified for documentation by Jaques Grobler
# License: BSD 3 clause

from sklearn import datasets

import matplotlib.pyplot as plt

#Load the digits dataset
digits = datasets.load_digits()

#Display the first digit
plt.figure(1, figsize=(3, 3))
plt.imshow(digits.images[110], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()


# # MathJAX

# When $a \ne 0$, there are two solutions to \(ax^2 + bx + c = 0\) and they are
# $$x = {-b \pm \sqrt{b^2-4ac} \over 2a}.$$

# In[ ]:





# In[ ]:




