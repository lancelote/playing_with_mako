from mako.template import Template
from mako.runtime import Context
from io import StringIO
from os.path import join


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
