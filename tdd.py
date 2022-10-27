class TestCase:
    def __init__(self, name):
        self.name  = name

    def setUp(self):
        pass
    
    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()
        
class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None
        super().__init__(name)

    def testMethod(self):
        self.wasRun = 1
    
    def setUp(self):
        self.wasRun = 1
        self.wasSetUp = 1
        
class TestCaseTest(TestCase):
    def testRunning(self):
        test = WasRun("testMethod")
        assert(not test.wasRun)
        test.run()
        assert(test.wasRun)
        
    def testSetUp(sefl):
        test = WasRun("testMethod")
        test.run()
        print(test.wasSetUp)
        assert(test.wasSetUp)
    

TestCaseTest("testRunning").run()
TestCaseTest("testSetUp").run()

# test = WasRun("testMethod")
# print(test.wasRun)
# test.run()
# print(test.wasRun)
