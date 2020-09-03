"""
@author Jacob Xie
@time 9/3/2020
"""

from flask_restx import Resource, Namespace, reqparse, abort
from werkzeug.datastructures import FileStorage
import pandas as pd

ns = Namespace("upload", description="Upload Excel and return spreadsheet")


xlsx_file = "xlsx_file"
xlsx_file_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
parser = reqparse.RequestParser()
parser.add_argument(xlsx_file,
                    type=FileStorage,
                    location="files")


@ns.route("/upload")
class FileUploadAPI(Resource):

    @ns.expect(parser)
    def post(self):
        args = parser.parse_args()
        f = args.get(xlsx_file)
        if f is not None and f.content_type == xlsx_file_type:
            foo = pd.read_excel(f)
            print(foo)
        else:
            abort(404)
        return {'status': 'Done'}
