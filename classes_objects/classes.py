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

#calling display function
complex1.display_complex()