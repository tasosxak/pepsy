from pepsy import Pepsy,document,alert,bind


styles = {
		'container': {
			'color' : 'red',
			'border' : '1px solid gray',
			'display' : 'flex',
			'align-items' : 'center',
			'flex-direction': 'column',
		}
	}
	

class Welcome(Pepsy.Component):

	def __init__(self,props):
		self.props = props

	def render(self):
		"""
		<b>Tasos</b>
		"""
		return Pepsy.create_element('b', {} , 'You are welcome' + " " +  self.props['name'])
		
class App(Pepsy.Component):

	
	def __init__(self,props):
		self.props = props
		self.state = {'message' : 'Hello world!', 'claps' : 0 }

	def clap(self,event):
		#alert(str(event.target.id) +  " " + str(self.state['claps']))
		#self.set_state({'message' : 'Hello world! You did ' + str(self.state['claps'] +1 ) + " claps!", 'claps' : self.state['claps'] + 1 } , lambda x: alert(x['message'] + "HAHAHA"))
		self.set_state({'claps' : self.state['claps'] + 1})

	def render(self):
		"""
		<div style="color:red;"><button click='clap'>Click me!</button><p>Hello world!</p><Bold></Bold></div>
		"""
		return Pepsy.create_element('div', {'style': styles['container']}, [Pepsy.create_element('button', {'id': 'george' , 'click' : lambda event : self.clap(event)}, "Click me!" ),Pepsy.create_element('p', {},self.state['message'] + str(self.state['claps'])),Pepsy.create_element(Welcome, {'name' : self.props['name']},[])])
		



Pepsy.mount(Pepsy.create_element(App, {'name' : 'tasos'},[]),document.getElementById('app'))

