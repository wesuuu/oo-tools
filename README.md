# oo-tools

Some basic object oriented tools for Python3.6+

## Development

Development occurs inside a Docker container.

Use the commands inside the ./bin directory to perform basic functions

`build.sh` will build the docker container

`enter.sh` will mount the current working directory of this repo into the docker container

`test.sh` will run the unit tests inside the docker container

## Examples

### Create an object that can save and load itself

```python
from oo_tools.save import Saver

class MyObj(Saver):
    name = 'foo'

filepath = '/tmp/myobj.obj'

myojb = MyObj
myobj.name = 'bar'

myobj.filepath = filepath
myobj.save()

del myobj # delete it from memory

myobj2 = MyObj()
myobj2.filepath = filepath

myobj2.name # equals 'foo'

myobj2.load()

myobj2.name # now equals 'bar' from save file
```
