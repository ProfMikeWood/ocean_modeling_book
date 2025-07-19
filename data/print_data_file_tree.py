import os

def print_file_tree(start_directory):
    output = ''
    for root, dirs, files in os.walk(start_directory):
        level = root.replace(start_directory, '').count(os.sep)
        indent = ' ' * 4 * (level)
        output +='\n'+ f'{indent}{os.path.basename(root)}/'
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            if f[0]!='.':
                output+='\n'+f'{subindent}{f}'
    return(output)


ecco_files = print_file_tree('ECCO')

full_output = ''
full_output += 'ECCO files:\n' + ecco_files + '\n\n'

# Save the output to a text file
with open('data_file_tree.txt', 'w') as f:
    f.write(full_output)
