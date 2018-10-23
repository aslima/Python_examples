from sklearn.svm import SVC
from sklearn import datasets
from sklearn.model_selection import train_test_split
import pickle

#load the Iris dataset
iris = datasets.base.load_iris()

#split features & target
X, y = iris.data, iris.target

#split trainning and testing datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=123)

# Instantiate and fit the model
clf = SVC(kernel='linear')
clf.fit(X_train,y_train)

# Open a binary file to write  
saved_SVM = open('svm_file.pickle', 'wb')
# Save the trained model in file
pickle.dump(clf,saved_SVM)
saved_SVM.close()

# Open the file as binary to read
SVM_file = open('svm_file.pickle', 'rb')
# Load saved model
clf_loaded = pickle.load(SVM_file)
SVM_file.close()

#Compare model results
print('predition with the saved model: ',clf_loaded.predict(X_test[0:1]))
print('predition with the original model: ',clf.predict(X_test[0:1]))