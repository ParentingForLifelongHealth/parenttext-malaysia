# Malaysia Parenttext Pipeline

This project builds RapidPro flows for the Malaysia ParentText chatbot. It takes input from specific Google Sheets spreadsheets and produces RapidPro flow JSON files that are ready to upload to any RapidPro server.

## Usage

The pipeline is intended to be run by triggering a Github Actions workflow or by running commands on the command line.

## Github actions (work in progress)

1. Navigate to the page for the [Produce RapidPro Flows][1] action
2. Click on the _Run workflow_ button; a drop-down will appear
3. Make sure _Branch_ is set to _main_
4. Click on the green _Run workflow_ button

## Running from command line

These steps need to be followed if you want to run the pipeline from the command line or develop the pipeline further.

### Setup

1. Clone or fork the repo to a local folder
1. Install Python >= 3.6
1. Create a Python virtual environment `python -m venv .venv`
1. Activate the environment Linux: `source .venv/bin/activate`, Windows: `.venv/Scripts/activate`
1. Upgrade pip `pip install --upgrade pip`
1. Install project Python dependencies `pip install -r requirements.txt`
1. Install latest Node and NPM Long-Term Support (LTS) versions
1. Install project Node dependencies `npm install`
1. Make sure you have a correct `credentials.json` file in the same directory as the cloned repo. 

## Run

This repo contains two main scripts:

```
python process_safeguarding_words.py
```
This process takes excel files with safeguarding words received from local teams and converts to JSON format that can be digested by the main pipeline. For example of required excel input files, see the folder "excel_files" in this repo

```
python produce_flows.py
```
script produce_flows.py contains the full process to produce RapidPro flows from the relevant Google Sheets. It takes a number of inputs from the 'config.py' file so any adjustments should be made in that file. That file contains information on what the various inputs mean
