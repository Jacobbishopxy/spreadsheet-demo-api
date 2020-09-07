"""
@author Jacob Xie
@time 9/3/2020
"""

from flask_restx import Resource, Namespace, reqparse

ns = Namespace("hello")

param_name = "name"
parser = reqparse.RequestParser()
parser.add_argument(param_name, type=str)


@ns.route("/hello")
class HelloWorld(Resource):

    @ns.expect(parser)
    def get(self):
        args = parser.parse_args()
        n = args.get(param_name)
        if n is not None:
            return f"Hello {n}!"
        return "Hello World!"
