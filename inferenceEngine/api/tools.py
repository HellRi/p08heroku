import io, os, json
import numpy as np
import cv2
from tensorflow.keras.models import load_model#,Model

class Tools():
    def __init__(self):
        self.pathStatic = os.path.join(os.getcwd(),'api','static')
        # chargement du model
        self.model = load_model(os.path.join(self.pathStatic,'model'), compile=False)

        self.imgHeight, self.imgWidth = 224, 224

    def predictMask(self, ndImg):
        '''
        params: image au format ndArray (224,224,3)

        retrun: un mask au format ndArray (224,224,8)
        '''
        assert ndImg.shape[0]==self.imgHeight
        assert ndImg.shape[1]==self.imgWidth
        assert ndImg.shape[2]==3

        z = self.model.predict(np.expand_dims(ndImg, axis=0))
        z = np.squeeze(z)
        mask = z.reshape(self.imgHeight, self.imgWidth, 8)

        return mask

    def serializ(self, ndImg):
        # redimentionnement de l'image
        img = cv2.resize(ndImg,(self.imgHeight,self.imgWidth))

        memfile = io.BytesIO()
        np.save(memfile, img)

        serialized = memfile.getvalue()
        serialized_as_json = json.dumps(serialized.decode('latin-1'))
        # serializedForJson = serialized.decode('latin-1')

        return serialized_as_json
        # return serializedForJson

    def deSerializ(self, jsonImg):
        memfile = io.BytesIO()
        memfile.write(json.loads(jsonImg).encode('latin-1'))
        memfile.seek(0)
        img = np.load(memfile)

        return img