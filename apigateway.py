import fastapi
import uvicorn
import requests

app = fastapi.FastAPI()

@app.get("/compute/{values}")
def getComputeData(values: str):
    try:
        url = f"http://compute-srv:2000/compute/{values}"
        response = requests.get(url)
        
        if response.ok:
            return response.json()

    except requests.exceptions.RequestException as e:
        raise fastapi.HTTPException(
            status_code=502,
            detail=f"Błąd połączenia z serwisem wewnętrznym: {str(e)}"
        )

@app.get("/history")
def getHistotyData():
    try:
        url = f"http://0.0.0.0:3000/history"
        response = requests.get(url)
        
        if response.ok:
            return response.json()

    except requests.exceptions.RequestException as e:
        raise fastapi.HTTPException(
            status_code=502,
            detail=f"Błąd połączenia z serwisem wewnętrznym: {str(e)}"
        )




if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=7001, log_level="info")