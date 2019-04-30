# Title: TemplateDraw Module
# Author(s): Alexie McDonald

# Import all relevant libraries: Generate_hash for the randomization
from GenerateHash import generate_hash

def generate_template(name, hash_word):
    # Generate a hash output to randomize parameters
    finalhash = int(generate_hash(hash_word), 16)
    # Declare template data
    template_sword = [[10,10,127,140], [10,10,137,150], [10,10,147,140], [10,10,127,160], [10,10,147,160], [10,10,157,170], [10,10,167,180]]
    # Generate a specific template based on the template name requested
    if (name == "Person" or name == ""):
        template_body = [[30,10,97,49], [10,30,87,56], [10,30,127,59], [30,10,97,88], [10,80,107,98], [10,10,97,108], [10,10,117,108], [10,30,86,118], [10,30,127, 118], [10,10,97,178], [10,10,117,178], [10,30,87,188], [10,30,127,188], [30,28,97,59]]
        template_hat = [[30,10,97,49], [10,30,87,56], [10,30,127,56]]
        template_bandana = [[50,10,87,59]]
        template_body_armor = [[10, 50, 107, 98], [51, 20, 86, 108]]
        template_wand = [[10,10,127,140], [10,10,137,150], [10,10,147,160], [10,10,157,170], [10,10,167,180]]
        template_body_suit = [[10,80,107,98], [10,10,97,178], [10,10,117,178], [10,30,87,188], [10,30,127,188]]
        hat_templates = [template_hat, template_bandana]
        body_templates = [template_body_armor, template_body_suit]
        weapon_templates = [template_sword, template_wand]
        # Compile an array of template data randomized based on input hash
        total_template = [template_body, hat_templates[finalhash%2], body_templates[finalhash%2], weapon_templates[finalhash%2]]
    elif (name == "Ghost"):
        template_ghost_body = [[80, 10, 69, 35], [10, 20, 59, 45],[10, 20, 149, 45],[10, 80, 49, 65],[10, 80, 159, 65],[10, 10, 59, 145], [10, 10, 69, 135],[10, 10, 79, 145], [10, 10, 89, 135], [10, 10, 99, 145], [10, 10, 109, 135], [10, 10, 119, 145], [10, 10, 129, 135], [10, 10, 139, 145], [10, 10, 149, 135], [10, 10, 159, 145], [10, 20, 88, 70], [10, 20, 118, 70]]
        template_ghost_hat = [[10, 10, 99, 10]]
        total_template = [template_ghost_body, template_ghost_hat, template_sword]
    # Return the array of data
    return total_template
