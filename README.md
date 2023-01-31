<p align="center">
<img src="https://github.com/tasosxak/pepsy/blob/master/pepsylogo.png?raw=true" /></center>
</p>


Pepsy is a Python library for dealing with the DOM like ReactJS.

## Installation

## Usage

```python
from pepsy.pepsy import Pepsy,document
from welcome import Welcome

class App(Pepsy.Component):

    def __init__(self,props):
        self.props = props
        self.state = {'name': 'Tasos'}

    def render(self):
        """
        <Welcome name={this.state['name']} />
        """
        return Pepsy.create_element(Welcome, {'name' : self.state['name']}, [])

Pepsy.mount(Pepsy.create_element(App, {}, []), document.getElementById('app'))
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
