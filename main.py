from fastapi import FastAPI
from scoring import compute_company_profile

app = FastAPI()

@app.get("/company/{company_name}")
def get_company(company_name: str):
    result = compute_company_profile(company_name)

    if result is None:
        return {"error": "Company not found"}

    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)

