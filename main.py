from fastapi import FastAPI
from pydantic import BaseModel

# Just removing some stuff around base64 encoding and gubbins
import helpers

# Initialize FastAPI app
app = FastAPI()


# Run with: uvicorn main:app --reload


class Employee(BaseModel):
    firstName: str
    lastName: str


# Initial route used to set up integration plugin
@app.post("/")
async def root():
    return {
        "version": "1.0.0",
        "name": "FastAPI Demo",
        "logoBase64": helpers.jpg_to_base64("logo.jpg"),
        "actions": [
            {
                "key": "exportCandidate",
                "label": "Send to FastAPI",
                "iconSvgBase64": helpers.svg_file_to_base64("icon.svg"),
                "metaEndpoint": "/export",
                "mappings": [
                    {
                        "key": "firstName",
                        "label": "First Name",
                        "value": "{{candidate_first_name}}",
                    },
                    {
                        "key": "lastName",
                        "label": "Last Name",
                        "value": "{{candidate_last_name}}",
                    },
                ],
            }
        ],
        "configurationFormFields": [
            {
                "key": "apiKey",
                "label": "API Key",
                "required": True,
                "type": "string",
                "sensitive": True,
                "useAsHttpHeader": "x_plugin_test_api_key",
            },
        ],
    }


# Called when send to FastAPI is clicked i.e. render the form
@app.post("/export")
async def export_meta():
    fields = [
        {
            "key": "firstName",
            "label": "First Name",
            "required": False,
            "type": "string",
        },
        {
            "key": "lastName",
            "label": "Last Name",
            "required": False,
            "type": "string",
        },
        {
            "key": "startDate",
            "label": "Start Date",
            "required": False,
            "type": "date",
        },
        {
            "key": "cv",
            "label": "CV",
            "required": False,
            "type": "file",
        },
        {
            "key": "country",
            "label": "Country",
            "required": False,
            "type": "string",
            "singleSelectOptions": [
                {"label": "United Kingdom", "value": "UK"},
                {"label": "United States", "value": "US"},
            ],
            "performRefetchOnChange": True,
        },
    ]
    return {
        "actionVersion": "1.0.0",
        "key": "exportCandidate",
        "label": "Export Candidate",
        "description": "Export the candidate details",
        "formFields": list(fields),
        "submitEndpoint": "/submit",
    }


# Called when submit is clicked - for HRIS this is the last action in the lifecycle
@app.post("/submit")
async def submit(payload: dict):
    print(payload)
    first_name = helpers.get_field_value(payload, "firstName")
    last_name = helpers.get_field_value(payload, "lastName")

    if first_name != "Dave":
        return {
            "resultVersion": "1.0.0",
            "key": "exportCandidate",
            "success": False,
            "errors": [
                {"key": "firstName", "error": "You are not Dave, you must be Dave"}
            ],
            "toast": {"error": "You are not Dave"},
        }

    return {
        "resultVersion": "1.0.0",
        "key": "exportCandidate",
        "success": True,
        "message": f"{first_name} {last_name} was successfully sent to FastAPI.",
    }
