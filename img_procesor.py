from IPython import display
from matplotlib import pyplot as plt
import cv2

class img_procesor():

    def procs_img(img_path: str):
        img = cv2.imread(img_path)
        display.display(display.Image(img_path))
    
        #recortar imagen central
        x,y,r = img.shape    # guardar tamaño de la imagen
        print(x,y)
    
        if x > y or x == y:
            print("yes if")
    
            cropped_image = img[int((x-y)/2):int(x-(x-y)/2)]  # recorte central, maximo horizontal
        else:
            
            print(int((y-x)/2))
            cropped_image = img[: , int((y-x)/2):int(y-((y-x)/2))] # recorte central, maximo vertical
    
    
    
        
        
        print(cropped_image.shape)
        plt.imshow(cropped_image)
        plt.show()
        
        # reescalado de imagen
        img = cv2.resize(cropped_image,(224,224))   
        img = img.reshape(1,224,224,3) 
        
        
        return img


