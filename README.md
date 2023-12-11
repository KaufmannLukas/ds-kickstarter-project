# ds-kickstarter-project

## Introduction

The project evaluates kickstarter campaign data from 2009 to 2018 in order to predict the expected amount of money for current or future project ideas via an user interface.

## About Dataset

[Kaggle - Kickstarter Projects](https://www.kaggle.com/datasets/ulrikthygepedersen/kickstarter-projects)


## Setup Environment

setup first time:
``` bash
conda env create -f environment.yml
```

activate the environment
```bash
conda activate ds-kickstarter
```

update the environment:
``` bash
conda env update --file environment.yml --prune
```


## Interface Example

run the interface by typing
```bash
python3 main.py
```
here is an example of how the interface and the predicted output looks like:


The input was:

- Name - Intimacy Cards
- Country - Germany             
- Combined_category - Games - Playing Cards
- Goal - 10000                                
- Month - 10                  
- Duration_days - 30                              

```
------------------------------
Welcome to kickstarter prediction project.
What is the name of your project?
>>> Intimacy Cards
Whats your country?
    0: United States
    1: United Kingdom
    2: Canada
    3: Australia
    4: New Zealand
    5: Netherlands 
    6: Sweden
    7: Denmark
    8: Norway
    9: Ireland
   10: Germany
   11: France
   12: Spain
   13: Belgium
   14: Italy
   15: Switzerland
   16: Austria
   17: Luxembourg
   18: Singapore
   19: Hong Kong
   20: Mexico
   21: Japan
>>> 10
What is the goal of your project?
>>> 10000
How many days will your project be online?
>>> 30
On which month will you start?
>>> 10
Select your main category:
    0: Fashion
    1: Film & Video
    2: Art
    3: Technology
    4: Journalism
    5: Publishing
    6: Theater
    7: Music
    8: Photography
    9: Games
   10: Design
   11: Food
   12: Crafts
   13: Comics
   14: Dance
>>> 9
Main category: Games
Select your sub category:
    0: Puzzles
    1: Video Games
    2: Tabletop Games
    3: Games
    4: Gaming Hardware
    5: Live Games
    6: Playing Cards
    7: Mobile Games
>>> 6
Sub category: Playing Cards
Games - Playing Cards
------------------------------------------------------------
         Name_length - 14                  
             Country - Germany             
   Combined_category - Games - Playing Cards
                Goal - 10000               
             Backers - 0                   
               Month - 10                  
       Duration_days - 30                  
                Name - Intimacy Cards      
------------------------------------------------------------

You can expect:
- backers --- prediction -------
|         5 |          626.95$ |
|        10 |          626.95$ |
|        25 |         1738.67$ |
|        50 |         3842.96$ |
|        75 |         6717.12$ |
|       100 |         7719.76$ |
--------------------------------
|       125 |        10792.91$ |
|       150 |        11497.47$ |
|       175 |        13302.41$ |
|       200 |        13302.41$ |
|       250 |        15359.70$ |
|       300 |        19294.52$ |
|       500 |        34452.08$ |
|      1000 |        53332.82$ |
|     10000 |       512139.63$ |
--------------------------------
You need at least 125 backers for your project ;)
```

The final output will make predictions for the calculated 'Pledged' values based on different numbers of backers.

The input example of Intimacy Cards was actually a live kickstarter campaign running on the platform. Looking back after it finished, this kickstarter project collected 11264 $ from 208 backers. Our model predicted that the project would need at least 125 backers to succeed, and if the number of backers is 200, the predicted outcome was 13302.41 $.