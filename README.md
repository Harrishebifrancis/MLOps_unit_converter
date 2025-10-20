# 🧮 Unit Converter – LAB 1 (MLOps IE-7374)

This project is a simple **Unit Converter** built as part of **LAB 1 – MLOps (IE-7374)**.  
It demonstrates fundamental software engineering and MLOps practices such as:

- ✅ Virtual environment creation  
- ✅ Git & GitHub project setup  
- ✅ Python module development  
- ✅ Unit testing with **Pytest** and **Unittest**  
- ✅ Continuous Integration (CI) with **GitHub Actions**

---

## 📁 Project Structure

```
MLOps_unit_converter/
├── src/
│   └── unit_converter.py        # Main unit conversion logic
├── test/
│   ├── test_pytest.py           # Pytest tests
│   └── test_unittest.py         # Unittest tests
├── requirements.txt             # Dependencies
├── pytest.ini                   # Configures Python path for pytest
└── .github/
    └── workflows/
        ├── pytest_action.yml    # CI workflow for Pytest
        └── unittest_action.yml  # CI workflow for Unittest
```

---

## 🛠️ Setup & Installation

### 1️⃣ Clone the Repository
```bash
git clone <your_repo_url>
cd MLOps_unit_converter
```

### 2️⃣ Create and Activate a Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate    # macOS/Linux
# or
.venv\Scripts\activate       # Windows
```

### 3️⃣ Install Project Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🧪 Running Tests

### ✅ Run Pytest
```bash
pytest -q
```

Expected output:
```
..........                                                                                                               [100%]
10 passed in 0.01s
```

### ✅ Run Unittest
```bash
python -m unittest -v test.test_unittest
```

Expected output:
```
Ran 5 tests in 0.000s

OK
```

---

## 🤖 Continuous Integration (CI)

This project uses **GitHub Actions** to automate testing every time you push code to GitHub.

- 🧪 **Testing with Pytest** – Runs Pytest tests on push  
- 🧪 **Python Unittests** – Runs Unittest suite on push  

To verify:
1. Go to the **Actions** tab in your GitHub repository.
2. You should see both workflows running.
3. ✅ Green check marks mean everything passed successfully.

---

## 📏 How to Use the Unit Converter

You can use the converter as a Python module or directly from the command line.

### 📌 Option 1: Use It in Python
```python
from src.unit_converter import convert_units

print(convert_units(10, "km", "miles"))             # ➜ 6.2137
print(convert_units(100, "celsius", "fahrenheit"))  # ➜ 212.0
```

### 📌 Option 2: Use It as a CLI (Command Line Tool)

If you added the `if __name__ == "__main__"` block to `src/unit_converter.py`, you can run:

```bash
python -m src.unit_converter 5 km miles
python -m src.unit_converter 100 celsius fahrenheit
```

---

## 🔄 Supported Unit Conversions

| From Unit      | To Unit         |
|----------------|------------------|
| km             | miles            |
| miles          | km               |
| celsius        | fahrenheit       |
| fahrenheit     | celsius          |
| kg             | pounds           |
| pounds         | kg               |

---

## 📊 Learning Outcomes

By completing this project, you practiced:

- 🐍 Creating and managing virtual environments  
- 📁 Structuring a Python project for scalability  
- ✅ Writing unit tests with `pytest` and `unittest`  
- ⚙️ Automating workflows with **GitHub Actions**  
- 🔄 Continuous Integration (CI) and version control with Git & GitHub  

---

## 📜 License

This project was created for educational purposes as part of **LAB 1 – MLOps (IE-7374)**.  
Feel free to use, modify, and extend it for learning or demonstration.

---

🚀 **Congratulations!** You’ve successfully built, tested, and automated a Python project with CI — exactly what this lab is all about.
