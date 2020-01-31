import unittest
import io
import day_1
import day_2
from day_3 import manhattan, solve_step_1, solve_step_2
import day_4
import day_5

class TestDay1(unittest.TestCase):

    def test_step_1(self):
        '''Fuel intakes - step 1'''
        self.assertEqual(day_1.solve_step_1([12]),      2)
        self.assertEqual(day_1.solve_step_1([14]),      2)
        self.assertEqual(day_1.solve_step_1([1969]),    654)
        self.assertEqual(day_1.solve_step_1([100756]),  33583)

    def test_step_2(self):
        '''Fuel intakes - step 2'''
        self.assertEqual(day_1.solve_step_2([14]),      2)
        self.assertEqual(day_1.solve_step_2([1969]),    966)
        self.assertEqual(day_1.solve_step_2([100756]),  50346)


class TestDay2(unittest.TestCase):

    def test_intcodes(self):
        with open('day_2.txt') as f:
            intcodes = [int(i) for i in f.read().split(',')]

        self.assertEqual(day_2.solve_step_1(intcodes), 5110675)
        self.assertEqual(day_2.solve_step_2(intcodes), 4847)

class TestDay3(unittest.TestCase):

    def test_manhattan(self):
        '''Sample Manhattan distances'''
        self.assertEqual(manhattan((100, -100)), 200)
        self.assertEqual(manhattan((3, 3)), 6)

    def test_solve(self):
        '''Step 1 and step 2 example solutions'''
        wires = ['R8','U5','L5','D3'], ['U7','R6','D4','L4']
        self.assertEqual( solve_step_1(*wires), 6 )
        
        wires = ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'], \
                ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']
        self.assertEqual( solve_step_1(*wires), 159 )

        wires = ['R98', 'U47', 'R26', 'D63', 'R33' ,'U87', 'L62', 'D20', 'R33', 'U53', 'R51'], \
                ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']
        self.assertEqual( solve_step_1(*wires), 135 )

        with open('day_3.txt') as f:
            wires = [line.strip().split(',') for line in f]
        
        self.assertEqual( solve_step_1(*wires), 5319 )
        self.assertEqual( solve_step_2(*wires), 122514 )


class TestDay4(unittest.TestCase):

    def test_sorted_passwords(self):
        self.assertTrue(day_4.is_sorted(111111))
        self.assertFalse(day_4.has_duplicates(123456))

    def test_password_with_sequence_of_2(self):
        self.assertFalse(day_4.password_has_sequence_of_2(111222))
        self.assertTrue(day_4.password_has_sequence_of_2(112222))

    def test_step_1(self):
        self.assertEqual(day_4.solve_step_1(145852, 616942), 1767)

    def test_step_2(self):
        self.assertEqual(day_4.solve_step_2(145852, 616942), 1192)


class TestDay5(unittest.TestCase):

    def test_get_operands(self):
        intcodes = [2, 4, 3, 4, 33]
        operands = day_5.get_operands(intcodes, 1, [1, 1, 0], 3)
        expected = [4, 3, 33]
        self.assertListEqual(operands, expected)

    def test_parse_opcode_and_modes(self):
        opcode, modes = day_5.parse_opcode_and_modes(2)
        self.assertEqual(opcode, 2)
        self.assertListEqual(modes, [0, 0, 0])

        opcode, modes = day_5.parse_opcode_and_modes(1002)
        self.assertEqual(opcode, 2)
        self.assertListEqual(modes, [0, 1, 0])

        opcode, modes = day_5.parse_opcode_and_modes(1102)
        self.assertEqual(opcode, 2)
        self.assertListEqual(modes, [1, 1, 0])

    def test_step_2(self):
        cases = [
            {
                'intcodes': [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1],
                'input': '0',
                'expected': 0
            },
            {
                'intcodes': [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1],
                'input': '10',
                'expected': 1
            },
            {
                'intcodes': [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9],
                'input': '0',
                'expected': 0
            },
            {
                'intcodes': [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9],
                'input': '10',
                'expected': 1
            },
            {
                'intcodes': [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31, 1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104, 999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99],
                'input': '3',
                'expected': 1001
            }
        ]
        for case in cases:
            print(case)
            stdin = io.StringIO(case['input'])
            stdout = io.StringIO()
            intcodes = case['intcodes']
            day_5.run(intcodes, stdin, stdout)
            self.assertEqual(int(stdout.getvalue()), case['expected'])



if __name__ == '__main__':
    unittest.main()
    
