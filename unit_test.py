class Student:
    """Student class"""
    def __init__(self, lname, fname, major, gpa=0.0):
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + "with gpa: " + str(self.gpa)

    Include setUp() and tearDown() methods

    def setUp(self):
        self.student = t('Duck', 'Daisy', "Forensics", 3.5)

    def tearDown(self):
        del self.student

    def
'''
I am supplying this code below only as an example and template. I will be working to finish this code ASAP.
I have some questions... I will review prior Modules and lectures. I should be able to complete this. 
 def test_initial_value_required_attributes(self):
        self.assertEqual(self.person.last_name, 'Duck')
        self.assertEqual(self.person.first_name, 'Daisy')

    def test_inital_all_attributes(self):
        person = t('Duck', 'Daisy', '111-11-1111') # this is not self.person from setUp, but local
        assert person.last_name == 'Duck'                 # note no self here on person or assert
        assert person.first_name == 'Daisy'
        assert person.ssn == '111-11-1111'

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            p = t('123', 'Daisy')

    def test_object_not_created_error_fist_name(self):
        with self.assertRaises(ValueError):
            p = t('Duck', '123')

    def test_object_not_created_error_ssn(self):
        with self.assertRaises(ValueError):
            p = t('Duck', 'Daisy', 'abc')

    def test_person_class_display_name(self):
        self.assertEqual(str(self.person), "Duck, Daisy:")   # Uses person from setUp()

    def test_person_class_display_name_ssn(self):
        p = t('Duck', 'Daisy', '111-11-1111')    # Does not use person from setUp(), has local p
        self.assertEqual(str(p), "Duck, Daisy:111-11-1111")

    def test_person_str(self):
        self.assertEqual(str(self.person), 'Duck, Daisy:')

if __name__ == '__main__':
    unittest.main()
'''
