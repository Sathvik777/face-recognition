import urllib2
import urllib
import cv2
import numpy as np
import os


NEG_LINK='https://image-net.org/api/text/imagenet.synset.geturls?wnid=n07697537'


def store_raw_images_neg():
    neg_images_link = NEG_LINK
    neg_image_urls = urllib2.urlopen(NEG_LINK).read().unicode('\x80abc', errors='strict') 

    if not os.path.exists('neg'):
        os.makedirs('neg')

    for i in neg_image_urls.split('\n'):
        try:
            print(i)
            urllib.urlretrieve(i, "neg/"+str(pic_num)+".jpg")
            img = cv2.imread("neg/"+str(pic_num)+".jpg",cv2.IMREAD_GRAYSCALE)
            # should be larger than samples / pos pic (so we can place our image on it)
            resized_image = cv2.resize(img, (100, 100))
            cv2.imwrite("neg/"+str(pic_num)+".jpg",resized_image)
            pic_num += 1

        except Exception as e:
            print(str(e))



store_raw_images_neg()
