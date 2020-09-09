# -*- coding: utf-8 -*-
'''
Created on Sep 6, 2020

@author: rosin
'''
import unittest
import time
import json

from selenium import webdriver
#Completa el formulario, registra un miembro y 
#verifica que se genere correctamente el JSON de todos los miembros de la lista
class Test07_Validar_JSON_tabla(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.NAME = "Prueba ETC"
        self.EMAIL = "pruebaetcjsontabla@gmail.com"
        self.PHONE = "0123456789"


    def test07_Validar_JSON_tabla(self):
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
        
        JSON_ESPERADO = "["
        for n in range(1, rows+1):
            dato = self.driver.find_element_by_xpath("//*[@id='member-table']/tbody/tr["+str(n)+"]/th").text.rstrip()
            nameTemp = self.driver.find_element_by_xpath("//*[@id='member-table']/tbody/tr["+str(n)+"]/td[1]").text
            emailTemp = self.driver.find_element_by_xpath("//*[@id='member-table']/tbody/tr["+str(n)+"]/td[2]").text
            phoneTemp = self.driver.find_element_by_xpath("//*[@id='member-table']/tbody/tr["+str(n)+"]/td[3]").text.replace("Call or SMS ", "")
            datoInt = int(dato)
            blog = {'id':datoInt,'name':nameTemp,'email':emailTemp,'phoneNumber':phoneTemp}
            
            if n == rows:
                JSON_ESPERADO += json.dumps(blog, separators=(',', ':'))
            else:
                JSON_ESPERADO += json.dumps(blog, separators=(',', ':')) + ","
        
    
        JSON_ESPERADO += "]"
        
        
        JSON_ELEMENT = self.driver.find_element_by_xpath("//*[@id='member-art']/div[2]/div/div/a")
        self.driver.execute_script("arguments[0].scrollIntoView();", JSON_ELEMENT)
        JSON_ELEMENT.click()
        time.sleep(1)
        
        new_window = self.driver.window_handles[1]
        self.driver.switch_to_window(new_window)
        
        JSON_OBTENIDO = self.driver.find_element_by_xpath("/html/body/pre").text
        
        self.assertEqual(JSON_OBTENIDO, JSON_ESPERADO, f"El JSON es diferente al esperado: {JSON_ESPERADO}")
         
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()