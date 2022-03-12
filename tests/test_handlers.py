# test_handlers.py
import unittest
# from chocan_admin_handler import *
# from report_generation_handler import *
# from service_provider_handler import *
import src.chocan_admin_handler
import src.report_generation_handler
import src.service_provider_handler

class TestAuthMethods(unittest.TestCase):
    def test_auth(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
    
    def test_admin(self):
        admin = src.chocan_admin_handler.adminHandler
        #Tests weekly reports
        self.assertAlmostEqual(admin.weeklyReports(self), 1)
        #Tests account creation
        self.assertAlmostEqual(admin.addAcct(self), 1)
        #Tests account deletion
        self.assertAlmostEqual(admin.delAcct(self), 1)
        #Tests account updates
        self.assertAlmostEqual(admin.updateAcct(self), 1)
    
    def test_service(self):
        service = src.service_provider_handler.providerHandler
        #Ensure report deletion is working through service handler
        self.assertAlmostEqual(service.deleteMemberReport(self), None)
        #Ensure report display is working through service handler
        self.assertAlmostEqual(service.displayService(self), None)
        #Ensure report creation is working through service handler
        self.assertAlmostEqual(service.makeReport(self, 4), None)
        #Ensure report requesting is working through service handler
        self.assertAlmostEqual(service.requestReport(self), None)
        #Ensure validation is working through service handler a valid id
        self.assertAlmostEqual(service.validate(self, 1), 1)
        #Ensure validation is working through service handler for an invalid id
        self.assertAlmostEqual(service.validate(self, 0), 0)
if __name__ == '__main__':
    unittest.main()