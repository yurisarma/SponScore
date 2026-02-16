from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from scoring import compute_company_profile

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins for now
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "SponScore API is live"}

@app.get("/company/{company_name}")
def get_company(company_name: str):
    result = compute_company_profile(company_name)

    if result is None:
        return {"error": "Company not found"}

    return result



