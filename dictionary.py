import pandas as pd
dic = {"grade" : ["10", "11", "12"],
       "class" : ["math", "english", "history", "literature", "hebrew", "bible", "citizenship"],
       "math_topic" : ["algebra", "geometry"],
       "english_topic" : ["the wave", "the enemy"],
       "history_topic" : ["World War I", "World War II"],
       "literature_topic" : ["tehila", "the lady and the peddler"],
       "hebrew_topic" : ["number name", "reading comprehension"],
       "bible_topic" : ["tora", "nevim"],
       "citizenship_topic" : ["legal rights", "the three authorities"]
       }

mySeries = pd.Series(data = dic["grade"])
print(mySeries)