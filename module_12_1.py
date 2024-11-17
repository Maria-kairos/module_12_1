import unittest
import runner

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        walk_ = runner.Runner('a')
        for i in range(10):
            walk_.walk()
        self.assertEqual(walk_.distance, 50)
        print ('Test "walk" OK')

    def test_run(self):
        run_ = runner.Runner('a')
        for i in range(10):
            run_.run()
        self.assertEqual(run_.distance, 100)
        print('Test "run" OK')

    def test_challenge(self):
        challenge1 = runner.Runner('a')
        challenge2 = runner.Runner('b')
        for i in range(10):
            challenge1.run()
            challenge2.walk()
        self.assertNotEqual(challenge1.distance, challenge2.distance)
        print('Test "challenge" OK')

if __name__ == '__main__':
    unittest.main()