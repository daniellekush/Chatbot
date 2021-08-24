import pickle
import tensorflow as tf
import tflearn
training_data1 = pickle.load(open("training_data", "rb"))
train_x = training_data1['train_x']
train_y = training_data1['train_y']

tf.reset_default_graph()
net = tflearn.input_data(shape=[None, len(train_x[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
net = tflearn.regression(net)

model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')
model.fit(train_x, train_y, n_epoch=250, batch_size=200, show_metric=True)
model.save('model.tflearn')

#print("model created successfully")
