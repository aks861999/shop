from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import requests
import json
import uvicorn

app = FastAPI()



@app.get('/sweaters')
async def get_sweaters():

    
    
    sheet_url = 'https://docs.google.com/spreadsheets/d/1pm2eBiux4l9Z-3P1eSAinP5NJ7v3v7YfpVFRfVW3rPA/gviz/tq?tqx=out:json&sheet=sweater'
    response = requests.get(sheet_url)
    
    print(response.status_code)

    data = []

    if response.status_code == 200:
        json_str = response.text.replace("/*O_o*/\ngoogle.visualization.Query.setResponse(", "")[:-2]
        data = json.loads(json_str)
        records = [
            {
                'Timestamp': row['c'][0]['v'],
                'Sweater Photo': row['c'][1]['v'],
                'Sweater Size': row['c'][2]['v'],
                'Price': row['c'][3]['v']
            }
            for row in data['table']['rows']
        ]
        data = records
    

    print(data)

    '''

    if data:
        return JSONResponse(content=data)
    raise HTTPException(status_code=500, detail="Failed to fetch data")



    
    '''
    if data:
        return JSONResponse(content=data)
    else:
        raise HTTPException(status_code=500, detail="Failed to fetch data")
    
