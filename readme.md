# 🔄 Currency & Unit Converter

A simple and user-friendly **Currency & Unit Converter** built with **Python and Streamlit**.

This project performs currency, length, weight, and temperature conversions without using any external API. It is designed to practice Python programming, modular code structure, functions, dictionaries, and Streamlit application development.

## 🚀 Features

- 💱 Currency Conversion
  - INR
  - USD
  - EUR
  - GBP
  - JPY
  - AUD
  - CAD

- 📏 Length Conversion
  - Meter
  - Kilometer
  - Centimeter
  - Mile
  - Foot

- ⚖️ Weight Conversion
  - Kilogram
  - Gram
  - Pound
  - Ounce

- 🌡️ Temperature Conversion
  - Celsius
  - Fahrenheit
  - Kelvin

- 🖥️ Interactive Streamlit Web Interface
- ❌ Input validation and error handling
- 🔌 No external API required

## 🛠️ Technologies Used

- Python
- Streamlit
- Functions
- Dictionaries
- Conditional Statements
- Exception Handling
- Modular Programming

## 📁 Project Structure

```text
currency-unit-converter/
│
├── app.py
├── main.py
├── currency.py
├── unit.py
├── utils.py
├── requirements.txt
├── README.md
└── .gitignore
```

### File Description

| File | Description |
|---|---|
| `app.py` | Streamlit web application |
| `main.py` | Command-line version of the converter |
| `currency.py` | Currency conversion logic |
| `unit.py` | Length, weight, and temperature conversion logic |
| `utils.py` | Helper and input-validation functions |
| `requirements.txt` | Python dependencies |
| `.gitignore` | Files ignored by Git |

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/divya234-hue/unit-currency-convertor](https://github.com/divya234-hue/unit-currency-convertor
```

### 2. Open the project directory

```bash
cd currency-unit-converter
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

## 💡 Example

### Currency

```text
1000 INR → USD
```

### Length

```text
10 kilometer → mile
```

### Weight

```text
5 kilogram → pound
```

### Temperature

```text
100 celsius → fahrenheit
```

## 🧠 How It Works

The application uses separate Python modules for different responsibilities.

```text
User Input
    ↓
Streamlit Interface
    ↓
Conversion Function
    ↓
Conversion Calculation
    ↓
Result
```

For currency conversion, predefined exchange rates are stored in `currency.py`. Since this project does not use an API, exchange rates are **manually defined and are not real-time rates**.

## 🔮 Future Improvements

- Add more currencies
- Add more units
- Add conversion history
- Add natural-language input such as:
  `Convert 500 INR to USD`
- Add charts and conversion statistics
- Add live exchange rates using an API
- Deploy the Streamlit application online

## 👩‍💻 Learning Goals

This project was created to practice:

- Python programming
- Writing reusable functions
- Working with dictionaries
- Error handling
- Modular project structure
- Building interactive applications with Streamlit
- Developing projects suitable for an AI Engineering portfolio

