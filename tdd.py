class TestCase:
    def __init__(self, name):
        self.name  = name

    def setUp(self):
        pass
    
    def run(self):
        result = TestResult()
        result.testStarted()
        
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()
        return result
        
class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None
        super().__init__(name)

    def setUp(self):
        self.log = "setUp "

    def testMethod(self):
        self.log = self.log + "testMethod "

    def testBrokenMethod(self):
        raise Exception
        
    def tearDown(self):
        self.log += "tearDown "

        
class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")
        
    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert("setUp testMethod tearDown " == test.log)
    
    def tearDown(self):
        pass

    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert("1 run, 0 failed" == result.summary())

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        result = test.run()
        assert("1 run, 1 failed" == result.summary())

class TestResult:
    def __init__(self):
        self.runCount = 0
    
    def testStarted(self):
        self.runCount += 1

    def summary(self):
        return f"{self.runCount} run, 0 failed"

TestCaseTest("testTemplateMethod").run()
TestCaseTest("testResult").run()
TestCaseTest("testFailedResult").run()