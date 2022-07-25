from IPython import display
import tensorflow as tf
from matplotlib import pyplot as plt
import imageio as iio


class img_procesor():

    def procs_img(img_path: str):
        img = iio.imread(img_path)
        display.display(display.Image(img_path))
        
        #recortar imagen central
        x,y,r = img.shape    # guardar tamaño de la imagen
    
        if x > y or x == y:    
            cropped_image = img[int((x-y)/2):int(x-(x-y)/2)]  # recorte central, maximo horizontal
        else:
            cropped_image = img[: , int((y-x)/2):int(y-((y-x)/2))] # recorte central, maximo vertical
    
    
    
        
        
        plt.imshow(cropped_image)
        plt.show()
        
        # reescalado de imagen
        img = tf.image.resize(cropped_image,(224,224))
        img = tf.reshape(img, (1,224,224,3), name=None)
        
        
        return img


