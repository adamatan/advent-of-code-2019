import unittest
import hashlib
import day_1
import day_2
from day_3 import manhattan, solve_step_1, solve_step_2, get_wire_coordinates
import day_4
import day_6
import day_8

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


class TestDay6(unittest.TestCase):

    STEP_1_SAMPLE_DATA = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L']
    STEP_2_SAMPLE_DATA = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L', 'K)YOU', 'I)SAN']

    def test_step_1_sample_data(self):
        '''Count on a small set from the AOC web apge'''
        orbits, _ = day_6.parse(self.STEP_1_SAMPLE_DATA)
        self.assertEqual(day_6.count_orbit_pairs(orbits, day_6.SUN), 42)

    def test_step_1_full_input_data(self):
        '''Count from the full input data file'''
        input_data = day_6.get_input_data(day_6.INPUT_FILENAME)
        orbits, _ = day_6.parse(input_data)
        self.assertEqual(day_6.count_orbit_pairs(orbits, day_6.SUN), 223251)

    def test_step_2_sample_data(self):
        '''Test orbit BFS traversal with short sample data'''
        _, symmetric_orbits = day_6.parse(self.STEP_2_SAMPLE_DATA)
        self.assertEqual(day_6.bfs(symmetric_orbits, 'YOU', 'SAN'), 4)

    def test_step_2_full_input_data(self):
        '''Test orbit BFS traversal with full input file data'''
        input_data = day_6.get_input_data(day_6.INPUT_FILENAME)
        _, symmetric_orbits = day_6.parse(input_data)
        self.assertEqual(day_6.bfs(symmetric_orbits, 'YOU', 'SAN'), 430)

class TestDay8(unittest.TestCase):
    def test_step_1(self):
        '''Test step 1 with the file input'''
        pixels = day_8.parse_input()
        actual = day_8.solve_step_1(pixels, day_8.INPUT_HEIGHT, day_8.INPUT_WIDTH)
        expected = 1452
        self.assertEqual(actual, expected)

    def test_layer_merge(self):
        '''Test layer merge with a small example'''
        test_input = ['0', '2', '2', '2', '1', '1', '2', '2', '2', '2', '1', '2', '0', '0', '0', '0']
        actual_image = day_8.merge_layers(test_input, 2, 2)
        expected_image = ['0', '1', '1', '0']
        self.assertEqual(actual_image, expected_image)

    def test_step_2(self):
        pixels = day_8.parse_input()
        actual = day_8.solve_step_2(pixels, day_8.INPUT_HEIGHT, day_8.INPUT_WIDTH)
        actual_hash = hashlib.sha256(''.join(tuple(actual)).encode()).hexdigest()
        expected_hash = 'e356894b6073bed46eeccde6e56075a4e16f760efcd432188f15b26757210e89'
        self.assertEqual(actual_hash, expected_hash)

if __name__ == '__main__':
    unittest.main()
    
