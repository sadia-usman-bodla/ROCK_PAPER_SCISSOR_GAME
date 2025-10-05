# Rock-Paper-Scissors Game 🎮

This is a simple **Rock-Paper-Scissors game** implemented in Python, where the user plays against the computer. The game keeps track of scores and announces the winner after each round and at the end of the match.

---

## 📌 Features

* Play **Rock, Paper, Scissors** against the computer.
* Score tracking for both **user** and **computer**.
* Handles **draws**, **wins**, and **losses**.
* Best of 5 rounds per game session.
* Interactive console input for user choices.

---

## 🎮 How to Play

1. Run the Python script:

```bash
python your_script_name.py
```

2. When prompted:

```
start game
1. Yes
2. NO/Exit
```

* Press `1` to start the game.
* Press `2` to exit.

3. For each round, choose your move:

```
1. rock
2. scissor
3. paper
```

* Enter the number corresponding to your choice.

4. The computer will randomly select a move, and the result will be displayed:

```
Computer value: rock
User value: paper
You win!
```

5. After 5 rounds, the final winner will be announced with scores:

```
Finally you win game
User score: 3
Computer score: 2
```

---

## ⚡ Game Rules

* **Rock vs Paper** → Paper wins
* **Rock vs Scissor** → Rock wins
* **Paper vs Scissor** → Scissor wins
* Same choices → Draw

---

## 🛠️ Requirements

* Python 3.x
* No external libraries required (uses built-in `random` module)

---

## 💡 Notes

* The game is console-based and interactive.
* Scores are automatically tracked and displayed at the end.
* You can play multiple games in a session until you choose to exit.

---

## 🗓 Example Output

```
start game
1.  Yes
2.  NO/Exit
1
Round 1:
User choice: rock
Computer value: scissor
You win!

Round 2:
User choice: paper
Computer value: rock
You win!

Round 3:
User choice: scissor
Computer value: scissor
Game draw!

Final Scores:
User: 3
Computer: 1
Congratulations! You win the game!
```
