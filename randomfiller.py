import tensorflow as tf
from tensorflow import keras

import numpy as np
import os
import time

#print("program started")

model = keras.models.load_model("fillersdataset2")

path_to_file = "fillersdataset1.txt"

text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
# length of text is the number of characters in it
#print('Length of text: {} characters'.format(len(text)))

# Take a look at the first 250 characters in text
#print(text[:250])

# The unique characters in the file
vocab = sorted(set(text))
#print('{} unique characters'.format(len(vocab)))

# Creating a mapping from unique characters to indices
char2idx = {u:i for i, u in enumerate(vocab)}
idx2char = np.array(vocab)

'''
def get_model():
    # Create a simple model.
    inputs = keras.Input(shape=(32,))
    outputs = keras.layers.Dense(1)(inputs)
    model = keras.Model(inputs, outputs)
    model.compile(optimizer="adam", loss="mean_squared_error")
    return model


model = get_model()

# Train the model.
test_input = np.random.random((128, 32))
test_target = np.random.random((128, 1))
model.fit(test_input, test_target)

# Calling `save('my_model')` creates a SavedModel folder `my_model`.
model.save("my_model")

# It can be used to reconstruct the model identically.
reconstructed_model = keras.models.load_model("my_model")

# Let's check:
np.testing.assert_allclose(
    model.predict(test_input), reconstructed_model.predict(test_input)
)

# The reconstructed model is already compiled and has retained the optimizer
# state, so training can resume:
reconstructed_model.fit(test_input, test_target)'''

#model.load_weights(tf.train.latest_checkpoint(checkpoint_dir))

#model.build(tf.TensorShape([1, None]))

#model.summary()

#print("SUCCESSFULLY LOADED TRAINED MODEL FROM FILE: "+path_to_file)

global lungime
lungime = 60

def generate_text(model, start_string):
    # Evaluation step (generating text using the learned model)

    # Number of characters to generate
    global lungime
    num_generate = lungime #500

    # Converting our start string to numbers (vectorizing)
    input_eval = [char2idx[s] for s in start_string]
    input_eval = tf.expand_dims(input_eval, 0)

    # Empty string to store our results
    text_generated = []

    # Low temperature results in more predictable text.
    # Higher temperature results in more surprising text.
    # Experiment to find the best setting.
    
    temperature = 1.0

    # Here batch size == 1
    model.reset_states()
    for i in range(num_generate):
        predictions = model(input_eval)
        # remove the batch dimension
        predictions = tf.squeeze(predictions, 0)

        # using a categorical distribution to predict the character returned by the model
        predictions = predictions / temperature
        predicted_id = tf.random.categorical(predictions, num_samples=1)[-1,0].numpy()

        # Pass the predicted character as the next input to the model
        # along with the previous hidden state
        input_eval = tf.expand_dims([predicted_id], 0)

        text_generated.append(idx2char[predicted_id])

    return (start_string + ''.join(text_generated))

#print(generate_text(model, start_string=u" "))

def genfiller():
    return(generate_text(model, start_string=" "))

def randomfiller():
    filler = genfiller().split("\n")[0].replace("\n","").replace("\r","")
    return filler
