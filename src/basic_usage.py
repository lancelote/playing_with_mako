from io import StringIO
from os.path import join

from mako.template import Template
from mako.runtime import Context
from mako.lookup import TemplateLookup


# Simple example #
##################

my_template0 = Template('hello world')
# print(my_template0.render())

# Passing arguments #
#####################

my_template1 = Template('hello, ${name}!')
# print(my_template1.render(name='Pavel'))

# More details #
################

my_template2 = Template('hello, ${name}!')
buffer = StringIO()
context = Context(buffer, name='Pavel')
my_template2.render_context(context)
# print(buffer.getvalue())

# File-based template #
#######################

my_template3 = Template(filename=join('templates', 'my_template1.mako'))
# print(my_template3.render(name='Pavel'))

# Cache for a better performance #
##################################

my_template4 = Template(filename=join('templates', 'my_template1.mako'),
                        module_directory='modules')
# print(my_template4.render(name='Pavel'))

# Using TemplateLookup #
########################

my_lookup = TemplateLookup(directories=['templates'])
my_template5 = Template("""<%include file="header.mako"/> awesome world!""",
                        lookup=my_lookup)
# print(my_template5.render())
