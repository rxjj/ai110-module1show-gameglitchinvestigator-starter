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

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
