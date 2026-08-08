# 🎯 Mastermind – 4-Digit Number Guessing Game

A simple **Python console-based Mastermind game** where the computer generates a random 4-digit number and the player tries to guess it. 🧠🎮

The game provides feedback about how many digits from the beginning of the guess are correct.

---

## 📌 Table of Contents

- [✨ Features](#-features)
- [🛠️ Technologies Used](#️-technologies-used)
- [📂 Project Structure](#-project-structure)
- [🎮 How the Game Works](#-how-the-game-works)
- [🔄 Program Flow](#-program-flow)
- [🧩 Game Logic](#-game-logic)
- [🔍 Digit-by-Digit Comparison](#-digit-by-digit-comparison)
- [▶️ How to Run](#️-how-to-run)
- [💻 Example Gameplay](#-example-gameplay)
- [🧠 Concepts Learned](#-concepts-learned)
- [🚀 Possible Improvements](#-possible-improvements)
- [🐛 Important Note](#-important-note)
- [📈 Project Roadmap](#-project-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [🎯 Summary](#-summary)

---

# ✨ Features

- 🎲 Generates a random 4-digit secret number.
- 🔢 Accepts only valid 4-digit guesses.
- 🛡️ Handles invalid input using `try-except`.
- 🔁 Allows the player to keep guessing until the correct number is found.
- 📊 Counts the number of attempts.
- 🎯 Checks digits from left to right.
- 💬 Provides feedback about correctly matched digits.
- 🏆 Displays a congratulatory message when the player wins.

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| 🐍 Python | Main programming language |
| 🎲 `random` module | Generates the secret number |
| 🔄 `while` loop | Repeats the guessing process |
| 🔢 `int()` | Converts user input into an integer |
| 🛡️ `try-except` | Handles invalid input |
| 🔍 `enumerate()` | Checks digits by position |
| 📝 f-strings | Displays dynamic messages |

---

# 📂 Project Structure

```text
Mastermind/
│
├── 🐍 mastermind.py
│
└── 📖 README.md


                 🎮 START
                    │
                    ▼
          🎲 Generate Secret Number
                    │
                    ▼
            👋 Welcome Message
                    │
                    ▼
             ⌨️ Enter Guess
                    │
                    ▼
          ❓ Is the input valid?
             /             \
           NO               YES
           │                 │
           ▼                 ▼
     ❌ Show Error       📊 Increase
       Message             Attempts
           │                 │
           │                 ▼
           │          🎯 Is Guess Correct?
           │             /          \
           │           YES           NO
           │            │             │
           │            ▼             ▼
           │         🏆 WIN!      🔍 Compare
           │                         Digits
           │                           │
           │                           ▼
           │                    💬 Give Feedback
           │                           │
           └───────────────────────────┘
                                       │
                                       ▼
                                  🔁 Try Again