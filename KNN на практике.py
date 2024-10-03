import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv('penguins.csv')
data = data.dropna()

labels = data['species']
features = data[['bill_length_mm', 'bill_depth_mm']]

train_features, test_features, train_labels, test_labels = train_test_split( 
            features, labels, test_size=0.2, random_state=123)

best_accuracy = 0
worst_accuracy = 1

for model_index in range(1, 21):
    for n_neighbours in range(1, 11):
        for weights in ['uniform', 'distance']:
            model = KNeighborsClassifier(n_neighbors=n_neighbours, weights=weights)

            model.fit(train_features, train_labels)

            labels_pred = model.predict(test_features)
            accuracy = accuracy_score(test_labels, labels_pred)

            if accuracy > best_accuracy:
                best_accuracy = accuracy
            if accuracy < worst_accuracy:
                worst_accuracy = accuracy
            

print('Best accuracy: {:.6f}'.format(best_accuracy)) 
print('Worst accuracy: {:.6f}'.format(worst_accuracy))