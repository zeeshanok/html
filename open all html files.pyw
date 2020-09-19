import glob, os

for file in glob.iglob('**/*.html', recursive=True):
    os.system(f'"{file}"')