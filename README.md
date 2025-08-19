# 🌡️ Temperature Converter CLI

This is a simple Python command-line tool to convert between different temperature units: Celsius, Fahrenheit, and Kelvin. It also logs your conversion history in a text file and gives options to view or delete it.

---

## 📂 Files

### `main.py`

This is the entry point of the program. It imports and runs the main loop from `tempcon`.

```bash
python main.py
```

### `tempcon.py`

Contains the core logic for:

* Performing temperature conversions
* Logging conversion history
* Viewing and deleting history
* Handling user interaction via CLI

---

## ✅ Features

* 🔁 Converts between:

  * Celsius ↔ Fahrenheit
  * Celsius ↔ Kelvin
  * Fahrenheit ↔ Kelvin
* 📝 Logs each conversion to `history.txt`
* 📖 View all past conversions
* 🗑️ Clear your conversion history
* 🔒 Handles invalid inputs gracefully

---

## 🚀 How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/temperature-converter-cli.git
   cd temperature-converter-cli
   ```

2. Run the program:

   ```bash
   python main.py
   ```

---

## 📋 Usage

When prompted, select an option:

```
Press:
 1 for Celsius to Fahrenheit
 2 for Fahrenheit to Celsius
 3 for Celsius to Kelvin
 4 for Fahrenheit to Kelvin
 5 for Kelvin to Celsius
 6 for Kelvin to Fahrenheit
 or 'v' to view history
 or 'q' to quit
 or 'd' to delete history
```

---

## 📁 Example

```
Press:
 1 for Celsius to Fahrenheit
 ...
Enter to convert: 100
100 Celsius = 212.00 Fahrenheit

Press: v
Your history:
100 Celsius = 212.00 Fahrenheit
```

---

## 🛠️ Requirements

* Python 3.x

No third-party packages are needed.

---

## 📌 Notes

* The conversion history is stored in a local file called `history.txt` in the same directory.
* This is a simple CLI project — perfect for beginners practicing file handling, loops, and exception handling in Python.

---

## 🧑‍💻 Author

ME!
