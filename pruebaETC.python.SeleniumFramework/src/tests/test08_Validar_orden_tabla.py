# -*- coding: utf-8 -*-
'''
Created on Sep 6, 2020

@author: rosin
'''
import unittest
import time

from selenium import webdriver

#Completa el formulario, registra un miembro y 
#verifica que los miembros de la lista esten ordenados por nombre en orden alfabetico
class Test08_Validar_orden_tabla(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.NAME = "APrueba ETC"
        self.EMAIL = "pruebaetcordentabla@gmail.com"
        self.PHONE = "0123456789"

    def test08_Validar_orden_tabla(self):
        
        self.driver.get("http://localhost:8080/jboss-kitchensink-html5-mobile/")
        time.sleep(1)
        
        self.driver.find_element_by_link_text("Add a Member").click()
        time.sleep(1)
        
        self.driver.find_element_by_id("name").send_keys(self.NAME)
        self.driver.find_element_by_id("email").send_keys(self.EMAIL)
        self.driver.find_element_by_id("phoneNumber").send_keys(self.PHONE)
        time.sleep(1)
        
        self.driver.find_element_by_id("register").click()
        time.sleep(1)
        
        self.driver.find_element_by_link_text("List Members").click()
        self.driver.find_element_by_id("refreshButton").click()
        time.sleep(1)
        
        rows = len(self.driver.find_elements_by_xpath("//*[@id='member-table']/tbody/tr"))
        
        prevName = ""
        for n in range(1, rows+1):
            nameTemp = self.driver.find_element_by_xpath("//*[@id='member-table']/tbody/tr["+str(n)+"]/td[1]").text
            if n == 1:
                prevName = nameTemp
                continue
                
            self.assertGreaterEqual(nameTemp, prevName, "Orden alfabetico erroneo") 
            prevName = nameTemp
    
    
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()