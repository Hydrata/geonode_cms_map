# geonode_cms_map
A DjangoCMS plugin allowing users to add geonode maps to CMS pages. 

# Installation
1. In the project root directory (the one with manage.py in it), create a folder called `/apps/`
2. Create an empty file in this new directory called `/apps/__init.py`
2. Clone the code as a submodule into your Django project `git submodule add https://github.com/Hydrata/geonode_cms_map.git`
3. Commit to your main repo if you want now.
4. Add the new models to your database with `python manage.py syncdb`
5. Restart your webserver & you should now be able to add geonode maps as CMS plugins
