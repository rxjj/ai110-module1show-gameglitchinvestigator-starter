# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started? - When I first ran the game, it did open normally but I've noticed some problems while testing it. One bug was that the hints were backwards. Like when it said the sercert number was 24 and I guessesd 50, the game told me to go higher instead of lower. Second I also did notice that starting a new did not clear the old guess I've made. Third, decimal guesses such as 24.9 were converted to 24 and accepted as the correct answer.  

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|Secret = 24, Guess 50|Game should say "Go LOWER" |Game said "Go Higher" | No console error |
|Clicked "New Game" after making guesses| Previous guess history should reset | Old guesses remained in the history |No console error |
|Secret = 24, Guess = 24.9 | Decimal input should be rejected as an invaild whole-number guess |Game converted 24.9 to 24 and said "Correcte!" |No console error |

---

## 2. How did you use AI as a teammate? I used ChatGPT and GitHub Copilot as AI tools while working on this project. ChatGPT helped me understand the bugs and guided me through testing, while Copilot helped me make changes directly to the code. One correct suggestion from Copilot was to move check_guess() into logic_utils.py and fix the backwards higher/lower hints. I verified this by running the game with a secret number of 68 and guessing 80, and the game correctly told me to go lower. I did not accept every AI result without checking it because I reviewed the changes and tested them myself before keeping them instead of assuming they were correct. Copilot also suggested updating parse_guess() so that an input with only spaces would be treated as an empty guess. I decided not to make that change because it wasn't related to the two main bugs I was trying to fix. I wanted to keep the changes simple and focus on fixing the backwards hints and the decimal input problem. I tested my fixes by running pytest and testing both problems myself in the game.
 
---

## 3. Debugging and testing your fixes? I decided a bug was really fixed by testing the game after making the changes instead of just assuming the code was correct. I ran pytest and all five tests passed. I also manually tested the game by guessing 80 when the secret number was 68, and it correctly told me to go lower. I tested the decimal bug by entering 68.9, and the game rejected it instead of converting it to 68. AI helped me understand what the tests were checking and helped create tests for the bugs I was fixing.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
