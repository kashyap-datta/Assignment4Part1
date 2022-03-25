import os
import shutil
import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from requestmodel import Request
import sys
import visualize
from dataprocessing.zipping import zipfiles
sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), '..')))
from dataprocessing.query_filename import query_filename
from dataprocessing.query_filename import query_catalog
from dataprocessing.nowcast_results import load_sevirfile
import tensorflow as tf

app = FastAPI()
model = tf.keras.models.load_model('model\mse_model.h5',compile=False,custom_objects={"tf": tf})




#Index route
@app.get('/')
def index():
    return {'message':'Welcome to Nowcasting Model'}

@app.post('/predict')
def predict(data:Request): 

    data = data.dict()
    location = data['location']
    begintime = data['begintime']
    endtime = data['endtime']
    if(len(location) == 0 or len(begintime) == 0 or len(endtime) == 0 ):
        return "Enter all the fields"

    dirpath = "data" 
    if os.path.exists(dirpath) and os.path.isdir(dirpath):
        shutil.rmtree(dirpath)
    archivepath = "archive.zip"
    if os.path.exists(archivepath): 
        os.remove(archivepath)
    oppath = "output.png"
    if os.path.exists(oppath): 
        os.remove(oppath)

    filename = query_filename(location,begintime,endtime)
    print(filename)
    if(filename != 'nofile'):
        load_sevirfile(filename)
        #query_catalog(filename)
        cmd = "python nowcast_datagen\make_nowcast_dataset.py --sevir_data data\sevir --sevir_catalog CATALOG.csv --output_location data\interim"
        os.system(cmd)
        visualize.predict_data()
        return zipfiles("output.png")
    else:
        return "Location not found. Please try different location"

    
    

    
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

