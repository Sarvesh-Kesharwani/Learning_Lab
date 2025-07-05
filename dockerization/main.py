from fastapi import FastAPI, Path, HTTPException, Query
import json
import random

app = FastAPI()


@app.get("/")
def root():
    return {"message": "patient management system API."}


def get_all_patients(order: str):
    with open("patients.json", "r") as f:
        patient_details = json.load(f)
    if order == "asc":
        return sorted(patient_details, reverse=False)
    else:
        return sorted(patient_details, reverse=True)


def get_patient_with_id_(id: int):
    with open("patients.json", "r") as f:
        patient_details = json.load(f)
    return patient_details["P00" + str(id)]


@app.get("/random_patient")
def get_random_patient():
    return {"patient_details": get_patient_with_id_(random.randint(1, 5))}


@app.get("/get_patient_data/{patient_id}")
def get_patient_with_id(patient_id: int = Path(..., description="ID of the patient.")):
    if patient_id < 3:
        return get_patient_with_id_(patient_id)
    else:
        return HTTPException(status_code=404, detail="Patient not found!")


@app.get("/sorted_patient_list/{sort_by}")
def sorted_patients(
    sort_by: str = Query(..., description="order to sort patients with their ids."),
):
    return get_all_patients(sort_by)
