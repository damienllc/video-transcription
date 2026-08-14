## Video Transcription

### 📝 Presentation

This project's purpose is to get a personnal tool, free access, to extract script and translation from a video/audio (YouTube, Dailymotion, ...).\
This application will be installable on your own computer.

### 🧰 Tech point

* **Language:** Python
* **Packages:**
   * *to define*
* ...

### ⚙️ Setup the project

* **Create your Python virtual environment:** 
```sh
cd backend/
python -m venv .venv
```

* **Launch the venv:** 
```sh
cd backend/app/
source .venv/bin/activate
```
> 💡 *To quit the venv, you just need to execute:* `deactivate`

* **Install dependences:**:
```sh
pip install -e .
pip install -e ".[dev]"
```

* **Launch in local:**
```sh
# To execute in your venv
python -m uvicorn app.main:app --reload
```

* **Test the API:**
  * Go on [http://localhost:8000/](http://localhost:8000/)
  * You may see a page with only message : `{"message":"Welcome to the Trans-Script API !"}`
  * Go to the [http://localhost:8000/docs](http://localhost:8000/docs) route, and you access 

### 🖥️ Install the application   
