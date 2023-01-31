from pepsy.pepsy import Pepsy, document


styles = {
    'container': {
        'color': 'red',
        'border': '1px solid gray',
        'display': 'flex',
        'align-items': 'center',
        'flex-direction': 'column',
    }
}


class Message(Pepsy.Component):

    def __init__(self, props):
        self.props = props

    def render(self):
        
        if self.props['hits'] == 0:
            return Pepsy.create_element('b', {}, 'Press the button :)')
        else:
            return Pepsy.create_element('b', {}, 'You pressed the button' + " " + self.props['hits'] + " times")


class App(Pepsy.Component):

    def __init__(self, props):
        self.props = props
        self.state = { 'hits': 0}

    def clap(self, event):
        # alert(str(event.target.id) +  " " + str(self.state['claps']))
        #self.set_state({'message': 'You pressed the button ' + str(self.state['claps'] + 1) + " times!", 'claps': self.state['claps'] + 1}, lambda x: alert(x['message'] + "HAHAHA"))
        self.set_state({'hits': self.state['hits'] + 1})

    def render(self):
        """
        <div style={styles['container']}><button click='clap'>Click me!</button><Message hits={this.state['hits']}></Message></div>
        """
        return Pepsy.create_element('div', {'style': styles['container']}, [Pepsy.create_element('button', {'id': 'george', 'click': lambda event: self.clap(event)}, "Click me!"),Pepsy.create_element(Message, {'hits': self.state['hits']}, [])])

Pepsy.mount(Pepsy.create_element(App, {}, []), document.getElementById('app'))
