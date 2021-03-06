# -*- coding: utf-8 -*-
'''
Created on Sep 6, 2020

@author: rosin
'''
import unittest
import time

from selenium import webdriver

#Verifica que no se permita registrar un miembro con un nombre que contenga mas de 25 letras y espacios
class Test04_Validar_nombre_mas_25_letras_espacios(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.NAME = " ETC Prueba ETC Prueba ETC"
        self.EMAIL = "pruebaetc@gmail.com"
        self.PHONE = "0123456789"
        self.MENSAJE_ESPERADO = "1-25 letters and spaces"
    
    
    def test04_Validar_nombre_mas_25_letras_espacios(self):
        
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
        
        MENSAJE_OBTENIDO = self.driver.find_element_by_xpath("//*[@id='reg']/fieldset/div[1]/div/span").text
        
        self.assertEqual(MENSAJE_OBTENIDO, self.MENSAJE_ESPERADO, f"El mensaje es diferente al esperado: {self.MENSAJE_ESPERADO}")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()