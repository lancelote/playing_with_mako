from io import StringIO
from os.path import join, dirname, realpath, pardir, abspath

from mako.lookup import TemplateLookup
from mako.runtime import Context
from mako.template import Template

ROOT = abspath(join(dirname(realpath(__file__)), pardir))
TEMPLATES = join(ROOT, 'templates')
MODULES = join(ROOT, 'modules', )


def sample0():
    """Simple example."""
    my_template = Template('hello world')
    return my_template.render()


def sample1():
    """Passing arguments."""
    my_template = Template('hello, ${name}!')
    return my_template.render(name='Pavel')


def sample2():
    """More details."""
    my_template = Template('hello, ${name}!')
    buffer = StringIO()
    context = Context(buffer, name='Pavel')
    my_template.render_context(context)
    return buffer.getvalue()


def sample3():
    """File-based template."""
    my_template = Template(filename=join(TEMPLATES, 'my_template1.mako'))
    return my_template.render(name='Pavel')


def sample4():
    """Cache for a better performance."""
    my_template = Template(filename=join(TEMPLATES, 'my_template1.mako'),
                           module_directory=MODULES)
    return my_template.render(name='Pavel')


def sample5():
    """Using TemplateLookup."""
    my_lookup = TemplateLookup(directories=[TEMPLATES])
    my_template = Template("""<%include file="header.mako"/> awesome world!""",
                           lookup=my_lookup)
    return my_template.render()


def sample6():
    """Getting template from lookup."""


__all__ = [f'sample{i}' for i in range(7)]
