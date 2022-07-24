from img_procesor import img_procesor
from IPython import display
import numpy as np
from tensorflow import keras
import tensorflow as tf
import cv2
from matplotlib import pyplot as plt
from dog_list import dog_class



def sort_index(lst, rev=True):
    index = range(len(lst))
    s = sorted(index, reverse=rev, key=lambda i: lst[i],value=lambda i: lst[i])
    return s


#cargar modelo
model = tf.keras.models.load_model('modelo/modelo_perros.h5')



#cargar imagen
img_path = 'imagenes/perro5.png'
img = img_procesor.procs_img(img_path)





#generar prediccion
predictions = model.predict(img)
score = predictions[0]


#analizar puntaje
print(dog_class.dogindex(score.argmax()))


#crear lista indice con los 3 mayores puntajes
top_index_list = sort_index(score[:3])



#mostrar 3 mayores puntajes
print("----------")

for i in range(3):
    print("{:.2f}".format(score[top_index_list[i]]*100) , "% -->" , dog_class.dogindex(top_index_list[i]))
    

#print(score.shape)


