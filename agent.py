import random
import numpy as np
import os
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense,Activation,Flatten,Conv2D
from collections import deque
from keras.optimizers import Adam
import time

os.environ['KMP_DUPLICATE_LIB_OK']='True'
class DQLAgent:
    def __init__(self):
        # parameter / hyperparameter
        self.state_size = 5 # distance [(playerx-m1x),(playery-m1y),(playerx-m2x),(playery-m2y)]
        self.action_size = 2 # right, left, no move 
        
        self.gamma = 0.95
        self.learning_rate = 0.001 
        
        self.epsilon = 1  # explore
        self.epsilon_decay = 0.995
        self.epsilon_min = 0.01
        
        self.memory = deque(maxlen = 1000)
        
        self.model = self.build_model()
        
        
    def build_model(self):
        # neural network for deep q learning
        model = Sequential()
        model.add(Dense(48, input_shape = (1,self.state_size), activation = "relu"))
        model.add(Dense(self.action_size,activation = "linear"))
        model.compile(loss = "mse", optimizer = Adam(lr = self.learning_rate))
        return model
    
    def remember(self, state, action, reward, next_state, done):
        # storage
        self.memory.append((state, action, reward, next_state, done))
    
    def act(self, state):
        state = np.array(state)
        state = state.reshape(1,1,5)
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_size)
        act_values = self.model.predict(state)
        return np.argmax(act_values[0][0])
    
    def replay(self, batch_size):
        # training
        if len(self.memory) < batch_size:
            return
        minibatch = random.sample(self.memory,batch_size)
        for state, action, reward, next_state, done in minibatch:
            state = np.array(state)
            state = state.reshape(1,1,5)
            next_state = np.array(next_state)
            next_state = next_state.reshape(1,1,5)
            if done:
                target = reward 
            else:

                target = reward + self.gamma*np.amax(self.model(next_state, training=False))
            train_target = self.model(state, training=False)
            train_target = train_target.numpy()
            train_target[0][0][action] = target
            self.model.fit(state,train_target,verbose=0)
            
    def adaptiveEGreedy(self):
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

