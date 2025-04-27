 # Agent-Powered Data Analysis Notebook

 This project provides a Jupyter notebook that uses an OpenAI-backed agent to analyze and visualize customer data.
 The notebook drives a `CodeAgent` (from [smolagents](https://github.com/openai/smolagents)) to:
 - Load table metadata from a schema file
 - Query and process CSV-based data
 - Generate plots (e.g., bar charts, boxplots) on demand

 ## Prerequisites

 - An OpenAI API key (set in a `.env` file as `OPENAI_API_KEY`)

 ## Installation

 Clone the repository and install required packages:
 ```bash
 pip install -r requirements.txt
 ```

 ## Generating Sample Data

 A helper script creates a fake customer dataset at `data/customers.csv`:
 ```bash
 python generate_fake_data.py
 ```

 ## Running the Notebook

 Launch Jupyter and open the notebook:
 ```bash
 jupyter notebook analyst_notebook.ipynb
 # or
 jupyter lab analyst_notebook.ipynb
 ```

 The notebook imports two modules:
 - `analyst_tools.py`: defines the `table_metadata_loader` tool
 - `analyst_agent.py`: constructs the `analyst` CodeAgent

 You can then execute cells to ask the agent questions, for example:
 ```python
 analyst.run("How many users we have by sex? please plot")
 analyst.run("What is the average customer tenure? Create a boxplot.")
 ```

 ## File Structure

 - `analyst_tools.py`: contains the `@tool` definitions for metadata loading
 - `analyst_agent.py`: initializes the `analyst` agent with its tools and model
 - `analyst_notebook.ipynb`: the interactive notebook driving analysis
 - `generate_fake_data.py`: script to generate sample customer data
 - `data/`: contains `customers.csv` (generated) and `schema.txt`
 - `requirements.txt`: core package requirements
 - `.env`: environment variables (not checked in)