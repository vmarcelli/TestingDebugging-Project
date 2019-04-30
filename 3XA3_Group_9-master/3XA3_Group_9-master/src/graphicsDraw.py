# Title: GraphicsDraw Module
# Author(s): Alexie McDonald

# Import all relevant libraries: PIL for the image drawing, generate hash and use hash for hash output values, and templatedraw to gather template information
from PIL import Image, ImageDraw
from GenerateHash import generate_hash
from UseHash import hash_to_colours
from TemplateDraw import generate_template

class generateImage():

    def __init__(self):
        # Initialize new canvas
        self.img = Image.new("RGB", (230, 230))
        self.draw = ImageDraw.Draw (self.img)


    def generate_and_return_image(self, file_name, stri, colouropt, hatopt, temp, hashes):
        userstring = stri
        location = file_name
        # Determine which parameters to fix or to change
        # If the parameters are the default value (i.e. blank, random), randomize them
        if (hashes == ""):
            # If no hash entered, generate with the default parameter "sha256"
            hashval = generate_hash(userstring)
        else:
            #If hash entered, generate a hash function of that encoding
            hashval = generate_hash(userstring, hashes)
        # Generate colour set
        colours = hash_to_colours(hashval)
        template_choices = ["Person", "Ghost"]
        if (colouropt == ""):
            # Choose the first colour generated
            randcolour = colours[0]
        else:
            randcolour = colouropt
        if (hatopt == ""):
            # Choose the second colour generated
            hatcolour = colours[1]
        else:
            hatcolour = hatopt
        if (temp == "Random"):
            # Convert hexadecimal value to integer, and choose either the first or second template at random
            template = template_choices[int(hashval, 16) % 2]
        else:
            template = temp
            

        # Draw plain white background
        w = 230
        h = 230
        x1 = 0
        y1 = 0
        # Draw the rectangle with the dimensions specified: w being width, h  being heigh, (x1, y1) being the left most coordinate of the polygon
        self.draw.polygon([(x1,y1),
        (x1+w,y1), (x1+w,y1+h), (x1,y1+h)], fill='white')
        # Get template from templateDraw module
        templates = generate_template(template, userstring)
        # Draw all layers of the image based on the template given
        if (template == "Person"):
            for i in templates[0]:
                self.draw.polygon([(i[2],i[3]),
                (i[2]+i[0],i[3]), (i[2]+i[0],i[3]+i[1]), (i[2],i[3]+i[1])], fill=randcolour)
            for j in templates[1]:
                self.draw.polygon([(j[2],j[3]),
                (j[2]+j[0],j[3]), (j[2]+j[0],i[3]+j[1]), (j[2],j[3]+j[1])], fill=hatcolour)
            for k in templates[2]:
                self.draw.polygon([(k[2],k[3]),
                (k[2]+k[0],k[3]), (k[2]+k[0],k[3]+k[1]), (k[2],k[3]+k[1])], fill=hatcolour)
            for l in templates[3]:
                self.draw.polygon([(l[2],l[3]),
                (l[2]+l[0],l[3]), (l[2]+l[0],l[3]+l[1]), (l[2],l[3]+l[1])], fill=hatcolour)
        elif (template == "Ghost"):
            for i in templates[0]:
                self.draw.polygon([(i[2],i[3]),
                (i[2]+i[0],i[3]), (i[2]+i[0],i[3]+i[1]), (i[2],i[3]+i[1])], fill=randcolour)
            for j in templates[1]:
                self.draw.polygon([(j[2],j[3]),
                (j[2]+j[0],j[3]), (j[2]+j[0],i[3]+j[1]), (j[2],j[3]+j[1])], fill=hatcolour)
            for k in templates[2]:
                self.draw.polygon([(k[2]+10,k[3]-20),
                (k[2]+k[0]+10,k[3]-20), (k[2]+k[0]+10,k[3]+k[1]-20), (k[2]+10,k[3]+k[1]-20)], fill=hatcolour)

        # Save the image in the location specified
        self.img.save(location + ".jpg")
        # Open the saved image in the image viewer
        self.img.show()

