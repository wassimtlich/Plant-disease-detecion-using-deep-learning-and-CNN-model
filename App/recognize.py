
import numpy as np
from PIL import Image
from keras.preprocessing.image import img_to_array
import argparse
import pickle
import cv2
import matplotlib.pyplot as plt


default_image_size = tuple((256, 256))

def convert_image_to_array(image_dir):
    try:
        image = cv2.imread(image_dir)
        res = cv2.resize(image, dsize=(256, 256), interpolation=cv2.INTER_CUBIC)
        if image is not None :            
            return img_to_array(res)
        else :
            return np.array([])
    except Exception as e:
        print(f"Error : {e}")
        return None
def recognize(image):
	image_array = convert_image_to_array(image)
	inp=np.array(image_array)
	np_image_list = np.array([inp], dtype=np.float16) / 225.0
	model_file = f"/home/tlich/Bureau/ml_files/cnn_model.pkl"
	saved_classifier_model = pickle.load(open(model_file,'rb'))
	prediction = saved_classifier_model.predict(np_image_list) 
	label_binarizer = pickle.load(open(f"/home/tlich/Bureau/ml_files/label_transform.pkl",'rb'))
	return label_binarizer.inverse_transform(prediction)[0]


'''
parser = argparse.ArgumentParser()
parser.add_argument('-image',type=str,required=True,
		help='Specify the address of an image.')
args = parser.parse_args()
# Load the image.
address = args.image'''
address ="/home/tlich/Bureau/ml_files/potlb.JPG"
'''image_array = convert_image_to_array(address)
inp=np.array(image_array)
np_image_list = np.array([inp], dtype=np.float16) / 225.0

model_file = f"/home/tlich/Bureau/ml_files/cnn_model.pkl"
saved_classifier_model = pickle.load(open(model_file,'rb'))
prediction = saved_classifier_model.predict(np_image_list) 
label_binarizer = pickle.load(open(f"/home/tlich/Bureau/ml_files/label_transform.pkl",'rb'))
print(label_binarizer.inverse_transform(prediction)[0])'''
print(recognize('/home/tlich/Bureau/ml_files/pep.JPG'))

           


