'''
Created on Sep 7, 2020

@author: rosin
'''
import unittest
import time
from selenium import webdriver

#Ingresa a la url y da clic en el link List Members, 
#abre otra pestaña con la misma url, completa el formulario y registra un miembro, 
#se posiciona sobre la primera pestaña abierta y verifica que al dar clic al botón Refresh Members 
#se actualice la lista con el miembro agregado en la segunda pestaña 
class Test12_Refrescar_tabla(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.NAME = "Prueba ETC Refresh"
        self.EMAIL = "refreshmembers@gmail.com"
        self.PHONE = "0123456789"

    def test12_Refrescar_tabla(self):
        
        self.driver.get("http://localhost:8080/jboss-kitchensink-html5-mobile/")
        
        self.driver.find_element_by_link_text("List Members").click()
        
        time.sleep(5)
        
        rows = len(self.driver.find_elements_by_xpath("//*[@id='member-table']/tbody/tr"))
        
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
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
        
        self.driver.switch_to.window(self.driver.window_handles[0])
        
        time.sleep(5)
        
        self.driver.find_element_by_id("refreshButton").click()
        
        time.sleep(5)
        
        rowsFinal = len(self.driver.find_elements_by_xpath("//*[@id='member-table']/tbody/tr"))
        
        self.assertEqual(rows+1, rowsFinal)
        


        
        
        


    def tearDown(self):
        self.driver.close()





if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()