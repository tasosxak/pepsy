from pepsy import Pepsy,document
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