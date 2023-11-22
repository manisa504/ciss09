![image](https://miro.medium.com/v2/resize:fit:800/1*Y5wIQF5GtCGkkpGVy8axCw.png)
# Cookie Cats: Understanding Player Retention through AB Testing

## Project Overview
Cookie Cats is a popular mobile puzzle game developed by Tactile Entertainment. This project centers around an analysis of an AB test conducted within the game. The primary focus is to understand how the placement of gates within the game, specifically moving the first gate from level 30 to level 40, affects player retention.

## Project Content
The project is structured as follows:

### 1. Introduction
This section provides an introduction to Cookie Cats, the game mechanics, and the rationale behind gate placement changes.

### 2. The AB-test Data
Detailed information about the dataset used for the analysis is provided, including player variables, game rounds played, and retention metrics.

### 3. Distribution of Game Rounds
Analysis and visualization of the distribution of game rounds played during the initial week after installing the game.

### 4. Overall 1-day Retention
An exploration of the 1-day retention rate, a critical metric indicating the percentage of players returning to play the game a day after installation.

### 5. 1-day Retention by AB-group
Comparison of 1-day retention between players in the control group (gate at level 30) and the experimental group (gate at level 40).

### 6. Confidence in the Difference
Utilizing bootstrapping to estimate the uncertainty around the observed difference in 1-day retention between the two AB-groups.

### 7. 7-day Retention by AB-group
Similar analysis as done for 1-day retention, now focusing on the 7-day retention metrics between the two AB-groups.

### 8. Bootstrapping the Difference Again
Bootstrapping analysis to understand the uncertainty and differences in 7-day retention between the gate placements.

### 9. Conclusion
Summarizing findings from the analysis and drawing conclusions regarding the optimal placement of gates for maximizing player retention.

## Should We Move the Gate from Level 30 to Level 40?
As per the data and the bootstrap analysis conducted, the conclusion is drawn based on the evidence gathered. The decision regarding whether to move the gate from level 30 to level 40 is indicated in the project, stating "move_to_level_40 = False" or "move_to_level_40 = True".

---

This README provides a structured overview of the analysis conducted on the Cookie Cats game, focusing on player retention metrics concerning gate placement. Each section delves into specific aspects of the AB test analysis, aiming to derive insights crucial for game improvement and player engagement.

Please refer to the detailed notebooks and code for in-depth analysis and methodologies used in the project.

