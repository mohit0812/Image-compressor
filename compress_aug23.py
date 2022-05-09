import os
import sys

import cv2

QUALITY_PERCENTAGE = 90

def compress(base_dir):
    UNKNOWN_DIR = os.path.join(base_dir, 'unknown')
    COMPRESS_DIR = os.path.join(base_dir, 'compress')
    if not os.path.exists(COMPRESS_DIR):
        os.mkdir(COMPRESS_DIR)
    print("Compressing", UNKNOWN_DIR)
    data_list = os.listdir(UNKNOWN_DIR)
    
    for img_name in data_list:
        img_path = os.path.join(UNKNOWN_DIR, img_name)
        try:
            img = cv2.imread(img_path)
        except:
            continue

        if img is not None:
            print('Original Dimensions : '+img_name,img.shape)
 
            scale_percent = 60 
            shape = img.shape
            if shape[0] > shape[1]:
                if shape[0] <= 2160:
                    scale_percent = 100
                else:
                    scale_percent = 216000 / shape[0]
                    print(scale_percent)
            else:
                if shape[1] <= 2160:
                    scale_percent = 100
                else:
                    scale_percent = 216000 / shape[1]
                    print(scale_percent)

            width = int(img.shape[1] * scale_percent / 100)
            height = int(img.shape[0] * scale_percent / 100)
            dim = (width, height)
            
            resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
            
            print('Resized Dimensions : ',resized.shape)
        
            os.chdir(COMPRESS_DIR)
            cv2.imwrite(img_name, resized, [int(cv2.IMWRITE_JPEG_QUALITY), QUALITY_PERCENTAGE])
            os.chdir('..')


if __name__ == "__main__":
    compress(os.path.join(os.path.dirname(sys.argv[0])))
