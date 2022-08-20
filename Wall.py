class Wall:

    def __init__(self, height =0, width=0):

        if width < 0:
            self.__width = 0
        else:
            self.__width = width
        
        if height < 0:
            self.__height = 0
        else:
            self.__height = height
        
    
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, width):
        if width > 0:
            self.__width = width
        else:
            self.__height = 0

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, height):
        if height > 0:
            self.__height = height  
        else:
            self.__height = 0

    @property
    def area(self):
        return self.__width*self.__height