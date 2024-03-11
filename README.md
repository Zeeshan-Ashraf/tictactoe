# How to run this game
clone the repo into local system by running command `git clone git@github.com:Zeeshan-Ashraf/tictactoe.git`

you can run this inside a python environment `venv` (runs on `python 3.9` version)

### create venv
`python3 -m venv <nameOfEnv>`


### activate venv
`source <nameOfEnv>/bin/activate`

the activation of env will show as `(<nameOfEnv>)` as prefix in terminal


### install requirements (if any)
install requirements.txt by running command
`pip3 install -r requirements.txt`

### run the game
1. change directory to folder where `main.py` exists

2. execute command: `python3 main.py`
3. provide name of player
4. provide row col (0 indexed) with space seperated

e.g:

```
(tictactoe) ftz@ftz-MacBook-Air tictactoe % python3 main.py
Enter Name of Player 1: z
Enter Name of Player 2: s
| | | |
| | | |
| | | |
z 's Symbol:  X
s 's Symbol:  O

Player z turn
Enter Row Col: 1 1
| | | |
| |X| |
| | | |

Player s turn
...
...
```

# LLD Design draw.io: 
`https://drive.google.com/file/d/1iB63FB7C4KUvtDWPkK2mKbitjsfBWbtz/view?usp=sharing`

check folder structure & models 