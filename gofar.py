#import package
from fastapi import FastAPI,Request, Header, HTTPException
import pandas as pd

df = pd.DataFrame()
df["username"] = ["kudanil", "kudalumping", "kudaasli"]
df ["location"] = ['sungai nil', 'jawa', 'kandang']

#buat kaya pass gitu
API_KEY = "kudakudanil1"

#buat object
app = FastAPI()

#buat rule funct + url yang bisa digunakan user (endpoint)
# end point ambil data adalah get, maka:


# @app.get("/") #slash saja untuk get all, kalo mau halaman dalemnya pake /survey misalnya
# def DataHandling():
#     return {
#         "message":"ini data fastapi all",
#         "favorit":"kuda",
#         "kuda":"lumping"
# }

'''
tulisan yang muncul:
INFO:     Started server process [5036]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)

Note: 127.0.0.1 adalah IP Local atau Local Host. 8000 adalah port
'''

#menampilkan header

@app.get("/") #slash saja untuk get all, kalo mau halaman dalemnya pake /survey misalnya
def DataHandling(request:Request):
    headers = request.headers
    return {
        "message":"ini data fastapi all",
        "favorit":"kuda",
        "kuda":"lumping",
        "headers": headers
}

#endpoint get alldata from dataframe
@app.get("/data/{location}")
def DFhandler(location):
    return df.to_dict(orient="records")



#endpoint dengan parameter dinamis
@app.get("/data/{loc}")
def DFhandler(loc):
    result = df.query(F"location == {loc}")
    return result.to_dict(orient="records")



#endpoint secret
@app.get("/secret") 
def DataSecret(api_key: str = Header(None)):
# cek api key dulu
    if api_key != API_KEY or api_key ==None :
         return {
        "error" : "kuda tahu kamu salah"
    }
    return {
        "secret" : "hanya kuda yang tahu"
    }