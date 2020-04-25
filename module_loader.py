from os.path import dirname, basename, isfile, join
import glob

modules = glob.glob(join(dirname(__file__), "**/modules/*.py"))
app_modules = [basename(f)[:-3] for f in modules if isfile(f) and 'test' not in f and not f.endswith('__init__.py')]
