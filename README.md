#### Hack To The Rescue: Autism fact-checker (by Altruistic Visiumees)

### 1. Tech requirements:
 Create a `app/constants.py` file with a constant called OPEN_AI_KEY for storing the token needed to query ChatGPT.
 Install the requirements from `requirements.txt`or run `pipenv install`.

 ### 2. Run web app:
 ```
 cd app
 streamlit run main.py --server.port=8501
 ```

 ### 3. Troubleshooting:
 - If you want run the previous command ` streamlit run main.py --server.port=8501` again, you might encounter this error: `Port 8501 is already in use`.
    When that happens just copy paste this address in your browser: `http://localhost:8501/`
 - If you encounter any issue during the installation, don't hesitate to contact `ixeia.sanchez@visium.ch` or `maksim.zubkov@visium.ch`.