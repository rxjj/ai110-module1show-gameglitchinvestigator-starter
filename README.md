# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] the purpose of the game is to guess a randomly generated secert number within a limited number of attempts while using higher and lower hints.
- [x] I found several bugs while testing the game. The higher and lower hints were backwards, decimal guesses such as 24.9 were converted into 24 instead of being rejected, and starting a new game did not completely clear the previous game's history.
- [x] I fixed the higher and lower hint logic and changed the input handling so decimal guesses are rejected instead of converted into integers. I also moved the core game logic into logic_utils.py and added automated tests to verify the fixes.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. <!--  The game generates a secret number and gives the user a limited number of attempts. Describe this step -->
2. <!--The user enters a number greater than the secret number, and the game correctly tells the user to go lower. -->
3. <!-- The user enters a number lower than the secret number, and the game correctly tells the user to go higher. -->
4. <!--  If the user enters a decimal such as 68.9, the game rejects the input instead of converting it into a whole number. -->
5. <!--When the user enters the correct secret number, the game displays the winning message and updates the score.-->

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# python -m pytest
============================= test session starts ==============================
collected 5 items

tests/test_game_logic.py .....                                      [100%]

============================== 5 passed in 0.05s ===============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
