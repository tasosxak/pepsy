from pepsy import Pepsy


class Welcome(Pepsy.Component):

    def __init__(self, props):
        self.props = props

    def render(self):
        """
        <b>You are welcome Tasos</b>
        """
        return Pepsy.create_element(
            'b',
            {},
            'You are welcome' + " " + self.props['name']
        )