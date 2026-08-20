from pip._internal.utils import filetypes

Links_list={"math_topic" : ["https://www.youtube.com/watch?v=PnkNCksJYfs", "https://www.youtube.com/watch?v=AFEjozNv6Fw"],
       "english_topic" : ["https://www.youtube.com/playlist?list=PLa73vB0GuqvY6wvkCzf47v7SJ-Mt7g-Js", "https://perpage.io/summary/c88e2590-ffa1-11e7-a7b7-75f73a2fd480/The-Enemy---%D7%A1%D7%99%D7%9B%D7%95%D7%9D-%D7%9C%D7%91%D7%92%D7%A8%D7%95%D7%AA"],
       "history_topic" : ["https://historia.co.il/series/ww1/", "https://campus.ort.org.il/course/view.php?id=79&section=2"],
       "literature_topic" : ["https://www.youtube.com/watch?v=H-qewaOy6jk", "https://a-y.org.il/%D7%97%D7%95%D7%9E%D7%A8%D7%99-%D7%9C%D7%99%D7%9E%D7%95%D7%93/%D7%A1%D7%A4%D7%A8%D7%95%D7%AA/%D7%A1%D7%99%D7%A4%D7%95%D7%A8%D7%99-%D7%A2%D7%92%D7%A0%D7%95%D7%9F/%D7%94%D7%90%D7%93%D7%95%D7%A0%D7%99%D7%AA-%D7%95%D7%94%D7%A8%D7%95%D7%9B%D7%9C-%D7%A9%D7%99-%D7%A2%D7%92%D7%A0%D7%95%D7%9F/"],
       "language_topic" :[ "https://www.lashon.co/%D7%A9%D7%9D-%D7%94%D7%9E%D7%A1%D7%A4%D7%A8", "https://www.gov.il/BlobFolder/dynamiccollectorresultitem/language-expression-and-comprehension/he/mea_language-expression-and-comprehension.pdf"],
       "bible_topic" : ["https://www.kanlomdim.co.il/%D7%97%D7%95%D7%9E%D7%A8%D7%99-%D7%9C%D7%99%D7%9E%D7%95%D7%93/%D7%A7%D7%98%D7%92%D7%95%D7%A8%D7%99%D7%94/%D7%AA%D7%A0-%D7%9A-%D7%9C%D7%9B%D7%99%D7%AA%D7%94-%D7%99", "https://www.daat.ac.il/he-il/tanach/iyunim/neviim"],
       "citizenship_topic" : ["https://sites.google.com/site/ezrahutgroup/Home/part2/zchuyot", "https://he.wikibooks.org/wiki/%D7%90%D7%96%D7%A8%D7%97%D7%95%D7%AA_%D7%9C%D7%91%D7%92%D7%A8%D7%95%D7%AA/%D7%94%D7%9E%D7%A9%D7%98%D7%A8_%D7%95%D7%A8%D7%A9%D7%95%D7%99%D7%95%D7%AA_%D7%94%D7%A9%D7%9C%D7%98%D7%95%D7%9F_%D7%91%D7%99%D7%A9%D7%A8%D7%90%D7%9C/%D7%94%D7%A4%D7%A8%D7%93%D7%AA_%D7%A8%D7%A9%D7%95%D7%99%D7%95%D7%AA:_%D7%90%D7%99%D7%96%D7%95%D7%A0%D7%99%D7%9D_%D7%95%D7%91%D7%9C%D7%9E%D7%99%D7%9D"]}


from tkinter import *
import urllib.request
from urllib.request import urlopen
import dictionary

def topic_links( topic):
    root = Tk()
    for i in range(2):
        link = Label(root, text=dictionary.dic[topic][i], fg="blue", cursor="hand2")
        link.pack()
        link.bind("<Button-1>", lambda e: topic_links(Links_list[topic][i]))
        print(Links_list[topic][i])

    root.mainloop()
topic_links('math_topic')