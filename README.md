[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/jUSnJpKv)

# Agarpyo
Agarpyo is a game inspired by Agar.io which allows you to play solo with the aim of achieving the best possible score within a given time. To gain points, you have to eat foods.

# Installation

## 👨‍💻 Prerequisites
- Git
- Anaconda Navigator

## 🎯 Installation step by step (on Windows)
1. **Clone the project where you want it to be**
```
https://github.com/B2-Info-23-24/agarpyo-b2-b-AlexNbl27.git
```
💡 I recommend to clone the folder in `Downloads`

2. **Rename the created folder**
```
mv agarpyo-b2-b-AlexNbl27 agarpyo-noblet
```
3. **Move into the renamed folder**
```
cd agarpyo-noblet
```
4. **Open Anaconda Navigator**

5. **Import the python environment**
<br>In the application, go to the tab `Environements`. Then, you should see a button `Import`  at the bottom of the window. Click on it. A popup appears. Click on the folder icon just under the text `Local Drive`. The Windows explorer opens. Now, you have to find the location where you put the folder `agarpyo`. Once you find it, open it and click on the file `agarpyo_env.yaml`. Finally, click on the `Import` button.

6. **Open the environment**
<br> Once the python environment is imported, go to the tab `Home`. Make sure to change the current environment to `agarpyo_env`. You should read : *All applications on agarpyo_env*. If it is correct, you can now install (or launch if already installed) the `CMD.exe Prompt` by clicking on the button `Install`.

7. **Move to project folder location**
<br>This is the step where you have to do it a little bit by yourself. In the command prompt, you have to navigate to the location where you put the folder `agarpyo-noblet`. You can use these two commands :
- Navigate inside a folder
```
cd folder_name
```
- Navigate to previous location :
```
cd ..
```
💡 If you followed my recommendation and you put the cloned folder into `Downloads`, you normally just have to type the following command :
```
cd Downloads/agarpyo-noblet
```
Once you finally found the folder, you should see a line like that in your command prompt :
```
(agarpyo_env) C:<path>\Agarpyo>
```
`<path>` should be the rest of your path before your folder's location. If you enter the following command, you should see all these files and folders :
```
dir
```
```
05/02/2024  21:08                 8 .gitignore
05/02/2024  21:14    <DIR>          .vscode
07/02/2024  12:24               560 agarpyo_env.yaml
06/02/2024  22:16    <DIR>          App
07/02/2024  13:47             2 255 README.md
```

8. **Launch the project**
```
python App/main.py
```

**Here we go! Agarpyo is yours 🥳**

# Features

## Game modes

### 🖱️ Play with mouse

When you are in the menu, you can choose to play with mouse by clicking on the button `Play With Mouse`. Then, the player will follow your mouse.

### ⌨️ Play with keyboard

When you are in the menu, you can choose to play with keyboard by clicking on the button `Play With Keyboard` or clicking on the `Key P`.
<br> There are four keys to move the player :
- `Key ARROW UP`
- `Key ARROW DOWN`
- `Key ARROW RIGHT`
- `Key ARROW LEFT`

## Difficulties

- **Easy (default)**, when the game will starts, there will be **2 traps** and **5 foods**.

- **Normal**, when the game will starts, there will be **3 traps** and **3 foods**.

- **Hard**, when the game will starts, there will be **4 traps** and **2 foods**.

## Interface

### 🤟 Navigation

Here are differentes ways to navigate among the application :
- `Key Q` : Quit the application
- `Close button` : Quit the application
- `Escape button` : Exit the current activity. If you are in the game, it returns in the menu. If you are in the menu, it quits the application.

### 🎨 Colors

- **🔵 Blue** : it represents the `foods`
- **🟣 Purple** : it represents the `traps`
- **🔴 Red** : it represents the `player`







