#!/usr/bin/python3
class Vector:
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def multiScalar(self,v):
        try:
            if isinstance(v,float): 
                print("i am float")
            else:
                raise ValueError

            length=len(self.coordinates)
            tmpList = []
            for i in range(0,length):
               tmpList.append(self.coordinates[i] * v)

            print (tmpList)

        except ValueError:
            raise ValueError('The lengths are not same ')


    def minus(self,v):
        try:
            if not v:
                raise TypeError
                
            l1 = len(self.coordinates)
            l2 = len(v.coordinates)

            if l1 != l2 :
                raise ValueError

            tmpList = []
            for i in range(0,l1):
               tmpList.append(self.coordinates[i] - v.coordinates[i])

            print (tmpList)

        except ValueError:
            raise ValueError('The lengths are not same ')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')



    def plus(self,v):
        try:
            if not v:
                raise TypeError
                
            l1 = len(self.coordinates)
            l2 = len(v.coordinates)

            if l1 != l2 :
                raise ValueError

            tmpList = []
            for i in range(0,l1):
               tmpList.append(self.coordinates[i] + v.coordinates[i])

            print (tmpList)

        except ValueError:
            raise ValueError('The lengths are not same ')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')