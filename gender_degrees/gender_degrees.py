# Title: gender_degrees.py
# Desc: The "Storytelling Through Data Visualization" guided project from
#       Dataquest, focusing on making line charts look cleaner and comparable.
# Date: 3/11/2017
# Note: percent-bachelors-degrees-women-usa.csv contains the percentage of 
#       bachelor's degrees granted to women from 1970 to 2012. The data came
#       from The Department of Education Statistics and was cleaned up by
#       Randal Olsen, at University of Pennsylvania.

get_ipython().magic('matplotlib inline')
import pandas as pd
import matplotlib.pyplot as plt

women_degrees = pd.read_csv('percent-bachelors-degrees-women-usa.csv')

stem_cats = ['Engineering', 'Computer Science', 'Psychology', 'Biology', 
             'Physical Sciences', 'Math and Statistics']
lib_arts_cats = ['Foreign Languages', 'English', 'Communications and Journalism', 
                 'Art and Performance', 'Social Sciences and History']
other_cats = ['Health Professions', 'Public Administration', 'Education', 
              'Agriculture','Business', 'Architecture']

cb_dark_blue = (0/255,107/255,164/255)
cb_orange = (255/255, 128/255, 14/255)

fig = plt.figure(figsize=(18, 18))

# First column. STEM majors.
for sp in range(0,18,3):
    cat_index = int(sp/3)
    ax = fig.add_subplot(6,3,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[stem_cats[cat_index]], 
            c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[stem_cats[cat_index]], 
            c=cb_orange, label='Men', linewidth=3)
    ax.spines["right"].set_visible(False)    
    ax.spines["left"].set_visible(False)
    ax.spines["top"].set_visible(False)    
    ax.spines["bottom"].set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_yticks([0,100])
    ax.axhline(50, c=(171/255, 171/255, 171/255), alpha=0.3)
    ax.set_title(stem_cats[cat_index])
    ax.tick_params(bottom="off", top="off", left="off", right="off", 
                   labelbottom="off")
    
    if cat_index == 0:
        ax.text(2005, 86, 'Men')
        ax.text(2003, 8, 'Women')
    elif cat_index == 5:
        ax.text(2005, 65, 'Men')
        ax.text(2003, 33, 'Women')
        ax.tick_params(labelbottom="on")

# Second column. Liberal Arts majors.
for sp in range(1,16,3):
    cat_index = int((sp-1)/3)
    ax = fig.add_subplot(6,3,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[lib_arts_cats[cat_index]], 
            c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[lib_arts_cats[cat_index]], 
            c=cb_orange, label='Men', linewidth=3)
    ax.spines["right"].set_visible(False)    
    ax.spines["left"].set_visible(False)
    ax.spines["top"].set_visible(False)    
    ax.spines["bottom"].set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_yticks([0,100])
    ax.axhline(50, c=(171/255, 171/255, 171/255), alpha=0.3)
    ax.set_title(lib_arts_cats[cat_index])
    ax.tick_params(bottom="off", top="off", left="off", right="off", 
                   labelbottom="off")
    
    if cat_index == 0:
        ax.text(2003, 79, 'Women')
        ax.text(2005, 20, 'men')
    elif cat_index == 4:
        ax.tick_params(labelbottom="on")
        
# Third column. Other majors.
for sp in range(2,18,3):
    cat_index = int((sp-2)/3)
    ax = fig.add_subplot(6,3,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[other_cats[cat_index]], 
            c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[other_cats[cat_index]], 
            c=cb_orange, label='Men', linewidth=3)
    ax.spines["right"].set_visible(False)    
    ax.spines["left"].set_visible(False)
    ax.spines["top"].set_visible(False)    
    ax.spines["bottom"].set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_yticks([0,100])
    ax.axhline(50, c=(171/255, 171/255, 171/255), alpha=0.3)
    ax.set_title(other_cats[cat_index])
    ax.tick_params(bottom="off", top="off", left="off", right="off", 
                   labelbottom="off")
    
    if cat_index == 0:
        ax.text(2003, 91, 'Women')
        ax.text(2005, 7, 'men')
    elif cat_index == 5:
        ax.text(2005, 62, 'Men')
        ax.text(2003, 33, 'Women')
        ax.tick_params(labelbottom="on")

plt.savefig("gender_degrees.png")
plt.show()



