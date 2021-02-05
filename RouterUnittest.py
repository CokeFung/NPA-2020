from RouterClass import Router
import unittest

newHostname = "R1"
newBrand = "Cisco"
newModel = "Catalyst 8300-1N1S-4T2X"

class TestRouter(unittest.TestCase):
        
    def test_01_basicMethods(self):
        print("\n---------------------basicMethods---------------------")
        hostname = "temp hostname"
        brand = "temp brand"
        model = "temp model"
        r1 = Router(hostname, brand, model)
        # set hostname, brand, model after created an objecet
        r1.setHostname(newHostname)
        r1.setBrand(newBrand)
        r1.setModel(newModel)
        # get new values of hostname, brand, model
        self.assertTrue(r1.getHostname() == newHostname)
        self.assertTrue(r1.getBrand() == newBrand)
        self.assertTrue(r1.getModel() == newModel)
        del r1

    def test_02_addInterface(self):
        print("\n---------------------addInterface---------------------")
        r1 = Router(newHostname, newBrand, newModel)
        intname = "g0/0"
        self.assertTrue(r1.add_interface(intname))     # add new interface
        self.assertFalse(r1.add_interface(intname))    # interface already exists
        del r1

    def test_03_getInterface(self):
        print("\n---------------------getInterface---------------------")
        r1 = Router(newHostname, newBrand, newModel)
        r1.add_interface("g0/0")
        self.assertFalse(r1.get_interface("g0/0") == {})     # found interface
        self.assertTrue(r1.get_interface("g0/1") == {})      # not found interface 
        del r1

    def test_04_showInterfaces(self):
        print("\n---------------------showInterface--------------------")
        r1 = Router(newHostname, newBrand, newModel)
        r1.add_interface("g0/0")
        r1.add_interface("g0/1")
        self.assertTrue(r1.show_interfaces())           # show all interfaces
        self.assertTrue(r1.show_interfaces("g0/0"))     # show only selected interface
        self.assertFalse(r1.show_interfaces("fake0/0")) # show error if interface not found
        del r1

    def test_05_connectToAnotherRouter(self):
        print("\n---------------connectToAnotherRouter-----------------")
        r1 = Router("R1", newBrand, newModel)
        r2 = Router("R2", newBrand, newModel)
        r3 = Router("R3", newBrand, newModel)
        r1.add_interface("g0/0")
        r2.add_interface("g0/0")
        r3.add_interface("g0/0")
        self.assertTrue(r1.connect_to(des_router=r2, intf="g0/0", withIntf="g0/0")) # Connect between R1 g0/0 and R2 g0/0
        self.assertFalse(r3.connect_to(des_router=r1, intf="g0/0", withIntf="g0/0")) # Show error when connect to R1 g0/0 with R3 g0/0
        del r1
        del r2
        del r3

    def test_06_show_cdp_neighbor(self):
        # Just print information
        print("\n------------------show_cdp_neighbor-------------------")
        r1 = Router("R1", newBrand, newModel)
        r2 = Router("R2", newBrand, newModel)
        r3 = Router("R3", newBrand, newModel)
        r1.add_interface("g0/0")
        r1.add_interface("g0/1")
        r2.add_interface("g0/0")
        r3.add_interface("g0/0")
        r1.connect_to(des_router=r2, intf="g0/0", withIntf="g0/0")
        r3.connect_to(des_router=r1, intf="g0/1", withIntf="g0/0")
        r1.show_cdp_neighbor()
        r2.show_cdp_neighbor()
        r3.show_cdp_neighbor()

if __name__ == "__main__":
    unittest.main()
