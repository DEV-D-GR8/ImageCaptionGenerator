import tensorflow as tf
from keras.applications.resnet50 import ResNet50, preprocess_input
from keras.models import Model, load_model
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing import image
import numpy as np

model = ResNet50(weights="imagenet",input_shape=(224,224,3))
model_new = Model(model.input,model.layers[-2].output)

def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return img_array

def encode_image(img):
    img = preprocess_image(img)
    feature_vector = model_new.predict(img)
    
    feature_vector = feature_vector.reshape((-1,))
    return feature_vector


def load_idx_to_word(file_path):
    loaded_dict = {}

    try:
        with open(file_path, "r") as file:
            for line in file:
                key, value = line.strip().split(": ", 1)
                key = int(key)
                loaded_dict[key] = value
    except FileNotFoundError:
        print(f"File '{file_path}' not found. Returning an empty dictionary.")
    
    return loaded_dict


def load_word_to_idx(file_path):
    loaded_dict = {}

    try:
        with open(file_path, "r") as file:
            for line in file:
                key, value = line.strip().split(": ", 1)
                value = int(value)
                loaded_dict[key] = value
    except FileNotFoundError:
        print(f"File '{file_path}' not found. Returning an empty dictionary.")
    
    return loaded_dict


idx_to_word = load_idx_to_word("App/idx_to_word.txt")
word_to_idx = load_word_to_idx("App/word_to_idx.txt")

caption_model = load_model('App/model_weights/model_9.h5')
    
def predict_caption(photo):

    in_text = "startseq"
    for i in range(35):
        sequence = [word_to_idx[w] for w in in_text.split() if w in word_to_idx]
        sequence = pad_sequences([sequence],maxlen=35,padding='post')
        
        ypred = caption_model.predict([photo,sequence])
        ypred = ypred.argmax()
        word = idx_to_word[ypred]
        in_text += (' ' + word)
        
        if word == "endseq":
            break

    final_caption = in_text.split()[1:-1]
    final_caption = ' '.join(final_caption)
    return final_caption

def generate_caption(img_path):
    img = encode_image(img_path)
    final_img = img.reshape((1, 2048))
    caption = predict_caption(final_img)

    return caption
