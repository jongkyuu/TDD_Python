class TestCase:
    def __init__(self, name):
        self.name  = name

    def setUp(self):
        pass
    
    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()
        
class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None
        super().__init__(name)

    def testMethod(self):
        self.log = self.log + "testMethod "
    
    def setUp(self):
        self.log = "setUp "
        
    def tearDown(self):
        self.log += "tearDown "

        
class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")
        
    # def testRunning(self):
    #     self.test.run()
    #     assert(self.test.wasRun)
        
    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert("setUp testMethod tearDown " == test.log)
    
    def tearDown(self):
        pass

# TestCaseTest("testRunning").run()
# TestCaseTest("testSetUp").run()
TestCaseTest("testTemplateMethod").run()

# test = WasRun("testMethod")
# print(test.wasRun)
# test.run()
# print(test.wasRun)
