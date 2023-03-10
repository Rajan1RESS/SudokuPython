"""Scraping soduko from web"""
from bs4 import BeautifulSoup
import requests

class Scrape:

    def __init__(self):
        self.values = []

    
    def scrape(self):
         sudoku_page = requests.get("https://four.websudoku.com/?",timeout=10)
         soup = BeautifulSoup(sudoku_page.content,"html.parser")
         table = soup.find("table",id={"puzzle_grid"})
         for e in table.findAll("input"):
            self.values.append(e.get("value"))



    def change_to_mat(self):
        mat = [[],[],[],[],[],[],[],[],[]]
        i = 0
        j = 0
        for item in self.values:
            if i==9:
                i=0
                j+=1
            if item is None:
                mat[j].append(0)
            else:
                mat[j].append(item)
            i+=1
        return mat    
    
