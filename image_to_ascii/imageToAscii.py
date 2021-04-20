try:
    import Image
except ImportError:
    import PIL
    from PIL import Image
#ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
ASCII_CHARS = ["□"]
a = ''

class ImageToAscii:
    def __init__(self,imagePath: str=None,width:int=100,outputFile:str=None):
        '''
        path - The path/name of the image ex: <image_name.png>\n
        width - The width you want the Ascii art to have\n
        outputfile - If you want to store the Ascii art in a txt file then set it to <file_name.txt> else keep it None  
        '''
        self.path = imagePath
        self.width = width
        try:
            self.image = PIL.Image.open(self.path)
            width, height = self.image.size
            totalPixels = width * height
        except:
            if imagePath is None:
                print("Invalid path name")
            elif self.width is None:
                print("Invalid Width provided")        
        self.new_image_data = self.pixelsToAscii(self.converToGrayscale(self.resizeImage(self.image)))

        self.pixel_count = len(self.new_image_data)

        self.ascii_image = "\n".join([self.new_image_data[index:(index+self.width)] for index in range(0, self.pixel_count, self.width)])
        if outputFile is not None:
            with open(outputFile, "w") as f:
                f.write(self.ascii_image)
        print(self.ascii_image)
        
    def resizeImage(self,image):
        width, height = image.size
        ratio = height/width
        new_height = int(self.width * ratio)
        resized_image = image.resize((self.width, new_height))
        
        return(resized_image)


    def converToGrayscale(self,image):
        grayscale_image = image.convert("L")
        return(grayscale_image)
        

    def pixelsToAscii(self,image):
        pixels = image.getdata()
        characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
        return(characters)    

