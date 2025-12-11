# CSC226 Final Project

## Instructions

**Author(s)**: Nahom Mesfin, Naod Ksmu

**Google Doc Link**: https://docs.google.com/document/d/1c5iFrh-c3z9K5B_EGnLQzz5f1H1ZO61oGB9eO4YOZB8/edit?usp=sharing

---

## Milestone 1: Setup, Planning, Design

**Title**: "Clone of Super mario."

**Purpose**:"To create game like Super Mario, with player movement, enemies, collectibles, and levels, while practicing OOP, game design, and teamwork."

**Source Assignment(s)**: `Team work 11 : The Legend of Tuna`

**CRC Card(s)**:
  - Create a CRC card for each class that your project will implement.
  - See this link for a sample CRC card and a template to use for your own cards (you will have to make a copy to edit):
    [CRC Card Example](https://docs.google.com/document/d/1JE_3Qmytk_JGztRqkPXWACJwciPH61VCx3idIlBCVFY/edit?usp=sharing)
  - Tables in markdown are not easy, so we suggest saving your CRC card as an image and including the image(s) in the 
    README. You can do this by saving an image in the repository and linking to it. See the sample CRC card below - 
    and REPLACE it with your own:
  
![Don't leave me in your README!](image/img_1.png "Image of CRC card as an example. Upload your CRC card(s) in place of this one. ")
![Don't leave me in your README!](image/img_2.png "Image of CRC card as an example. Upload your CRC card(s) in place of this one. ")
![Don't leave me in your README!](image/img_3.png "Image of CRC card as an example. Upload your CRC card(s) in place of this one. ")
![Don't leave me in your README!](image/img_4.png "Image of CRC card as an example. Upload your CRC card(s) in place of this one. ")


**Branches**: This project will **require** effective use of git. 

Each partner should create a branch at the beginning of the project, and stay on this branch (or branches of their 
branch) as they work. When you need to bring each others branches together, do so by merging each other's branches 
into your own, following the process we've discussed in previous assignments, then re-branching out from the merged code.  

```
    Branch 1 starting name: Ksmun
    Branch 2 starting name: Terrefen
```

### References 

Throughout this project, you will likely use outside resources. Reference all ideas which are not your own, 
and describe how you integrated the ideas or code into your program. This includes online sources, people who have 
helped you, AI tools you've used, and any other resources that are not solely your own contribution. Update this 
section as you go. DO NOT forget about it!


We have used Chatgpt 
-> To help up with game logic especially cameral logic where the character stays the same place and other world things move. 
-> To deal with gravity logic when mario jumps, that was confusing to implement hence it helped
https://www.pygame.org/docs/ Pygame documentation to understand the most of the methods  
https://supermarioplay.com/fullscreen supermario game for reference, it helped us see what we are working with and understand how to clone it better

---

## Milestone 2: Code Setup and Issue Queue

 Most importantly, keep your issue queue up to date, and focus on your code. 🙃

 Reflect on what you’ve done so far. How’s it going? Are you feeling behind/ahead? What are you worried about? 
What has surprised you so far? Describe your general feelings. Be honest with yourself; this section is for you, not me.

```
**So far, the project has been a learning experience for us. We feel somewhere between on track and slightly behind, mainly
 because some tasks took longer than expected. The setup phase surprised us—those small configuration issues took more 
 time than we thought they would. We’ve also realized how important it is to write cleaner, more organized code early 
 on to avoid confusion later. Emotionally, we’re feeling a mix of motivation and a bit of pressure, but in a productive way.
  We’re getting more comfortable with debugging and planning our work. Our main concerns now are staying consistent with 
  updates and managing our time effectively, but overall, we believe we can fully catch up if we stay focused.
```

---

## Milestone 3: Virtual Check-In

Indicate what percentage of the project you have left to complete and how confident you feel. 

**Completion Percentage**: `40%`

**Confidence**: Describe how confident you feel about completing this project, and why. Then, describe some 
  strategies you can employ to increase the likelihood that you'll be successful in completing this project 
  before the deadline.

```
    *we feel somewhat confident about completing this project. we understand the basics, but some parts are still challenging. 
    we believe we can finish it if we stay focused and work step by step.To improve my chances of finishing on time, We will break the project into small tasks,
    work on it a little every day, test my code often, and ask for help when I get stuck.*
```

---

## Milestone 4: Final Code, Presentation, Demo

### User Instructions

In a paragraph, explain how to use your program. Assume the user is starting just after they hit the "Run" button 
in PyCharm.

After hitting the “Run” button in PyCharm, the game window opens automatically and the program begins.
You control Mario using the arrow keys: the left and right arrows move him across the world, and the up arrow makes him jump.
As you move, the camera scrolls to follow Mario, revealing blocks, enemies, flowers, and eventually the princess at the end 
of the level. Mario can land on top of blocks, hit them from below to break or collect coins, and defeat enemies by jumping
on them. If he touches an enemy from the side, he loses a life and is pushed backward. Your score appears at the top of the
screen along with your remaining lives. The goal is simple: reach the princess at the far right side of the map. If Mario 
runs out of lives, a Game Over screen appears; if he reaches the princess, you’ll see a Win screen. You can close the game
at any time by clicking the window’s X button.

### Errors and Constraints
Every program has bugs or features that had to be scrapped for time. These bugs should be tracked in the issue queue. 
You should already have a few items in here from the prior weeks. Create a new issue for any undocumented errors and 
deficiencies that remain in your code. Bugs found that aren't acknowledged in the queue will be penalized.

### Reflection

Each partner should write three to four well-written paragraphs address the following (at a minimum):
- Why did you select the project that you did?
- How closely did your final project reflect your initial design?
- What did you learn from this process?
- What was the hardest part of the final project?
- What would you do differently next time, knowing what you know now?
- How well did you work with your partner? What made it go well? What made it challenging?

```
  Partner 1: *
  
  We chose this project because we both grew up on platformer games and wanted to try building one from scratch. 
  The final result isn’t exactly what we first planned, but it’s close enough that we’re proud of it. We got movement,
  enemies, blocks, and scrolling working, even though things like collision and physics took way longer than we expected.
  The whole process taught us a lot about organizing code, debugging, and actually planning before jumping in.

  The hardest part was definitely getting collisions to feel right one tiny mistake broke everything. If we did this again,
  we’d set up cleaner structure from the start and test things earlier. Working together went well overall; we communicated,
  helped each other when things got frustrating, and split the work in a way that made sense. The only challenge was staying
  consistent, but once we found our rhythm, the project moved smoothly.
  
  *
```

```
 Partner 2: **Replace this with your reflection
```

---