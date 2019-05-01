# Super Staticgen 3
# This isn't even my final form!
# Michael Rudden 2019

import os
import markdown

from settings import *

try:
    site_title = title
    print(site_title)
except:
    print("Check config/settings.py for title!")

if __name__ == "__main__":
    print("Compiling site from \"doc_files\" into \"public\" folder")

    template_path = 'config/template/'
    build_path = 'doc_files/'
    output_path = 'public/'
    
    for file_name in os.listdir(build_path):

        template_file_path = template_path + "base.html"
        input_file_path = build_path + file_name
        output_file_path = output_path + file_name[:-3] + ".html"
        
        print("Opening " + template_file_path)
        template_file = open(template_file_path, 'r')

        print("Processing " + file_name)
        input_file = open(input_file_path, 'r')
        input_file_contents = []

        output_file = open(output_file_path, 'w')

        # Markdown testing in line
        html_output = markdown.markdown(input_file.read())
        print("\n\n------\n\n")
        print(html_output)
        print("\n\n------\n\n")
        
        '''
        for line in input_file:
            input_file_contents.append(line)

        print("\n" + file_name + " contents:")
        
        print(len(input_file_contents))
        output_string = ""

        line_count = 0
        for line in input_file_contents:
            line_count += 1

            if line_count is len(input_file_contents):
                output_string = output_string + line
            else:
                output_string = output_string + line + "<br>\n"

        print(output_string)
        '''
        
        template_data = template_file.read()

        #output_data = template_data.replace("{% body %}", output_string)

        # Markdown testing in line
        output_data = template_data.replace("{% site_title %}", site_title)
        output_data = output_data.replace("{% body %}", html_output)

        output_file.write(output_data)
        
