# MaaS LLM Connectivity Setup Instructions

Follow the steps below to verify connectivity with the MaaS LLM service.

---

## 1. Login to Fresco Playground

1. Open the following URL in your browser:

```
https://play.fresco.me
```

2. Login using your credentials.

---

## 2. Launch the AI Lab Environment

1. After logging in, locate the **Search bar**.
2. Search for:

```
AI Lab
```
<img width="2882" height="1196" alt="image" src="https://github.com/user-attachments/assets/0955e714-b690-451d-85a8-759aec84ecf1" />


3. Click **Launch** to start the lab environment.
4. Wait for the virtual environment to initialize.

---

## 3. Navigate to the Project Folder

Once the lab environment is launched:

1. On the **desktop**, locate the **Project** folder.
2. Navigate to the following path:

```
Desktop/Project/Instructions/MaaS
```

---

## 4. Copy the API Key

Inside the **MaaS** folder:

1. Open the file:

```
api-key
```

2. Copy the API key provided in this file.

---

## 5. Update the Connectivity Script

1. Open the file:

```
maas_connectivity_check.py
```

2. Locate the section where the **API key** needs to be provided.

3. Replace the placeholder key with the API key copied from the `api-key` file.

Example:

```python
API_KEY = "PASTE_YOUR_KEY_HERE"
```

---

## 6. Run the Connectivity Check

1. Open a **terminal** in the MaaS folder.

2. Execute the following command:

```bash
python maas_connectivity_check.py
```

---

## 7. Verify LLM Connectivity

If the configuration is correct:

- The script will successfully connect to the **LLM service**.
- A **response from the model** will be displayed in the terminal.

This confirms that the **MaaS LLM connectivity is working properly**.
<img width="1212" height="1252" alt="image" src="https://github.com/user-attachments/assets/352b7ea5-4e5f-458a-b1b9-67bd67b8c199" />

---

## Expected Outcome

Successful execution should indicate:

- API key authentication is valid  
- Connection to the LLM endpoint is successful  
- A model response is returned
