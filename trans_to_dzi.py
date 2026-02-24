import pyvips

def create_dzi(input_path, output_name):
    image = pyvips.Image.new_from_file(input_path, access='sequential')
    
    image.dzsave(output_name)

create_dzi('THESIS.png', 'THESIS_ouput')