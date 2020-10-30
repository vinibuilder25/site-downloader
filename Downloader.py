import os
# For the script run you need the 'wget' installed in your machine
# Linux :apt-get install wget   Windows: http://gnuwin32.sourceforge.net/packages/wget.htm

site = 'https://www.pygame.org' #insert the site url here
n_site = site.lstrip('https://www.') or site.lstrip('https://')
print(n_site)                           #"n-site" is the name of the folder generate by the script
n_site = site.split('/')                # or you can name by yourself, just change the variable.
path = f'/home/viniciusb/Sites/{n_site[0]}'
c_path = f'mkdir {path}'               # Dont forget to put your own directory into the variable 'path'
downloader = f'wget \
     --recursive \
     --no-clobber \
     --page-requisites \
     --html-extension \
     --convert-links \
     --restrict-file-names=windows \
     --domains website.org \
     --no-parent \
         {site}'
os.system(c_path)
os.system(f'cd {path}')
os.system(f'{downloader}')