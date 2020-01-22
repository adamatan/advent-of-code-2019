import unittest
from solve import manhattan, solve_step_1, solve_step_2, get_wire_coordinates

class TestDay3(unittest.TestCase):

    def test_manhattan(self):
        self.assertEqual(manhattan((100, -100)), 200)
        self.assertEqual(manhattan((3, 3)), 6)

    def test_solve(self):
        wires = ['R8','U5','L5','D3'], ['U7','R6','D4','L4']
        self.assertEqual( solve_step_1(*wires), 6 )
        
        wires = ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'], \
                ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']
        self.assertEqual( solve_step_1(*wires), 159 )

        wires = ['R98', 'U47', 'R26', 'D63', 'R33' ,'U87', 'L62', 'D20', 'R33', 'U53', 'R51'], \
                ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']
        self.assertEqual( solve_step_1(*wires), 135 )

        with open('input.txt') as f:
            wires = [line.strip().split(',') for line in f]
        
        self.assertEqual( solve_step_1(*wires), 5319 )
        self.assertEqual( solve_step_2(*wires), 122514 )

if __name__ == '__main__':
    unittest.main()
    
