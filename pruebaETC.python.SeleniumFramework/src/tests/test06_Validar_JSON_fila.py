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
#verifica que se genere correctamente el JSON para el miembro agregado
class Test06_Validar_JSON_fila(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.NAME = "Prueba ETC"
        self.EMAIL = "pruebaetcjsonfila@gmail.com"
        self.PHONE = "0123456789"


    def test06_Validar_JSON_fila(self):
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
        
        ID_MAYOR = 0
        ROW_INDEX = 0
        for n in range(1, rows+1):
            dato = self.driver.find_element_by_xpath("//*[@id='member-table']/tbody/tr["+str(n)+"]/th").text
            datoInt = int(dato)
            if datoInt > ID_MAYOR:
                ID_MAYOR = datoInt
                ROW_INDEX = n
        
    
        blog = {'id':ID_MAYOR,'name':self.NAME,'email':self.EMAIL,'phoneNumber':self.PHONE}
        JSON_ESPERADO = json.dumps(blog, separators=(',', ':'))
        
        FILA_JSON = ROW_INDEX
        
        JSON_ELEMENT = self.driver.find_element_by_xpath("//*[@id='members']/tr["+str(FILA_JSON)+"]/td[4]/a")
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