from browser import  document,alert,bind

class Pepsy:
	root = None
	hash_ref = {}
	class Component:
		def __init__():
			pass

		def should_update(self):
			return True

		def set_state(self, new_state, func = None):
			self.state = { **self.state , **new_state}
			if self.should_update():
				Pepsy.refresh(self, self.render())
			if func:
				return func(self.state)
		 	
		def before_mount(self):
			pass
		def after_mount(self):
			pass
		def render(self):
			pass

	@classmethod
	def find(self, vref):
		return self.hash_ref[vref]
	
	
	@classmethod
	def create_element(self,tag, props,children):
		if  not isinstance(tag, str)  and issubclass(tag , Pepsy.Component):
			pepnode = tag(props)
			vnode = {'tag':  tag, 'props': props, 'ref': pepnode,'children' : [pepnode.render()]}
			self.hash_ref[pepnode] = vnode
			if Pepsy.root == None: Pepsy.root = vnode
			return vnode
		vnode = {'tag':  tag, 'props': props, 'children' : children}
		if Pepsy.root == None: Pepsy.root = vnode
		return vnode

	@classmethod
	def mount(self,vnode,container):
		if not isinstance(vnode['tag'], str) and issubclass(vnode['tag'] ,Pepsy.Component):
			vnode['ref'].before_mount()
			self.mount(vnode['children'][0], container)
			vnode['ref'].after_mount()
		else:
			el = document.createElement(vnode['tag'] )
			vnode['el'] = el

			for vkey, vvalue in vnode['props'].items():
				if vkey in ('click'):
					el.bind(vkey, vvalue)
				elif vkey == "style":
					el.style = vvalue
				else:
					el.attrs[vkey] = vvalue

			if  isinstance(vnode['children'], str):
				 el.text = vnode['children']
			else:
				for child in vnode['children']:
					self.mount(child, el)

			container.appendChild(el)
	
	@classmethod
	def refresh(self, pepnode ,new_children):
		old_vnode = Pepsy.find(pepnode)
		new_vnode =  {'tag':  old_vnode['tag'],  'ref': pepnode ,'children' : [new_children]} 
		#old_vchild  = old_vnode['children'][0]
		#new_vnode['children'][0]['el'] = old_vchild['el']
		old_vnode['ref'].before_mount()
		Pepsy.patch(old_vnode, new_vnode)
		old_vnode['ref'].after_mount()
		#old_vnode['children'] = [new_vnode]
		
	@classmethod
	def unmount(self,vnode):
		vnode['el'].remove()

	@classmethod
	def patch(self,n1,n2):
		
		if not isinstance(n1['tag'], str) and not isinstance(n2['tag'], str) and n1['children'][0]['tag'] != n2['children'][0]['tag']:
			el = n1['children'][0]['el']
			self.mount(n2, el.parent)
			self.unmount(n1['children'][0])
		else:
			if  n1['tag'] != n2['tag']:
				alert("ddd")
				el = n1['children'][0]['el']
				self.mount(n2, el.parent)
				self.unmount(n1['children'][0])
			else:	
				if  isinstance(n2['children'], str):
				 	el = n1['el']
				 	el.text = n2['children']
				else:
					len1 = len(n1['children'])
					len2 = len(n2['children'])
					c = min(len1,len2)
					for i in range(c):
						self.patch(n1['children'][i] , n2['children'][i])
					if ( len1 > len2):
						for i in range(c,len1):
							self.unmount(n1['children'][i])
					elif ( len2 > len1):
						for i in range(c,len2):
							self.mount(n2['children'][i],el)
						
		
