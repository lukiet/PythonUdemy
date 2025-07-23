class ComplexNumber:
    #constructor methods
    def __init__(self,real =0, imag = 0):
        print('Complex number constructor executing...')
        self.real_part = real
        self.imag_part =imag

    def display_complex(self):
        print("{0} + {1}j".format(self.real_part,self.imag_part))

#creating a new object
complex1 = ComplexNumber(30,50)
complex2 = ComplexNumber(23,90)

#calling display function
complex1.display_complex()
complex2.display_complex()

#new object plus new attribute
complex3 = ComplexNumber(91,23)
complex3.new_attribute = 56

complex3.display_complex()
print(complex3.real_part, complex3.imag_part, complex3.new_attribute)