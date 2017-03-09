from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 
from apscheduler.schedulers.blocking import BlockingScheduler
import webbrowser
import os

def hallscan():
 #Give the link of the webpage in double quotes here
 my_url = "https://in.bookmyshow.com/buytickets/badrinath-ki-dulhania-hyderabad/movie-hyd-ET00041555-MT/20170310"

 uClient = uReq(my_url)
 page_html = uClient.read()
 uClient.close()

 page_soup = soup(page_html,"html.parser")

 containers = page_soup.findAll("li",{"class":"list "})

 for contain in containers:
  hall = contain.findAll("div",{"class":"__name"})
  hall_name = hall[0].a.strong.text
  
  #Check for the hall name by inspect element and place it below
  if hall_name == 'Prasads: Hyderabad':      
   #Open some metallica song if Hit
   webbrowser.open("https://www.youtube.com/watch?v=kShTN0Jz6Jg")     

scheduler = BlockingScheduler()
#Can adjust the time for compiler scheduling by changing seconds
scheduler.add_job(hallscan, 'interval', seconds=10)
scheduler.start()
