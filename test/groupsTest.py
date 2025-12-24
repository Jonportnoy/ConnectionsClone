import unittest
from src.groups import get_groups

def printGroups(groups: tuple) -> None:
    """
    prints groups in readable format
    :param groups: groups to print out
    """
    for group in groups:
        print(f"{group[0]}:\n   {group[1]}\n   {group[2]}\n   {group[3]}\n   {group[4]}")



class MyTestCase(unittest.TestCase):

    def test_get_groups(self):
        s = get_groups()
        d = get_groups()
        self.assertNotEqual(s, d)



if __name__ == '__main__':
    unittest.main()
