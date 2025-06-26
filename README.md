# Pinpoint Plugin External Service Example

This repo shows a simple FastAPI implementation of a Pinpoint integration HRIS plugin 

## Set up
* clone the repo
* CD in to repo
* run `python2 -m venv .venv` which will create a `.venv` dir in your repo directory
* run `source .venv/bin/activate`
* run `pip3 install -r requirements.txt`

## Run the application
Once all dependencies are installed and you have activate the virtual environment you can then just run:
`uvicorn main:app --reload` which will start the FastAPI application on port 8000

## Plugin Endpoints

1. `localhost:8000/` - the initial set up endpoint
2. `localhost:8000/export` - the endpoint hit when a user clicks on send to FastAPI
3. `localhost:8000/submit` - the form submission endpoint

All endpoints are requested by Pinpoint using the `POST` method